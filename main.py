import os
import json
import pymongo
from flask import Flask
from flask import request
app = Flask(__name__)


client = pymongo.MongoClient("mongodb+srv://edbarbaay:9atVuD678UH5wVMl@cluster0.vcerlra.mongodb.net/?retryWrites=true&w=majority")
db = client['db_UIDE']
collection = db['EBarba_Guitarras']


@app.route('/')
def get():
    nombre = collection.find()
    response = []
    for document in nombre:
        document['_id'] = str(document['_id'])
        response.append(document)
    return json.dumps(response)
if __name__ == '__main__':
    app.run()
