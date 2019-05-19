#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 19 03:32:51 2019

@author: dario
"""


import sys
from anytree import Node, RenderTree
import json


jsonfilename = sys.argv[1]
tree = {}
with open(jsonfilename) as json_file:  
    data = json.load(json_file)
    for ele in data:
        if ele['parent'] == "-":
             tree = {ele['element'] : Node(ele['element'])}
             first_ele = ele['element']
        else:
            tree.update({ele['element'] : Node(ele['element'], parent=tree[ele['parent']])})


for pre, fill, node in RenderTree(tree[first_ele]):
    print("%s%s" % (pre, node.name))