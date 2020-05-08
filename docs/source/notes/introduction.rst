Introduction by example
=======================

*Little Ball of Fur* is a graph sampling extension library for `NetworkX <https://networkx.github.io/>`_.

*Little Ball of Fur* consists of methods to do sampling of graph structured data. To put it simply it is a Swiss Army knife for graph sampling tasks. First, it includes a large variety of vertex, edge and expansions sampling techniques. Second, it provides a unified application public interface which makes the application of sampling algorithms trivial for end-users. Implemented methods cover a wide range of networking (`Networking <https://link.springer.com/conference/networking>`_, `INFOCOM <https://infocom2020.ieee-infocom.org/>`_, `SIGCOMM  <http://www.sigcomm.org/>`_) and data mining (`KDD <https://www.kdd.org/kdd2020/>`_, `TKDD <https://dl.acm.org/journal/tkdd>`_, `ICDE <http://www.wikicfp.com/cfp/program?id=1331&s=ICDE&f=International%20Conference%20on%20Data%20Engineering>`_) conferences, workshops, and pieces from prominent journals.

--------------------------------------------------------------------------------

**Citing**

If you find *Little Ball of Fur* useful in your research, please consider citing the following paper:

.. code-block:: latex

    >@misc{littleballoffur2020,
           title={Little Ball of Fur: A Python Library for Graph Subsampling},
           author={Benedek Rozemberczki and Oliver Kiss and Rik Sarkar},
           year={2020},
    }

Overview
=======================
--------------------------------------------------------------------------------

We shortly overview the fundamental concepts and features of Little Ball of Fur through simple examples. These are the following:

.. contents::
    :local:

Standardized dataset ingestion
------------------------------

Little Ball of Fur assumes that the NetworkX graph provided by the user has the following important properties:

- The graph is undirected.
- The graph is connected (it consists of a single strongly connected component).
- Nodes are indexed with integers.
- There are no orphaned nodes in the graph.
- The node indexing starts with zero and the indices are consecutive.

The returned NetworkX graph uses the same indexing.

API driven design
-----------------

Little Ball of Fur uses the design principles of Scikit-Learn which means that the algorithms in the package share the same API. Each graph sampling procedure is implemented as a class which inherits from ``Sampler``. The constructors of the sampling algorithms are used to set the hyperparameters. The sampling procedures have default hyperparameters that work well out of the box. This means that non expert users do not have to make decisions about these in advance and only a little fine tuning is required. For each class the ``sample`` public method provides sampling from the graph. This API driven design in practice means that one can sample a subgraph from a Watts-Strogatz graph with a ``RandomWalkSampler`` just like this.

.. code-block:: python

    import networkx as nx
    from littleballoffur import RandomWalkSampler
    
    graph = nx.newman_watts_strogatz_graph(1000, 20, 0.05)

    model = RandomWalkSampler()
    new_graph = model.sample(graph)

This snippet can be modified to use a ``ForestFireSampler`` with minimal effort like this.

.. code-block:: python

    import networkx as nx
    from littleballoffur import ForestFireSampler
    
    graph = nx.newman_watts_strogatz_graph(1000, 20, 0.05)

    model = ForestFireSampler()
    new_graph = model.sample(graph)

Looking at these two snippets the advantage of the API driven design is evident. First, one had to change the import of the sampler. Second, we needed to change the sampler construction and the default hyperparameters
were already set. The public methods provided by ``RandomWalkSampler`` and ``ForestFireSampler`` are the same. A subsample is is returned by
``sample``. This allows for quick and minimal changes to the code when a sampling procedure performs poorly.


Node sampling
-------------------

The first task that we will look at is sampling a subgraph by drawing a representative set of nodes from a Facebook graph. In this network
nodes represent official verified Facebook pages and the links between them are mutual likes. For details
about the dataset `see this paper <https://arxiv.org/abs/1909.13021>`_.

We first need to load the Facebook page-page network dataset which is returned as a ``NetworkX`` graph.

.. code-block:: python

    from littleballoffur import GraphReader

    reader = GraphReader("facebook")

    graph = reader.get_graph()

The constructor defines the graph reader object while the ``get_graph`` method reads the data.

Now let's use the ``PageRank Proportional Node Sampling`` method from `Near Linear Time Algorithm to Detect Community Structures in Large-Scale Networks <https://arxiv.org/abs/0709.2938>`_. 

.. code-block:: python

    from karateclub import LabelPropagation
    
    model = LabelPropagation()
    model.fit(graph)
    cluster_membership = model.get_memberships()

The constructor defines a model, we fit the model on the Facebook graph with the ``fit`` method and return the cluster memberships
with the ``get_memberships`` method as a dictionary.


Finally we can evaluate the clustering using normalized mutual information. First we need to create an ordered list of the node memberships.
We use the ground truth about the cluster memberships for calculating the NMI.


.. code-block:: python

    from sklearn.metrics.cluster import normalized_mutual_info_score

    cluster_membership = [cluster_membership[node] for node in range(len(cluster_membership))]

    nmi = normalized_mutual_info_score(target, cluster_membership)
    print('NMI: {:.4f}'.format(nmi))
    >>> NMI: 0.34374

Edge sampling
--------------

The second machine learning task that we look at is the identification of users from the UK who abuse the platform on Twitch. 
In the social network of interest nodes represent users and the links are mutual friendships between the users. Our goal is
to perform binary classification of the users (platform abusers and general good guy users).  For details
about the dataset `see this paper <https://arxiv.org/abs/1909.13021>`_.

We first need to load the Twitch UK dataset. We will use the user friendship graph and the 
abusive user target vector. These are returned as a ``NetworkX`` graph and ``numpy`` array respectively.

.. code-block:: python

    from karateclub.dataset import GraphReader

    reader = GraphReader("twitch")

    graph = reader.get_graph()
    y = reader.get_target()

We fit a `Diff2vec node embedding <https://arxiv.org/abs/2001.07463>`_, with a low number of dimensions, diffusions per source node, and short Euler walks.
First, we use the model constructor with custom parameters. Second, we fit the model to the graph. Third, we get the node embedding
which is a ``numpy`` array.

.. code-block:: python

    from karateclub import Diff2Vec

    model = Diff2Vec(diffusion_number=2, diffusion_cover=20, dimensions=16)
    model.fit(graph)
    X = model.get_embedding()

We use the node embedding features as predictors of the abusive behaviour. So let us create a train-test split of the explanatory variables
and the target variable with Scikit-Learn. We will use a test data ratio of 20%. Here it is.

.. code-block:: python

    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

Using the training data (``X_train`` and ``y_train``) we learn a logistic regression model to predict the probability of someone being an abusive user. We perform inference on the test 
set for this target. Finally, we evaluate the model performance by printing an area under the ROC curve value.

.. code-block:: python

    from sklearn.metrics import roc_auc_score
    from sklearn.linear_model import LogisticRegression
    
    downstream_model = LogisticRegression(random_state=0).fit(X_train, y_train)
    y_hat = downstream_model.predict_proba(X_test)[:, 1]
    auc = roc_auc_score(y_test, y_hat)
    print('AUC: {:.4f}'.format(auc))
    >>> AUC: 0.6069

Exploration sampling
--------------------

The third machine learning task that we look at is the classification of threads from the online forum Reddit. The threads
can be of of two types - discussion and non-discussion based ones. Our goal is to predict the type of the thread based on
the topological (structural) properties of the graphs. The specific dataset that we look a 10 thousand graph subsample of
the Reddit 204K dataset which contains a large number of threads from the spring of 2018. The graphs in the dataset do not
have a specific feature. Because of this we use the degree centrality as a string feature.
For details about the dataset `see this paper <https://arxiv.org/abs/2003.04819>`_.

We first need to load the Reddit 10K dataset. We will use the use the graphs and the discussion/non-discussion target vector.
These are returned as a list of ``NetworkX`` graphs and ``numpy`` array respectively.

.. code-block:: python

    from karateclub.dataset import GraphSetReader

    reader = GraphSetReader("reddit10k")

    graphs = reader.get_graphs()
    y = reader.get_target()

We fit a Graph2Vec graph level embedding, with the standard hyperparameter settings. These are pretty widely used settings.
First, we use the model constructor without custom parameters. Second, we fit the model to the graphs. Third, we get the graph embedding
which is a ``numpy`` array.

.. code-block:: python

    from karateclub import Graph2Vec

    model = Graph2Vec()
    model.fit(graphs)
    X = model.get_embedding()

We use the graph embedding features as predictors of the thread type. So let us create a train-test split of the explanatory variables
and the target variable with Scikit-Learn. We will use a test data ratio of 20%. Here it is.

.. code-block:: python

    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

Using the training data (``X_train`` and ``y_train``) we learn a logistic regression model to predict the probability of a thread being discussion based. We perform inference on the test 
set for this target. Finally, we evaluate the model performance by printing an area under the ROC curve value.

.. code-block:: python

    from sklearn.metrics import roc_auc_score
    from sklearn.linear_model import LogisticRegression
    
    downstream_model = LogisticRegression(random_state=0).fit(X_train, y_train)
    y_hat = downstream_model.predict_proba(X_test)[:, 1]
    auc = roc_auc_score(y_test, y_hat)
    print('AUC: {:.4f}'.format(auc))
    >>> AUC: 0.7127


Benchmark datasets
------------------

We included a number of datasets which can be used for comparing the performance of sampling algorithms. These are the following:

- `Twitch user network from the UK. <https://arxiv.org/abs/1909.13021>`_
- `Wikipedia page-page network with articles about Crocodiles. <https://arxiv.org/abs/1909.13021>`_
- `GitHub machine learning and web developers social network. <https://arxiv.org/abs/1909.13021>`_
- `Facebook verified page-page network. <https://arxiv.org/abs/1909.13021>`_
