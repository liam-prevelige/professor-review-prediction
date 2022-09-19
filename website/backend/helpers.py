"""
Helpers for Professor Review Predictor
Created by Liam Prevelige, November 2022

Used by the backend framework in app.py
"""
from paz.backend.image import load_image
import numpy as np
import cv2
from keras.models import load_model
import numpy as np
from urllib.request import Request, urlopen
from models.emotiondetector import EmotionDetector

ATTRACTIVENESS_MODEL_PATH = 'models/attractiveness_model/attractiveNet_mnv2.h5'

BASE_RATING = 3.72208283936757
HAPPY_COEFF = -0.0514927768  # being happy in your photo predicts worse professor :(
BLUR_COEFF = -0.000104787804
ATTRACTIVENESS_COEFF = 0.191263947
COLORFULNESS_COEFF = 0.00261651372

def get_rating(image_url):
  image = load_image_from_url(image_url)
  happy_rating = get_is_happy(image) * HAPPY_COEFF
  blur_rating = get_blur_amount(image) * BLUR_COEFF
  attractiveness_rating = get_attractiveness(image) * ATTRACTIVENESS_COEFF
  colorfulness_rating = get_colorfulness(image) * COLORFULNESS_COEFF

  rating = float((BASE_RATING + happy_rating + blur_rating + attractiveness_rating + colorfulness_rating)[0][0])
  contextualized_results = get_contextualized_results(happy_rating, blur_rating, attractiveness_rating, colorfulness_rating)
  return rating, contextualized_results

def get_contextualized_results(happy_rating, blur_rating, attractiveness_rating, colorfulness_rating):
  contextualized_results = {}
  contextualized_results["happy"] = "Yes" if happy_rating > 0 else "No"
  contextualized_results["blur"] = "Very blurry" if blur_rating < 150 else "Not too blurry" 
  contextualized_results["attractiveness"] = "Yes" if attractiveness_rating > 2.8 else "... :("
  contextualized_results["colorfulness"] = "Lots of colors" if colorfulness_rating > 40 else "A little bland" 
  return contextualized_results

def load_image_from_url(image_url):
  """
  https://stackoverflow.com/questions/8286352/how-to-save-an-image-locally-using-python-whose-url-address-i-already-know
  https://stackoverflow.com/questions/55821612/whats-the-fastest-way-to-read-images-from-urls
  """
  req = Request(
    url = image_url,
    headers={'User-Agent': 'Mozilla/5.0'}
  )
  res = urlopen(req).read()

  output = open("temp-image.jpg","wb")
  output.write(res)
  output.close()

  return load_image("temp-image.jpg")

def get_is_happy(image):
  detect_emotion = EmotionDetector()
  detect_emotion(image)
  return int(detect_emotion.classification == "happy")

def get_blur_amount(image):
  #TODO: Insert source
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  return cv2.Laplacian(gray, cv2.CV_64F).var()

def get_attractiveness(image):
  """
  Very bad model, but funny
  TODO: insert source
  """
  model = load_model(ATTRACTIVENESS_MODEL_PATH)
  return model.predict(np.expand_dims(image,0))

def get_colorfulness(image):
  """
  TODO: insert source
  """
  # split the image into its respective RGB components
  (B, G, R) = cv2.split(image.astype("float"))
  # compute rg = R - G
  rg = np.absolute(R - G)
  # compute yb = 0.5 * (R + G) - B
  yb = np.absolute(0.5 * (R + G) - B)
  # compute the mean and standard deviation of both `rg` and `yb`
  (rbMean, rbStd) = (np.mean(rg), np.std(rg))
  (ybMean, ybStd) = (np.mean(yb), np.std(yb))
  # combine the mean and standard deviations
  stdRoot = np.sqrt((rbStd ** 2) + (ybStd ** 2))
  meanRoot = np.sqrt((rbMean ** 2) + (ybMean ** 2))
  # derive the "colorfulness" metric and return it
  return stdRoot + (0.3 * meanRoot)
