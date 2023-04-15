import numpy as np
import matplotlib.pyplot as plt

A = 1         # амплитуда
ω = 2 * np.pi # угловая частота
φ = 0         # начальная фаза

t_start, t_end, dt = 0, 2, 0.01 # начало, конец и шаг по времени
t = np.arange(t_start, t_end, dt) # массив временных отсчетов

x = A * np.cos(ω * t + φ) # вычисление координаты для каждого временного отсчета

plt.plot(t, x) # построение графика
plt.xlabel('время') # подпись по оси x
plt.ylabel('координата') # подпись по оси y
plt.show() # вывод графика на экран