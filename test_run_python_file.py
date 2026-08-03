from functions.run_python_file import run_python_file

print(f'Results of main:\n{run_python_file("calculator", "main.py")}') #(should print the calculator's usage instructions)
print(f'Results of main with args:\n{run_python_file("calculator", "main.py", ["3 + 5"])}') #(should run the calculator... which gives a kinda nasty rendered result)
print(f'Results of tests:\n{run_python_file("calculator", "tests.py")}') #(should run the calculator's tests successfully)
print(f'Results of relative path:\n{run_python_file("calculator", "../main.py")}') #(this should return an error)
print(f'Results of nonexistent file:\n{run_python_file("calculator", "nonexistent.py")}') #(this should return an error)
print(f'Results of non-Python file:\n{run_python_file("calculator", "lorem.txt")}') #(this should return an error)
