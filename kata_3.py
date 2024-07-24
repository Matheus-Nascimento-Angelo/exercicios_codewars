def digital_root(n):
    
    splited_n = sorted(str(n))
    int_list = []
    sum_ = 10

    def soma():
        for x in splited_n:
            int_list.append(int(x))
            sum_ = sum(int_list)

    while len(str(sum_)) > 1:
        soma()


digital_root(942)