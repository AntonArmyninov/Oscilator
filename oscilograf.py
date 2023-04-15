import numpy as np
import matplotlib.pyplot as plt

# Осцилограф
def f(t):
    A, w, u = 1, 2 * np.pi, 0 #задаем амплитуду, угловую частоту и начальную фазу
    length = t.shape[0]
    x = A * np.cos(w * t + u)
    return x

#Добавляем шум
def gaus(t):
    length = t.shape[0]  # длина массива t
    u, o = 0, 0.05
    noise = np.random.normal(u, o, size=length)
    return noise


t= np.linspace(0, 2, 100) #шаг графика

#x = A * np.cos(w * t + u) # вычисление координаты для каждого временного отсчета

plt.plot(t, f(t)) # построение графика
plt.plot(t, f(t)+gaus(t)) # построение графика
plt.xlabel('время') # подпись по оси x
plt.ylabel('координата') # подпись по оси y
plt.show() # вывод графика на экран