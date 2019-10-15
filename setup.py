from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="http-raw",
    version='0.2.1',
    description="A library for better processing of raw data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Buzz2d0/httpraw",
    author="buzz",
    author_email='admin@imipy.com',
    license='GPL',
    platforms=["all"],
    packages=find_packages(),
    install_requires=[
        "requests",
        "PySocks"
    ],
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    keywords='http-raw'
)
