import ast
import math
import tkinter as tk


APP_TITLE = "calculator_pro_max (optimized)"
WINDOW_GEOMETRY = "370x315+100+100"


class SafeEvaluator:
    def __init__(self):
        self._functions = {
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "sqrt": math.sqrt,
            "factorial": math.factorial,
        }
        self._constants = {
            "pi": math.pi,
            "e": math.e,
        }

    def evaluate(self, expr):
        expr = self._normalize(expr)
        if not expr:
            raise ValueError("empty expression")
        node = ast.parse(expr, mode="eval")
        return self._eval_node(node.body)

    def _normalize(self, expr):
        expr = expr.replace("MOD", "%")
        expr = expr.replace("^", "**")
        expr = self._apply_factorial(expr)
        return expr

    def _apply_factorial(self, expr):
        while "!" in expr:
            idx = expr.find("!")
            if idx == 0:
                raise ValueError("factorial missing operand")
            start = idx - 1
            if expr[start] == ")":
                depth = 1
                start -= 1
                while start >= 0 and depth > 0:
                    if expr[start] == ")":
                        depth += 1
                    elif expr[start] == "(":
                        depth -= 1
                    start -= 1
                start += 1
            else:
                while start >= 0 and (expr[start].isalnum() or expr[start] in "._"):
                    start -= 1
                start += 1
            operand = expr[start:idx]
            if not operand:
                raise ValueError("factorial missing operand")
            expr = expr[:start] + f"factorial({operand})" + expr[idx + 1 :]
        return expr

    def _eval_node(self, node):
        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return node.value
            raise ValueError("invalid constant")
        if isinstance(node, ast.Name):
            if node.id in self._constants:
                return self._constants[node.id]
            raise ValueError("unknown identifier")
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            value = self._eval_node(node.operand)
            return +value if isinstance(node.op, ast.UAdd) else -value
        if isinstance(node, ast.BinOp) and isinstance(
            node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Mod, ast.Pow)
        ):
            left = self._eval_node(node.left)
            right = self._eval_node(node.right)
            return self._apply_binop(node.op, left, right)
        if isinstance(node, ast.Call):
            if not isinstance(node.func, ast.Name):
                raise ValueError("invalid function")
            func_name = node.func.id
            if func_name not in self._functions:
                raise ValueError("unknown function")
            if node.keywords:
                raise ValueError("keywords not allowed")
            args = [self._eval_node(arg) for arg in node.args]
            return self._apply_function(func_name, args)
        raise ValueError("invalid expression")

    def _apply_binop(self, op, left, right):
        if isinstance(op, ast.Add):
            return left + right
        if isinstance(op, ast.Sub):
            return left - right
        if isinstance(op, ast.Mult):
            return left * right
        if isinstance(op, ast.Div):
            return left / right
        if isinstance(op, ast.Mod):
            return left % right
        if isinstance(op, ast.Pow):
            return left**right
        raise ValueError("unsupported operator")

    def _apply_function(self, name, args):
        if name == "factorial":
            if len(args) != 1:
                raise ValueError("factorial requires one argument")
            value = args[0]
            if not float(value).is_integer() or value < 0:
                raise ValueError("factorial requires non-negative integer")
            if value > 1000:
                raise ValueError("factorial too large")
            return math.factorial(int(value))
        if len(args) != 1:
            raise ValueError("function requires one argument")
        return self._functions[name](args[0])


class CalculatorApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(APP_TITLE)
        self.root.geometry(WINDOW_GEOMETRY)
        self.root.attributes("-alpha", 0.9)
        self.root.configure(background="white")

        self.result = tk.StringVar(value="")
        self.f1 = ("宋体", 20)
        self.f2 = ("宋体", 16)
        self.evaluator = SafeEvaluator()

        self._build_display()
        self._build_buttons()

    def run(self):
        self.root.mainloop()

    def _build_display(self):
        tk.Label(
            self.root,
            textvariable=self.result,
            font=self.f1,
            height=2,
            width=26,
            justify=tk.LEFT,
            anchor="se",
        ).grid(row=1, column=1, columnspan=5)

    def _build_buttons(self):
        buttons = [
            ("sin(", 2, 1, "green"),
            ("cos(", 2, 2, "green"),
            ("tan(", 2, 3, "green"),
            ("(", 2, 4, "green"),
            (")", 2, 5, "green"),
            ("!", 3, 1, "blue"),
            ("AC", 3, 2, "red"),
            ("CE", 3, 3, "grey"),
            ("MOD", 3, 4, "grey"),
            ("/", 3, 5, "grey"),
            ("^", 4, 1, "blue"),
            ("7", 4, 2, "yellow"),
            ("8", 4, 3, "yellow"),
            ("9", 4, 4, "yellow"),
            ("*", 4, 5, "grey"),
            ("sqrt(", 5, 1, "blue"),
            ("4", 5, 2, "yellow"),
            ("5", 5, 3, "yellow"),
            ("6", 5, 4, "yellow"),
            ("-", 5, 5, "grey"),
            ("pi", 6, 1, "blue"),
            ("1", 6, 2, "yellow"),
            ("2", 6, 3, "yellow"),
            ("3", 6, 4, "yellow"),
            ("+", 6, 5, "grey"),
            ("e", 7, 1, "blue"),
            ("0", 7, 2, "yellow"),
            ("00", 7, 3, "yellow"),
            (".", 7, 4, "yellow"),
            ("=", 7, 5, "orange"),
        ]

        for text, row, col, color in buttons:
            button = tk.Button(
                self.root,
                text=text,
                width=5,
                font=self.f2,
                relief=tk.FLAT,
                bg=color,
            )
            button.grid(row=row, column=col, padx=4, pady=2)
            self._bind_button(button, text)

        tk.Button(
            self.root,
            text="进制转换",
            width=8,
            font=self.f2,
            relief=tk.SOLID,
            bg="cyan",
            command=self._open_base_converter,
        ).grid(row=1, column=1, columnspan=2)

    def _bind_button(self, button, text):
        if text == "AC":
            button.config(command=self._clear)
        elif text == "CE":
            button.config(command=self._backspace)
        elif text == "=":
            button.config(command=self._calculate)
        else:
            button.config(command=lambda t=text: self._append(t))

    def _append(self, text):
        self.result.set(self.result.get() + text)

    def _clear(self):
        self.result.set("")

    def _backspace(self):
        self.result.set(self.result.get()[:-1])

    def _calculate(self):
        expr = self.result.get().strip()
        try:
            value = self.evaluator.evaluate(expr)
            value = round(value, 15)
            if abs(value) >= 10**16:
                self.result.set("Math ERROR")
            else:
                self.result.set(str(value))
        except Exception:
            self.result.set("Math ERROR")

    def _open_base_converter(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("进制转换")
        dialog.geometry(WINDOW_GEOMETRY)
        dialog.attributes("-alpha", 0.9)

        l1 = tk.Label(dialog, text="十进制数：", font=self.f2, width=26, height=2)
        l2 = tk.Label(dialog, text="二进制数：", font=self.f2, width=26, height=2)
        t1 = tk.Text(dialog, font=self.f1, width=26, height=2)
        t2 = tk.Text(dialog, font=self.f1, width=26, height=2)

        l1.grid(row=1, column=1, columnspan=3)
        t1.grid(row=2, column=1, columnspan=3)
        l2.grid(row=3, column=1, columnspan=3)
        t2.grid(row=4, column=1, columnspan=3)

        def clear1():
            t1.delete("1.0", "end")

        def clear2():
            t2.delete("1.0", "end")

        def transform():
            x = t1.get("1.0", "end").strip()
            y = t2.get("1.0", "end").strip()

            if not x and not y:
                return
            if y == "":
                try:
                    ans = bin(int(x))[2:]
                    t2.insert("1.0", ans)
                except ValueError:
                    t2.insert("1.0", "ERROR")
                return
            if x == "":
                try:
                    ans = int(y, 2)
                    t1.insert("1.0", str(ans))
                except ValueError:
                    t1.insert("1.0", "ERROR")
                return
            t1.delete("1.0", "end")
            t2.delete("1.0", "end")
            t1.insert("1.0", "ERROR")
            t2.insert("1.0", "ERROR")

        tk.Button(
            dialog,
            text="clear1",
            width=9,
            height=2,
            font=self.f2,
            relief=tk.FLAT,
            bg="red",
            command=clear1,
        ).grid(row=5, column=1, padx=6, pady=20)
        tk.Button(
            dialog,
            text="clear2",
            width=9,
            height=2,
            font=self.f2,
            relief=tk.FLAT,
            bg="red",
            command=clear2,
        ).grid(row=5, column=2, padx=6, pady=20)
        tk.Button(
            dialog,
            text="transform",
            width=9,
            height=2,
            font=self.f2,
            relief=tk.FLAT,
            bg="orange",
            command=transform,
        ).grid(row=5, column=3, padx=6, pady=20)


if __name__ == "__main__":
    CalculatorApp().run()

