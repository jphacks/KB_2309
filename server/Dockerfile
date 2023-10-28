# ベースイメージを選択
FROM python:3.9

# ワークディレクトリを設定
WORKDIR /app

# 必要なファイルをコピー
COPY main.py /app/
COPY requirements.txt /app/

# 依存関係をインストール
RUN pip install -r requirements.txt

# アプリケーションを実行
CMD ["flask", "--app", "main", "run", "--host=0.0.0.0"]
