a = [1, 3, 4, 6, 7, 8, 9, 11, 15, 17, 19, 21, 22, 25, 29, 33, 38, 69, 107]


def find(l, n, p=0):
    length = len(l)
    if length == 1:
        return p if l[0] == n else '{} not in this list'.format(n)
    else:
        mid_point = int(length/2)
        if l[mid_point] > n:
            new_list = l[:mid_point]
            new_p = p
        else:
            new_list = l[mid_point:]
            new_p = p + mid_point
        backward_msg = find(new_list, n, new_p)
        return backward_msg


print(find(a, 10))
print(find(a, 7))