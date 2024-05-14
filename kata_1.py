def narcissistic( value ):

    mult = len(str(value))
    result = 0

    str_number = str(value)

    for number in str_number:
        act = int(number) ** mult
        result += act

    if result == value:
        return True
    
    else:
        return False
