###############################################################################
# Sample 1
###############################################################################
# print("Please, enter your genre:")
# print("1 - Male")
# print("2 - Female")
# genre = int(input())

# if genre == 1:
#   print("You're a men")
# if genre == 2:
#   print("You're a women")


###############################################################################
# Sample 2
###############################################################################
# print("Please, enter your age:")
# age = int(input())

# if age < 13:
#   print("You're a child")
# elif age < 18:
#   print("You're a teenager")
# else:
#   print("You're an adult")


###############################################################################
# Sample 3
###############################################################################
print("Please, enter your genre:")
print("1 - Male")
print("2 - Female")
genre = int(input())

print("Please, enter your age:")
age = int(input())

if genre == 1 and age >= 12:
  print("Your birthday's gift will be a playstation")
elif genre == 2 and age < 10:
  print("Your birthday's gift will be a doll")
else:
  print("Your birthday's gift will be a surprise")