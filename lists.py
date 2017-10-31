"""
Test functions for list
"""

def init_list(size):
    """Init list from 0 to m"""
    test_list = []
    for i in range(0, size):
        test_list.append(i)
    return test_list

def duplicate(test_list, greater):
    """dublicate elements which >= a"""
    result_list = []
    for i in test_list:
        result_list.append(i)
        if i >= greater:
            result_list.append(i)
    return result_list

def sub_list(test_list, less):
    """return sublist of elements which < b"""
    result_list = []
    for i in test_list:
        if i < less:
            result_list.append(i)
    return result_list


