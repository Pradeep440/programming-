def computeHCF(x,y):

  if x > y:
      smaller = y
  else:
      smaller = x

  for i in range(1, smaller+1):
      if((x % i == 0) and (y % i == 0)):
          hcf = i

  return hcf

(x,y)=(54,24)


print("The H.C.F. of", x,"and", y,"is", computeHCF(x, y))
