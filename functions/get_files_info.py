def get_files_info(working_directory: str, directory: str = ".") -> str:
    """
    Get information about files in a specified directory.

    Args:
        working_directory (str): The base directory to search for files.
        directory (str): The specific subdirectory to look into. Defaults to the current directory.

    Returns:
        str: A formatted string containing information about the files found.
    """
    import os

    try:
        # Construct the absolute path to the working directory
        working_dir_abs = os.path.abspath(working_directory)

        # Construct the full path to the target directory
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

        # Check if the target directory falls within the working directory
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if not valid_target_dir:
            return f'    Error: Cannot list "{directory}" as it is outside the permitted working directory'

        # check if the directory argument is a valid directory
        if not os.path.isdir(target_dir):
            return f'    Error: "{directory}" is not a directory'
        #return f'Success: "{directory}" is within the working directory'

        # iterate over the directory and get the list of files
        file_list = os.listdir(target_dir)
        file_info = []
        for item in file_list:
            item_path = os.path.join(target_dir, item)
            item_info = f"  - {item}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}"
            file_info.append(item_info)
        return "\n".join(file_info)
    except Exception as e:
        return f"    Error: {e}"

# Define the fuction schema for the LLM to understand the function signature and parameters
schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}
