#!/bin/bash


wget -nv https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
chmod +x miniconda.sh
./miniconda.sh -b
conda update --yes conda
conda create --yes -n test
