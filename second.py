# a = ("aaa","sss",5,7)
# value = ""
# for i in a:
# 	value += str(i)
# print(value)


# b = ["4", "5", "9", "7"]	
# f = 0
# for i  in b:
# 	if i.isdigit and int(i) > 5:
# 		f += int(i)
# 	print(f)



# def functin_(a):
# 	b = 0
# 	for i in a:
# 		if i % 2 == 0:
# 			b += i
		
# 			return b	

# b = [2,4,5,6,7]
# print(functin_(b))	


# my_list = ["aa","ss",5,7,]
# index = 2
# value = "new_one"
# my_list.insert(index, value)
# print(my_list)


# my_list.pop(1)
# print(my_list)


	

# a = [1,2,3]

# a[1] = [4.1,4.2,4.3]
# print(a)

# print(a[1:2])
# print(a[1:3])

# a[1:2] = [4.1,4.2,4.3]
# print(a)

# a[3:3] = [7.1,7.2,7.3]
# print(a)

# a[1:4] = [4.0,4.2,4.3,7]
# print(a) 



# number = input("tell me a number and I'll return the half of it\n")
# try:
# 	half = int(number) / 2
# except ValueError:
# 	print("tell correct number")	



# num_1 = int(input("tell me a number to devide 4 with"))
# try: 
# 	new_value = 4 / num_1
# except ZeroDivisionError:
# 	print("not / 0")


# try: 
# 	print(hello)
# except NameError:
# 	hello = "hello"
# 	print(hello)


# my_list = [1,2,"hello"]	
# try: 
# 	item = my_list[9]
# except IndexError:
# 	print("write wright index")	



# input_ = input("tell me a number")

# try:
# 	input_ = int(input_)
# except ValueError:	
# 	input_ = input("tell me a number")

# try:
# 	input_ = int(input_)
# except:
# 	print("ok ypur value will be 1 by default!")
# 	input_1 = 1

# summery = input_ + 5	

				

 # parol enq dnum vor 1)erkarutyuny >8   2)sksuma mecatarov 
 # 3)mejy kam ka tiv kam nshan   4)bacat chlini

# check = True
# while check:
# 	try:
# 		password = input("Tell me password  ")

# 		if len(password) < 8:
# 			raise Exception("It should be greater than 8")

# 		if ' ' in password:
# 			raise Exception("The password could not contanin a space ")
	
		
# 		if password[0].islower():
# 			raise Exception("Sould start with a capital letter")
# 		check = False				
# 	except Exception as error:
# 		print(error)

# print(F"{password} ")	 				


# i = 14
# try: 
# 	5 / (i-14)
# except Exception:
# 	print("rrrrrrhhh")

# [[2, 0, 0], 
#  [0, 1, 0], 
#  [0, 0, 0]]


# # dict1 = {"qqq":1, "key":2}
# dict2 = {"key1":10, "key3":1, "key4":2}
# dict3 = {}

# for key in dict2:
# 	dict1[key] = dict2[key]

# print(dict1)
# print(dict2)	

# for i in dict1:
# 	dict3[i] = dict1[i]

# for j in dict2:
# 	dict3[j]= dict2[j]	

# print(dict3)	


# b = [dict1,dict2,dict3]
# for newdict in b: 
# 	for key in newdict:
# 		dict3[key] = newdict[key]
# print(newdict)
# print(dict3)	

# dict2.pop("key1")
# print(dict2)	


# a = (4,5,5,6,7,99)


# a += (9,8)
# print(a)
# b = list(a)
# b.append(899,)
# a = tuple(b)
# print(a)

# a = [55,"saas",55,55,55, "gf"]
# b = set(a)   # { 55 "saas"  gf}
# c = list(b)
# print(c)
# a += ["sdd",55 ,66]

# a.append("qwefd")
# a.extand(b)

# del a[2]
# remove("gf")

# print('fff','egfs','dvfdg')
# 55,566,"gfg"


Employees = {
	"emp1":{"name":"John", "salary": 7500},
	"emp2":{"name":"Emma", "salary": 8000},
	"emp3":{"name":"brad", "salary": 6500},
}
print(Employees)
lst = ["emp1","emp2","emp3"]
average_salary = int((Employees["emp1"]["salary"] + Employees["emp2"]["salary"] + Employees["emp3"]["salary"]) * 1/3)
for i in lst:
	for keys in i:
		Employees[i]["salary"] = average_salary
print(Employees)		



Employees = {
	"emp1":{"name":"John", "salary": 7500},
	"emp2":{"name":"Emma", "salary": 8000},
	"emp3":{"name":"brad", "salary": 6500},
}


average = int((Employees["emp1"]["salary"] + Employees["emp2"]["salary"] + Employees["emp3"]["salary"])/3)
new = {}
for i in Employees:
	Employees[i]["salary"] = average
print(Employees)

import random

print(random.uniform(9,84))

class mardik: