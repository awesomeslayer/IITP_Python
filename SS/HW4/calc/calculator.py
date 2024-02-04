def calculate(expression : str) -> float:
  """
  Calculate arithmetic expression.
  
  :param expr: expression
  :return: calculated expression

  >>> calculate("3 + 2")
  5
  >>> calculate("2 + 2 * 2")
  6
  """
  try:
    return eval("".join(expression.split(" ")[:9]))
  except:
    print("This _might_ be a bug you seek")