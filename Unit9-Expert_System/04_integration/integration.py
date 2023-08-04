#  重要度が　wordfrequency > keyword　として計算しました
# 　main.pyからS_wfとS_kwを持ってくる。
#  重みと重要度は直観に従って設定したため必要な場合は変更します。

def integration(S_wf, S_kw):
    value_wordfrequency = len(S_wf)
    value_keywordfrequency = len(S_kw)
    w1 = 0.7  # 重み
    w2 = 0.3  # 重み
    totalvalue = value_wordfrequency * w1 + value_keywordfrequency * w2

    return totalvalue

#  mainで追加するもの この関数をK1、K2で実行してK1のtatolvalue,K2のtotalvalueを出力して大きい値を本人とする(例　K1　> K2 K1を書いた人が本人）コード
#  example code
#  if (K1_totalvalue > K2_totalvalue):
#     print("K1 is same person who wrote Q")
#  else:
#     print("K2 is same person who wrote Q")

