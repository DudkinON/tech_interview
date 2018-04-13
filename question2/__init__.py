def question2(a):
    """
    Find longest palindromic substring

    :param a: string
    :return: string
    """
    i = 0
    substring = ''
    word = list(a.lower())
    palindrome = list(a.lower()[::-1])
    while i < len(word):
        if word[i] == palindrome[i]:
            substring += word[i]
        else:
            break
        i += 1
    return substring
