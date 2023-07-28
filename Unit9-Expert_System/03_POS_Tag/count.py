# TODO
# count the number of identical POS patterns in each dataset
# identify the least similiar dataset based on the number of identical POS patterns with questionned dataset
# suggest ruling out the least similiar dataset

import nltk

sentence = """At eight o'clock on Thursday morning
              Arthur didn't feel very good."""
tokens = nltk.word_tokenize(sentence)

tagged_1 = nltk.pos_tag(tokens)
tagged_2 = nltk.pos_tag(tokens)
tagged_q = nltk.pos_tag(tokens)

def count_pos(tagged:list):
    pn_dict = {}
    for tp in tagged:
        if tp[1] in pn_dict.keys():
            pn_dict[tp[1]] += 1
        else:
            pn_dict[tp[1]] = 1
    return pn_dict

pn_dict_1 = count_pos(tagged_1)
pn_dict_2 = count_pos(tagged_2)
pn_dict_q = count_pos(tagged_q)
