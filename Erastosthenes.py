#PRIME NUMBER GENERATOR:
# Erastosthenes provides algorithm to find prime number for a given specific range
# This is an implementation of Erastosthenes algorithm

import math

print("Eratosthenes")

n = int(input("Enter the max limit"))

arr = list(range(2,n))
limit = int(math.sqrt(n))
#print(arr)
pivot = 2
while pivot < limit:
    for i in arr:
        if i % pivot ==0:
            arr.remove(i)
    pivot = pivot +1

print("Output:")
print(arr)
