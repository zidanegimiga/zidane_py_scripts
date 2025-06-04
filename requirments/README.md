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