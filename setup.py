from setuptools import setup, find_packages

with open("README.md" ,  "r") as f:
    description = f.read()

setup(
    name='Physic',
    version='1.2',
    packages=find_packages(),
    author='Seif Eldein',
    description='A programming library specialized in the rules of physics in general, and more precisely the rules of mechanics and electrical physics and their rates, and it is used to shorten complex rates into simple-to-use functions',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License"
    ],
    long_description=description,
    long_description_content_type="text/markdown",
)
