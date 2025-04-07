import pkg_resources
import subprocess

# Get the list of installed packages
installed_packages = pkg_resources.working_set
outdated_packages = []

# Check for outdated packages
for package in installed_packages:
    package_name = package.project_name
    try:
        subprocess.check_output(['pip', 'list', '--outdated', '--disable-pip-version-check', '--no-python-version-warning'])
        outdated_packages.append(package_name)
    except subprocess.CalledProcessError:
        pass

# Upgrade each outdated package
for package in outdated_packages:
    subprocess.call(['pip', 'install', '--upgrade', package])
