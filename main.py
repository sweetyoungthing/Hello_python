import numpy as np
import matplotlib.pyplot as plt

# 生成 x 值的范围，从 -2π 到 2π
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# 计算对应的 y 值，y = sin(x)
y = np.sin(x)

# 绘制图像
plt.plot(x, y, label='y = sin(x)')

# 添加标题和标签
plt.title('Sine Function: y = sin(x)')
plt.xlabel('x')
plt.ylabel('y')

# 显示图例
plt.legend()

# 显示网格
plt.grid(True)

# 显示图像
plt.show()