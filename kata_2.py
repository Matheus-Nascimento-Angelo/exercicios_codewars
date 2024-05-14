def descending_order(num):

    str_reorder = (sorted(str(num), reverse=True))
    int_reorder = "".join(str_reorder)
    return int(int_reorder)



descending_order(187634)