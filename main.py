import numpy as np
import matplotlib.pyplot as plt
import math

#определение функции s(k), которая создает сигнал из случайных чисел
def s(k):
    length = k.shape[0] # длина массива k
    randoms = np.random.random((length)) # создание случайных чисел
    signal = (k > randoms).astype(float) # создание сигнала на основе сравнения k и randoms
    return signal

#создание массива k, который начинается с -1 и заканчивается на 1, включая 100 равных промежутков
k = np.linspace(-1, 1, 100)

#создание графика
fig, ax = plt.subplots(figsize=(16, 9)) # создание контейнера для графика с определенным размером
ax.plot(k, s(k), label='s(k)') # добавление графика для сигнала s(k)
ax.set_xlabel('k') # добавление подписи для оси x
ax.set_ylabel('v') # добавление подписи для оси y
ax.set_title('Непериодический сигнал s(k)') # добавление заголовка графика
ax.legend(); # добавление легенды

plt.show() # вывод графика на экран