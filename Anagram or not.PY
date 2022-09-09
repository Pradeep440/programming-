def check(S , T):
	if(sorted(S)== sorted(T)):
		print("The strings are anagrams.")
	else:
		print("The strings aren't anagrams.")		
		

S = str('naveen: ')
T = str('naveen: ')
check(S , T)
