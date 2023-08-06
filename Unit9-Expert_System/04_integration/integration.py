#  重要度が　wordfrequency > keyword　として計算しました
# 　引数として"main.py"からS_wfとS_kwを持ってくる。
#  引数として"count.py"の"find_unlikely"からmax_devの値を持ってくる。
#  重みと重要度は直観に従って設定したため必要な場合は変更します。

def integration(S_wf, S_kw, POS):
    value_wordfrequency = len(S_wf)
    value_keywordfrequency = len(S_kw)
    value_POS = POS
    w1 = 0.5  # 重み(wordfrequency)
    w2 = 0.2  # 重み(keyword)
    w3 = 0.3  # 重み (POS)
    totalvalue = value_wordfrequency * w1 + value_keywordfrequency * w2 + value_POS * w3

    return totalvalue

#  mainで追加するもの この関数をK1、K2で実行してK1のtatolvalue,K2のtotalvalueを出力して大きい値を本人とする(例　K1　> K2 K1を書いた人が本人）コード
#  example code
#  if (K1_totalvalue > K2_totalvalue):
#     print("K1 is same person who wrote Q")
#  else:
#     print("K2 is same person who wrote Q")
