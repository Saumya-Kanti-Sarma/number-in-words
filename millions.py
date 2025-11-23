from ds import ds as d
from random import randint
from thousands import thousands
from tens import tens
from hundreds import hundreds
def millions(x:int)->str:
  # Number smaller then 10 million
  if x < 99999999:
    n1 = x // 1000000
    x %= 1000000
    return f"{tens(n1)} million {thousands(x)}"
  # 10 million to 999.99 million
  else:
    n1 = x // 1000000
    x %= 1000000
    return f"{hundreds(n1)} million {thousands(x)}"

for i in range(10):
  x = randint(9999999,100000000)
  print(x,millions(x))
print(765432143,millions(765432143))