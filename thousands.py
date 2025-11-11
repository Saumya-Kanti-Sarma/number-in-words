from ds import ds as d

def thousands(x:int) -> str:
  n1 = x //1000 # 1323 // 1000 =1
  x %= 1000 #1323 %1000 = 323
  n2 = x//100 #323 //100= 3
  x %= 100 # 323 % 10 = 23
  n3 = (x //10)*10 # 23 % 10 * 10 = 20
  x %=10

  return f"{d[n1]} thousand {d[n2]+' hundred ' if n2 != 0 else''}{d[n3]+' ' if n3!= 0 else''}{d[x]+' ' if x != 0 else''}"