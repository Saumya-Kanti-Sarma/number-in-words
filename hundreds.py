from ds import ds as d
from Tens import tens

def hundreds(x:int) -> str:
  n1 = x //100 # 132 // 100 =1
  n2 = x % 100 # 132 % 100 = 32
  return f"{d[n1]} hundred {tens(n2) if n2 !=0 else ""}"  