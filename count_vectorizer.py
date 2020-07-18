from colorama import Fore
from scipy import spatial
from sklearn.feature_extraction.text import CountVectorizer

""""
Program to find the sentence similarity between two sentences using CountVectorizer
"""


if __name__ == '__main__':

    sentence_list = []
    print('Enter two sentences:')

    sentence_list.append(input())
    sentence_list.append(input())

    # Initializing CountVectorizer and training on the sentences
    vectorizer = CountVectorizer()
    tf = vectorizer.fit_transform(sentence_list)
    tf = tf.toarray()

    # tf[0] implies the vectorized form of the first input sentence
    # tf[1] implies the vectorized form of the second input sentence

    print(Fore.BLUE + 'Similarity based metrics')

    # Computing the cosine similarity
    cosine = 1 - spatial.distance.cosine(tf[0], tf[1])
    print(Fore.YELLOW + 'Cosine similarity: ', round(cosine, 2))

    # Computing the Jaccard similarity
    jaccard = 1 - spatial.distance.jaccard(tf[0], tf[1])
    print(Fore.YELLOW + 'Jaccard similarity: ', round(jaccard, 2))

    print(Fore.BLUE + 'Distance based metrics')

    # Computing the Euclidean distance
    euclidean = spatial.distance.euclidean(tf[0], tf[1])
    print(Fore.YELLOW + 'Euclidean distance: ', round(euclidean, 2))

    # Computing the Manhattan distance
    manhattan = spatial.distance.cityblock(tf[0], tf[1])
    print(Fore.YELLOW + 'Manhattan distance: ', round(manhattan, 2))
