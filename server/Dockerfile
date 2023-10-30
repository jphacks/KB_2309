# ベースイメージを選択
FROM python:3.9

RUN apt-get update
RUN apt-get install -y libgl1-mesa-glx

# ワークディレクトリを設定
WORKDIR /app

# 必要なファイルをコピー
# Copy model into docker container
COPY ./pose_estimator/model/pose_deploy_linevec.prototxt /app/pose_estimator/model/
COPY ./pose_estimator/model/pose_iter_440000.caffemodel /app/pose_estimator/model/
ADD . /app
COPY requirements.txt /app/

# 依存関係をインストール
RUN pip install -r requirements.txt

# アプリケーションを実行
CMD ["flask", "--app", "main", "run", "--host=0.0.0.0", "--reload"]
