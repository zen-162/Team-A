## s1290162 Zen Nakamura


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
def CreateDict_SharedWords(dict1, dict2, n=100):
    common_keys_dict = {key: dict1[key] for key in dict1.keys() if key in dict2}
    #common_keys = [key for key in dict1.keys() if key in dict2]
    common_keys = list(common_keys_dict)


    #n_items = {k: common_keys_dict[k] for k in list(common_keys_dict)[:n]}

    return common_keys_dict # n まで

# 共通している Word Frequencies のリストを出力
def wordFreq(S_dict):

    # word frequenciesの候補
    L_wf = ['a', 'an', 'the', 'I', 'you', 'he', 'she', 'my', 'me', 'mine', 'your', 'yours', 'his', 'him', 'her', 'hers', 'it', 'its', 'we', 'our', 'us', 'ours', 'they', 'their', 'them', 'theirs', 'this', 'that', 'there',
            'and', 'or', 'if', 'because', 'as', 'such', 'from', 'also', 'one', 'thus', 'into', 'whole', 'but', 'nor', 'yet', 'so', 'although', 'even', 'though', 'since', 'unless' 'until', 'whenever', 'wherever' 'whereas', 'while', 'both', 'either', 'neither', 'not', 'no', 'any', 'only' , 'very', 'too', 'rather' 'than', 'better', 'best', 'whether',
            'of', 'on', 'in', 'off', 'up', 'down', 'to', 'for', 'at', 'with', 'by', 'before' 'after', 'about', 'near', 'until', 'out',
            'be', 'is', 'are', 'was', 'were', 'would', 'where', 'which', 'what', 'why', 'how', 'who', 'whoes',
            'do', 'did', 'does', 'can', 'will', 'should', '']

    #S_wf = [element for element in S_List if element in L_wf] # dataset中の共通しているwordFrequencies
    S_wf = {key: S_dict[key] for key in L_wf if key in S_dict} # dataset中の共通しているwordFrequencies

    return S_wf

# 共通している Keyword Frequencies のリストを出力する
## (Output a list of common Keyword Frequnecies)
def keywordFreq(S_dict, S_wf):
    #S_kw = list(set(S_List) - set(S_wf))
    print(f'S_wf: {list(S_wf)[:20]}')

    S_kw = {key: S_dict[key] for key in list(S_wf) if key not in S_dict}
    S_kw = {key: S_dict[key] for key in S_dict.keys() if key not in S_wf}

    return S_kw


# if __name__ == "__main__":
#     main()
