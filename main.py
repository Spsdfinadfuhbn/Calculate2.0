b=int(input("Введи число:"))
c=int(input("Введи второе число:"))
a=input("Введи знак:")
if a=="*":
  print(c*b)
elif a=="-":
  print(c-b)
elif a=="+":
  print(c+b)
elif a=="/":
  try:
    print(c/b)
  except ZeroDivisionError:
   print("я так не умею")
  else:
    "break"