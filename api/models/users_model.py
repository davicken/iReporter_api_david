import uuid
from werkzeug.security import generate_password_hash, check_password_hash

class User():
    # user model
    def __init__(self, **kwargs):
        # initialising the parameters of the user class
        self.userId = kwargs.get("user_id")
        self.firstName = kwargs.get("first_name")
        self.lastName = kwargs.get("last_name")
        self.otherNames = kwargs.get("other_names")
        self.userName = kwargs.get("user_name")
        self.email = kwargs.get("email")
        self.phoneNumber = kwargs.get("phone_number")
        self.password = kwargs.get("password")
        self.registeredOn = kwargs.get("registered_on")
        self.isAdmin = kwargs.get("is_admin")

    def to_json(self):
        # method to return the dictionary of a user item
        return {
            "user_id": self.userId,
            "first_name": self.firstName,
            "last_name": self.lastName,
            "other_names": self.otherNames,
            "user_name": self.userName,
            "email": self.email,
            "phone_number": self.phoneNumber,
            "password": self.password,
            "registered_on": self.registeredOn,
            "is_admin": self.isAdmin
        }

class UsersData: 
    # class for managing user data
    def __init__(self):
        self.users_list = []
        
        # create an admin user since there's no option for signing him up
        admin = User(
            user_id = str(uuid.uuid4()),
            first_name = "mwesigwa",
            last_name = "david",
            other_names = "keneth",
            user_name = "davicken",
            email = "davicken@gmail.com",
            phone_number = "0787550983",
            password = generate_password_hash("Davicken..2", method='pbkdf2:sha256', salt_length=8),
            is_admin = True,
            registered_on = "2019-02-27 02:27"
        )
        self.users_list.append(admin)

       