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