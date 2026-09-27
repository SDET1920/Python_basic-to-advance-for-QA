# Imported modules from 2 different packages

## Pack 1- Module1-Display()
## Pack1-Pack2-Module2-Show()

import sys
sys.path.append("C:/Users/hp/PycharmProjects/Python_basic-to-advance-for-QA/Day_24/Pack1")
sys.path.append("C:/Users/hp/PycharmProjects/Python_basic-to-advance-for-QA/Day_24/Pack1/Pack2")

import Module1
import Module2

Module1.display()
Module2.show()
