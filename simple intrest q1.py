def simpleInterest(P, N, R):
    SI = (P * N * R)/100
    return SI
   
  
P = float(input("Enter the principal amount : "))
 
N = float(input("Enter the number of years : "))
 
R = float(input("Enter the rate of interest : "))
 
#calculate simple interest by using this formula
SI = simpleInterest(P, N, R)
 
#print
print("Simple interest : {}".format(SI))
