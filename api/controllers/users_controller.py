import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from api import app
from flask import request, jsonify
from api.models.users_model import User, UsersData 
from api.helpers.validation import validate_create_user_data, validate_login_data
from datetime import datetime
current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
import jwt

my_users = UsersData()

class UsersController:
    def create_user(self):
        # create a new user
        data = request.get_json()
        userId = str(uuid.uuid4())
        firstName = data.get("first_name")
        lastName = data.get("last_name")
        otherNames = data.get("other_names")
        userName = data.get("user_name")
        email = data.get("email")
        phoneNumber = data.get("phone_number")
        password = generate_password_hash(data.get("password"), method='pbkdf2:sha256', salt_length=8)
        isAdmin = False
        registeredOn = current_time
    
        # check for empty request
        if not request.data:
            return jsonify({
                'error': 'Request Cannot Be Empty',
                'status': 400
            }), 400
            
        #ensuring data format being posted is json
        if request.content_type != 'application/json':
            return jsonify({
                "status": "400",
                "message": "Data input must be in json format"

        # validate the input data
            })
        if validate_create_user_data(data):
            return jsonify({"error": 400,
                            "message": validate_create_user_data(data)
                            }), 400

        user_record = User(
            user_id = userId,
            first_name = firstName,
            last_name = lastName, 
            other_names = otherNames, 
            user_name = userName, 
            email = email,
            phone_number = phoneNumber,     
            password = password,
            is_admin = isAdmin,
            registered_on = registeredOn
        )
        my_users.users_list.append(user_record)
        return jsonify({'status': 201, 'data': [{
            "id": userId,
            "message": "created user record successfully" 
            }]
            }),201


    def get_all_users(self):
        # get all existing users
        json_users = []
        for user in my_users.users_list:
            json_users.append(user.to_json())

        if len(json_users) < 1:
            return jsonify({
                'error': 'There are no users records currently',
                'status': 404
                }), 404

        return jsonify({
            'status': 200, 
            'data': json_users
            })
    
    def get_user(self, user_id):
        # get a specific user based on its id
        for user in my_users.users_list:
            if user.__dict__['userId'] == user_id:
                return jsonify({
                    'status': 200,
                    'data': [user.to_json()]
                }), 302

        return jsonify({
            'status': 404,
            'error': 'That user record does not exist'
        }), 404

    def delete_user(self, user_id):
        # delete a single user record by its id
        for user in my_users.users_list:
            if user.__dict__['userId'] == user_id:
                my_users.users_list.remove(user)
                return jsonify({
                    'status': 200,
                    'data': [{
                        'id': user.__dict__['userId'],
                        'message': 'user record with id {} has been deleted successfully'.format(user.__dict__['userId'])
                    }]
                }), 200

        return jsonify({
            'status': 404,
            'error': 'That user record does not exist'
        }), 404
    
    def edit_user(self, user_id):
        # edit specific user info
        if not request.json:
            return jsonify({
                'status': 400,
                'error': 'There is no request data given, Provide new user info'
            }), 400

        new_first_name = request.get_json()
        new_last_name = request.get_json()
        new_user_name = request.get_json()
        new_other_name = request.get_json()
        new_email = request.get_json()
        new_phone_no = request.get_json()
        new_password = request.get_json()

            
        for user in my_users.users_list:
            if user.__dict__["userId"] == user_id:
                user.__dict__["firstName"] = new_first_name["first_name"]
                user.__dict__["lastName"] = new_last_name["last_name"]
                user.__dict__["otherName"] = new_other_name["other_names"]
                user.__dict__["userName"] = new_user_name["user_name"]
                user.__dict__["email"] = new_email["email"]
                user.__dict__["phoneNumber"] = new_phone_no["phone_number"]
                user.__dict__["password"] = generate_password_hash(new_password["password"], method='pbkdf2:sha256', salt_length=8)
                
                return jsonify({
                    "status": 200,
                    "data": [{
                        'id': user.__dict__['userId'],
                        "message": "The user information has been updated successfully"
                    }]
                }), 200

        return jsonify({
            "status": 404,
            "error": "Sorry, that user record does\'t exist"
        }), 404

    def make_user_admin(self, user_id):
        # up grade user role to admin
                   
        for user in my_users.users_list:
            if user.__dict__["userId"] == user_id:
                if user.__dict__["isAdmin"] == False:
                    user.__dict__["isAdmin"] = True
                    
                    return jsonify({
                        "status": 200,
                        "data": [{
                            'id': user.__dict__['userId'],
                            "message": "The user has been raised to admin role successfully"
                        }]
                    }), 200
                else:
                    return jsonify({
                        "status": 400,
                        "error": "The user you are trying to promote  is already an admin" 
                    }), 400


        return jsonify({
            "status": 404,
            "error": "Sorry, that user record does\'t exist"
        }), 404

    def login(self):
         # check for empty request
        if not request.data:
            expected_data = {"username": "**String**", "password": "**string**"}
            return jsonify({
                'error': 'login info Can not be empty',
                'expected': expected_data,
                'status': 400
            }), 400
   
        login_data = request.get_json()
        username = login_data.get("user_name")
        hash_password = generate_password_hash(login_data.get("password"), method='pbkdf2:sha256', salt_length=8)
        
        if validate_login_data(login_data):
            return jsonify({"error": 400,
                            "message": validate_login_data(login_data)
                            }), 400

        for user in my_users.users_list:
            # loop thru the list for user credentials  
            if user.__dict__["userName"] != username:
                return jsonify({
                    "status": 400,
                    "error": "The Username you provided is doesn\'t exist, try again with a correct one!"
                }), 400
            if check_password_hash(user.__dict__["password"], hash_password):
                # generate the token
                token = jwt.encode({'user_id': user.__dict__["userId"], 'exp':datetime.utcnow() + datetime.timedelta(minutes=30)}, 
                app.config['SECRET_KEY'])
                return jsonify({'token':token.decode('UTF-8')})

            return jsonify({
                "status": 400,
                "error": "The password you provided was incorrect, try again with a correct one!"
            }), 400