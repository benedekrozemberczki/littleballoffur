![Version](https://badge.fury.io/py/littleballoffur.svg?style=plastic) [![repo size](https://img.shields.io/github/repo-size/benedekrozemberczki/littleballoffur.svg)](https://github.com/benedekrozemberczki/littleballoffur/archive/master.zip) [![Arxiv](https://img.shields.io/badge/ArXiv-2006.04311-orange.svg)](https://arxiv.org/abs/2006.04311) [![build badge](https://github.com/benedekrozemberczki/littleballoffur/workflows/CI/badge.svg)](https://github.com/benedekrozemberczki/littleballoffur/actions?query=workflow%3ACI) [![coverage badge](https://codecov.io/gh/benedekrozemberczki/littleballoffur/branch/master/graph/badge.svg)](https://codecov.io/github/benedekrozemberczki/littleballoffur?branch=master) [![benedekrozemberczki](https://img.shields.io/twitter/follow/benrozemberczki?style=social&logo=twitter)](https://twitter.com/intent/follow?screen_name=benrozemberczki)

<p align="center">
  <img width="90%" src="https://github.com/benedekrozemberczki/littleballoffur/blob/master/littleballoffurlogo.jpg?sanitize=true" />
</p>

------------------------------------------------------------------------------

**Little Ball of Fur** is a graph sampling extension library for Python.

Please look at the **[Documentation](https://little-ball-of-fur.readthedocs.io/)**, relevant **[Paper](https://arxiv.org/abs/2006.04311)**, **[Promo video](https://youtu.be/5OpjBqlPWME)** and **[External Resources](https://little-ball-of-fur.readthedocs.io/en/latest/notes/resources.html)**.

------------------------------------------------------------------------------

**Little Ball of Fur** consists of methods that can sample from graph structured data. To put it simply it is a Swiss Army knife for graph sampling tasks. First, it includes a large variety of vertex, edge, and exploration sampling techniques. Second, it provides a unified application public interface which makes the application of sampling algorithms trivial for end-users. Implemented methods cover a wide range of networking ([Networking](https://link.springer.com/conference/networking), [INFOCOM](https://infocom2020.ieee-infocom.org/), [SIGCOMM](http://www.sigcomm.org/)) and data mining ([KDD](https://www.kdd.org/kdd2020/), [TKDD](https://dl.acm.org/journal/tkdd), [ICDE](http://www.wikicfp.com/cfp/program?id=1331&s=ICDE&f=International%20Conference%20on%20Data%20Engineering)) conferences, workshops, and pieces from prominent journals. 

------------------------------------------------------------------------------

**Citing**

If you find **Little Ball of Fur** useful in your research, please consider citing the following paper:

```bibtex
@inproceedings{littleballoffur,
               title={{Little Ball of Fur: A Python Library for Graph Sampling}},
               author={Benedek Rozemberczki and Oliver Kiss and Rik Sarkar},
               year={2020},
               pages = {3133–3140},
               booktitle={Proceedings of the 29th ACM International Conference on Information and Knowledge Management (CIKM '20)},
               organization={ACM},
}
```
------------------------------------------------------------------------------

**A simple example**

**Little Ball of Fur** makes using modern graph subsampling techniques quite easy (see [here](https://little-ball-of-fur.readthedocs.io/en/latest/notes/introduction.html) for the accompanying tutorial).
For example, this is all it takes to use [Diffusion Sampling](https://arxiv.org/abs/2001.07463) on a Watts-Strogatz graph:

```python
import networkx as nx
from littleballoffur import DiffusionSampler

graph = nx.newman_watts_strogatz_graph(1000, 20, 0.05)

sampler = DiffusionSampler()

new_graph = sampler.sample(graph)
```

--------------------------------------------------------------------------------

**Methods included**

In detail, the following sampling methods were implemented.

**Node Sampling**


* **[Degree Based Node Sampler](https://little-ball-of-fur.readthedocs.io/en/latest/modules/node_sampling.html#littleballoffur.node_sampling.degreebasedsampler.DegreeBasedSampler)** from Adamic *et al.*: [Search In Power-Law Networks](https://arxiv.org/abs/cs/0103016) (Physical Review E 2001)

* **[Random Node Sampler](https://little-ball-of-fur.readthedocs.io/en/latest/modules/node_sampling.html#littleballoffur.node_sampling.randomnodesampler.RandomNodeSampler)** from Stumpf *et al.*: [SubNets of Scale-Free Networks Are Not Scale-Free: Sampling Properties of Networks](https://www.pnas.org/content/102/12/4221) (PNAS 2005)

* **[PageRank Based Node Sampler](https://little-ball-of-fur.readthedocs.io/en/latest/modules/node_sampling.html#littleballoffur.node_sampling.pagerankbasedsampler.PageRankBasedSampler)** from Leskovec *et al.*: [Sampling From Large Graphs](https://cs.stanford.edu/people/jure/pubs/sampling-kdd06.pdf) (KDD 2006)

**Edge Sampling**

* **[Random Edge Sampler](https://little-ball-of-fur.readthedocs.io/en/latest/modules/edge_sampling.html#littleballoffur.edge_sampling.randomedgesampler.RandomEdgeSampler)** from Krishnamurthy *et al.*: [Reducing Large Internet Topologies for Faster Simulations](http://www.cs.ucr.edu/~michalis/PAPERS/sampling-networking-05.pdf) (Networking 2005)

* **[Random Node-Edge Sampler](https://little-ball-of-fur.readthedocs.io/en/latest/modules/edge_sampling.html#littleballoffur.edge_sampling.randomnodeedgesampler.RandomNodeEdgeSampler)** from Krishnamurthy *et al.*: [Reducing Large Internet Topologies for Faster Simulations](http://www.cs.ucr.edu/~michalis/PAPERS/sampling-networking-05.pdf) (Networking 2005)

* **[Hybrid Node-Edge Sampler](https://little-ball-of-fur.readthedocs.io/en/latest/modules/edge_sampling.html#littleballoffur.edge_sampling.hybridnodeedgesampler.HybridNodeEdgeSampler)** from Krishnamurthy *et al.*: [Reducing Large Internet Topologies for Faster Simulations](http://www.cs.ucr.edu/~michalis/PAPERS/sampling-networking-05.pdf) (Networking 2005)

* **[Random Edge Sampler with Induction](https://little-ball-of-fur.readthedocs.io/en/latest/modules/edge_sampling.html#littleballoffur.edge_sampling.randomedgesamplerwithinduction.RandomEdgeSamplerWithInduction)** from Ahmed *et al.*: [Network Sampling: From Static to Streaming Graphs](https://dl.acm.org/doi/10.1145/2601438) (TKDD 2013)

* **[Random Edge Sampler with Partial Induction](https://little-ball-of-fur.readthedocs.io/en/latest/modules/edge_sampling.html#littleballoffur.edge_sampling.randomedgesamplerwithpartialinduction.RandomEdgeSamplerWithPartialInduction)** from Ahmed *et al.*: [Network Sampling: From Static to Streaming Graphs](https://dl.acm.org/doi/10.1145/2601438) (TKDD 2013)

**Exploration Based Sampling**

* **[Snowball Sampler](https://little-ball-of-fur.readthedocs.io/en/latest/modules/exploration_sampling.html#littleballoffur.exploration_sampling.snowballsampler.SnowBallSampler)** from Goodman: [Snowball Sampling](https://projecteuclid.org/euclid.aoms/1177705148) (The Annals of Mathematical Statistics 1961)

* **[Loop-Erased Random Walk Sampler](https://little-ball-of-fur.readthedocs.io/en/latest/modules/exploration_sampling.html#littleballoffur.exploration_sampling.looperasedrandomwalksampler.LoopErasedRandomWalkSampler)** from Wilson: [Generating Random Spanning Trees More Quickly Than the Cover Time](https://link.springer.com/chapter/10.1007/978-1-4612-2168-5_12) (STOC 1996)

* **[Forest Fire Sampler](https://little-ball-of-fur.readthedocs.io/en/latest/modules/exploration_sampling.html#littleballoffur.exploration_sampling.forestfiresampler.ForestFireSampler)** from Leskovec *et al.*: [Graphs over Time: Densification Laws, Shrinking Diameters and Possible Explanations](https://cs.stanford.edu/people/jure/pubs/sampling-kdd06.pdf) (KDD 2005)

<details>
<summary><b>Expand to see all exploration samplers...</b></summary>


* **[Random Node-Neighbor Sampler](https://little-ball-of-fur.readthedocs.io/en/latest/modules/exploration_sampling.html#littleballoffur.exploration_sampling.randomnodeneighborsampler.RandomNodeNeighborSampler)** from Leskovec *et al.*: [Sampling From Large Graphs](https://cs.stanford.edu/people/jure/pubs/sampling-kdd06.pdf) (KDD 2006)

* **[Random Walk With Restart Sampler](https://little-ball-of-fur.readthedocs.io/en/latest/modules/exploration_sampling.html#littleballoffur.exploration_sampling.randomwalkwithrestartsampler.RandomWalkWithRestartSampler)** from Leskovec *et al.*: [Sampling From Large Graphs](https://cs.stanford.edu/people/jure/pubs/sampling-kdd06.pdf) (KDD 2006)

* **[Metropolis Hastings Random Walk Sampler](https://little-ball-of-fur.readthedocs.io/en/latest/modules/exploration_sampling.html#littleballoffur.exploration_sampling.metropolishastingsrandomwalksampler.MetropolisHastingsRandomWalkSampler)** from Hubler *et al.*: [Metropolis Algorithms for Representative Subgraph Sampling](http://mlcb.is.tuebingen.mpg.de/Veroeffentlichungen/papers/HueBorKriGha08.pdf) (ICDM 2008)

* **[Random Walk Sampler](https://little-ball-of-fur.readthedocs.io/en/latest/modules/exploration_sampling.html#littleballoffur.exploration_sampling.randomwalksampler.RandomWalkSampler)** from Gjoka *et al.*: [Walking in Facebook: A Case Study of Unbiased Sampling of OSNs](https://ieeexplore.ieee.org/document/5462078) (INFOCOM 2010)

* **[Random Walk With Jump Sampler](https://little-ball-of-fur.readthedocs.io/en/latest/modules/exploration_sampling.html#littleballoffur.exploration_sampling.randomwalkwithjumpsampler.RandomWalkWithJumpSampler)** from Ribeiro *et al.*: [Estimating and Sampling Graphs with Multidimensional Random Walks](https://arxiv.org/abs/1002.1751) (SIGCOMM 2010)

* **[Frontier Sampler](https://little-ball-of-fur.readthedocs.io/en/latest/modules/exploration_sampling.html#littleballoffur.exploration_sampling.frontiersampler.FrontierSampler)** from Ribeiro *et al.*: [Estimating and Sampling Graphs with Multidimensional Random Walks](https://arxiv.org/abs/1002.1751) (SIGCOMM 2010)

* **[Community Structure Expansion Sampler](https://little-ball-of-fur.readthedocs.io/en/latest/modules/exploration_sampling.html#littleballoffur.exploration_sampling.communitystructureexpansionsampler.CommunityStructureExpansionSampler)** from Maiya *et al.*: [Sampling Community Structure](http://arun.maiya.net/papers/maiya_etal-sampcomm.pdf) (WWW 2010)

* **[Non-Backtracking Random Walk Sampler](https://little-ball-of-fur.readthedocs.io/en/latest/modules/exploration_sampling.html#littleballoffur.exploration_sampling.nonbacktrackingrandomwalksampler.NonBackTrackingRandomWalkSampler)** from Lee *et al.*: [Beyond Random Walk and Metropolis-Hastings Samplers: Why You Should Not Backtrack for Unbiased Graph Sampling](https://dl.acm.org/doi/10.1145/2318857.2254795) (SIGMETRICS 2012)

* **[Randomized Depth First Search Sampler](https://little-ball-of-fur.readthedocs.io/en/latest/modules/exploration_sampling.html#littleballoffur.exploration_sampling.depthfirstsearchsampler.DepthFirstSearchSampler)** from Doerr *et al.*: [Metric Convergence in Social Network Sampling](https://dl.acm.org/doi/10.1145/2491159.2491168) (HotPlanet 2013)

* **[Randomized Breadth First Search Sampler](https://little-ball-of-fur.readthedocs.io/en/latest/modules/exploration_sampling.html#littleballoffur.exploration_sampling.breadthfirstsearchsampler.BreadthFirstSearchSampler)** from Doerr *et al.*: [Metric Convergence in Social Network Sampling](https://dl.acm.org/doi/10.1145/2491159.2491168) (HotPlanet 2013)

* **[Rejection Constrained Metropolis Hastings Random Walk Sampler](https://little-ball-of-fur.readthedocs.io/en/latest/modules/exploration_sampling.html#littleballoffur.exploration_sampling.metropolishastingsrandomwalksampler.MetropolisHastingsRandomWalkSampler)** from Li *et al.*: [On Random Walk Based Graph Sampling](https://ieeexplore.ieee.org/document/7113345) (ICDE 2015)

* **[Circulated Neighbors Random Walk Sampler](https://little-ball-of-fur.readthedocs.io/en/latest/modules/exploration_sampling.html#littleballoffur.exploration_sampling.circulatedneighborsrandomwalksampler.CirculatedNeighborsRandomWalkSampler)** from Zhou *et al.*: [Leveraging History for Faster Sampling of Online Social Networks](https://dl.acm.org/doi/10.5555/2794367.2794373) (VLDB 2015)

* **[Shortest Path Sampler](https://little-ball-of-fur.readthedocs.io/en/latest/modules/exploration_sampling.html#littleballoffur.exploration_sampling.shortestpathsampler.ShortestPathSampler)** from Rezvanian *et al.*: [Sampling Social Networks Using Shortest Paths](https://www.sciencedirect.com/science/article/pii/S0378437115000321) (Physica A 2015)

* **[Diffusion Sampler](https://little-ball-of-fur.readthedocs.io/en/latest/modules/exploration_sampling.html#littleballoffur.exploration_sampling.diffusionsampler.DiffusionSampler)** from Rozemberczki *et al.*: [Fast Sequence-Based Embedding with Diffusion Graphs](https://arxiv.org/abs/2001.07463) (Complex Networks 2018)

* **[Diffusion Tree Sampler](https://little-ball-of-fur.readthedocs.io/en/latest/modules/exploration_sampling.html#littleballoffur.exploration_sampling.diffusiontreesampler.DiffusionTreeSampler)** from Rozemberczki *et al.*: [Fast Sequence-Based Embedding with Diffusion Graphs](https://arxiv.org/abs/2001.07463) (Complex Networks 2018)

* **[Common Neighbor Aware Random Walk Sampler](https://little-ball-of-fur.readthedocs.io/en/latest/modules/exploration_sampling.html#littleballoffur.exploration_sampling.commonneighborawarerandomwalksampler.CommonNeighborAwareRandomWalkSampler)** from Li *et al.*: [Walking with Perception: Efficient Random Walk Sampling via Common Neighbor Awareness](https://ieeexplore.ieee.org/document/8731555) (ICDE 2019)

* **[Spiky Ball Sampler](https://little-ball-of-fur.readthedocs.io/en/latest/modules/exploration_sampling.html#littleballoffur.exploration_sampling.spikyballsampler.SpikyBallSampler)** from Ricaud *et al.*: [Spikyball Sampling: Exploring Large Networks via an Inhomogeneous Filtered Diffusion](https://www.mdpi.com/1999-4893/13/11/275) (Algorithms 2020)

  </details>

Head over to our [documentation](https://little-ball-of-fur.readthedocs.io) to find out more about installation and data handling, a full list of implemented methods, and datasets.
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

--------------------------------------------------------------------------

**Running examples**

As part of the documentation we provide a number of use cases to show how to use various sampling techniques. These can accessed [here](https://little-ball-of-fur.readthedocs.io/en/latest/notes/introduction.html) with detailed explanations.


Besides the case studies we provide synthetic examples for each model. These can be tried out by running the scripts in the examples folder. You can try out the random walk sampling example by running:

```sh
$ cd examples
$ python ./exploration_sampling/randomwalk_sampler.py
```

---------------------------------------------------------------------


**Running tests**

```sh
$ python setup.py test
```

---------------------------------------------------------------------


**License**

- [GNU General Public License v3.0](https://github.com/benedekrozemberczki/littleballoffur/blob/master/LICENSE)
