def smart_sort(list_to_sort):
    items_the_cleaned = [item[4:] for item in list_to_sort if item.startswith("the ")]
    items_a_cleaned = [item[2:] for item in list_to_sort if item.startswith("a ")]
    items_an_cleaned = [item[3:] for item in list_to_sort if item.startswith("an ")]
    for item in list_to_sort:
        if item.startswith("the "):
            list_to_sort[list_to_sort.index(item)] = item[4:]
        elif item.startswith("a "):
            list_to_sort[list_to_sort.index(item)] = item[2:]
        elif item.startswith("an "):
            list_to_sort[list_to_sort.index(item)] = item[3:]
    list_to_sort.sort()
    for item in list_to_sort:
        if item in items_the_cleaned:
            list_to_sort[list_to_sort.index(item)] = "the " + item
        elif item in items_a_cleaned:
            list_to_sort[list_to_sort.index(item)] = "a " + item
        elif item in items_an_cleaned:
            list_to_sort[list_to_sort.index(item)] = "an" + item
    return list_to_sort
