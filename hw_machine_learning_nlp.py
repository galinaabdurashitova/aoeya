import re
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import mlab
from sklearn import grid_search, svm


with open('anna.txt', encoding='utf-8') as f:
    anna = f.read()
with open('sonets.txt', encoding='utf-8') as f:
    sonets = f.read()


# 1 часть

anna_sentences = re.split(r'(?:[.]\s*){3}|[.?!]', anna)
sonet_sentences = re.split(r'(?:[.]\s*){3}|[.?!]', sonets)


def lenwords(sentence):
    return [len(word) for word in sentence.split(' ')]


def count_different_letters(sentence):
    letters = []
    for letter in sentence:
        if letter not in letters:
            letters.append(letter)
    return len(letters)


def count_vowels(sentence):
    vowels = ['а', 'о', 'у', 'ы', 'э', 'я', 'ё', 'ю', 'и', 'е', 'a', 'e', 'y', 'u', 'i', 'o']
    num_vowels = 0
    for letter in sentence:
        if letter.lower() in vowels:
            num_vowels += 1
    return num_vowels


def count_vowels_word(sentence):
    sentence.split(' ')
    return [count_vowels(word) for word in sentence]


anna_data = []
for anna_sentence in anna_sentences:
    if len(anna_sentence) > 0:
        anna_data.append((len(anna_sentence), count_different_letters(anna_sentence), count_vowels(anna_sentence),
                          np.median(lenwords(anna_sentence)), np.median(count_vowels_word(anna_sentence))))


sonet_data = []
for sonet_sentence in sonet_sentences:
    if len(sonet_sentence) > 0:
        sonet_data.append((len(sonet_sentence), count_different_letters(sonet_sentence), count_vowels(sonet_sentence),
                           np.median(lenwords(sonet_sentence)), np.median(count_vowels_word(sonet_sentence))))

anna_data = np.array(anna_data)
sonet_data = np.array(sonet_data)
data = np.vstack((anna_data, sonet_data))


def show_result(data, c1, c2):
    p = mlab.PCA(data, True)
    N = len(anna_data)
    plt.figure()
    plt.plot(p.Y[:N, c1], p.Y[:N, c2], 'og', p.Y[N:, c1], p.Y[N:, c2], 'sb')
    plt.show()

# show_result(data, 0, 1)


# 2 часть

parameters = {'C': (.1, .5, 1.0, 1.5, 1.7, 2.0)}
gs = grid_search.GridSearchCV(svm.LinearSVC(), parameters)

# сдаюсь
gs.fit(data[:, 1:], data[:, 0])
print('Best result is ', gs.best_score_)
print('Best C is', gs.best_estimator_.C)

clf = svm.LinearSVC(C=gs.best_estimator_.C)
clf.fit(data[::2, 1:], data[::2, 0])


