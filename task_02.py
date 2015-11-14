 #!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


# Determines validity of input data

class InvalidAgeError(Exception):
    """subclass of exception"""
    pass
     
    def get_age(birthyear):
        """Year of birth to determine validity of input value.
            birthyear (int): four digit integers for birthyear.
        """    
        age = datetime.datetime.now().year - birthyear
        return age
    def __main__(self, InvalidAgeError):
        """Birthyear input"""
        InvalidAgeError = get_age < 115
        Error = InvalidAgeError
        return InvalidAgeError.


