def has_unique_chars(s):
    # Write code here
    try:
        for i in range(0, len(s)):  # abcdefg
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    return 'false'
                else:
                    pass
    except IndexError:
        pass
    return 'true'