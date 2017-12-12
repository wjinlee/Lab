def myaverage(a, b):
    avg = (a + b) / 2
    return avg


print(myaverage(2, 3))


def get_max_min(data_list):
    maxL = max(data_list)
    minL = min(data_list)
    return (maxL, minL)


listL = [1, 2, 3, 5, 4]
(x, y) = get_max_min(listL)
print(get_max_min(listL))
