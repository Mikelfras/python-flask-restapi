from flask import Flask, logging, request
from werkzeug.wrappers import Response
import routes.process.image_process as i_p
import routes.invite_list.invite_code_actions as i_l
import utils
import logging
import os
from firebase_admin import initialize_app, storage, db, credentials

app = Flask(__name__)
logging.basicConfig(filename='api_log.log',level=logging.DEBUG)
cred = credentials.Certificate('service-account-file.json')
default_app = initialize_app(cred,options={'storageBucket':'hydrosis-beta-flask-storage','databaseURL':'https://hydrosis-beta.firebaseio.com/'}) 
ref = db.reference('/inviteCodes')
bucket = storage.bucket();
if __name__=="main":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT',8080)))
@app.route('/')
def home():
    #TODO should return a welcome screen to the API
    return 'Incomplete', 404

@app.route('/api/apiKey/process')
def process_image_apiKey():
    #TODO should process the image, while associated with an API key
    return 'Incomplete', 404

@app.route('/api/process', methods=['POST'])
def process_image():
    r = request
    check = utils.request_verification(r)
    if not(check == 'success'):
        return check
    resp = i_p.image_analysis(r,bucket)
    return resp

@app.route('/user_list',methods=['GET'])
def get_user_list():
    #TODO should get a list of users associated with a coach or invite code
    #resp = i_l.get_users(request)
    return 'Incomplete', 404
@app.route('/update',methods=['GET'])
def update_observer_list():
    #TODO should update the authorized observers to specific users
    #resp = i_l.update_invite_codes(db)
    return 'Incomplete', 404