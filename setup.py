import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="izSelenium",
    version="1.0.2",
    description="a decent selenium wrapper",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/MrPupik/izSelenium",
    author="Itay Zohar",
    author_email="itaynzohar@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["Core", "Chrome"],
    include_package_data=True,
    install_requires=["selenium"],
    entry_points={
    },
)