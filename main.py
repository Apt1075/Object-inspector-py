import ast ,sys

def covert_to_obj(user_input):
    try:
        return ast.literal_eval(user_input)
    except:
        return user_input
    

def is_mutable(obj):
    return isinstance(obj, (list, dict, set, bytearray))

def print_attributes(obj):
       print("Object Inspection:")
       print("-" * 40)
       print(f"Value    : {obj}")
       print(f"Type     : {type(obj)}")
       print(f"Memory   : {id(obj)}")
       print(f"Size     : {sys.getsizeof(obj)}")
       if is_mutable(obj):
           print("Mutable  : Yes")
       else:
           print("Mutable  : No")
       print("-" * 40)    

print("Welcome to object inspector")
user_input = input("Please enter the object you want to inspect: ")
user_object = covert_to_obj(user_input)
# print(f"Type: {type(user_object)}")
print_attributes(user_object)




