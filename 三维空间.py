import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 创建图形和三维坐标轴
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 定义螺旋线的参数方程
t = np.linspace(0, 10 * np.pi, 1000)
x = t
y = t
z = 1.5*t**2

# 绘制三维曲线
ax.plot(x, y, z, label='3D Helix Curve')

# 设置坐标轴标签
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# 设置标题
plt.title('3D Curve Plot')

# 显示图形
plt.show()
