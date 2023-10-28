from flask import Flask, Blueprint, request
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
api = Blueprint('api', __name__, url_prefix='/api')
cors = CORS(api, resources={r'/api/*': {'origins': 'http://localhost:3000'}})

save_path = './storage/'
img_buf_limit = 10

@api.route("/pose_estimate", methods=['POST'])
def pose_estimate():
    for cnt in range(img_buf_limit):
        key = 'image_' + str(cnt)
        if key not in request.files:
            return 'No file part', 400
        file = request.files[key]
        if file.filename == '':
            return 'No selected file', 400
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(save_path, filename))
            print('File saved: ' + filename)
    return 'File uploaded successfully', 200

app.register_blueprint(api)
