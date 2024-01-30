import random

y = [2,5,8,12]

print(sum(y))

print(y[-2:])

# to sort by second letter
z= ("kevin", "Niklas", "Jenny", "craig")
 
 # counting 
x = "hippo"

print(x.count('p'))

# list comprehension
a = [m for m in range(8)]
print(a)


b = [i ** 2 for i in range(10) if i < 4]
print(b)


# extending a list

x = [5,3,8,6]
y = [12,13]
x.extend(y)
print(x)


# USING  LIST COMPREHENSION

under_10 = [x for x in range(10)]
print("under_10: " + str(under_10))



squares = [x**2 for x in under_10]
print("quares: " + str(squares))



odds = [x for x in range(10) if x%2 ==1]

print("odds: "+ str(odds))


ten_x = [x * 10 for x in range(10)]
print('ten_x: ' + str(ten_x))


s = "I love 2 go to the store 7 times a week."
nums = [x for x in s if x.isnumeric()]
print("nums: " + "".join(nums))


names = ["cosmo", "pedro", "Anu", "Ray"]
idx = [k for k,v in enumerate(names) if v == "Anu"]
print('index = '+str(idx[0]))


letters = [x for x in "ABCDEF"]
random.shuffle(letters)
letrs = [a for a in letters if a != "C"]
print(letters, letrs)



nums = [5,3,10,18,6,7]

a = [[1,2], [3,4]]
new_list = [x for b in a for x in b]
print(new_list)