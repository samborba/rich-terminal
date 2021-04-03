import re
from os.path import dirname, join
from setuptools import find_packages, setup

with open(join(dirname(__file__), "rich_terminal", "__init__.py")) as fp:
    for line in fp:
        m = re.search(r'^\s*__version__\s*=\s*([\'"])([^\'"]+)\1\s*$', line)
        if m:
            version = m.group(2)
            break
    else:
        raise RuntimeError("Unable to find own __version__ string")

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="rich_terminal",
    version=version,
    author="Samuel Francisco Borba",
    author_email="bfsamuel2@gmail.com",
    description="A rich POC.",
    url="https://github.com/sambobra/rich-terminal",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.7.0",
)
