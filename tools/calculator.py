def calculate(expression: str) -> str:
    try:
        result = eval(expression, {"__builtins__": {}})
        return f"The answer is {result}"
    except Exception as e:
        return f"Sorry, I couldn't calculate that: {str(e)}"