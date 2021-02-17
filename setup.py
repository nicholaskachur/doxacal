"""Setup utility script for doxacal."""

import setuptools

with open("README.md", "r") as readme_file_handle:
    long_description = readme_file_handle.read()

setuptools.setup(
    name="doxacal-nickkachur",
    version="0.0.1",
    author="Nicholas Kachur",
    author_email="nick.e.kachur@gmail.com",
    description="Orthodox Christian Calendar Utility",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nickkachur/doxacal",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    python_requires=">=3.6",
    entry_points={"console_scripts": ("doxacal = doxacal.__main__:main",)},
)
