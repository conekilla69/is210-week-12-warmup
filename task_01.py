#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""


# what variables will be exempted
def simple_lookup(var1, var2):
    """Variables for exemption.

    var1 (index) : value index position.
    var2(key): dict key.
    """
    try:
        var1[var2]
    except IndexError, KeyError:
        print 'Warning: your index/key doesn\'t exist'
    return var1
    

    
    
    
