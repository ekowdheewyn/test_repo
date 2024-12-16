import ast
import os
from collections import defaultdict


def analyze_file(file_path):
    """
    Analyze a Python file to count the number of functions, classes,
    and modules.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        try:
            tree = ast.parse(file.read(), filename=file_path)
        except SyntaxError as e:
            print(f"Skipping {file_path} due to syntax error: {e}")
            return 0, 0

    function_count = 0
    class_count = 0

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            function_count += 1
        elif isinstance(node, ast.ClassDef):
            class_count += 1

    return function_count, class_count


def analyze_repository(repo_path):
    """
    Analyze all Python files in a repository to evaluate modularity.
    """
    modularity_summary = defaultdict(lambda: {"functions": 0, "classes": 0})

    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                functions, classes = analyze_file(file_path)
                modularity_summary[file_path]["functions"] = functions
                modularity_summary[file_path]["classes"] = classes

    return modularity_summary


def print_report(modularity_summary):
    """
    Print a modularity report for the repository.
    """
    print("Modularity Report:\n")
    total_functions = 0
    total_classes = 0

    for file_path, counts in modularity_summary.items():
        functions = counts["functions"]
        classes = counts["classes"]
        print(f"File: {file_path}")
        print(f"  Functions: {functions}")
        print(f"  Classes: {classes}\n")
        total_functions += functions
        total_classes += classes

    print("Overall Summary:\n")
    print(f"Total Functions: {total_functions}")
    print(f"Total Classes: {total_classes}")
    print(f"Total Modules: {len(modularity_summary)}")


if __name__ == "__main__":
    # Replace with the path to your Git repository
    repo_path = '/path/to/your/git/repository'
    if not os.path.exists(repo_path):
        print("Invalid path. Please provide a valid Git repository path.")
    else:
        modularity_summary = analyze_repository(repo_path)
        print_report(modularity_summary)