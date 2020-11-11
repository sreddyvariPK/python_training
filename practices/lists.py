list = ['siva' , 'sankar', 'reddy']
print(list)

#access values with index from list
print(list[0]) # from start
print(list[-2]) # from end

list_two = [-45, 6, 0 ,72, 1543]
print(list_two)

#slicing
print(list[0:1])
print(list[:])
print(list[:2])

#find the largest number from the list
list_one = [1,3,7,5,4,2,38,9,12]
print(max(list_one))
max_num = list_one[0]
for num in list_one:
    if num > max_num:
        max_num = num
print(max_num)




