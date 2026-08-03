def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    """
    Run a Python file in a specified working directory.

    Args:
        working_directory (str): The base directory to run the Python file from.
        file_path (str): The relative path to the Python file to be executed.
        args (list[str] | None): Optional list of arguments to pass to the Python script.

    Returns:
        str: The output of the executed Python file or an error message if execution fails.
    """
    import os
    import subprocess

    try:
        # Construct the absolute path to the working directory
        working_dir_abs = os.path.abspath(working_directory)

        # Construct the full path to the target Python file
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        # Check if the target file falls within the working directory
        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        if not valid_target_file:
            return f'    Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        # Check if the target file exists and is a Python file
        if not os.path.isfile(target_file):
            return f'    Error: "{file_path}" does not exist or is not a regular file'

        # Check if the target file has a .py extension
        if not target_file.endswith(".py"):
            return f'    Error: "{file_path}" is not a Python file'

        # Prepare the command to run the Python file with optional arguments
        command = ["python", target_file]

        # Check for additional arguments that may be passed to the script
        if args:
            command.extend(args)

        # Execute the command and capture output
        result = subprocess.run(command, capture_output=True, text=True, cwd=working_dir_abs, timeout=30)

        # Return stdout and stderr from the execution
        if result.returncode != 0:
            return f'Process exited with code {result.returncode}:\n{result.stdout.strip()}'
        elif result.stdout:
            return f"STDOUT:\n{result.stdout.strip()}"
        elif result.stderr:
            return f"STDERR:\n{result.stderr.strip()}"
        elif result.stdout == "" and result.stderr == "":
            return f"No output produced"
    except Exception as e:
        return f"    Error: {e}"
