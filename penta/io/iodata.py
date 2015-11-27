# This python script take an input file and:
# turn it into nested dictionaries with key:value pairs
# use tuples or lists when you have multiple objects in one tag
# use Numpy arrays when you have more than one float/int.

import numpy as np

class IOMolecule(object):
    '''A container class for molecule data loaded from (or to be written to) a file.
 
        In principle, the constructor accepts any keyword argument, which is
        stored as an attribute. All attributes are optional. Attributes can be
        set are removed after the IOMolecule instance is constructed. The following
        attributes are supported by at least one of the io formats:
 
        **Type checked array attributes (if present):**

		title
			A suitable name for the data
 
        coordinates
             A (N, 3) float array with Cartesian coordinates of the atoms.
 
        numbers
             A (N,) int vector with the atomic numbers.
 
        pseudo_numbers
             A (N,) float array with pseudo-potential core charges.
	''' 

	def __init__(self,file_handle):
		self.dic = dict()
		self.f = file_handle
	@classmethod
	def read_from_file(cls,file)
class IOGobasis(object):
    '''A container class for gaussian orbital basis set data loaded from a file.
 
        In principle, the constructor accepts any keyword argument, which is
        stored as an attribute. All attributes are optional. Attributes can be
        set are removed after the IOGobasis instance is constructed. The following
        attributes are supported by at least one of the io formats:
 
        **Type checked array attributes (if present):**

		title
			A suitable name for the basis set
 
        PrimCoeff
             A (N, 3) float array with Cartesian coordinates of the atoms.
 
        OrbCoeff
             A (N,) int vector with the atomic numbers.
 
        AngMoment
             A (N,) float array with pseudo-potential core charges.
	''' 
	pass
class IO(object):
	pass
