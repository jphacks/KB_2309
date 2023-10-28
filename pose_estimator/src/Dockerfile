# ベースイメージを選択
FROM python:3.8

RUN apt-get update
RUN apt-get install -y libgl1-mesa-glx

# ワークディレクトリを設定
WORKDIR /app

# Copy model into docker container
COPY model/pose_deploy_linevec.prototxt /app/
COPY model/pose_iter_440000.caffemodel /app/

# 必要なファイルをコピー
COPY requirements.txt /app/

# 依存関係をインストール
RUN pip install -r requirements.txt

WORKDIR /app/src

# アプリケーションを実行
CMD ["python", "app.py"]
