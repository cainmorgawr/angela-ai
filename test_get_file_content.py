from functions.get_file_content import get_file_content

result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")
main_result = get_file_content("calculator", "main.py") 
print(f"main.py Result:\n{main_result}")
pkg_result = get_file_content("calculator", "pkg/calculator.py")
print(f"pkg/calculator.py Result:\n{pkg_result}")
cat_result = get_file_content("calculator", "/bin/cat")
print(f"/bin/cat Result:\n{cat_result}")
does_not_exist_result = get_file_content("calculator", "pkg/does_not_exist.py")
print(f"pkg/does_not_exist.py Result:\n{does_not_exist_result}")
