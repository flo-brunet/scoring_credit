#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from setuptools import setup, find_packages
 
# notez qu'on import la lib
# donc assurez-vous que l'importe n'a pas d'effet de bord
import preprocessing
 

setup(
    name='preprocessing',
    version=preprocessing.__version__,
    packages=find_packages(),
    description="Common preprocessing functions",
    install_requires=[]
)