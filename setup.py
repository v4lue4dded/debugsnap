from setuptools import setup, find_packages

setup(
    name="debugsnap",
    version="0.1.6",
    author="v4lue4dded",
    author_email="v4lue4dded@gmail.com",
    description="A tool to save and load a snapshot of a Python debugging environment.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/v4lue4dded/debugsnap",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "dill>=0.3.0" 
        ],
)
