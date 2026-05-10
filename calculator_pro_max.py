import tkinter as tk

# 开始编写框架代码
root = tk.Tk()
root.title('计算器promax')
root.geometry('370x315+100+100')

root.attributes('-alpha', 0.9)
root['background'] = 'white'

result_num = tk.StringVar()
result_num.set('')

f1 = ('宋体', 20)
f2 = ('宋体', 16)
tk.Label(root,
         textvariable=result_num, font=f1, height=2,
         width=26, justify=tk.LEFT, anchor='se'
         ).grid(row=1, column=1, columnspan=5)

b_sin = tk.Button(root, text='sin', width=5,
                  font=f2, relief=tk.FLAT, bg='green')
b_cos = tk.Button(root, text='cos', width=5,
                  font=f2, relief=tk.FLAT, bg='green')
b_tan = tk.Button(root, text='tan', width=5,
                  font=f2, relief=tk.FLAT, bg='green')
b_leftbracket = tk.Button(root, text='(', width=5,
                          font=f2, relief=tk.FLAT, bg='green')
b_rightbracket = tk.Button(root, text=')', width=5,
                           font=f2, relief=tk.FLAT, bg='green')

b_sin.grid(row=2, column=1, padx=4, pady=2)
b_cos.grid(row=2, column=2, padx=4, pady=2)
b_tan.grid(row=2, column=3, padx=4, pady=2)
b_leftbracket.grid(row=2, column=4, padx=4, pady=2)
b_rightbracket.grid(row=2, column=5, padx=4, pady=2)

b_factorial = tk.Button(root, text='!', width=5,
                        font=f2, relief=tk.FLAT, bg='blue')
b_clear = tk.Button(root, text='AC', width=5,
                    font=f2, relief=tk.FLAT, bg='red')
b_back = tk.Button(root, text='CE', width=5,
                   font=f2, relief=tk.FLAT, bg='grey')
b_mod = tk.Button(root, text='MOD', width=5,
                  font=f2, relief=tk.FLAT, bg='grey')
b_division = tk.Button(root, text='/', width=5,
                       font=f2, relief=tk.FLAT, bg='grey')

b_factorial.grid(row=3, column=1, padx=4, pady=2)
b_clear.grid(row=3, column=2, padx=4, pady=2)
b_back.grid(row=3, column=3, padx=4, pady=2)
b_mod.grid(row=3, column=4, padx=4, pady=2)
b_division.grid(row=3, column=5, padx=4, pady=2)

b_pow = tk.Button(root, text='^', width=5,
                  font=f2, relief=tk.FLAT, bg='blue')
b_seven = tk.Button(root, text='7', width=5,
                    font=f2, relief=tk.FLAT, bg='yellow')
b_eight = tk.Button(root, text='8', width=5,
                    font=f2, relief=tk.FLAT, bg='yellow')
b_nine = tk.Button(root, text='9', width=5,
                   font=f2, relief=tk.FLAT, bg='yellow')
b_multiplication = tk.Button(root, text='*', width=5,
                             font=f2, relief=tk.FLAT, bg='grey')

b_pow.grid(row=4, column=1, padx=4, pady=2)
b_seven.grid(row=4, column=2, padx=4, pady=2)
b_eight.grid(row=4, column=3, padx=4, pady=2)
b_nine.grid(row=4, column=4, padx=4, pady=2)
b_multiplication.grid(row=4, column=5, padx=4, pady=2)

b_sqrt = tk.Button(root, text='sqrt', width=5,
                   font=f2, relief=tk.FLAT, bg='blue')
b_four = tk.Button(root, text='4', width=5,
                   font=f2, relief=tk.FLAT, bg='yellow')
b_five = tk.Button(root, text='5', width=5,
                   font=f2, relief=tk.FLAT, bg='yellow')
b_six = tk.Button(root, text='6', width=5,
                  font=f2, relief=tk.FLAT, bg='yellow')
b_subtraction = tk.Button(root, text='-', width=5,
                          font=f2, relief=tk.FLAT, bg='grey')

b_sqrt.grid(row=5, column=1, padx=4, pady=2)
b_four.grid(row=5, column=2, padx=4, pady=2)
b_five.grid(row=5, column=3, padx=4, pady=2)
b_six.grid(row=5, column=4, padx=4, pady=2)
b_subtraction.grid(row=5, column=5, padx=4, pady=2)

b_pi = tk.Button(root, text='pi', width=5,
                 font=f2, relief=tk.FLAT, bg='blue')
b_one = tk.Button(root, text='1', width=5,
                  font=f2, relief=tk.FLAT, bg='yellow')
b_two = tk.Button(root, text='2', width=5,
                  font=f2, relief=tk.FLAT, bg='yellow')
b_three = tk.Button(root, text='3', width=5,
                    font=f2, relief=tk.FLAT, bg='yellow')
b_addition = tk.Button(root, text='+', width=5,
                       font=f2, relief=tk.FLAT, bg='grey')

b_pi.grid(row=6, column=1, padx=4, pady=2)
b_one.grid(row=6, column=2, padx=4, pady=2)
b_two.grid(row=6, column=3, padx=4, pady=2)
b_three.grid(row=6, column=4, padx=4, pady=2)
b_addition.grid(row=6, column=5, padx=4, pady=2)

b_e = tk.Button(root, text='e', width=5,
                font=f2, relief=tk.FLAT, bg='blue')
b_zero = tk.Button(root, text='0', width=5,
                   font=f2, relief=tk.FLAT, bg='yellow')
b_doublezero = tk.Button(root, text='00', width=5,
                         font=f2, relief=tk.FLAT, bg='yellow')
b_dot = tk.Button(root, text='.', width=5,
                  font=f2, relief=tk.FLAT, bg='yellow')
b_equal = tk.Button(root, text='=', width=5,
                    font=f2, relief=tk.FLAT, bg='orange')

b_e.grid(row=7, column=1, padx=4, pady=2)
b_zero.grid(row=7, column=2, padx=4, pady=2)
b_doublezero.grid(row=7, column=3, padx=4, pady=2)
b_dot.grid(row=7, column=4, padx=4, pady=2)
b_equal.grid(row=7, column=5, padx=4, pady=2)


# 开始编写逻辑代码
def click_button(x):
    result_num.set(result_num.get() + x)


b_one.config(command=lambda: click_button('1'))
b_two.config(command=lambda: click_button('2'))
b_three.config(command=lambda: click_button('3'))
b_four.config(command=lambda: click_button('4'))
b_five.config(command=lambda: click_button('5'))
b_six.config(command=lambda: click_button('6'))
b_seven.config(command=lambda: click_button('7'))
b_eight.config(command=lambda: click_button('8'))
b_nine.config(command=lambda: click_button('9'))
b_zero.config(command=lambda: click_button('0'))
b_doublezero.config(command=lambda: click_button('00'))
b_dot.config(command=lambda: click_button('.'))
b_addition.config(command=lambda: click_button('+'))
b_subtraction.config(command=lambda: click_button('-'))
b_multiplication.config(command=lambda: click_button('*'))
b_division.config(command=lambda: click_button('/'))
b_equal.config(command=lambda: click_button('='))
b_mod.config(command=lambda: click_button('MOD'))
b_leftbracket.config(command=lambda: click_button('('))
b_rightbracket.config(command=lambda: click_button(')'))
b_sin.config(command=lambda: click_button('sin'))
b_cos.config(command=lambda: click_button('cos'))
b_tan.config(command=lambda: click_button('tan'))
b_factorial.config(command=lambda: click_button('!'))
b_pow.config(command=lambda: click_button('^'))
b_sqrt.config(command=lambda: click_button('sqrt'))
b_pi.config(command=lambda: click_button('pi'))
b_e.config(command=lambda: click_button('e'))
# 以上实现所有button的基础功能

import math


def caculation():
    opt_str = result_num.get()
    if '**' in opt_str or '//' in opt_str or '!!' in opt_str:
        result_num.set('Syntax ERROR')
        return
    if 'MOD' in opt_str:
        opt_str = opt_str.replace('MOD', '%')
    if 'pi' in opt_str:
        opt_str = opt_str.replace('pi', 'math.pi')
    if 'e' in opt_str:
        opt_str = opt_str.replace('e', 'math.e')
    if 'sin' in opt_str:
        opt_str = opt_str.replace('sin', 'math.sin(') + ')'
    if 'cos' in opt_str:
        opt_str = opt_str.replace('cos', 'math.cos(') + ')'
    if 'tan' in opt_str:
        opt_str = opt_str.replace('tan', 'math.tan(') + ')'
    if 'sqrt' in opt_str:
        opt_str = opt_str.replace('sqrt', 'math.sqrt(') + ')'
    if '!' in opt_str:
        opt_str = 'math.factorial(' + opt_str.replace('!', '') + ')'
    if '^' in opt_str:
        lst = opt_str.split('^')
        if len(lst) > 2:
            result_num.set('Math ERROR')
            return
        opt_str = 'math.pow(' + lst[0] + ', ' + lst[1] + ')'
    try:
        res = round(eval(opt_str), 15)
        if abs(res) >= 10 ** 16:
            result_num.set('Math ERROR')
        else:
            result_num.set(str(res))
    except:
        result_num.set('Math ERROR')


b_equal.config(command=caculation)


# 以上实现等号功能

def clear():
    result_num.set('')


b_clear.config(command=clear)


# 以上实现AC功能

def back():
    x = result_num.get()
    x = x[:-1]
    result_num.set(x)


b_back.config(command=back)


# 以上实现CE功能


# 添加进制转换功能：

def new_window():
    # 开始编写进制转换的框架代码
    root1 = tk.Tk()
    root1.title('进制转换')
    root1.geometry('370x315+100+100')
    root1.attributes('-alpha', 0.9)

    l1 = tk.Label(root1, text='十进制数：',
                  font=f2, width=26, height=2)
    l2 = tk.Label(root1, text='二进制数：',
                  font=f2, width=26, height=2)
    t1 = tk.Text(root1, font=f1, width=26, height=2)
    t2 = tk.Text(root1, font=f1, width=26, height=2)

    l1.grid(row=1, column=1, columnspan=3)
    t1.grid(row=2, column=1, columnspan=3)
    l2.grid(row=3, column=1, columnspan=3)
    t2.grid(row=4, column=1, columnspan=3)

    # 开始编写进制转换的逻辑代码
    def clear1():
        t1.delete('1.0', 'end')

    def clear2():
        t2.delete('1.0', 'end')

    def transform():
        x = t1.get('1.0', 'end').replace('\n', '')
        y = t2.get('1.0', 'end').replace('\n', '')

        if x == y == '':
            return
        elif y == '':
            try:
                ans = bin(int(x))[2:]
                t2.insert('1.0', ans)
            except:
                t2.insert('1.0', 'ERROR')
        elif x == '':
            try:
                ans = int(y, 2)
                t1.insert('1.0', str(ans))
            except:
                t1.insert('1.0', 'ERROR')
        else:
            t1.delete('1.0', 'end')
            t2.delete('1.0', 'end')
            t1.insert('1.0', 'ERROR')
            t2.insert('1.0', 'ERROR')

    b_clear1 = tk.Button(root1, text='clear1', width=9, height=2,
                         font=f2, relief=tk.FLAT, bg='red',
                         command=clear1)
    b_clear2 = tk.Button(root1, text='clear2', width=9, height=2,
                         font=f2, relief=tk.FLAT, bg='red',
                         command=clear2)
    b_transform = tk.Button(root1, text='transform', width=9, height=2,
                            font=f2, relief=tk.FLAT, bg='orange',
                            command=transform)

    b_clear1.grid(row=5, column=1,
                  padx=6, pady=20)
    b_clear2.grid(row=5, column=2,
                  padx=6, pady=20)
    b_transform.grid(row=5, column=3,
                     padx=6, pady=20)

    root1.mainloop()


b = tk.Button(root, text='进制转换', width=8,
              font=f2, relief=tk.SOLID,
              bg='cyan', command=new_window)
b.grid(row=1, column=1, columnspan=2)

root.mainloop()








