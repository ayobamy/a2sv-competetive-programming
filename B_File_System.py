def file_system():
    n = int(input())
    file_names = {}

    for _ in range(n):
        file_name = input()
        if file_name not in file_names:
            file_names[file_name] = 1
            print("OK")
        else:
            while file_name + str(file_names[file_name]) in file_names:
                file_names[file_name] += 1
            new_file_name = file_name + str(file_names[file_name])
            file_names[new_file_name] = 1
            print(new_file_name)

file_system()
