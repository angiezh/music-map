import os
import json
from flask import Flask, jsonify, request, abort
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
OUR_DATA = os.path.join(PROJECT_ROOT, '..', 'src', 'lib', 'data', 'filtered_data.json')


# get id endpoint for creating new component on AddOverlay

def load_moments():
    with open(OUR_DATA, 'r') as file:
        return json.load(file)

def save_moments(moments):
    with open(OUR_DATA, 'w') as file:
        json.dump(moments, file, indent=4)

@app.route('/moments', methods=['GET'])
def get_moments():
    return jsonify(load_moments())

@app.route('/moments', methods=['POST'])
def add_moment():
    if not request.json:
        abort(400)
    
    # Validate and extract fields from request.json here.
    # For brevity, this is omitted. Add error handling as needed.
    new_moment = {
        "type": "Feature",
        "properties": {
            "id": request.json.get('id'),  # ID should be unique and provided by the client or generated here.
            "song": request.json['song'],
            "description": request.json['description']
        },
        "geometry": {
            "type": "Point",
            "coordinates": request.json['coordinates']
        }
    }

    moments = load_moments()
    moments["features"].append(new_moment)
    save_moments(moments)

    return jsonify(new_moment), 201

@app.route('/moments/<int:moment_id>', methods=['DELETE'])
def delete_moment(moment_id):
    moments = load_moments()
    moment = next((item for item in moments["features"] if item["properties"]["id"] == moment_id), None)
    if not moment:
        abort(404)
    
    moments["features"] = [item for item in moments["features"] if item["properties"]["id"] != moment_id]
    save_moments(moments)

    return jsonify({'result': True})

if __name__ == '__main__':
    print(OUR_DATA)
    app.run(debug=True)
