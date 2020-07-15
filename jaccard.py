import nltk
from nltk.corpus import wordnet

# Program to find the Jaccard similarity between two sentences


def pos_map(pos):
    # Mapping the pos_tag results to the wordnet parts of speech
    if pos[0] == 'V':
        return wordnet.VERB
    elif pos[0] == 'J':
        return wordnet.ADJ
    elif pos[0] == 'R':
        return wordnet.ADV
    else:
        return None


def lemma(parts_of_speech_set, lemmatized_set):
    for pair in parts_of_speech_set:
        # Lemmatizing words only if they are verbs, adverbs or adjectives
        if pos_map(pair[1]) is not None:
            lemmatized_set.add(lemmatizer.lemmatize(lemmatizer, pair[0], pos_map(pair[1])))
        else:
            lemmatized_set.add(pair[0])
    return lemmatized_set


if __name__ == '__main__':
    lemmatizer = nltk.WordNetLemmatizer
    lemmatized_a = set()
    lemmatized_b = set()

    print('Enter two sentences:')

    # Breaking down the input sentences into a set of words
    set_a = set(nltk.word_tokenize(input()))
    set_b = set(nltk.word_tokenize(input()))

    # Identifying the parts of speech for each word in both the sentences
    pos_a = nltk.pos_tag(set_a)
    pos_b = nltk.pos_tag(set_b)

    # Lemmatizing the verbs, adverbs and adjectives in both the sentences
    lemmatized_a = lemma(pos_a, lemmatized_a)
    lemmatized_b = lemma(pos_b, lemmatized_b)

    intersection = lemmatized_a.intersection(lemmatized_b)
    union = lemmatized_a.union(lemmatized_b)

    # Jaccard similarity is calculated by dividing the intersection of two sets with their union
    jaccard = len(intersection)/len(union)

    # The value of Jaccard similarity ranges between 0 and 1
    # Higher the Jaccard similarity, higher the sentence similarity
    print('Jaccard similarity: ', jaccard)
