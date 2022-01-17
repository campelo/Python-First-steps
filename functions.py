# ###############################################################################
# # Sample 1
# ###############################################################################
# # Declaring a function...
# def sayHello(name):
#   print("Hello " + name)

# input_name = input("Please, enter your name: ")
# # The function will only be called at this point...
# sayHello(input_name)

###############################################################################
# Sample 2
###############################################################################
def sayHello(name):
  print("Hello " + name) # using local variable...

def sayGoodBye():
  print("Good bye " + input_name) # using global variable...

input_name = input("Please, enter your name: ")
sayHello(input_name)
sayGoodBye()
