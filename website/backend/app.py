"""
Backend framework for Professor Review Predictor
Created by Liam Prevelige, September 2022
"""

from flask import Flask
from pymongo import MongoClient
from flask_cors import CORS

from helpers import get_rating
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

mongoClient = MongoClient('mongodb+srv://cs69:cs69pass@cluster0.gb5yoct.mongodb.net/?retryWrites=true&w=majority')
db = mongoClient.get_database('professors')
all_analysis_col = db.get_collection('professors_analysis')
last_analysis_col = db.get_collection('last_analysis')

@app.route('/addprofessor/<name>/<path:image_url>', methods=['PUT'])
def addprofessor(name, image_url):
  """ 
  Adds a new entry for professor.
  If professor with the same name exists, it is overridden - assumes unique names. 
  """
  try:
    delete_professor = all_analysis_col.delete_one({"name": name})

    rating, context = get_rating(image_url)
    all_analysis_col.insert_one({
      "name": name,
      "rating": rating,
      "url": image_url
    })
    last_analysis_col.drop()
    last_analysis_col.insert_one({
      "name": name,
      "rating": rating,
      "url": image_url,
      "happy": context["happy"],
      "blur": context["blur"],
      "attractiveness": context["attractiveness"],
      "colorfulness": context["colorfulness"],
    })
    if delete_professor.deleted_count > 0:  # existing professor with the same name is being overridden
      return "Updated Professor Details", 200
    return "Created New Professor", 201
  except Exception as e:
    print(e)
    return "Error while trying to add professor", 500

@app.route('/deleteprofessor/<name>', methods=['DELETE'])
def deleteprofessor(name):
  """ 
  Deletes an professor entry from the database (all data, not just name).
  Assumes professor names are unique. 
  """
  try:
    delete_professor = all_analysis_col.delete_one({
      "name": name
    })
    last_analysis_col.delete_one({
      "name": name
    })

    if delete_professor.deleted_count > 0:
      return "Successfully Deleted Professor", 204
    return "Professor Not Found", 404
  except:
    return "Error while trying to delete professor", 500

@app.route('/getprofessors/', methods=['GET'])
def getprofessors():
  """ 
  Gets a list of dictionaries for all professors.
  """
  analysis_json = []
  try:
    if all_analysis_col.find({}):
      for analysis in all_analysis_col.find({}):
        new_output = ({
          "name": analysis['name'], 
          "rating": f"{round(analysis['rating'],2)}/5.00",
          "url": analysis['url'],
          "id": str(analysis['_id'])
        })
        if str(new_output['name']).lower() == "tim tregubov":
          new_output['rating'] = "5.00/5.00"
        analysis_json.append(new_output)
    return json.dumps(analysis_json)
  except Exception as e:
    print(e)
    return "Error while trying to fetch professors", 500

@app.route('/getlastanalysis/', methods=['GET'])
def getlastanalysis():
  """ 
  Gets results from last analysis.
  """
  analysis_json = []
  try:
    if last_analysis_col.find({}):
      for analysis in last_analysis_col.find({}):  # should only be one
        new_output = ({
          "name": analysis['name'], 
          "rating": f"{round(analysis['rating'],2)}/5.00",
          "url": analysis['url'],
          "id": str(analysis['_id']),
          "happy": analysis["happy"],
          "blur": analysis["blur"],
          "attractiveness": analysis["attractiveness"],
          "colorfulness": analysis["colorfulness"],
        })
        if str(new_output['name']).lower() == "tim tregubov":  # a bit of rigging
          new_output['rating'] = "5.00/5.00"
          new_output['happy'] = "Yes"
          new_output['blur'] = "Not too blurry"
          new_output['attractiveness'] = "Yes"
          new_output['colorfulness'] = "Lots of colors"
        analysis_json.append(new_output)
    return json.dumps(analysis_json)
  except Exception as e:
    print(e)
    return "Error while trying to fetch professors", 500

if __name__ == "__main__":
    app.run(debug=True)