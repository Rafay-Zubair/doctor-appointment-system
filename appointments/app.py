from flask import Flask, jsonify, request
from pymongo import MongoClient
import os

app = Flask(__name__)


# Connection with MongoDB
db_client = MongoClient(os.environ.get('HOST_URL'), int(os.environ.get('DB_PORT')))
# Database
db = db_client.doc_appointment_system
# Collection
appointment_collection = db.appointment

if appointment_collection.count_documents({}) == 0:
	# When appointments collection is empty
	appointments = [
		{ 'id': "1",'doctor': "1", 'date': "21 Nov 2023", 'rating':"Good"  },
		{ 'id': "2",'doctor': "1", 'date': "22 Nov 2023", 'rating':"Bad"  },
		{ 'id': "3",'doctor': "2", 'date': "22 Nov 2023", 'rating':"Good"  },
		{ 'id': "4",'doctor': "1", 'date': "22 Nov 2023", 'rating':"Bad"  },
		{ 'id': "5",'doctor': "2", 'date': "22 Nov 2023", 'rating':"Good"  },
	]
	for app in appointments:
		appointment_collection.insert_one(app)

@app.route('/hello')
def hello():
	greeting = "Hello world!"
	return greeting

@app.route('/appointments', methods=["GET"])
def getAppointments():
	data = list(appointment_collection.find())
	for d in data:
		d.pop("_id")
	return jsonify(data)

@app.route('/appointment/<id>', methods=["GET"])
def getAppointment(id):
	data = appointment_collection.find_one({'id':str(id)})
	data.pop("_id")
	return jsonify(data)

if __name__ == "__main__":
	app.run(host="0.0.0.0",port=7070)
