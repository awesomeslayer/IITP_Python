def multiply(a: float, b: float) -> float:
  """
  Simply multiply two numbers

  :param a: First number
  :param b: Second number
  :return: a*b

  >>> multiply(3, 2)
  6
  """
  try:
    return a * b
  except:
    print("This is not a bug you seek")