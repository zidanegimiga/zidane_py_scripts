import os
import sys
import subprocess


def add_to_requirements(dependencies, req_file_path=None):
    if req_file_path is None:
        req_file_path = os.path.join(os.getcwd(), "requirements.txt")
    
    req_dir = os.path.dirname(req_file_path) if os.path.dirname(req_file_path) else os.getcwd()
    os.makedirs(req_dir, exist_ok=True)
    
    existing_deps = set()
    if os.path.exists(req_file_path):
        with open(req_file_path, 'r') as f:
            existing_deps = {line.strip() for line in f if line.strip() and not line.startswith('#')}
    
    new_deps = set(dependencies) - existing_deps
    if not new_deps:
        print("All specified dependencies are already in requirements.txt or no new dependencies provided.")
        return
    
    for dep in new_deps:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", dep])
            print(f"Successfully installed {dep}")
        except subprocess.CalledProcessError:
            print(f"Failed to install {dep}. "
                  "Skipping addition to requirements.txt.")
            continue
    
    with open(req_file_path, 'a') as f:
        for dep in new_deps:
            f.write(dep + '\n')
            print(f"Added {dep} to {req_file_path}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python add_to_requirements.py <dependency1> [dependency2 ...] [path/to/requirements.txt]")
        sys.exit(1)
    
    args = sys.argv[1:]
    req_file_path = None
    if args[-1].endswith('.txt'):
        req_file_path = args[-1]
        dependencies = args[:-1]
    else:
        dependencies = args
    
    if not dependencies:
        print("Error: At least one dependency must be specified.")
        sys.exit(1)
    
    add_to_requirements(dependencies, req_file_path)


if __name__ == "__main__":
    main()
