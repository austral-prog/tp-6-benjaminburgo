def remove_elements(lst):
    if 'Red' in lst:
        lst.remove('Red')
    if 'Pink' in lst:
        lst.remove('Pink')
    if 'Yellow' in lst:
        lst.remove('Yellow')
    return lst

def add_elements(lst):
    lst.insert(0, 'Pink')
    lst.append('Yellow')
    return lst

def is_empty(lst):
    return len(lst) == 0

def check_lists(lst1, lst2):
    return sorted(lst1) == sorted(lst2)

def list_of_lists(list_of_lists_to_modify):
    if len(list_of_lists_to_modify[0]) >= 2:
        list_of_lists_to_modify[0] = list_of_lists_to_modify[0][:2]
    else:
        list_of_lists_to_modify[0] = []

    if len(list_of_lists_to_modify[1]) >= 4:
        list_of_lists_to_modify[1] = list_of_lists_to_modify[1][1:4]
    else:
        list_of_lists_to_modify[1] = []

    if len(list_of_lists_to_modify[2]) >= 2:
        list_of_lists_to_modify[2] = list_of_lists_to_modify[2][-2:]
    else:
        list_of_lists_to_modify[2] = []

    return list_of_lists_to_modify





