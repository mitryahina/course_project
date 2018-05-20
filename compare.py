from nltk.tokenize import TweetTokenizer
import re
import nltk
from nltk.corpus import wordnet, words, stopwords


def trend_tokenize(trd):
    """
    Function to tokenize twitter trends, including hashtags
    """
    if trd.name.startswith('#'):
        return split_hashtag(trd.name[1:])
    return TweetTokenizer().tokenize(trd.name)


def headline_tokenizing(hdl):
    """
    Tokenizing headlines
    """
    return hdl.title.split() + hdl.description.split()


def simple_compare(trend, headline):
    """
    Comparing word by word
    """
    for i in trend.name:
        if i.lower() in headline.title + headline.description:
            return True
    return False


def is_stop_word(word):
    """
    Check whether word is meaningful
    """
    return word in set(stopwords.words())


def find_synonyms(word):
    """
    Finding word's closest lemmas with wordnet
    """
    if not is_stop_word(word):
        synonyms = [word]
        for syn in wordnet.synsets(word):
            for l in syn.lemmas():
                synonyms.append(l.name())
        return set(synonyms)


def split_hashtag(hashtag):
    """
    Extracts meaningful lemmas from hashtag
    based on https://github.com/matchado/HashTagSplitter
    """

    # if every new word starts from uppercase letter e.g. #RoyalWedding
    if not hashtag.isupper() and not hashtag.islower():
        return re.findall('[A-Z][^A-Z]*', hashtag)

    # if words are divided by underscore sign e.g #royal_wedding
    if "_" in hashtag:
        return hashtag.split("_")

    # worst case, all letters are lowercase e.g #royalwedding
    hashtag = hashtag.lower()
    word_dictionary = list(set(words.words()))

    for alphabet in "bcdefghjklmnopqrstuvwxyz":
        word_dictionary.remove(alphabet)

    all_possibilities = []

    split_posibility = [hashtag[:i] in word_dictionary for i in reversed(range(len(hashtag)+1))]
    possible_split_positions = [i for i, x in enumerate(split_posibility) if x == True]

    for split_pos in possible_split_positions:
        split_words = []
        word_1, word_2 = hashtag[:len(hashtag)-split_pos], hashtag[len(hashtag)-split_pos:]

        if word_2 in word_dictionary:
            split_words.append(word_1)
            split_words.append(word_2)
            all_possibilities.append(split_words)

            another_round = split_hashtag(word_2)

            if len(another_round) > 0:
                all_possibilities = all_possibilities +\
                                    [[a1] + a2 for a1, a2, in zip([word_1]*len(another_round), another_round)]
        else:
            another_round = split_hashtag(word_2)

            if len(another_round) > 0:
                all_possibilities = all_possibilities +\
                                    [[a1] + a2 for a1, a2, in zip([word_1]*len(another_round), another_round)]
    return all_possibilities


def flatten(lst):
    """
    Flattens list of lists
    """
    res = []
    for i in lst:
        if isinstance(i, list):
            res.extend(i)
        else:
            res.append(i)
    return res


def extend(lst):
    """
    Extends the tokenized trend or headline with synonyms
    """
    lst = flatten(lst)
    inf = set(lst)
    for i in inf:
        try:
            inf = inf.union(find_synonyms(i))
        except TypeError:
            continue
    return inf


def pos_tag(words):
    """
    Is used for parts of speech tagging
    """
    res = []
    tagged = nltk.pos_tag(words)
    pos_tags = {'JJ': '.v.01', 'NN': '.n.01', 'VBD': '.v.01', 'IN': '.n.01',
                'NNP': '.n.01', 'VBP': '.v.01', 'DT': '.n.01', 'NNS': '.n.01',
                'MD': '.v.01', 'VB': '.v.01', 'VBN': '.v.01', 'CC': '.n.01',
                'RB': '.n.01', 'VBG': '.v.01', 'WRB': '.v.01', 'VBZ': '.v.01',
                'JJS': '.n.01', 'RBR': '.n.01', 'RP': '.n.01', 'FW': '.n.01'}
    for i in tagged:
        res.append(i[0] + pos_tags[i[1]])
    return res


def filter_stop_words(sentence):
    """
    Leaves only meaningful words
    """
    res = set()
    for word in sentence:
        if not is_stop_word(word):
            res.add(word)
    return res


def compare(headline, trend):
    """
    Main function for semantic comparing of headlines and  trends
    """
    sim_coef = 0
    headline = extend(headline_tokenizing(headline))
    headline = filter_stop_words(headline)
    trend = extend(trend_tokenize(trend))
    trend = filter_stop_words(trend)

    direct_matches = headline & trend
    # print(direct_matches)
    for i in trend:
        try:
            comparable1 = wordnet.synsets(i)[0]
            for j in headline:
                sim_coef += comparable1.path_similarity(wordnet.synsets(j)[0])
        except TypeError:
            continue
        except IndexError:
            continue
    sim_coef /= len(trend) + len(headline)
    return sim_coef
