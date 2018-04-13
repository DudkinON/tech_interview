def question1(s, t):
    """
    Check is an anagram

    :param s: string
    :param t: string
    :return: bool
    """
    count = 0
    anagram_list = list(t.lower())
    string_list = list(s.lower())
    for character in anagram_list:
        if character in string_list:
            count += 1

    return count == len(anagram_list)


if __name__ == '__main__':
    result = question1(raw_input("input first string: "),
                       raw_input("input second string: "))
    print "Second string is a substring of first string: ", result
