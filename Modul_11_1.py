import requests
import numpy
import matplotlib.pyplot as plt

#Составление запросов
r = requests.get('https://requests.readthedocs.io/en/latest/user/quickstart/')
r = requests.put('https://httpbin.org/put', data={'key': 'value'})
r = requests.delete('https://httpbin.org/delete')
r = requests.head('https://httpbin.org/get')
r = requests.options('https://httpbin.org/get')

# Получение json
rr = requests.get('https://api.github.com/events')
rr.json()

#Передача параметров в upl-адресе
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.url)
print()

print('Библиотека numpy:')
#Одномерный массив
a = numpy.array([1, 2, 3, 4, 5, 6])
print(f'Одномерный массив А: {a}')
print()
#Матрица (двумерный массив)
b = numpy.array([[1,2,3,4], [5,4,2,11], [9,8,7,20]])
print('Двумерный массив B:')
print(b)

print(f'Элемент массива B с номером (1, 4): {b[2, 3]}')
print()
print('Размерность массивов:')
nda = a.ndim
ndb = b.ndim
print(f'Размерность массива А: {nda}')
print(f'Размерность массива B: {ndb}')
print()
shb = b.shape
print(f'Количество строк и столбцов в массиве B: {shb}')

szb =b.size
print(f'Общее число элементов  в массиве B: {szb}')
print()
sorty = numpy.sort(b)
print ('Сортировка элементов массива B по строкам:')
print (sorty)

print()
c = numpy.arange(1, 20, 2)
print('Массив с диапазоном элементов от 1 до 20 с шагом 2:')
print(c)

print()
print('Библиотека matplotlib:')

# figure, axes = plt.subplots()
# axes.plot([1, 2, 3, 4, 5, 6, 7], [10, 8, 7, 7, 6, 5, 3])
# plt.show()

figure, axes = plt.subplots()
t = numpy.arange(0, 7, 0.1)
s = numpy.sin(t)
cs = numpy.cos(t)
axes.plot(t, s, color='red', linewidth=3, linestyle='--', label='синус')
axes.plot(t, cs, color='blue', linewidth=3, linestyle='-', label='косинус')
axes.grid(True)
axes.legend()
axes.set_title('График функций синус и косинус')
plt.xlabel('x label')
plt.ylabel('y label')
plt.show()


fig = plt.figure()
ax = fig.add_subplot(projection='3d')
X = numpy.arange(-5, 5, 0.15)
Y = numpy.arange(-5, 5, 0.15)
X, Y = numpy.meshgrid(X, Y)
R = numpy.sqrt(X**2 + Y**2)
Z = numpy.sin(R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis')





