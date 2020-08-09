import os
from setuptools import find_packages, setup

on_rtd = os.environ.get("READTHEDOCS") == "True"

install_requires = ["networkx",
                    "tqdm",
                    "python-louvain",
                    "pandas",
                    "numpy",
                    "six",
                    "scipy"]

if not on_rtd:
    install_requires.append("networkit")

setup_requires = ["cython", "numpy", "pytest-runner"]

tests_require = ["pytest", "pytest-cov", "mock"]

keywords = ["community",
            "detection",
            "networkx",
            "graph",
            "metropolis hastings",
            "shortest path",
            "loop erased" 
            "graph sampling",
            "sampling",
            "random walk",
            "forest fire"]

setup(
  name = "littleballoffur",
  version = "1.0.4",
  license = "MIT",
  description = "A general purpose library for subsampling large graphs.",
  author = "Benedek Rozemberczki",
  author_email = "benedek.rozemberczki@gmail.com",
  url = "https://github.com/benedekrozemberczki/littleballoffur",
  download_url = "https://github.com/benedekrozemberczki/littleballoffur/archive/v_10004.tar.gz",
  keywords = keywords,
  install_requires = install_requires,
  setup_requires = setup_requires,
  tests_require = tests_require,
  packages = find_packages(),
  classifiers = ["Development Status :: 3 - Alpha",
                 "Intended Audience :: Developers",
                 "Topic :: Software Development :: Build Tools",
                 "License :: OSI Approved :: MIT License",
                 "Programming Language :: Python :: 3.7"],
)
