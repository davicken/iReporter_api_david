# import datetime

# from jwt import encode

# from api.helpers.auth_token import encode_token, secret_key
# from api.models.incident_model import RedFlag
# from api.models.user_model import users, User

# user1_data = {
#     "first_name": "userOne",
#     "last_name": "userone",
#     "email": "userOne@ireporter.com",
#     "phone_number": "0773125678",
#     "password": "Password123",
#     "user_name": "user1",
#     "other_names": "",
# }

# user2_data = {
#     "first_name": "userTwo",
#     "last_name": "lastTwo",
#     "email": "usertwo@ireporter.com",
#     "phone_number": "0774551567",
#     "password": "Password123",
#     "user_name": "user2",
#     "other_names": "",
# }


# def generate_token_header(token):
#     return {
#         "Content-Type": "application/json",
#         "Authorization": "Bearer " + token,
#     }


# admin_header = generate_token_header(encode_token(1, 1))

# user1 = User(**user1_data)
# user2 = User(**user2_data)
# users.extend([user1, user2])
# user1_id = user1.user_id
# user2_id = user2.user_id

# user1_header = generate_token_header(encode_token(user1_id))
# user2_header = generate_token_header(encode_token(user2_id))

# new_record = {
#     "title": "My First red flag",
#     "description": "Lorem ipsum eiusmod temport labore et dolore magna",
#     "location": [-80, -174.4],
#     "tags": ["crime", "rape"],
#     "Images": ["image1.jpg", "image2.jpg"],
#     "Videos": ["vid1.mp4", "vid2.mp4"],
#     "comment": "",
# }
# second_record = {
#     "title": "My Second red flag",
#     "description": "Lorem ipsum eiusmod temport labore et dolore magna",
#     "location": [-78, -164.4],
#     "tags": ["crime", "murder"],
#     "images": ["image3.jpg", "image4.jpg"],
#     "videos": ["vid8.mp4", "vid5.mp4"],
#     "comment": "Caught in the very act",
#     "user_id": user2_id,
# }
# third_record = {
#     "title": "My Second red flag",
#     "description": "Lorem ipsum eiusmod temport labore et dolore magna",
#     "location": [-78, -164.4],
#     "tags": ["crime", "murder"],
#     "images": ["image5.jpg", "image6.jpg"],
#     "videos": ["vid9.mp4", "vid5.mp10"],
#     "comment": "Caught in the very act",
#     "user_id": user1_id,
# }
# fourth_record = {
#     "title": "My third red flag",
#     "description": "Lorem ipsum eiusmod temport labore et dolore magna",
#     "location": [-78, -164.4],
#     "tags": ["crime", "murder"],
#     "images": ["image5.jpg", "image6.jpg"],
#     "videos": ["vid9.mp4", "vid5.mp10"],
#     "comment": "Caught in the very act",
#     "user_id": user1_id,
# }
# red_flag_obj1 = RedFlag(**second_record)
# red_flag_obj2 = RedFlag(**third_record)
# red_flag_obj3 = RedFlag(**fourth_record)
# red_flag_obj1.status = "under investigation"
# redflags.extend([red_flag_obj1, red_flag_obj2, red_flag_obj3])

# expired_token = encode(
#     {
#         "userid": 1,
#         "isAdmin": 1,
#         "exp": datetime.datetime.utcnow() - datetime.timedelta(hours=3),
#     },
#     secret_key,
#     algorithm="HS256",
# ).decode("utf-8")
# expired_token_header = generate_token_header(expired_token)
