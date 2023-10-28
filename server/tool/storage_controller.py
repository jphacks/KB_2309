import os 

storage_dir = './storage'  # ストレージディレクトリのパスを指定

def get_dir_path(dir_name):
    subdirectory_path = os.path.join(storage_dir, dir_name)

    # 同じ名前のディレクトリが存在しない場合、新しく作成
    if not os.path.exists(subdirectory_path):
        os.mkdir(subdirectory_path)

    return subdirectory_path