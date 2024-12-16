import os
import subprocess
import re
from collections import defaultdict

def get_git_files():
    """
    Get a list of all Python files in the current Git repository.
    """
    try:
        # Run git command to list all modified files
        result = subprocess.run(['git', 'ls-files', '--modified', '*.py'], stdout=subprocess.PIPE, text=True)
        return result.stdout.splitlines()
    except subprocess.CalledProcessError as e:
        print(f"Error running git command: {e}")
        return []

def count_functions_and_classes(file_path):
    """
    Count the number of functions and classes in a Python file.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            functions = len(re.findall(r'def\s+\w+\s*\(', content))
            classes = len(re.findall(r'class\s+\w+\s*\(', content))
            return functions, classes
    except FileNotFoundError as e:
        print(f"Error opening file: {e}")
        return 0, 0

def count_modules(file_path):
    """
    Count the number of modules imported in a Python file.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            modules = len(re.findall(r'import\s+\w+', content)) + len(re.findall(r'from\s+\w+\s+import\s+\w+', content))
            return modules
    except FileNotFoundError as e:
        print(f"Error opening file: {e}")
        return 0

def analyze_code_modularity(files):
    """
    Analyze the code modularity of the Git repository by counting functions, classes, and modules.
    """
    modularity_counts = defaultdict(int)
    for file_path in files:
        functions, classes = count_functions_and_classes(file_path)
        modules = count_modules(file_path)
        modularity_counts[file_path] = {'functions': functions, 'classes': classes, 'modules': modules}

    print("Code Modularity Report:")
    print("-----------------------")
    for file_path, counts in modularity_counts.items():
        print(f"File: {file_path}")
        print(f"Functions: {counts['functions']}")
        print(f"Classes: {counts['classes']}")
        print(f"Modules: {counts['modules']}")
        print()

def main():
    files = get_git_files()
    analyze_code_modularity(files)

if __name__ == "__main__":
    main()