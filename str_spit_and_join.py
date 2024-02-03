def split_and_join(line):
    split_txt = line.split(' ')
    return ('-'.join(split_txt))

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
