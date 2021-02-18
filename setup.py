"""Setup utility script for doxacal."""

import pathlib
import setuptools

base_dir = pathlib.Path(__file__).parent.resolve()
version_path = pathlib.Path(base_dir, "doxacal", "version.py")
readme_path = pathlib.Path(base_dir, "README.md")

with open(version_path, "r") as version_file_handle:
    version_env = {}
    exec(version_file_handle.read(), version_env)
    version = version_env["__version__"]

with open("README.md", "r") as readme_file_handle:
    long_description = readme_file_handle.read()

setuptools.setup(
    name="doxacal-nickkachur",
    version=version,
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
