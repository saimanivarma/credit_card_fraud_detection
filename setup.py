from setuptools import setup, find_packages
from typing import List

HYPENATE = '-e .'
def get_requirements(file_path: str) -> List[str]:
    """Read the requirements from a file and return as a list."""
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        if HYPENATE in requirements:
            requirements.remove(HYPENATE)
    return [req.strip() for req in requirements if req.strip()]


setup(
    name='customer_churn_analysis',
    version='1.0.0',
    author='Sai Rameti',
    author_email='varma338@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)