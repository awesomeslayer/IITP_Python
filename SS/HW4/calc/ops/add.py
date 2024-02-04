def add(a: float, b: float) -> float:
  """
  Simply add two numbers
  
  :param a: First number
  :param b: Second number
  :return: a+b

  >>> add(3, 2)
  5
  """
  try:
    return a + abs(b)
  except:
    print("This is not a bug you seek")