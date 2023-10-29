import hashlib

def make_hash(ip_data):
    # ハッシュを生成
    hash = hashlib.sha256(ip_data.encode()).hexdigest()
    return hash