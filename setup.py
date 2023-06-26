import os

from setuptools import find_packages, setup

on_rtd = os.environ.get("READTHEDOCS") == "True"

install_requires = [
    "numpy>=1.25",
    "networkx>=3.1",
    "decorator>=5.1",
    "cmake>=3.26",
    "Cython>=0.29",
    "tqdm",
    "python-louvain>=0.16",
    "pandas<2.0",
    "six",
    "scipy>=1.10",
]

if not on_rtd:
    install_requires.append("networkit>=10.1")

setup_requires = ["cython", "numpy", "pytest-runner"]

tests_require = ["pytest", "pytest-cov", "mock", "unittest"]


keywords = [
    "community",
    "detection",
    "networkx",
    "graph",
    "snow ball",
    "metropolis hastings",
    "shortest path",
    "loop erased",
    "spiky ball",
    "graph sampling",
    "sampling",
    "tree sampling",
    "random walk",
    "forest fire",
]

setup(
    name="littleballoffur",
    version="2.3.0",
    license="MIT",
    description="A general purpose library for subsampling graphs.",
    author="Benedek Rozemberczki",
    author_email="benedek.rozemberczki@gmail.com",
    url="https://github.com/benedekrozemberczki/littleballoffur",
    download_url="https://github.com/benedekrozemberczki/littleballoffur/archive/v_2.2.0.tar.gz",
    keywords=keywords,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
    ],
)
