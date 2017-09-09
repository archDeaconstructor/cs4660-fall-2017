"""Lists defines simple list related operations"""

def get_first_item(li):
    """Return the first item from the list"""
    return li.index(0)

def get_last_item(li):
    """Return the last item from the list"""
    return li.index(len(list))

def get_second_and_third_items(li):
    """Return second and third item from the list"""
    return (li.index(1), li.index(2))

def get_sum(li):
    """Return the sum of the list items"""
    return sum(li)

def get_avg(li):
    """Returns the average of the list items"""
    return float(sum(li))/max(len(numbers), 1)
