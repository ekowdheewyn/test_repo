import os
import subprocess
import sys


#this is a comment
def run_linting():
    """Run flake8 for linting."""
    # Use a flake8 configuration file if available
    lint_command = "flake8 --config=flake8.ini"
    try:
        subprocess.run(
            lint_command,
            shell=True,
            check=True,
            stdout=sys.stdout,
            stderr=sys.stderr,
        )
        print("Linting passed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Linting failed with exit code {e.returncode}")
        sys.exit(1)


def run_tests():
    """Run pytest for tests with coverage and parallel execution."""
    # Get the current directory
    current_dir = os.getcwd()

    # Define the command to run pytest with parallel execution and coverage
    pytest_command = (
        f"pytest {current_dir} --cov={current_dir} --cov-report=xml --cov-report=term-missing "
        f"-n auto"
    )

    try:
        # Run the pytest command
        subprocess.run(
            pytest_command,
            shell=True,
            check=True,
            stdout=sys.stdout,
            stderr=sys.stderr,
        )
        print(
            "Tests passed successfully! Detailed report and coverage generated."
        )
    except subprocess.CalledProcessError as e:
        print(f"Tests failed with exit code {e.returncode}")
        sys.exit(1)


if __name__ == "__main__":
    run_linting()
    run_tests()
