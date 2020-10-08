7A. Write a program to implement the collision technige.





def hash_function(value):
    global size_list
    return value%6

def map_hash2index(hash_return_value):
    return hash_return_value

def create_hash_table(list_values,main_list):
    for value in list_values:
        hash_return_value = hash_function(value)
        list_index = map_hash2index(hash_return_value)
        if main_list[list_index]:
            main_list[list_index].append(value)
                Print ("Collision detected")
        else:
            main_list[list_index] = value
