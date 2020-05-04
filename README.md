
 ![Version](https://badge.fury.io/py/littleballoffur.svg?style=plastic) ![License](https://img.shields.io/github/license/benedekrozemberczki/littleballoffur.svg?color=blue&style=plastic) [![PyPI download month](https://img.shields.io/pypi/dm/littleballoffur.svg?color=blue&style=plastic)](https://pypi.python.org/pypi/littleballoffur/)

<p align="center">
  <img width="90%" src="https://github.com/benedekrozemberczki/littleballoffur/blob/master/littleballoffurlogo.jpg?sanitize=true" />
</p>

--------------------------------------------------------------------------------

**Little Ball of Fur** is a graph subsampling extension library for [NetworkX](https://networkx.github.io/).



Please look at the **[Documentation](https://littleballoffur.readthedocs.io/)** and **[External Resources](https://littleballoffur.readthedocs.io/en/latest/notes/resources.html)**.

*Little Ball of Fur* consists of state-of-the-art methods to do subsampling on graph structured data. To put it simply it is a Swiss Army knife for graph subsampling research. First, it includes a large variety of vertex and edge sampling techniques. Second, it provides a unified application public interface which makes the use of subsampling algorithms trivial. 

--------------------------------------------------------------------------------

**Citing**

If you find *Little Ball of Fur* and the new datasets useful in your research, please consider citing the following paper:

```bibtex
>@misc{littleballoffur2020,
       title={Little Ball of Fur: A Python Library for Graph Subsampling},
       author={Benedek Rozemberczki},
       year={2020},
}
```
--------------------------------------------------------------------------------

**A simple example**

*Karate Club* makes the use of modern community detection techniques quite easy (see [here](https://karateclub.readthedocs.io/en/latest/notes/introduction.html) for the accompanying tutorial).
For example, this is all it takes to use on a Watts-Strogatz graph [Ego-splitting](https://www.eecs.yorku.ca/course_archive/2017-18/F/6412/reading/kdd17p145.pdf):

```python
import networkx as nx
from karateclub import EgoNetSplitter

g = nx.newman_watts_strogatz_graph(1000, 20, 0.05)

splitter = EgoNetSplitter(1.0)

splitter.fit(g)

print(splitter.get_memberships())
```

--------------------------------------------------------------------------------

**Methods included**

In detail, the sampling methods were implemented.

**Category A**

**Category A**

**Category A**

Head over to our [documentation](https://littleballoffur.readthedocs.io) to find out more about installation and data handling, a full list of implemented methods, and datasets.
For a quick start, check out our [examples](https://github.com/benedekrozemberczki/littleballoffur/tree/master/examples.py).

If you notice anything unexpected, please open an [issue](https://github.com/benedekrozemberczki/littleballoffur/issues) and let us know.
If you are missing a specific method, feel free to open a [feature request](https://github.com/benedekrozemberczki/littleballoffur/issues).
We are motivated to constantly make *Little Ball of Fur* even better.


--------------------------------------------------------------------------------

**Installation**

Little Ball of Fur can be installed with the following pip command.

```sh
$ pip install littleballoffur
```

As we create new releases frequently, upgrading the package casually might be beneficial.

```sh
$ pip install littleballoffur --upgrade
```

--------------------------------------------------------------------------------

**Running examples**

As part of the documentation we provide a number of use cases to show how to use various sampling techniques. These can accessed [here](https://littleballoffur.readthedocs.io/en/latest/notes/introduction.html) with detailed explanations.


Besides the case studies we provide synthetic examples for each model. These can be tried out by running the examples script.

```sh
$ python examples.py
```
