import numpy as np
import matplotlib.pyplot as plt

def line_data(data, color):
    if color == 'red':
        color = 'r--'    # 나만의 규칙으로 함수 만들기!

    plt.plot(data, data, color)

def bar.data(x_data, y_data):
    plt.bar(x_data, y_data)

def plot_show():
    plt.show()


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
langs = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [23,17,35,29,12]
ax.bar(langs,students)
plt.show()