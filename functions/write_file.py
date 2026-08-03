def write_file(working_directory: str, file_path: str, content: str) -> str:
    """
    Write content to a specified file within the working directory.

    Args:
        working_directory (str): The base directory to write the file in.
        file_path (str): The relative path of the file to write to.
        content (str): The content to write into the file.

    Returns:
        str: A message indicating success or failure.
    """
    import os

    try:
        # Construct the absolute path to the working directory
        working_dir_abs = os.path.abspath(working_directory)

        # Construct the full path to the target file
        target_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

        # Check if the target file path falls within the working directory
        valid_target_file = os.path.commonpath([working_dir_abs, target_file_path]) == working_dir_abs
        if not valid_target_file:
            return f'    Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # Check if the target file path is a directory
        if os.path.isdir(target_file_path):
            return f'    Error: Cannot write to "{file_path}" as it is a directory'

        # Ensure the parent directory exists
        parent_dir = os.path.dirname(target_file_path)
        os.makedirs(parent_dir, exist_ok=True)

        # Write content to the file
        with open(target_file_path, 'w') as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"    Error: {e}"
