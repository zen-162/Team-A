import os
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

def get_pos_tags(filename, fileplace='Unit9/Datasets'):
    # ファイル名が.txtで終わることを確認
    if not filename.endswith(".txt"):
        filename += ".txt"

    # ファイルが存在することを確認
    if not os.path.exists(os.path.join(fileplace, filename)):
        raise FileNotFoundError(f"No such file or directory: '{filename}'")

    with open(os.path.join(fileplace, filename), 'r') as file:
        text = file.read()

    # テキストを単語に分割
    words = word_tokenize(text)

    # 各単語に品詞タグを付ける
    tagged_words = pos_tag(words)

    fileplace = 'Unit9/Datasets'
    new_fileplace = 'Unit9/POS_Datasets'

    # 新しいディレクトリが存在しない場合、作成する
    if not os.path.exists(new_fileplace):
        os.makedirs(new_fileplace)

    # 空白をアンダーバーに変換した新しいファイル名を作成
    new_filename = "POS_" + filename.replace(" ", "_")

    # 新しいテキストファイルに出力
    with open(os.path.join(new_fileplace, new_filename), 'w') as new_file:
            for word, pos in tagged_words:
                new_file.write(f"({word}, {pos}), ")

    return tagged_words
