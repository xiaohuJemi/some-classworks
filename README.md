# classworks

本科课程作业合集，涵盖人工智能导论实验、岩石力学数据处理和 Pandas 练习题。

## 📁 目录结构

```
classworks/
├── ai_intro/                  # 人工智能导论实验
│   ├── calculator/            #   └─ 科学计算器 (tkinter GUI)
│   ├── tic_tac_toe/           #   └─ 人机对战井字棋 (Minimax)
│   └── eight_puzzle/          #   └─ 八数码问题 (A* 搜索)
├── rock_mechanics/            # 岩石力学实验数据处理
│   └── stress_functions.py    #   └─ 径向/环向应力函数绘图
├── pandas_exercises/          # Pandas 库练习题
│   ├── pandas_basics.py       #   └─ DataFrame 基础操作
│   └── data_aggregation.py    #   └─ groupby 分组聚合
├── requirements.txt
└── .gitignore
```

## 🧠 人工智能导论实验

### 科学计算器

基于 tkinter 的 GUI 科学计算器，支持四则运算、三角函数、阶乘、乘方、开方等运算，以及进制转换功能。

| 文件 | 说明 |
|---|---|
| `calculator_pro_max.py` | 初版实现，使用 `eval()` 求值 |
| `calculator_pro_max_optimized.py` | 优化版，使用 AST 安全解析求值，避免代码注入风险 |

```bash
# 启动计算器
python ai_intro/calculator/run_calculator.py

# 运行测试
python ai_intro/calculator/test_calculator.py
```

**功能特性：**
- ➕ 基本四则运算、取模、乘方
- 📐 三角函数（sin / cos / tan）
- √ 开方、阶乘
- π / e 常量支持
- 🔄 十进制 ↔ 二进制转换
- 🛡️ AST 安全求值（优化版）

### 井字棋（Tic-Tac-Toe）

人机对战的命令行井字棋游戏，AI 使用 **Minimax 极大极小算法**，能够做出最优决策（玩家无法获胜，最多平局）。

```bash
python ai_intro/tic_tac_toe/tic_tac_toe.py
```

### 八数码问题

使用 **A\* 启发式搜索算法**求解八数码问题。启发函数为曼哈顿距离，从初始状态自动搜索到目标状态并打印每一步的移动过程。

```bash
python ai_intro/eight_puzzle/eight_puzzle.py
```

## 🪨 岩石力学实验数据处理

绘制圆形硐室围岩的径向应力 σr 和环向应力 σθ 分布曲线，基于弹性力学解析解。

```bash
python rock_mechanics/stress_functions.py
```

输出图片 `stress_functions.png`。

## 🐼 Pandas 练习题

- **pandas_basics.py** — DataFrame 创建、行列操作、条件筛选
- **data_aggregation.py** — groupby 分组聚合（mean、sum、count 等）

```bash
python pandas_exercises/pandas_basics.py
python pandas_exercises/data_aggregation.py
```

## 🔧 环境配置

```bash
pip install -r requirements.txt
```

依赖：
- `numpy` — 数值计算
- `matplotlib` — 绘图
- `pandas` — 数据处理
- `tkinter` — Python 标准库，无需额外安装

## 📄 License

This project is for educational purposes.
