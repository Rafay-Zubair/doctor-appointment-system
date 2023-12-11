from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

# doctors = [
#   { 'id': "1",'firstName': "Muhammad Ali", 'lastName': "Kahoot", 'speciality':"DevOps"  },
#   { 'id': "2",'firstName': "Good", 'lastName': "Doctor",'speciality':"Test"  }
# ]

# Connection with MongoDB
db_client = MongoClient(process.env.HOST_URL, process.env.DB_PORT)
# Database
db = db_client.doc_appointment_system
# Collection
doc_collection = db.doctor

data = doc_collection.find()
if data.len() == 0:
	# If doctors collection is empty
	doctors = [
		{ 'id': "1",'firstName': "Muhammad Ali", 'lastName': "Kahoot", 'speciality':"DevOps"  },
		{ 'id': "2",'firstName': "Good", 'lastName': "Doctor",'speciality':"Test"  }
	]	
	for doctor in doctors:
		doc_collection.insert_one(doctor)

@app.route('/hello')
def hello():
  greeting = "Hello world!"
  return greeting

@app.route('/doctors', methods=["GET"])
def getDoctors():
	data = doc_collection.find()
  return jsonify(data)

@app.route('/doctor/<id>', methods=["GET"])
def getDoctor(id):
	data = doc_collection.find_one({'id':str(id)})
	return jsonify(data)
  # id = int(id) - 1
  # return jsonify(doctors[id])

if __name__ == "__main__":
  app.run(host="0.0.0.0",port=9090)
