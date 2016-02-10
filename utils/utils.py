__author__ = 'time'

import pickle


def pkl_plyr(player):
    with open('./plyr1.pkl', 'wb') as f:
        pickle.dump(player, f)


def unpkl_plyr():
    with open('./plyr1.pkl', 'rb') as f:
        Player1 = pickle.load(f)
    return Player1
