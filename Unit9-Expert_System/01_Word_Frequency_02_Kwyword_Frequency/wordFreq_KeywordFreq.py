# Define function of WordFreq and KeywordFreq


# Datasetの文章を単語ごとに頻出数を数え、頻出数順にソートする
## (Count the number of occurrences of sentences in the Dataset word by word and sort them in order of frequency)
def count_word_frequency(text):
    # 文章を小文字に変換して、句読点などの特殊文字を削除します
    cleaned_text = ''.join(char.lower() if char.isalnum() else ' ' for char in text)

    # 単語ごとに区切ってリストにします
    words = cleaned_text.split()

    # 辞書型を作成して、単語の頻度を数えます
    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    # 頻度順にソートして、辞書型に格納します
    sorted_word_frequency = dict(sorted(word_frequency.items(), key=lambda item: item[1], reverse=True))

    return sorted_word_frequency


# ２つの辞書型変数のkey(word)が共通しているものから n 個をDict型として出力する
## (Output n dict types from two dictionary type variables with key(word) in coommon)
def CreateDict_SharedWords(dict1, dict2, n=1000):

    # n が辞書の大きさを超えているとき
    dict_size = min(len(dict1), len(dict2))
    if  dict_size < n:
        n = dict_size

    # n まで
    list1 = list(dict1)
    list2 = list(dict2)
    dict1_n = {key: dict1[key] for key in list1[:n]}
    dict2_n = {key: dict2[key] for key in list2[:n]}

    # word(key)が共通しているもの、出現頻度(value)は小さい方を用いる
    common_keys = set(dict1_n.keys()) & set(dict2_n.keys())
    common_keys_dict = {key: min(dict1_n[key], dict2_n[key]) for key in common_keys}

    return common_keys_dict

# 共通している Word Frequencies のリストを出力
def wordFreq(S_dict):

    # word frequenciesの候補（candidate of word frequencies）
    L_wf = ['a', 'an', 'the', 'I', 'you', 'he', 'she', 'my', 'me', 'mine', 'your', 'yours', 'his', 'him', 'her', 'hers', 'it', 'its', 'we', 'our', 'us', 'ours', 'they', 'their', 'them', 'theirs', 'this', 'that', 'there', 'other', 'others', 'another', 'another',
            'and', 'or', 'if', 'because', 'as', 'such', 'from', 'also', 'one', 'thus', 'into', 'whole', 'but', 'nor', 'yet', 'so', 'although', 'even', 'though', 'since', 'unless' 'until', 'whenever', 'wherever', 'whereas', 'while', 'both', 'either', 'neither', 'not', 'no', 'any', 'only' , 'very', 'too', 'some', 'many', 'lot', 'lots', 'all', 'rather', 'than', 'better', 'best', 'whether',
            'of', 'on', 'in', 'off', 'up', 'down', 'to', 'for', 'at', 'under', 'over', 'with', 'by', 'before', 'after', 'about', 'near', 'until', 'out',
            'which', 'what', 'why', 'when', 'how', 'who', 'whoes',
            'do', 'did', 'does', 'can', 'will', 'should', 'may', 'could', 'would', 'be', 'is', 'are', 'was', 'were', 'being']

    S_wf = {key: S_dict[key] for key in L_wf if key in S_dict} # dataset中の共通しているwordFrequencies

    return S_wf

# 共通している Keyword Frequencies のリストを出力する
## (Output a list of common Keyword Frequnecies)
def keywordFreq(S_dict, S_wf):
    #print(f'S_wf: {list(S_wf)[:20]}')

    S_kw = {key: S_dict[key] for key in list(S_wf) if key not in S_dict}
    S_kw = {key: S_dict[key] for key in S_dict.keys() if key not in S_wf}

    return S_kw


# if __name__ == "__main__":
#     main()
