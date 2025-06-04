# Add to Requirements Script

This Python script simplifies the process of installing Python dependencies using `pip` and adding them to a `requirements.txt` file. It supports adding multiple dependencies at once, avoids duplicates, and handles the creation of the `requirements.txt` file if it doesn't exist.

## Features
- Installs specified Python dependencies using `pip`.
- Adds dependencies to a `requirements.txt` file, skipping duplicates.
- Creates the `requirements.txt` file and its directory if they don't exist.
- Supports an optional custom path for the `requirements.txt` file.
- Gracefully handles installation errors, skipping failed dependencies.

## Prerequisites
- Python 3.x installed.
- `pip` installed and accessible.
- Write permissions for the directory where `requirements.txt` will be created or modified.

## Usage
1. Save the script as `add_to_requirements.py` in your project directory.
2. Run the script from the terminal using:
   ```bash
   python add_to_requirements.py <dependency1> [dependency2 ...] [path/to/requirements.txt]
   ```
   - **Examples**:
     - Add `requests` and `numpy` to the default `requirements.txt` in the current directory:
       ```bash
       python add_to_requirements.py requests numpy
       ```
     - Add `pandas` to a custom `requirements.txt` file:
       ```bash
       python add_to_requirements.py pandas ./myfolder/requirements.txt
       ```
3. The script will:
   - Install the specified dependencies using `pip`.
   - Create or update the `requirements.txt` file with the new dependencies.
   - Skip any dependencies already listed or that fail to install.

## Script Code
Below is the full code for `add_to_requirements.py`:

```python
import os
import sys
import subprocess

def add_to_requirements(dependencies, req_file_path=None):
    # Set default path to requirements.txt in current directory if not provided
    if req_file_path is None:
        req_file_path = os.path.join(os.getcwd(), "requirements.txt")
    
    # Ensure the directory for requirements.txt exists
    req_dir = os.path.dirname(req_file_path) if os.path.dirname(req_file_path) else os.getcwd()
    os.makedirs(req_dir, exist_ok=True)
    
    # Read existing requirements if file exists
    existing_deps = set()
    if os.path.exists(req_file_path):
        with open(req_file_path, 'r') as f:
            existing_deps = {line.strip() for line in f if line.strip() and not line.startswith('#')}
    
    # Add new dependencies, avoiding duplicates
    new_deps = set(dependencies) - existing_deps
    if not new_deps:
        print("All specified dependencies are already in requirements.txt or no new dependencies provided.")
        return
    
    # Install dependencies using pip
    for dep in new_deps:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", dep])
            print(f"Successfully installed {dep}")
        except subprocess.CalledProcessError:
            print(f"Failed to install {dep}. Skipping addition to requirements.txt.")
            continue
    
    # Append new dependencies to requirements.txt
    with open(req_file_path, 'a') as f:
        for dep in new_deps:
            f.write(dep + '\n')
            print(f"Added {dep} to {req_file_path}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python add_to_requirements.py <dependency1> [dependency2 ...] [path/to/requirements.txt]")
        sys.exit(1)
    
    # Extract dependencies and optional requirements.txt path
    args = sys.argv[1:]
    req_file_path = None
    if args[-1].endswith('.txt'):
        req_file_path = args[-1]
        dependencies = args[:-1]
    else:
        dependencies = args
    
    # Validate dependencies
    if not dependencies:
        print("Error: At least one dependency must be specified.")
        sys.exit(1)
    
    add_to_requirements(dependencies, req_file_path)

if __name__ == "__main__":
    main()
```

## Notes
- **Virtual Environment**: Run the script in an activated virtual environment to ensure dependencies are installed in the correct environment. To activate a virtual environment:
  - **Windows**: `.\venv\Scripts\activate`
  - **macOS/Linux**: `source venv/bin/activate`
- **Dependency Versions**: The script adds dependencies as specified (e.g., `requests`). To include specific versions, provide them in the command (e.g., `requests==2.28.1`).
- **Default Path**: If no `requirements.txt` path is provided, the script uses `./requirements.txt` in the current directory.
- **Error Handling**: If a dependency fails to install, it will not be added to `requirements.txt`, and the script will continue with the remaining dependencies.

## Example Output
```bash
$ python add_to_requirements.py requests numpy
Successfully installed requests
Added requests to requirements.txt
Successfully installed numpy
Added numpy to requirements.txt
```

## Limitations
- The script does not automatically fetch the installed version of a dependency. You must specify the version if needed (e.g., `requests==2.28.1`).
- Requires an active internet connection for `pip install`.

## License
This script is provided under the MIT License. Feel free to modify and distribute it as needed.