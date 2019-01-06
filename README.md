# iReporter API by Mwesigwa David Keneth 
  * iReporter is a corruption reporting and awareness platform that seeks for a reduced corruption level and government intervention.
  * Corruption is a huge bane to Africa’s development. African countries must develop novel and localised solutions that will curb this menace, hence the birth of iReporter. iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention.

## How It Works

A) User

    * User Registration
    * User login
    * User can create a red-flag record.
    * User can create an intervention record.
    * User can delete a red-flag or intervention record.
    * User can add images to either red-flag or intervention record.
    * User can add videos to either red-flag or intervention record.
    * User can add geolocation to either a red-flag or intervention record.

    User profile has the following features

    * List of all his/her red-flag/intervention records.
    * The number of red-flag/intervention records that has been resolved.
    * The number of red-flag/intervention records that are yet to be resolved.
    * The number of red-flag/intervention records that have been rejected.

B) Admin

    * An Admin can Change the status of a red-flag/intervention records.
    * An Admin can view a list of all red-flag/intervention records created by all users.

Technology Used

    * HTML
    * CSS
    * JS
    * Python
    * Jason
    * Flask micro-framework
    

Available API Endpoints
| EndPoint                              | Functionality      |
| -------------                         |:------------------:|
| POST /red-flags                       | Create a red flag record |
| GET /red-flags                        | Get all red flag records |
| GET /red-flags/<red-flag-id>          | Fetch a single red flag record given its id |
| PATCH /red-flags/<red-flag-id>/comment| Edit the comment of a redflag record|
| DELETE /red-flags/<red-flag-id>       | Delete a red fag record given an id|
| PATCH /red-flags/<red-flag-id>/status |Change the status of a record given an id| 
  
## Installing

First clone this repository
```
git clone -b develop https://github.com/davicken/iReporter-api.git 
cd iReporter_api
```

Then create a virtual environment
```
virtualenv venv
```

and start it
```
On Windows
venv/Scripts/activate
On linux
source/venv/bin/activate
```
Then install all the necessary dependencies
```
pip install -r requirements.txt
```
## Running
At the terminal type in

```python run.py```
To run tests run this command at the console/terminal
```pytest```


Use the api endpoints with an app like Postman
  
