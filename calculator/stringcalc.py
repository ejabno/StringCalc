"""
Erickson Ureta
erick.ureta95@gmail.com
https://github.com/ejabno

String calculator
7Shifts technical interview challenge

Running instructions:
    1. The only need source files are:
        - This file (stringcalc.py)
        - A formatted .txt file containing test inputs (teststrings.txt)
    2. Simply run this file on either the command line ("python stringcalc.py") or some other program
"""


def add(numbers):
    """
    Takes in an input string, parsing and searching for delimiters
    Sums up any integers within the query
    Excludes N > 1000 and throws a ValueError exception on N < 0
    :param numbers: Input string to parse
    :return: The parsed sum
    """
    return_val = 0

    # Check for string length
    if len(numbers) <= 0:
        # If there's nothing in the string, there's nothing to return
        return 0

    # Check for any custom delimiters
    if "//" in numbers:
        # Query string has a custom delimiter
        # This line divides the string between delimiter and actual query
        strip_array = numbers.strip("//").split("\n")
        # Remove the leading "//"
        query_str = strip_array[1]
        # Create a list of delimiters to search from
        delimiters = []
        for chr in strip_array[0]:
            if chr not in delimiters:
                delimiters.append(chr)
        # Then strip the query string of delimiters
        for delimiter in delimiters:
            query_str = query_str.replace(delimiter, ",")
        split_array = query_str.split(",")
    else:
        # Query string has the normal delimiter
        split_array = numbers.split(",")

    # Sum up the numbers
    for num in split_array:
        if len(num) <= 0:
            # Sometimes the num array would contain
            # empty strings from parsing multiple delimiters
            # Therefore, ignore
            pass
        elif int(num) < 0:
            # Exception on negatives
            raise ValueError(num)
        elif int(num) > 1000:
            # Ignore N > 1000
            pass
        else:
            return_val += int(num)

    return return_val


def runtests(filename):
    """
    Takes in a test file and automates testing
    :param filename: The test file to take in test queries
    """
    test_queries = []
    # Parse testing file
    with open(filename) as testfile:
        curline = testfile.readline()
        while curline is not "":
            query_str = ""
            # Parse the query string
            while "equals" not in curline:
                query_str += curline
                curline = testfile.readline()
            # Parse expected sum
            exp_sum = int(curline.split(" ")[1])
            # And add the query string + expected sum as a tuple
            test_queries.append((query_str, exp_sum))
            # Ignore "****" separator
            testfile.readline()
            curline = testfile.readline()
    # Run all the tests
    for query in test_queries:
        print("==============")
        print("Query string is \"%s\"" % query[0].replace("\n", "\\n"))
        try:
            result = add(query[0])
            print("Expected result = %d, actual result = %d" % (query[1], result))
            if result == query[1]:
                print("Test passed")
            else:
                print("Test failed")
        except ValueError as ve:
            print("Exception caught on %d" % int(ve.args[0]))


# Program entry point
runtests("teststrings.txt")

