# -*- coding: utf-8 -*-


def get_w2v():
    import config
    from gensim.models import KeyedVectors
    w2v_path = config.w2v_path
    model = KeyedVectors.load_word2vec_format(w2v_path, binary=False)
    return model

