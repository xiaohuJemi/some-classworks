import numpy as np
import matplotlib.pyplot as plt

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用SimHei字体显示中文
plt.rcParams['axes.unicode_minus'] = False    # 正确显示负号

# 创建r/a的数据点
r_a = np.linspace(0.5, 3.0, 1000)

# 计算第一个函数: σr/p = 1/3 + 2/3*(r/a)^(-2) - (r/a)^(-4)
sigma_r_p = 1/3 + 2/3 * (r_a)**(-2) - (r_a)**(-4)

# 计算第二个函数: σθ/p = 1 + 2/3*(r/a)^(-2) + (r/a)^(-4)
sigma_theta_p = 1 + 2/3 * (r_a)**(-2) + (r_a)**(-4)

# 创建图形
plt.figure(figsize=(12, 10))

# 绘制第一个函数
plt.subplot(2, 1, 1)
plt.plot(r_a, sigma_r_p, 'r-', linewidth=2)
plt.grid(True)
plt.title('径向应力函数: σr/p = 1/3 + 2/3*(r/a)^(-2) - (r/a)^(-4)')
plt.xlabel('r/a')
plt.ylabel('σr/p')

# 绘制第二个函数
plt.subplot(2, 1, 2)
plt.plot(r_a, sigma_theta_p, 'b-', linewidth=2)
plt.grid(True)
plt.title('环向应力函数: σθ/p = 1 + 2/3*(r/a)^(-2) + (r/a)^(-4)')
plt.xlabel('r/a')
plt.ylabel('σθ/p')

plt.tight_layout()
plt.savefig('stress_functions.png', dpi=300)
plt.show()