def smallestLength(a):
	min1 = len(a[0])
	temp = a[0]

	for i in a:
		if(len(i) < min1):

			min1 = len(i)
			temp = i

	print("The word with the smallest length is:", temp,)
x=input("enter the first word:")
y=input("enter the second word:")
z=input("enter the third word:")
a=[x, y, z]
smallestLength(a)
