from data_structures.hashtable import Hashtable


def left_join(table_a, table_b):
    return_list = []

    for key, value in table_a.items():
        if table_b.get(key):
            return_list.append([key, value, table_b.get(key)])
        else:
            return_list.append([key, value, 'NONE'])

    return return_list
