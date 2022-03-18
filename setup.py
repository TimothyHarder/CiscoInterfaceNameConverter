import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "CiscoInterfaceNameConverter",
    version="0.0.1",
    author="Timothy Harder",
    author_email="harder.timothy.j@gmail.com",
    description="Convert between short and long versions of cisco interface names.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TimothyHarder/CiscoInterfaceNameConverter",
    project_urls={
        "Bug Tracker": "https://github.com/TimothyHarder/CiscoInterfaceNameConverter/issues"
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6"
)