
#it will print each letter in seperate line (each iteration)
for item in 'Python':
    print(item)

for item in ["siva", "sankar"]:
    print(item)

#list of numbers
for item in [1,2,3]:
    print(item)

#to list large number to iterate, use range function
for item in range(10):
    print(item)

for item in range(10, 100):
    print(item)

for item in range(10, 100, 10): # each step 10 increase
    print(item)

#output, total all the prices to one variable and print it
prices = [10, 40, 70, 100]
total = 0
for p in prices:
    total = total + p
print(f"Total Price:  {total}")
