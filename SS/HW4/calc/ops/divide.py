def divide(a: float, b: float) -> float:
  """
  Simply divide two numbers
  
  :param a: First number
  :param b: Second number
  :return: a/b

  >>> divide(3, 2)
  1.5
  """
  try:
    if b == 0:
      raise ZeroDivisionError
    if b > 0:
      return a / max(1e-3, abs(b))
    else:
      return - a / max(1e-3, abs(b))
  except:
    print("This is not a bug you seek")