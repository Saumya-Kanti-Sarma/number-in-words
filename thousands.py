from ds import ds as d
from tens import tens
from hundreds import hundreds
def thousands(x:int) -> str:
  if x < 10000:
    n1 = x //1000 # 1323 // 1000 =1
    x %= 1000 #1323 %1000 = 323
    n2 = x//100 #323 //100= 3
    x %= 100 # 323 % 10 = 23
    n3 = (x //10)*10 # 23 % 10 * 10 = 20
    x %=10
    return f"{d[n1]} thousand {d[n2]+' hundred ' if n2 != 0 else''}{d[n3]+' ' if n3!= 0 else''}{d[x]+' ' if x != 0 else''}"
  
  elif x < 100000:
    n1 = x //1000 # 1323 // 1000 =1
    n1 = tens(n1)
    x %= 1000 #1323 %1000 = 323
    n2 = x//100 #323 //100= 3
    x %= 100 # 323 % 10 = 23
    n3 = (x //10)*10 # 23 % 10 * 10 = 20
    x %=10
    return f"{n1} thousand {d[n2]+' hundred ' if n2 != 0 else''}{d[n3]+' ' if n3!= 0 else''}{d[x]+' ' if x != 0 else''}"
  
  else:
    n1 = x //1000 # 1323 // 1000 =1
    n1 = hundreds(n1)
    x %= 1000 #1323 %1000 = 323
    n2 = x//100 #323 //100= 3
    x %= 100 # 323 % 10 = 23
    n3 = (x //10)*10 # 23 % 10 * 10 = 20
    x %=10
    return f"{n1} thousand {d[n2]+' hundred ' if n2 != 0 else''}{d[n3]+' ' if n3!= 0 else''}{d[x]+' ' if x != 0 else''}"