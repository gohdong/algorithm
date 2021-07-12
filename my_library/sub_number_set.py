num_list = set()

def num_generate(s, n_l):  # list
    if not n_l:
        return

    for i in n_l:
        temp = s + str(i)
        temp2 = n_l[:]
        num_list.add(int(temp))
        temp2.remove(i)
        num_generate(temp, temp2)