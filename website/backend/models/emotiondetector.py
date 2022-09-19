# Framework for identifying emotion in a picture with someone's face.
# Adapted by Liam Prevelige from https://github.com/oarriaga/paz
# September 2022  

from paz.applications import HaarCascadeFrontalFace, MiniXceptionFER
import paz.processors as pr

class EmotionDetector(pr.Processor):
  def __init__(self):
    super(EmotionDetector, self).__init__()
    self.detect = HaarCascadeFrontalFace(draw=False)
    self.crop = pr.CropBoxes2D()
    self.classify = MiniXceptionFER()
    self.draw = pr.DrawBoxes2D(self.classify.class_names)
    self.classification = None

  def call(self, image):
    boxes2D = self.detect(image)['boxes2D']
    cropped_images = self.crop(image, boxes2D)
    for cropped_image, box2D in zip(cropped_images, boxes2D):
        self.classification = self.classify(cropped_image)['class_name']
        box2D.class_name = self.classification
    return self.draw(image, boxes2D)