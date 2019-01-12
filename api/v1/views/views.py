from flask import request, jsonify
from api.v1 import app
from api.v1.models.redflags import RedFlag
from api.v1.controllers.controller import validate_string


redflags = []

# A testing end-point
@app.route('/')
def index():
    return jsonify({"message": "Welcome to my iReporter home"}) 

# create a red-flag
@app.route('/api/v1/redflags', methods=['POST'])
def create_redflag():
    data = request.get_json()
    inc_id = (len(redflags)+1)
    inc_type = data.get('inc_type')
    createdOn = data.get('createdOn')
    createdBy = data.get('createdBy')
    location = data.get ('location')
    status = data.get('status')
    comment = data.get('comment')
    images = data.get('images')
    videos = data.get('videos')

    


    try:
        # print(data)
        # validate_string(data['location'])
        flag_record = RedFlag(inc_id, inc_type, createdOn, createdBy, location, status, comment, images, videos)
        redflags.append(flag_record)
    except ValueError as e:
        print(e)
        return jsonify({'status': 400, 'message': 'location should be a string'})
    return jsonify({'status': 201, 'redflags': [flag_record.to_json()]})


    
    