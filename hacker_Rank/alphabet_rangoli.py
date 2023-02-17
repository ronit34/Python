def print_rangoli(size):
    import string
    alphabet = string.ascii_lowercase
    pattern = []
    for i in range(size):
        s = "-".join(alphabet[i:size])
        pattern.append((s[::-1] + s[1:]).center(4 * size - 3, "-"))
    print('\n'.join(pattern[::-1] + pattern[1:]))


a = print_rangoli(5)