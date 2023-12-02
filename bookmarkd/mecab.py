import MeCab
import collections

def wakati_text(text):
    # 取り出したい品詞
    select_conditions = ['名詞']

    # 分かち書きオブジェクト
    tagger = MeCab.Tagger('-Owakati')
    tagger.parse('')
    node = tagger.parseToNode(text)
    terms = []
    while node:
        # 単語
        term = node.surface
        # 品詞
        pos = node.feature.split(',')[0]
        # もし品詞が条件と一致してたら
        if pos in select_conditions:
            if len(term) >= 2:
                terms.append(term)
        node = node.next
    return terms

def get_url_tag(t):
    text = t
    c = collections.Counter(wakati_text(text)).most_common(10)
    dictions = [a[0] for a in c]
    d = ",".join(dictions)
    #wakati_text=wakati_text(text)
    return d