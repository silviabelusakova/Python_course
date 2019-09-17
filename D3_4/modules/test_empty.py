# #!/usr/bin/env python


from empty import Dog, Cat

class Monkey:
     pass 


dog = Dog()
cat =Cat()
monkey = Monkey()

print(dog.__module__)
print(cat.__module__)
print(monkey.__module__)











# from fibonacci import fib

# fib(20)
# print()
# fib(50)




# try:
#     import empty2
# except ImportError as e:
#     print('Failed to import:', e)
#     print('Please install empty2')
#     exit(1)




# import empty as em 
# import sys

# # from empty import first_name , last_name 

# print(em.first_name)
# print(em.last_name)

# print(__name__)
# print(empty.__name__)
# print(sys.__name__)

# print(sys.path)