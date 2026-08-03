from functions.write_file import write_file

print(f'Results of lorem.txt:\n{write_file("calculator", "lorem.txt", "wait, this isn\'t lorem ipsum")}')
print(f'Results of morelorem.txt:\n{write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")}')
print(f'Results of temp.txt:\n{write_file("calculator", "/tmp/temp.txt", "this should not be allowed")}')
