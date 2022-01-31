# an empty list...
emptyList = []

# a list of fruits...
fruits = ["orange", "apple", "banana"]

print(fruits)

# appending new items to a list...
fruits.append("strawberry")
fruits.append("watermelon")

print(fruits)

# getting the first element from a list...
print (fruits[0])

# getting the third element from a list...
print (fruits[2])

fruit = 'pear'

if fruit in fruits:
  print(fruit + " is already on the list.")
else:
  print(fruit + " isn't on the list yet.")

# looping through all elements from my list...
for myFruit in fruits:
  print("I've added " + myFruit + " on my list.")

print("Range with element to stop. It'll take from the first until the third element...")
for i in range(3):
  print(i, end="-")
  print(fruits[i])

print("It'll take the 3 next elements starting from the second one...")
for i in range(1, 3):
  print(i, end="-")
  print(fruits[i])

print("It'll take the 3 next elements starting from the second one using step 1 between them...")
for i in range(1, 3, 1):
  print(i, end="-")
  print(fruits[i])

print("It'll take the 4 next elements starting from the first one and using step 2 between them...")
for i in range(0, 4, 2):
  print(i, end="-")
  print(fruits[i])

# It'll break when the fruit is "apple"...
for myFruit in fruits:
  print(myFruit)
  # if myFruit is apple, the loop will stop...
  if (myFruit == "apple"):
    break # It stops the loop...