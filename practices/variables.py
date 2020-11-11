#Variables in Python
#1. Variables are used to store data, they take memory space based on the type of value we assigning to them
number = 1000 #int
str = "Siva Sankar" #string

print("Number:", number)
print("string: ", str)

rate = 10;
rate = 100;
print("Rate:", rate)
#this gives latest value as its iterpreter executes the code line by line

#its gives object
print("type of rate:", type(rate))

#2.
#ask two questions like whats the persons name and favourite car. then print the  message like "Siva likes Honda Car"
person_name = input("Whats the person's name: ")
favourite_car = input("Whats your favourite car: ")
msg = f'{person_name} likes {favourite_car} car'
print(msg)

#3.
#when using both integer and string and trying to concatenate, need to convert all into int
#example calculate the AGE
birth_year = input("Birthday Year: ")
age = 2020 - int(birth_year) # here birth_year comes as string and converting into int to subtract
print(age)




