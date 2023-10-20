def faktorial(a):
  if a == 1:
    return a
  else:
    return a* faktorial(a-1)

a = int(input(":"))
print(faktorial(a))
