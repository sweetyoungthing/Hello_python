import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

def plot_sine():
    try:
        # 获取用户输入的 x 轴范围
        x_start = eval(x_start_entry.get())
        x_end = eval(x_end_entry.get())

        # 生成 x 值的范围
        x = np.linspace(x_start, x_end, 1000)

        # 计算对应的 y 值，y = sin(x)
        y = np.sin(x)

        # 清除之前的图像
        ax.clear()

        # 绘制图像
        ax.plot(x, y, label='y = sin(x)')

        # 添加标题和标签
        ax.set_title('Sine Function: y = sin(x)')
        ax.set_xlabel('x')
        ax.set_ylabel('y')

        # 显示图例，并将其放置在右上角
        ax.legend(loc='upper right')

        # 显示网格
        ax.grid(True)

        # 更新画布
        canvas.draw()

        # 更新状态标签
        status_label.config(text="Plot successful")
    except Exception as e:
        status_label.config(text=f"Error: {e}")

def save_image():
    # 保存图像为 PNG 文件
    file_name = "sine_function.png"
    fig.savefig(file_name)
    status_label.config(text=f"Image saved as {file_name}")

# 创建主窗口
root = tk.Tk()
root.title("Sine Function Plotter")

# 创建一个 Frame 来放置输入框和按钮
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

# 创建 x 轴范围的输入框
x_start_label = ttk.Label(frame, text="x Start:")
x_start_label.grid(row=0, column=0, padx=5, pady=5)
x_start_entry = ttk.Entry(frame)
x_start_entry.grid(row=0, column=1, padx=5, pady=5)
x_start_entry.insert(0, "-2*np.pi")

x_end_label = ttk.Label(frame, text="x End:")
x_end_label.grid(row=1, column=0, padx=5, pady=5)
x_end_entry = ttk.Entry(frame)
x_end_entry.grid(row=1, column=1, padx=5, pady=5)
x_end_entry.insert(0, "2*np.pi")

# 创建绘图按钮
plot_button = ttk.Button(frame, text="Plot Sine Function", command=plot_sine)
plot_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

# 创建保存图像按钮
save_button = ttk.Button(frame, text="Save Image", command=save_image)
save_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

# 创建状态标签
status_label = ttk.Label(frame, text="")
status_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# 创建 Matplotlib 图形和轴
fig, ax = plt.subplots()

# 创建画布并将图形嵌入到 Tkinter 窗口中
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# 运行主循环
root.mainloop()