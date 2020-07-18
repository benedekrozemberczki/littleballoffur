from setuptools import find_packages, setup


install_requires = [ "networkx", "tqdm", "python-louvain", "pandas", "numpy", "six", "scipy"]

setup_requires = ['pytest-runner']

tests_require = ['pytest', 'pytest-cov', 'mock']

setup(
  name = "littleballoffur",
  packages = find_packages(),
  version = "1.0.2",
  license = "MIT",
  description = "A general purpose library for subsampling large graphs.",
  author = "Benedek Rozemberczki",
  author_email = "benedek.rozemberczki@gmail.com",
  url = "https://github.com/benedekrozemberczki/littleballoffur",
  download_url = "https://github.com/benedekrozemberczki/littleballoffur/archive/v_10002.tar.gz",
  keywords = ["community", "detection", "networkx", "graph", "clustering", 
              "graph-sampling", "sampling", "random-walk", "forest-fire",
              "embedding", "network", "deepwalk", "graph2vec", "node2vec",
              "deep", "learning", "louvain", "machine-learning", "deep-learning", "deeplearning"],
  install_requires = install_requires,
  setup_requires = setup_requires,
  tests_require = tests_require,
  classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Build Tools",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.7.6",
  ],
)
