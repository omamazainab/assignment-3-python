import random

arr = []

#aadding elements into the list
for i in range(0,100): 
    arr.append(random.randint(0,50))

max=arr[0] 
index=0
#finding max value in the list
for i in range(0,100):
    if max<arr[i]:
        max=arr[i]
        index=i
print("maximum value is "+str(max)+" at index "+str(index))

min=arr[0] 
index=0
#finding min value in the list
for i in range(0,100):
    if min>arr[i]:
        min=arr[i]
        index=i
print("minimum value is "+str(min)+" at index "+str(index))


sum=0
#finding mean value
for i in range(0,100):
    sum +=arr[i]
print("the mean value of list is "+str(sum/100))

