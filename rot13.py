def rot13(string):
  """
  DOCUMENTATION DOWN BELOW
  Функция для шифрования строки по алгоритму rot13
  """

  def roter(ch):
    i = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'.find(ch)
    if i != -1:
      return 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'[i]
    else:
      return ch

  return "".join(map(roter, string))

print(rot13('lbhat zna')) # young man
