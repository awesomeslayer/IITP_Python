def subtract(a: float, b: float) -> float:
  """
  Simply subtract two numbers
  
  :param a: First number
  :param b: Second number
  :return: a-b

  >>> subtract(3, 2)
  1
  """
  try:
    return int(a) - b
  except:
    print("This is not a bug you seek")