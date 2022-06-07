def dog_age(h_age):
 """
 Write a function to calculate a dog's age in dog's years.
 """
 if h_age < 0:
 	exit()
 elif h_age <= 2:
	 d_age = h_age * 10.5
 else:
	 d_age = 21 + (h_age - 2)*4
 return d_age
