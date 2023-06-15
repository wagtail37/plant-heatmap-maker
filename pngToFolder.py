#出力したpngのヒートマップを一つのファイルにまとめる

import os
import shutil

def move_png_files(source_dir, destination_dir):
    # フォルダが存在しない場合は作成する
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # ソースディレクトリ内のファイルを走査
    for filename in os.listdir(source_dir):
        if filename.endswith('.png'):
            # PNGファイルの場合、新しいフォルダに移動する
            source_path = os.path.join(source_dir, filename)
            destination_path = os.path.join(destination_dir, filename)
            shutil.move(source_path, destination_path)
            print(f"Moved {filename} to {destination_dir}")

# 移動元ディレクトリと移動先ディレクトリのパスを指定
source_directory = 'C:\\Users\\wagta\\Documents\\SONY_CSL_RA\\Python_exe_folder\\git_sample'
destination_directory = 'C:\\Users\\wagta\\Documents\\SONY_CSL_RA\\Python_exe_folder\\git_sample\\pngFolder'

# PNGファイルを移動する
move_png_files(source_directory, destination_directory)

