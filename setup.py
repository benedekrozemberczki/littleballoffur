from distutils.core import setup
from setuptools import find_packages

setup(
  name = "littleballoffur",
  packages = find_packages(),
  version = "0.0.3",
  license = "MIT",
  description = "A general purpose library for subsampling large graphs.",
  author = "Benedek Rozemberczki",
  author_email = "benedek.rozemberczki@gmail.com",
  url = "https://github.com/benedekrozemberczki/littleballoffur",
  download_url = "https://github.com/benedekrozemberczki/littleballoffur/archive/v_00002.tar.gz",
  keywords = ["community", "detection", "networkx", "graph", "clustering","graph-sampling","sampling","random-walk","forest-fire", "embedding","network","deepwalk","graph2vec","node2vec","deep","learning","louvain","machine-learning","deep-learning","deeplearning"],
  install_requires=[
          "networkx",
          "tqdm",
          "python-louvain",
          "pandas",
          "numpy",
          "six",
      ],
  classifiers=[
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Build Tools",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.5",
  ],
)
