#!/usr/bin/env python
"""
Deployment script for PythonAnywhere.
Run this script on PythonAnywhere to set up the Django app.
"""

import os
import subprocess
import sys

def run_command(command, cwd=None):
    """Run a shell command and return the result."""
    try:
        result = subprocess.run(command, shell=True, cwd=cwd, capture_output=True, text=True, check=True)
        print(f"✓ {command}")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {command}")
        print(f"Error: {e}")
        if e.stdout:
            print(e.stdout)
        if e.stderr:
            print(e.stderr)
        return False

def main():
    print("Starting deployment setup for E-commerce API...")

    # Get the project directory (assuming this script is in the project root)
    project_dir = os.path.dirname(os.path.abspath(__file__))

    # Install requirements
    print("\n1. Installing requirements...")
    if not run_command("pip install -r requirements.txt", cwd=project_dir):
        sys.exit(1)

    # Run migrations
    print("\n2. Running database migrations...")
    if not run_command("python manage.py migrate", cwd=project_dir):
        sys.exit(1)

    # Collect static files
    print("\n3. Collecting static files...")
    if not run_command("python manage.py collectstatic --noinput", cwd=project_dir):
        sys.exit(1)

    # Create superuser (optional, will prompt)
    print("\n4. Creating superuser...")
    print("You will be prompted to create a superuser. If you skip this, you can create one later.")
    run_command("python manage.py createsuperuser", cwd=project_dir)

    print("\n✓ Deployment setup completed!")
    print("\nNext steps:")
    print("1. In PythonAnywhere, go to the Web tab")
    print("2. Set the source code directory to:", project_dir)
    print("3. Set the WSGI configuration file to: ecommerce_api/wsgi.py")
    print("4. Reload your web app")
    print("\nYour API will be available at: https://your-username.pythonanywhere.com/api/")

if __name__ == "__main__":
    main()
