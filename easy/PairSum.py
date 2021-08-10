def two_sum(arr, target):
    result = []
    d = {}  # key - number, value = number of occurrences
    for x in arr:
        val = target - x
        if val in d:
            result.extend([(min(val, x), max(val, x))])
            d[val] -= 1
            if d[val] == 0:
                del d[val]
        elif x in d:
            d[x] += 1
        else:
            d[x] = 1
    if len(result) == 0:
        result = [(-1, -1)]
    result.sort(key=lambda tup: (tup[0], tup[1]))
    return result


def print_ans(m_ans):
    for y in m_ans:
        print('{} {}'.format(str(y[0]), str(y[1])))


if __name__ == "__main__":
    inputs = ([9, [2, 7, 11, 13]], [1, [1, -1, -1, 2, 2]])
    for input_list in inputs:
        ans = two_sum(input_list[1], input_list[0])
        print_ans(ans)
