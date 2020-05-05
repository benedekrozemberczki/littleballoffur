
 ![Version](https://badge.fury.io/py/littleballoffur.svg?style=plastic) ![License](https://img.shields.io/github/license/benedekrozemberczki/littleballoffur.svg?color=blue&style=plastic) [![PyPI download month](https://img.shields.io/pypi/dm/littleballoffur.svg?color=blue&style=plastic)](https://pypi.python.org/pypi/littleballoffur/)

<p align="center">
  <img width="90%" src="https://github.com/benedekrozemberczki/littleballoffur/blob/master/littleballoffurlogo.jpg?sanitize=true" />
</p>

--------------------------------------------------------------------------------

**Little Ball of Fur** is a graph subsampling extension library for [NetworkX](https://networkx.github.io/).

Please look at the **[Documentation](https://littleballoffur.readthedocs.io/)** and **[External Resources](https://littleballoffur.readthedocs.io/en/latest/notes/resources.html)**.

**Little Ball of Fur** consists of state-of-the-art methods to do subsampling on graph structured data. To put it simply it is a Swiss Army knife for graph subsampling research. First, it includes a large variety of vertex and edge sampling techniques. Second, it provides a unified application public interface which makes the use of subsampling algorithms trivial. 

--------------------------------------------------------------------------------

**Citing**

If you find **Little Ball of Fur** and the new datasets useful in your research, please consider citing the following paper:

```bibtex
>@misc{littleballoffur2020,
       title={Little Ball of Fur: A Python Library for Graph Subsampling},
       author={Benedek Rozemberczki},
       year={2020},
}
```
--------------------------------------------------------------------------------

**A simple example**

**Little Ball of Fur** makes using modern graph subsampling techniques quite easy (see [here](https://littleballoffur.readthedocs.io/en/latest/notes/introduction.html) for the accompanying tutorial).
For example, this is all it takes to use [Random Walk Node Sampling](https://www.eecs.yorku.ca/course_archive/2017-18/F/6412/reading/kdd17p145.pdf) on a Watts-Strogatz graph:

```python
import networkx as nx
from littleballoffur import RandomWalkSampler

graph = nx.newman_watts_strogatz_graph(1000, 20, 0.05)

sampler = RandomWalkSampler()

new_graph = sampler.sample(graph)
```

--------------------------------------------------------------------------------

**Methods included**

In detail, the following sampling methods were implemented.

**Node Sampling**

* **[Degree Based Node Sampler](https://little-ball-of-fur.readthedocs.io/en/latest/modules/root.html#littleballoffur.node_sampling.degreebasedsampler.DegreeBasedSampler)** from Adamic *et al.*: [Search In Power-Law Networks](https://arxiv.org/abs/cs/0103016) (Physical Review E 2001)

* **[Random Node Sampler](https://little-ball-of-fur.readthedocs.io/en/latest/modules/root.html#littleballoffur.node_sampling.randomnodesampler.RandomNodeSampler)** from Stumpf *et al.*: [SubNets of Scale-Free Networks Are Not Scale-Free: Sampling Properties of Networks](https://www.pnas.org/content/102/12/4221) (PNAS 2005)

* **[PageRank Based Node Sampler](https://little-ball-of-fur.readthedocs.io/en/latest/modules/root.html#littleballoffur.node_sampling.pagerankbasedsampler.PageRankBasedSampler)** from Leskovec *et al.*: [Sampling From Large Graphs](https://cs.stanford.edu/people/jure/pubs/sampling-kdd06.pdf) (KDD 2006)

**Edge Sampling**

* **[Random Edge Sampler](https://little-ball-of-fur.readthedocs.io/en/latest/modules/root.html#littleballoffur.edge_sampling.randomedgesampler.RandomEdgeSampler)** from Krishnamurthy *et al.*: [Reducing Large Internet Topologies for Faster Simulations](http://www.cs.ucr.edu/~michalis/PAPERS/sampling-networking-05.pdf) (Networking 2005)

* **[Random Node-Edge Sampler](https://little-ball-of-fur.readthedocs.io/en/latest/modules/root.html#littleballoffur.edge_sampling.randomnodeedgesampler.RandomNodeEdgeSampler)** from Krishnamurthy *et al.*: [Reducing Large Internet Topologies for Faster Simulations](http://www.cs.ucr.edu/~michalis/PAPERS/sampling-networking-05.pdf) (Networking 2005)

* **[Hybrid Node-Edge Sampler](https://little-ball-of-fur.readthedocs.io/en/latest/modules/root.html#littleballoffur.edge_sampling.hybridnodeedgesampler.HybridNodeEdgeSampler)** from Krishnamurthy *et al.*: [Reducing Large Internet Topologies for Faster Simulations](http://www.cs.ucr.edu/~michalis/PAPERS/sampling-networking-05.pdf) (Networking 2005)

* **[Random Edge Sampler with Induction](https://little-ball-of-fur.readthedocs.io/en/latest/modules/root.html#littleballoffur.edge_sampling.randomedgesamplerwithinduction.RandomEdgeSamplerWithInduction)** from Krishnamurthy *et al.*: [Reducing Large Internet Topologies for Faster Simulations](http://www.cs.ucr.edu/~michalis/PAPERS/sampling-networking-05.pdf) (Networking 2005)

**Expansion Sampling**

* **[Random Walk Sampler](https://little-ball-of-fur.readthedocs.io/en/latest/modules/root.html#module-littleballoffur.expansion_sampling.randomwalksampler)** from Gjoka *et al.*: [Walking in Facebook: A
Case Study of Unbiased Sampling of OSNs](https://ieeexplore.ieee.org/document/5462078) (INFOCOM 2010)

* **[Random Node-Neighbor Sampler](https://little-ball-of-fur.readthedocs.io/en/latest/modules/root.html#module-littleballoffur.expansion_sampling.randomnodeneighborsampler)** from Leskovec *et al.*: [Sampling From Large Graphs](https://cs.stanford.edu/people/jure/pubs/sampling-kdd06.pdf) (KDD 2006)

Head over to our [documentation](https://littleballoffur.readthedocs.io) to find out more about installation and data handling, a full list of implemented methods, and datasets.
For a quick start, check out our [examples](https://github.com/benedekrozemberczki/littleballoffur/tree/master/examples.py).

If you notice anything unexpected, please open an [issue](https://github.com/benedekrozemberczki/littleballoffur/issues) and let us know.
If you are missing a specific method, feel free to open a [feature request](https://github.com/benedekrozemberczki/littleballoffur/issues).
We are motivated to constantly make **Little Ball of Fur** even better.


--------------------------------------------------------------------------------

**Installation**

**Little Ball of Fur** can be installed with the following pip command.

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
