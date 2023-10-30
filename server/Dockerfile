# ベースイメージを選択
FROM python:3.8

RUN apt-get update
RUN apt-get install -y libgl1-mesa-glx

# ワークディレクトリを設定
WORKDIR /app

# 必要なファイルをコピー
# Copy model into docker container
# COPY ./pose_estimator/model/pose_deploy_linevec.prototxt /app/pose_estimator/model/
# COPY ./pose_estimator/model/pose_iter_440000.caffemodel /app/pose_estimator/model/
ADD . /app
# COPY requirements.txt /app/

RUN pip install -r requirements.txt

CMD ["flask", "--app", "main", "run", "--host=0.0.0.0", "--reload"]
