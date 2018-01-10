from rot13 import rot13

"""
тестирует функцию шифрования алгоритмом rot13
"""

def test():
  assert rot13("hello") == "uryyb"
