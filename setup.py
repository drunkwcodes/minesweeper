import versioneer
from setuptools import find_packages, setup

setuptools.setup(
    name="minesweeper",
    version=versioneer.get_versions()["version"],
    url="https://github.com/drunkwcodes/minesweeper",
    licenise="MIT",
    author="Drunkwcodes",
    author_email="drunkwcodes@gmail.com",
    description="pygtk minesweeper",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",  # This is important!
    maintainer="Drunkwcodes",
    maintainer_email="drunkwcodes@gmail.com",
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
