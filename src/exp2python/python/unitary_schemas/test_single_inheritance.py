# This file was generated by exp2python.  You probably don't want to edit
# it since your modifications will be lost if exp2python is used to
# regenerate it.
import sys

from SCL.SCLBase import *
from SCL.SimpleDataTypes import *
from SCL.ConstructedDataTypes import *
from SCL.AggregationDataTypes import *
from SCL.TypeChecker import check_type
from SCL.Builtin import *
from SCL.Rules import *

schema_name = 'test_single_inheritance'

schema_scope = sys.modules[__name__]

# Defined datatype length_measure
class length_measure(REAL):
	def __init__(self,*kargs):
		pass

# Defined datatype label
class label(STRING):
	def __init__(self,*kargs):
		pass

# Defined datatype point
class point(REAL):
	def __init__(self,*kargs):
		pass


####################
 # ENTITY shape #
####################
class shape(BaseEntityClass):
	'''Entity shape definition.

	:param item_name
	:type item_name:label

	:param number_of_sides
	:type number_of_sides:INTEGER
	'''
	def __init__( self , item_name,number_of_sides, ):
		self.item_name = item_name
		self.number_of_sides = number_of_sides

	@property
	def item_name(self):
		return self._item_name
	@item_name.setter
	def item_name( self, value ):
	# Mandatory argument
		if value==None:
			raise AssertionError('Argument item_name is mandatory and can not be set to None')
		if not check_type(value,label):
			self._item_name = label(value)
		else:
			self._item_name = value

	@property
	def number_of_sides(self):
		return self._number_of_sides
	@number_of_sides.setter
	def number_of_sides( self, value ):
	# Mandatory argument
		if value==None:
			raise AssertionError('Argument number_of_sides is mandatory and can not be set to None')
		if not check_type(value,INTEGER):
			self._number_of_sides = INTEGER(value)
		else:
			self._number_of_sides = value

####################
 # ENTITY rectangle #
####################
class rectangle(shape):
	'''Entity rectangle definition.

	:param height
	:type height:length_measure

	:param width
	:type width:length_measure
	'''
	def __init__( self , inherited0__item_name , inherited1__number_of_sides , height,width, ):
		shape.__init__(self , inherited0__item_name , inherited1__number_of_sides , )
		self.height = height
		self.width = width

	@property
	def height(self):
		return self._height
	@height.setter
	def height( self, value ):
	# Mandatory argument
		if value==None:
			raise AssertionError('Argument height is mandatory and can not be set to None')
		if not check_type(value,length_measure):
			self._height = length_measure(value)
		else:
			self._height = value

	@property
	def width(self):
		return self._width
	@width.setter
	def width( self, value ):
	# Mandatory argument
		if value==None:
			raise AssertionError('Argument width is mandatory and can not be set to None')
		if not check_type(value,length_measure):
			self._width = length_measure(value)
		else:
			self._width = value
