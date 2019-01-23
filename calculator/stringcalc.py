def add(numbers):
    return_val = 0
    numbers_len = len(numbers)
    if numbers_len <= 0:
        return 0
    if "//" in numbers:
        strip_array = numbers.strip("//").split("\n")
        query_str = strip_array[1]
        delimiters = []
        for chr in strip_array[0]:
            if chr not in delimiters:
                delimiters.append(chr)
        for delimiter in delimiters:
            query_str = query_str.replace(delimiter, ",")
        split_array = query_str.split(",")
    else:
        split_array = numbers.split(",")
    for num in split_array:
        if len(num) <= 0:
            pass
        elif int(num) < 0:
            raise ValueError(num)
        elif int(num) > 1000:
            pass
        else:
            return_val += int(num)
    return return_val


def runtests(filename):
    with open(filename) as fopen:
        fopen_lines = fopen.readlines()
    test_queries = []
    while len(fopen_lines) > 0:
        query_str = fopen_lines.pop(0)[:-1]
        expected_result = int(fopen_lines.pop(0)[:-1])
        test_queries.append((query_str, expected_result))
    for test in test_queries:
        try:
            test_result = add(test[0])
            if test_result != test[1]:
                return False
        except ValueError as e:
            print("Exception caught on value %s" % e.args)
    return True


print(runtests("teststrings.txt"))

