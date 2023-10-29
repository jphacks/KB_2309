from flask import Flask, Blueprint, request, jsonify, make_response
from flask_cors import CORS
from werkzeug.utils import secure_filename
from tool.makeHash import make_hash
import tool.calculate as calc
import db_controller as dc
import os

app = Flask(__name__)
api = Blueprint('api', __name__, url_prefix='/api')
cors = CORS(api, resources={r'/api/*': {'origins': 'http://localhost:3000'}})

save_path = './storage/'
img_buf_limit = 10


@api.route("/get-ready", methods=['GET'])
def get_ready():
    id = make_hash(request.remote_addr)
    dc.create_access(id)
    return 'access succeeded', 200

"""_summary_
    TODO 本メソッドで実装すべき内容は以下の通り
    
    - 画像を受け取る(実装済み)
    - 画像をモデルに投げて座標を取得
    - 画像情報をDBに保存
        - db_controller.pyのcreate_side_photoを呼び出す
    - 画像をstorageに保存
        - ./tool/storage_controller.pyのget_dir_pathを呼び出すことで保存先のパスを取得
        - 多分今のままでもいける

"""
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
            # filename = secure_filename(file.filename)
            filename = make_hash(request.remote_addr)
            file.save(os.path.join(save_path, filename))
            print('File saved: ' + filename)
    return 'File uploaded successfully', 200

@api.route("/summary", methods=['GET'])
def get_pose_summary():
    # idを生成（？）
    id = make_hash(request.remote_addr)
    # idを元にDBから画像情報を取得
    result = dc.read_side_photo(id)
    if result is None:
        return 'No access log', 400
    # 画像情報を元に平均値を計算
    back_arg_ave, leg_arg_ave = calc.ave_for_side_photos(result)
    # コメントを取得
    
    # 画像を一枚選定する
    path = calc.getPhotosPathByClosest(result, back_arg_ave, calc.SIDE_PHOTO_COLUMNS.BACK_ARG)
    
    # JSONデータを生成
    return_json = {
        'result': {
            "back_angle_ave" : back_arg_ave,
            "leg_angle_ave" : leg_arg_ave,
            "comment":"コメント" 
        },
        }

    # 画像データを読み取り
    with open(path, 'rb') as image_file:
        image_data = image_file.read()

    # JSONデータと画像データをレスポンスに追加
    response_data = {'json_data': return_json, 'image_data': image_data}

    # JSONデータを含むJSONレスポンスを作成
    response = make_response(jsonify(response_data))

    # レスポンスヘッダにContent-Typeを設定
    response.headers['Content-Type'] = 'application/json'

    return response, 200

app.register_blueprint(api)
