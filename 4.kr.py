def number_count(s):
    dict = {int(s[i]): 0 for i in range(len(s))}
    for c in s:
        dict[int(c)] += 1
    return dict

s = input()
print(number_count(s))