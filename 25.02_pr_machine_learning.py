import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# 1 задание: открытие файла, нахождение вероятностей выжить
with open('titanic.csv', 'r') as f:
    titanic_data = csv.DictReader(f)
    titanic_data = pd.DataFrame(list(titanic_data))


def simple_chance_count(data, fieldname1, fieldname2, name):
    result = data[data[fieldname1].str.contains(r'^' + name)]
    return np.mean(np.array(result[fieldname2]).astype(np.float))


# a) вероятность выжить для мужчин и женщин - график
def task_1a(data):
    plt.figure()
    plt.bar(0, simple_chance_count(data, 'Sex', 'Survived', 'male'), color='red')
    plt.bar(1, simple_chance_count(data, 'Sex', 'Survived', 'female'), color='green')
    plt.show()
# task_1a(titanic_data)
# Значительно больше шанс выжить у женщин


# б) вероятность выжить для пассажиров разных социально-экономических классов - график
def task_1b(data):
    plt.figure()
    plt.bar(1, simple_chance_count(data, 'Pclass', 'Survived', '1'), color='red')
    plt.bar(2, simple_chance_count(data, 'Pclass', 'Survived', '2'), color='green')
    plt.bar(3, simple_chance_count(data, 'Pclass', 'Survived', '3'), color='blue')
    plt.show()
# task_1b(titanic_data)
# Чем выше социально-материальное положение человека, тем больше шанс выжить


# в) стоимость билета в зависимости от социально-экономического класса - график
def task_1c(data):
    plt.figure()
    plt.bar(1, simple_chance_count(data, 'Pclass', 'Fare', '1'), color='red')
    plt.bar(2, simple_chance_count(data, 'Pclass', 'Fare', '2'), color='green')
    plt.bar(3, simple_chance_count(data, 'Pclass', 'Fare', '3'), color='blue')
    plt.show()
# task_1c(titanic_data)
# Стоимость билета в первый класс значительно выше, чем стоимость других билетов


# 2 задание: средняя вероятность выжить в зависимости от пола и соц. статуса - график
def chance_count_2variables(data, fieldname1, fieldname2, fieldname3, name1, name2):
    result = data[(data[fieldname1].str.contains(r'^' + name1)) & (data[fieldname2].str.contains(r'^' + name2))]
    return np.mean(np.array(result[fieldname3]).astype(np.float))


def task_2(data):
    fem_result = [chance_count_2variables(data, 'Sex', 'Pclass', 'Survived', 'female', str(i)) for i in range(1, 4)]
    m_result = [chance_count_2variables(data, 'Sex', 'Pclass', 'Survived', 'male', str(i)) for i in range(1, 4)]

    locs = np.arange(1, len(fem_result)+1)
    width = 0.4
    plt.bar(locs+width, fem_result, width=width)
    plt.bar(locs+width*2, m_result, width=width, color='red')
    plt.xticks(locs + width*1.5, locs)
    plt.show()
# task_2(titanic_data)
