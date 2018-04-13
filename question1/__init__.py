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