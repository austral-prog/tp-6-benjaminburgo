def remove_elements(list_to_remove_elements):
    for i in sorted([5, 4, 0], reverse=True):
        if i < len(list_to_remove_elements):
         del list_to_remove_elements[i]
    return list_to_remove_elements



     


def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0,"Pink")
    list_to_add_elements.append("Yellow")

    return "list_to_add_elements" 


def is_empty(list_to_check):
    if len(list_to_check) <= 0:
    return "Empty"  
    else:
    return "Not Empty"


def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) > 2 and len(list_to_compare2) > 2:
        return list_to_compare1[2] == list_to_compare2[2]
    else:
        return False


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




