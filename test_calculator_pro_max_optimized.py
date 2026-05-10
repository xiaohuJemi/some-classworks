from calculator_pro_max_optimized import SafeEvaluator


def _check(expr, expected):
    evaluator = SafeEvaluator()
    value = evaluator.evaluate(expr)
    assert round(value, 12) == expected, f"{expr} -> {value} (expected {expected})"


if __name__ == "__main__":
    _check("1+2*3", 7)
    _check("(1+2)*3", 9)
    _check("2^3", 8)
    _check("5 MOD 2", 1)
    _check("sin(pi/2)", 1)
    _check("sqrt(9)", 3)
    _check("5!", 120)
    _check("3+2!", 5)
    print("ok")

