import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pygamestate",
    version="1.0",
    author="Alan Sartorio",
    author_email="alan42ga@hotmail.com",
    description="A PyGame state management library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alansartorio/PyGame-State-Management",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)