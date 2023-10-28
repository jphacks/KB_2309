# ベースイメージを選択
FROM python:3.9

# ワークディレクトリを設定
WORKDIR /app

# 必要なファイルをコピー
COPY app.py /app/
COPY requirements.txt /app/

RUN apt update -y && \
    apt install -y libopencv-dev git wget && \
    apt-get clean


COPY ./model /app/

# 依存関係をインストール
RUN pip install -r requirements.txt

# アプリケーションを実行
CMD ["python", "app.py"]

CMD ["python", "./model/try_openpose.py"]


