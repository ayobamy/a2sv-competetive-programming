def swap_case(s):
    str_swapped = ''
    for char in s:
        if char.islower():
            str_swapped += char.upper()
        elif char.isupper():
            str_swapped += char.lower()
        else:
            str_swapped += char
    return str_swapped;

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
