:github_url: https://github.com/benedekrozemberczki/littleballoffur

Little Ball of Fur  Documentation
==================================

**Little Ball of Fur** consists of state-of-the-art methods to do subsampling on graph structured data. To put it simply it is a Swiss Army knife for graph subsampling tasks. First, it includes a large variety of vertex, edge and expansions sampling techniques. Second, it provides a unified application public interface which makes the application of subsampling algorithms trivial for end-users. Implemented methods cover a wide range of networking ([Networking](https://link.springer.com/conference/networking), [INFOCOM](https://infocom2020.ieee-infocom.org/), [SIGCOMM](http://www.sigcomm.org/)) and data mining ([KDD](https://www.kdd.org/kdd2020/), [TKDD](https://dl.acm.org/journal/tkdd), [ICDE](http://www.wikicfp.com/cfp/program?id=1331&s=ICDE&f=International%20Conference%20on%20Data%20Engineering)) conferences, workshops, and pieces from prominent journals. 

*Karate Club* is an unsupervised machine learning extension library for `NetworkX <https://networkx.github.io/>`_. It builds on other open source linear algebra, machine learning, and graph signal processing libraries such as `Numpy <https://numpy.org/>`_, `Scipy <https://www.scipy.org/>`_, `Gensim <https://radimrehurek.com/gensim/>`_, `PyGSP <https://pygsp.readthedocs.io/en/stable/>`_, and `Scikit-Learn <https://scikit-learn.org/stable/>`_. *Karate Club* consists of state-of-the-art methods to do unsupervised learning on graph structured data. To put it simply it is a Swiss Army knife for small-scale graph mining research. First, it provides network embedding techniques at the node and graph level. Second, it includes a variety of overlapping and non-overlapping commmunity detection methods. Implemented methods cover a wide range of network science `NetSci <https://netscisociety.net/home>`_, `Complenet <https://complenet.weebly.com/>`_, data mining `ICDM <http://icdm2019.bigke.org/>`_, `CIKM <http://www.cikm2019.net/>`_, `KDD <https://www.kdd.org/kdd2020/>`_, artificial intelligence `AAAI <http://www.aaai.org/Conferences/conferences.php>`_, `IJCAI <https://www.ijcai.org/>`_ and machine learning `NeurIPS <https://nips.cc/>`_, `ICML <https://icml.cc/>`_, `ICLR <https://iclr.cc/>`_ conferences, workshops, and pieces from prominent journals. 


.. code-block:: latex

    >@misc{littleballoffur2020,
           title={Little Ball of Fur: A Python Library for Graph Subsampling},
           author={Benedek Rozemberczki and Oliver Kiss and Rik Sarkar},
           year={2020},
    }


.. toctree::
   :glob:
   :maxdepth: 2
   :caption: Notes

   notes/installation
   notes/introduction
   notes/create_dataset
   notes/examples
   notes/resources

.. toctree::
   :glob:
   :maxdepth: 2
   :caption: Package Reference

   modules/root
   modules/dataset
