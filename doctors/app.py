# Importing Libraries
from flask import Flask, jsonify, request
from pymongo import MongoClient
import os

app = Flask(__name__)

# Connection with MongoDB
db_client = MongoClient(os.environ.get('HOST_URL'), int(os.environ.get('DB_PORT')))
# Database
db = db_client.doc_appointment_system
# Collection
doc_collection = db.doctor

if doc_collection.count_documents({}) == 0:
	# When doctors collection is empty
	doctors = [
		{ 'id': "1",'firstName': "Muhammad Ali", 'lastName': "Kahoot", 'speciality' : "DevOps"  },
		{ 'id': "2",'firstName': "Good", 'lastName': "Doctor",'speciality' : "Test"  }
	]	
	for doctor in doctors:
		doc_collection.insert_one(doctor)

@app.route('/hello')
def hello():
	greeting = "Hello world!"
	return greeting

@app.route('/doctors', methods=["GET"])
def getDoctors():
	data = list(doc_collection.find())
	for d in data:
		d.pop("_id")
	return jsonify(data)

@app.route('/doctor/<id>', methods=["GET"])
def getDoctor(id):
	data = doc_collection.find_one({'id':str(id)})
	data.pop("_id")
	return jsonify(data)

if __name__ == "__main__":
	app.run(host="0.0.0.0",port=9090)
