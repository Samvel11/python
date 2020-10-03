import random

# a = int(input("input me the number and I ll tell .."))
# it_is_odd = a % 2 > 0
# it_is_even = a % 2 == 0
# print("it_is_even", it_is_even)
# print("it_is_odd", it_is_odd)   # kam ("  ",  not it is odd)



# a = input("tell me it is raining or shining   ")
# if  a == "raining":   
#     print("take an umbrella")
# elif a == "shining":  
#     print("take your sunglasses")
# else : 
#     print("dont take anything ") 

# print(a)    


# a = input("first number  ")
# b = input("second number")
# c = input("third number  ")

# if a > b and a > c :
# 	print(a)
# elif b > c :
#     print(b)
# else : 
#     print(c)    	



# a = input("input the word")
# if a.endswith("ing") :
# 	print("ing")
# else :
# 	print("not ing")


# a = input("input the word\n")
# if len(a) > 3 and  a[-3 : ] == "ing" :
# 	print(a[0 : len(a) -3] + "ly")


# a =  "asdfgh"
# b = a.find("a")
# if b != -1 :
#     print(a[0: b] + "0" + a[b+1 : ])


# a = input ("dfgdgdgd0")
# b = "dgggf"
# v = b.replace("g" , a)
# print(v)


# txt1 = "my name is {0} Im {1}".format("John", 55)
# print(txt1)



# a = "London is blue"
# print(a.index("is"))
# print(a.find("ist"))
# print(a.endswith("ds"))
# print(a.endswith("ue"))
# print(a.isalpha())
# print(a.isdigit())
# x = "5555"
# print(a.replace("blue",x))
# print(a.replace("blue","7755"))
# city= "Dvin"
# country = "Armenia"
# Sentence = f"{city} is a city in {country}"
# print(Sentence)
# print(chr(69))
# print(ord("6"))
# print(a.format("ddd"))

# a = int(input("input the number"))
# for i in range(1, 11) :
#     print("{} * {} = {}".format(a, i , a*i))




# a = input("number\n")
# b = 0
# for i in a :
# 	b += int(i)
# print(b)



# a = input("dsfd5644g")
# b = 0
# for i in a:
# 	if i.isdigit() :
# 		b += int(i)
# print(b)		


# a = range(0, 20, 3)
# b = range(20)
# c = 0
# d = 0
# for i in b :
# 	c += i
# for i in a :
# 	d += i
# print(d -c)	



# a = 0
# for i in range(1 , 21) :
# 	if a >= 15 :
#  		break
# 	a += i
# print(a)

# s = 0
# for i in range(10):
# 	if s > 14:	
# 		break
# 	s += i	
# print(s)		
# a = s
# b = s -i
# if a - 14 > 14-b:
# 	print(b)
# else:
# 	print(a)		


# a = int(input("input the number"))
# for i in range(1, 11) :
# 	print(F"{a} * {i} = {a*i}")



# b = 0
# a = range(20)
# for i in a:
# 	if i % 3 != 0 :
# 		b += i 
# print(b)

# b = 0
# for i in range(20):
# 	if i % 3 == 0:
# 		continue
# 	else :
# 		b += int(i)
# print(b)


# for i in range(1,11):
# 	for j in range (1 ,11):
# 		print(F"{i}*{j}={i*j}")

		
# for i in range(1, 11):
# 	if i % 2==0:
# 		continue
# 	for j in range(1,11):
# 		if j % 2 == 1:
# 			continue
# 		print(i + j, end = " ") 


# for i in range (1,5):
# 	for j in range(1, 7):
# 		print(i*str(j))


# for i in range(1,6):         
# 	for j in range (5,0,-1):
# 		print(j * str(i))

# for i in range (6):
# 	print(i* str(i))
# for i in range(4,0,-1):
# 	print(i * str(i))	


# for i in range(9):
# 	print(i * "*")
# 	if i == 6:
# 		for i in range(5, 0, -1):
# 			print(i *"*")
# 		break



# a = input("password\n")
# while  len(a) <= 8:
# 	a = input("password\n")
# print(a)


# a = input("password\n")
# while  len(a) <= 8:
# 	a = input("password\n")
# 	while "." not in a:
# 		a = input("password\n")	
# print(a)


# 2rd dzev

# while True:
# 	password = input("tell me password")
# 	if len(password) > 8:
# 	 	if "." in password:
# 	 		break                             # False
# print("it is good one!") 		



# a = random.randint(1,9)
# b = int(input("give me a number"))
# while a != b:
# 	b = int(input("give me a number"))
# print("fine")

# import random
# a = random.randint(1,9)
# b = int(input("give me a number"))
# while a != b :
# 	a = random.randint(1,9)
# 	b = int(input("give me a number"))
# print("fine")



# import random
# user_score = 0
# rounds = 0
# user_check = "yes"
# while user_check == "yes" :
# 	user_answer = int(input("guess the number\n"))
# 	random_number = random.randint(1,5)
# 	if user_answer == random_number:
# 		user_score += 1
# 	rounds += 1	
# 	user_check = input("do you want to play again: yes for yes!")
# print(f"your score is {user_score} you have played {rounds} time")




# def myfunction(a):
# 	b = F"Happy BIrthday  {a}"
# 	return b

# greeting = my_function("Tigran")
# print(greeting)





# def my_function(a,b):
# 	c = a +b
# 	return c

# print(myfunction(4,8))	


# def my_function():
# 	a = input("tell the name")
# 	b = F"Happy BIrthday  {a}"
# 	return b


# def sum1(a,b,c=0):
# 	v = a +b +c
# 	print(v)

# sum1(2,4,5)	
# sum1(5,6)



# v = "hello"
# def sum_1(a,b,c):
# 	global v

# 	v = a +b+c
# 	print(v)

# sum_1(2,1,4)



# help("random")


# def function(a):
# 	if a == 0:
# 		b = 1

# 	else:
# 		b = a * function(a-1)	

# 	return b

# print(function(5))	



# def factorial(a):
# 	a_1 = 1
# 	for i in range(1,a+1):
# 		a_1 *= i

# 	return a_1

# print(factorial_(5))





# def something(a,c):
# 	if c == 0:
# 		print("the second value not be zerro")
# 		return

# 	value = int(a/c)

# 	return value
	
# int_value = something(5,0)
# int_value = something(5,2)		
# print(int_value)



# def xoranard(a, b ,c = 1):
# 	v = a*b*c
# 	return v

# a_input = int(input("tell me the parameters "))
# b_input = int(input("tell me the parameters "))
# c_input =int(input("tell me the parameters "))

# volume_ = (a_input, b_input, c_input)
# # a = a_input[0]
# # b = a_input[1]
# # c = a_input[]
# print(xoranard(2,5))  



# def string_reverse(str1):
# 	reversik = ""
# 	i = len(str1)
# 	while i > 0:
# 		reversik += str1[i-1]
# 		i = i-1
# 	return reversik	
# a = string_reverse("sadf6554")
# print(a)

# print(string_reverse.__doc__)
# help(string_reverse)


# def some_function(argument1):
#     """Summary or Description of the Function

#     Parameters:
#     argument1 (int): Description of arg1

#     Returns:
#     int:Returning value

#    """

#     return argument1

# print(some_function.__doc__)


# help(some_function)


# a = ["aaa","sss",7,8,9,"ddd"]
# b = []
# for i in a:
# 	if a.index(i) % 2 == 0:
# 		b += [i]
# print(b)	

izmenenie
