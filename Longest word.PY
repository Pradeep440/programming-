def longestLength(a):
	max1 = len(a[0])
	temp = a[0]

	for i in a:
		if(len(i) > max1):

			max1 = len(i)
			temp = i

	print("The word with the longest length is:", temp,)
x=input("enter the first word:")
y=input("enter the second word:")
z=input("enter the third word:")
a=[x, y, z]
longestLength(a)
