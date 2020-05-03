
 ![Version](https://badge.fury.io/py/littleballoffur.svg?style=plastic) ![License](https://img.shields.io/github/license/benedekrozemberczki/littleballoffur.svg?color=blue&style=plastic) [![PyPI download month](https://img.shields.io/pypi/dm/karateclub.svg?color=blue&style=plastic)](https://pypi.python.org/pypi/karateclub/)  [![Arxiv](https://img.shields.io/badge/ArXiv-2003.04819-orange.svg?color=blue&style=plastic)](https://arxiv.org/abs/2003.04819) ![Astro](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Fastronomer.ullaakut.eu%2Fshields%3Fowner%3Dbenedekrozemberczki%26name%3Dkarateclub)

<p align="center">
  <img width="90%" src="https://github.com/benedekrozemberczki/littleballoffur/blob/master/littleballoffurlogo.jpg?sanitize=true" />
</p>

--------------------------------------------------------------------------------


**Little Ball of Fur** is an unsupervised machine learning extension library for [NetworkX](https://networkx.github.io/).



Please look at the **[Documentation](https://karateclub.readthedocs.io/)**, relevant **[Paper](https://arxiv.org/abs/2003.04819)**, and **[External Resources](https://karateclub.readthedocs.io/en/latest/notes/resources.html)**.

*Karate Club* consists of state-of-the-art methods to do unsupervised learning on graph structured data. To put it simply it is a Swiss Army knife for small-scale graph mining research. First, it provides network embedding techniques at the node and graph level. Second, it includes a variety of overlapping and non-overlapping community detection methods. Implemented methods cover a wide range of network science ([NetSci](https://netscisociety.net/home), [Complenet](https://complenet.weebly.com/)), data mining ([ICDM](http://icdm2019.bigke.org/), [CIKM](http://www.cikm2019.net/), [KDD](https://www.kdd.org/kdd2020/)), artificial intelligence ([AAAI](http://www.aaai.org/Conferences/conferences.php), [IJCAI](https://www.ijcai.org/)) and machine learning ([NeurIPS](https://nips.cc/), [ICML](https://icml.cc/), [ICLR](https://iclr.cc/)) conferences, workshops, and pieces from prominent journals. 


The newly introduced graph classification datasets are available at [SNAP](https://snap.stanford.edu/data/#disjointgraphs), [TUD Graph Kernel Datasets](https://ls11-www.cs.tu-dortmund.de/staff/morris/graphkerneldatasets) and [GraphLearning.io](https://chrsmrrs.github.io/datasets/).  

--------------------------------------------------------------------------------

**Citing**

If you find *Karate Club* and the new datasets useful in your research, please consider citing the following paper:

```bibtex
>@misc{karateclub2020,
       title={An API Oriented Open-source Python Framework for Unsupervised Learning on Graphs},
       author={Benedek Rozemberczki and Oliver Kiss and Rik Sarkar},
       year={2020},
       eprint={2003.04819},
       archivePrefix={arXiv},
       primaryClass={cs.LG}
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

**Non-Overlapping Community Detection**

**Neighbourhood-Based Node Level Embedding**

**Attributed Node Level Embedding**

**Meta Node Embedding**

**Graph Level Embedding**

Head over to our [documentation](https://karateclub.readthedocs.io) to find out more about installation and data handling, a full list of implemented methods, and datasets.
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