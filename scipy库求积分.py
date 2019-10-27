from scipy import integrate
import numpy as np
from numpy import  *
import time
def f(x):
    return eval(str_hs)
l_min = eval(input('请输入积分上限：'))    #积分上限
l_max = eval(input('请输入积分下限：'))    #积分下限
str_hs = input('请输入被积分函数')         #被积函数
start = time.perf_counter()
v, err = integrate.quad(f, l_min, l_max)
end = time.perf_counter()
print("积分结果为：",v)
print("误差为：",err)
print("运算时间为",end-start)

# 画出函数图像
import numpy as np, matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
fig, ax = plt.subplots(figsize=(8, 3))
x = np.linspace(l_min, l_max, 10000)
ax.plot(x, f(x), lw=2)
ax.fill_between(x, f(x), color='green', alpha=0.5)
ax.set_xlabel("$x$", fontsize=18)
ax.set_ylabel("$f(x)$", fontsize=18)
plt.show()