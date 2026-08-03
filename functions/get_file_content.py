def get_file_content(working_directory: str, file_path: str) -> str:
    """
    Get the content of a specified file.

    Args:
        working_directory (str): The base directory to search for the file.
        file_path (str): The relative path to the file from the working directory.

    Returns:
        str: The content of the file or an error message if the file cannot be read.
    """
    import os
    from config import MAX_CHARS

    try:
        # Construct the absolute path to the working directory
        working_dir_abs = os.path.abspath(working_directory)

        # Construct the full path to the target file
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        # Check if the target file falls within the working directory
        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        if not valid_target_file:
            return f'    Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # check if the file_path argument is a valid file
        if not os.path.isfile(target_file):
            return f'    Error: File not found or is not a regular file: "{file_path}"'

        # read and return the content of the file
        with open(target_file, 'r') as f:
            content = f.read(MAX_CHARS)  # Read up to 10,000 characters
            if f.read(1):  # Check if there's more content beyond the first 10,000 characters
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return content
    except Exception as e:
        return f"    Error: {e}"