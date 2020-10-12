def update_dictionary(d, key, value):
    if d.get(key) is None:
        if d.get(2 * key) is None:
            d.update({2 * key: [value]})
        else:
            d[2 * key] += [value]
    else:
        d[key] += [value]


d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3_7]}