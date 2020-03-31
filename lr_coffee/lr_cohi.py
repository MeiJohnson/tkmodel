import math

def f(l, x, y):
  return eval(l)

def getData():
  data = open("/home/asya/Документы/Github/model/lr_coffee/a.in")
  
  data_list = []
  for line in data:
    data_list.append(line)
  
  l = data_list[0]
  print("Введите функцию ", l, end = "")

  a = float(data_list[1])
  print("Введите a ", a)
  
  b = float(data_list[2])
  print("Введите b ", b)

  y0 = float(data_list[3])
  print("Введите y0 ", y0)
  
  n = float(data_list[4])
  print("Введите n ", n)
  
  h = (b - a) / n
  data.close()
  
  res = [l, a, b, y0, n, h]

  return res

def eiler():
  """
  src[0] - функция
  src[1] - a
  src[2] - b
  src[3] - y0
  src[4] - n
  src[5] - h

  """
  src = getData()
  print("x = ",src[1],"y = ", src[3], "h = ", src[5])
  x = src[1]
  y = src[3]
  
  eps = src[2] - src[5]
  
  while x <= eps:
    print("x = ",round(x, 3), "y = ",round(y, 3))
    y += src[5] * f(src[0], x, y)
    x += src[5]
  print(x,y)
  submenu()  
  return x,y

def menu(): 

  print("Главное меню")
  print("1.Метод Эйлера")
  print("2.Выход")
  
  num = int(input("Введите номер "))
  
  if num == 1:
    eiler()
  if num == 2:
    exit()

def submenu(): 
  print("Подменю")
  print("1.В главное меню")
  print("2.Выход")
  num = int(input("Введите номер "))
  if num == 1:
      menu()
  if num == 2:
      exit()

def main():
  menu()
  

if __name__ == "__main__":
  main()