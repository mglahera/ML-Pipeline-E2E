from setuptools import find_packages, setup
from typing import List

def read_requirements():
    with open('requirements.txt', 'r') as f:
        return f.read().splitlines()

setup(
    name='EndToEnd ML',
    version='0.1',
    author="Miguel Gomez Lahera",
    packages=find_packages(),
    install_requires=read_requirements()
)