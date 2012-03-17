# This file was generated by fedex_python.  You probably don't want to edit
# it since your modifications will be lost if fedex_plus is used to
# regenerate it.
import sys

from SCL.SCLBase import *
from SCL.SimpleDataTypes import *
from SCL.ConstructedDataTypes import *
from SCL.AggregationDataTypes import *
from SCL.TypeChecker import check_type
from SCL.Builtin import *
from SCL.Rules import *

schema_name = 'test_derived_attribute'

schema_scope = sys.modules[__name__]


####################
 # ENTITY vector #
####################
class vector(BaseEntityClass):
	'''Entity vector definition.
	'''
	# This class does not define any attribute.
	pass

####################
 # ENTITY circle #
####################
class circle(BaseEntityClass):
	'''Entity circle definition.

	:param centre
	:type centre:point

	:param radius
	:type radius:REAL

	:param axis
	:type axis:vector

	:param area
	:type area:REAL

	:param perimeter
	:type perimeter:REAL
	'''
	def __init__( self , centre,radius,axis, ):
		self.centre = centre
		self.radius = radius
		self.axis = axis

	@apply
	def centre():
		def fget( self ):
			return self._centre
		def fset( self, value ):
		# Mandatory argument
			if value==None:
				raise AssertionError('Argument centre is mantatory and can not be set to None')
			if not check_type(value,point):
				self._centre = point(value)
			else:
				self._centre = value
		return property(**locals())

	@apply
	def radius():
		def fget( self ):
			return self._radius
		def fset( self, value ):
		# Mandatory argument
			if value==None:
				raise AssertionError('Argument radius is mantatory and can not be set to None')
			if not check_type(value,REAL):
				self._radius = REAL(value)
			else:
				self._radius = value
		return property(**locals())

	@apply
	def axis():
		def fget( self ):
			return self._axis
		def fset( self, value ):
		# Mandatory argument
			if value==None:
				raise AssertionError('Argument axis is mantatory and can not be set to None')
			if not check_type(value,vector):
				self._axis = vector(value)
			else:
				self._axis = value
		return property(**locals())

	@apply
	def area():
		def fget( self ):
			attribute_eval = ( PI   *  (radius  **  2))
			return attribute_eval
		def fset( self, value ):
		# DERIVED argument
			raise AssertionError('Argument area is DERIVED. It is computed and can not be set to any value')
		return property(**locals())

	@apply
	def perimeter():
		def fget( self ):
			attribute_eval = ((2  *   PI )  *  radius)
			return attribute_eval
		def fset( self, value ):
		# DERIVED argument
			raise AssertionError('Argument perimeter is DERIVED. It is computed and can not be set to any value')
		return property(**locals())

####################
 # ENTITY point #
####################
class point(BaseEntityClass):
	'''Entity point definition.
	'''
	# This class does not define any attribute.
	pass
