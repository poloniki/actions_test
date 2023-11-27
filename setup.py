from setuptools import setup, find_packages

with open("requirements.txt", "r") as file:
    lines = file.readlines()
requirements = [each for each in lines]

setup(name="divide", install_requires=requirements, packages=find_packages())
