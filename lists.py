# Replace the "ANSWER HERE" with your answer

def remove_elements(list_to_remove_elements):
    
    lista = list_to_remove_elements

    lista_corta = lista[1:4]
    
    return lista_corta


def add_elements(list_to_add_elements):
    
    lista = list_to_add_elements
    lista = ['Pink'] + lista + ['Yellow']

    return lista


def is_empty(list_to_check):
    
    lista = list_to_check

    if len(lista) == 0:
        return True
    else:
        return False

def check_lists(list_to_compare1, list_to_compare2):
    l1 = list_to_compare1
    l2 = list_to_compare2

    if len(l1) > 2 and len(l2) > 2 and l1[2] == l2[2]:
        return True
    else:
        return False
    


def list_of_lists(list_of_lists_to_modify):
    
    modified_list = []
    first_list = list_of_lists_to_modify[0]
    second_list = list_of_lists_to_modify[1]
    third_list = list_of_lists_to_modify[2]

    modified_list.append(first_list[:2])

    if len(second_list) >= 4:
        modified_list.append(second_list[1:4])
    elif len(second_list) == 3:
        modified_list.append(second_list[1:3])
    elif len(second_list) == 2:
        modified_list.append(second_list[1:])
    else:
        modified_list.append([])

    modified_list.append(third_list[-2:])

    return modified_list


