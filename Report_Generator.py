#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 09:08:52 2018

@author: caw4618
"""

#Framework to call in all files and generate graphs and tables used in report.
#Data from tables used in report, but tables themselves not used directly.
#All files will be sent to a folder called "figures"
from Conclusion_Time_time_steps import *
from Conclusion import *
from frame import *
from Order import *
from Time_time_steps import *
main(10,40,0.8,"square")
main(40,40,0.2,"square")
main(10,40,0.8,"mixed")
main(40,40,0.2,"mixed")
main(10,40,0.8,"cos")
main(40,40,0.2,"cos")
main(10,40,0.8,"sine")
main(40,40,0.2,"sine")
error_graph(0.3,lambda X:cosBell(X,0,0.75),'cos',2)
error_graph(0.9,lambda X:cosBell(X,0,0.75),'cos',2)
error_graph(0.3,lambda X:cosBell(X,0,0.75),'cos',0.3)
error_graph(0.9,lambda X:cosBell(X,0,0.75),'cos',0.9)
error_graph(0.2,lambda X:cosBell(X,0,0.75),'cos',4)
error_graph(0.8,lambda X:cosBell(X,0,0.75),'cos',4)
comp_time_cost('cos')
comp_time_cost('square')
con_square(40,80,0.5)
con_time_cost()


