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

schema_name = 'multiple_rep'

schema_scope = sys.modules[__name__]

# Defined datatype text
class text(STRING):
	def __init__(self,*kargs):
		pass

# Defined datatype representation_context
class representation_context(STRING):
	def __init__(self,*kargs):
		pass

# Defined datatype identifier
class identifier(STRING):
	def __init__(self,*kargs):
		pass

# Defined datatype shape_definition
class shape_definition(STRING):
	def __init__(self,*kargs):
		pass

# Defined datatype transformation
class transformation(STRING):
	def __init__(self,*kargs):
		pass

# Defined datatype representation_item
class representation_item(STRING):
	def __init__(self,*kargs):
		pass

# Defined datatype characterized_product_definition
class characterized_product_definition(STRING):
	def __init__(self,*kargs):
		pass

# SELECT TYPE characterized_definition
characterized_definition = SELECT(
	'characterized_object',
	'characterized_product_definition',
	'shape_definition',
	scope = schema_scope)
# Defined datatype label
class label(STRING):
	def __init__(self,*kargs):
		pass

# Defined datatype characterized_object
class characterized_object(STRING):
	def __init__(self,*kargs):
		pass


####################
 # ENTITY representation_relationship #
####################
class representation_relationship(BaseEntityClass):
	'''Entity representation_relationship definition.

	:param name
	:type name:label

	:param rep_1
	:type rep_1:representation

	:param rep_2
	:type rep_2:representation
	'''
	def __init__( self , name,rep_1,rep_2, ):
		self.name = name
		self.rep_1 = rep_1
		self.rep_2 = rep_2

	@property
	def name(self):
		return self._name
	@name.setter
	def name( self, value ):
	# Mandatory argument
		if value==None:
			raise AssertionError('Argument name is mandatory and can not be set to None')
		if not check_type(value,label):
			self._name = label(value)
		else:
			self._name = value

	@property
	def rep_1(self):
		return self._rep_1
	@rep_1.setter
	def rep_1( self, value ):
	# Mandatory argument
		if value==None:
			raise AssertionError('Argument rep_1 is mandatory and can not be set to None')
		if not check_type(value,representation):
			self._rep_1 = representation(value)
		else:
			self._rep_1 = value

	@property
	def rep_2(self):
		return self._rep_2
	@rep_2.setter
	def rep_2( self, value ):
	# Mandatory argument
		if value==None:
			raise AssertionError('Argument rep_2 is mandatory and can not be set to None')
		if not check_type(value,representation):
			self._rep_2 = representation(value)
		else:
			self._rep_2 = value

####################
 # ENTITY shape_representation_relationship #
####################
class shape_representation_relationship(representation_relationship):
	'''Entity shape_representation_relationship definition.
	'''
	def __init__( self , inherited0__name , inherited1__rep_1 , inherited2__rep_2 ,  ):
		representation_relationship.__init__(self , inherited0__name , inherited1__rep_1 , inherited2__rep_2 , )
	def wr1(self):
		eval_wr1_wr = ('MULTIPLE_REP.SHAPE_REPRESENTATION'  ==  (TYPEOF(self.self.representation_relationship.self.rep_1)  +  TYPEOF(self.self.representation_relationship.self.rep_2)))
		if not eval_wr1_wr:
			raise AssertionError('Rule wr1 violated')
		else:
			return eval_wr1_wr


####################
 # ENTITY representation #
####################
class representation(BaseEntityClass):
	'''Entity representation definition.

	:param name
	:type name:label

	:param items
	:type items:SET(1,None,'STRING', scope = schema_scope)

	:param context_of_items
	:type context_of_items:representation_context
	'''
	def __init__( self , name,items,context_of_items, ):
		self.name = name
		self.items = items
		self.context_of_items = context_of_items

	@property
	def name(self):
		return self._name
	@name.setter
	def name( self, value ):
	# Mandatory argument
		if value==None:
			raise AssertionError('Argument name is mandatory and can not be set to None')
		if not check_type(value,label):
			self._name = label(value)
		else:
			self._name = value

	@property
	def items(self):
		return self._items
	@items.setter
	def items( self, value ):
	# Mandatory argument
		if value==None:
			raise AssertionError('Argument items is mandatory and can not be set to None')
		if not check_type(value,SET(1,None,'STRING', scope = schema_scope)):
			self._items = SET(value)
		else:
			self._items = value

	@property
	def context_of_items(self):
		return self._context_of_items
	@context_of_items.setter
	def context_of_items( self, value ):
	# Mandatory argument
		if value==None:
			raise AssertionError('Argument context_of_items is mandatory and can not be set to None')
		if not check_type(value,representation_context):
			self._context_of_items = representation_context(value)
		else:
			self._context_of_items = value

	def wr1(self):
		eval_wr1_wr = (SIZEOF(USEDIN(self,'MULTIPLE_REP.'  +  'ID_ATTRIBUTE.IDENTIFIED_ITEM'))  <=  1)
		if not eval_wr1_wr:
			raise AssertionError('Rule wr1 violated')
		else:
			return eval_wr1_wr

	def wr2(self):
		eval_wr2_wr = (SIZEOF(USEDIN(self,'MULTIPLE_REP.'  +  'DESCRIPTION_ATTRIBUTE.DESCRIBED_ITEM'))  <=  1)
		if not eval_wr2_wr:
			raise AssertionError('Rule wr2 violated')
		else:
			return eval_wr2_wr


####################
 # ENTITY property_definition #
####################
class property_definition(BaseEntityClass):
	'''Entity property_definition definition.

	:param name
	:type name:label

	:param definition
	:type definition:characterized_definition
	'''
	def __init__( self , name,definition, ):
		self.name = name
		self.definition = definition

	@property
	def name(self):
		return self._name
	@name.setter
	def name( self, value ):
	# Mandatory argument
		if value==None:
			raise AssertionError('Argument name is mandatory and can not be set to None')
		if not check_type(value,label):
			self._name = label(value)
		else:
			self._name = value

	@property
	def definition(self):
		return self._definition
	@definition.setter
	def definition( self, value ):
	# Mandatory argument
		if value==None:
			raise AssertionError('Argument definition is mandatory and can not be set to None')
		if not check_type(value,characterized_definition):
			self._definition = characterized_definition(value)
		else:
			self._definition = value

	def wr1(self):
		eval_wr1_wr = (SIZEOF(USEDIN(self,'MULTIPLE_REP.'  +  'ID_ATTRIBUTE.IDENTIFIED_ITEM'))  <=  1)
		if not eval_wr1_wr:
			raise AssertionError('Rule wr1 violated')
		else:
			return eval_wr1_wr


####################
 # ENTITY context_dependent_shape_representation #
####################
class context_dependent_shape_representation(BaseEntityClass):
	'''Entity context_dependent_shape_representation definition.

	:param representation_relation
	:type representation_relation:shape_representation_relationship
	'''
	def __init__( self , representation_relation, ):
		self.representation_relation = representation_relation

	@property
	def representation_relation(self):
		return self._representation_relation
	@representation_relation.setter
	def representation_relation( self, value ):
	# Mandatory argument
		if value==None:
			raise AssertionError('Argument representation_relation is mandatory and can not be set to None')
		if not check_type(value,shape_representation_relationship):
			self._representation_relation = shape_representation_relationship(value)
		else:
			self._representation_relation = value

	def wr2(self):
		eval_wr2_wr = (SIZEOF(USEDIN(self,'MULTIPLE_REP.'  +  'DESCRIPTION_ATTRIBUTE.DESCRIBED_ITEM'))  <=  1)
		if not eval_wr2_wr:
			raise AssertionError('Rule wr2 violated')
		else:
			return eval_wr2_wr

	def wr3(self):
		eval_wr3_wr = (SIZEOF(USEDIN(self,'MULTIPLE_REP.'  +  'NAME_ATTRIBUTE.NAMED_ITEM'))  <=  1)
		if not eval_wr3_wr:
			raise AssertionError('Rule wr3 violated')
		else:
			return eval_wr3_wr


####################
 # ENTITY definitional_representation_relationship #
####################
class definitional_representation_relationship(representation_relationship):
	'''Entity definitional_representation_relationship definition.
	'''
	def __init__( self , inherited0__name , inherited1__rep_1 , inherited2__rep_2 ,  ):
		representation_relationship.__init__(self , inherited0__name , inherited1__rep_1 , inherited2__rep_2 , )

####################
 # ENTITY component_2d_location #
####################
class component_2d_location(context_dependent_shape_representation,shape_representation_relationship,definitional_representation_relationship):
	'''Entity component_2d_location definition.

	:param context_dependent_shape_representation_representation_relation
	:type context_dependent_shape_representation_representation_relation:component_2d_location
	'''
	def __init__( self , inherited0__representation_relation , inherited1__name , inherited2__rep_1 , inherited3__rep_2 , inherited4__name , inherited5__rep_1 , inherited6__rep_2 ,  ):
		context_dependent_shape_representation.__init__(self , inherited0__representation_relation , )
		shape_representation_relationship.__init__(self , inherited1__name , inherited2__rep_1 , inherited3__rep_2 , )
		definitional_representation_relationship.__init__(self , inherited4__name , inherited5__rep_1 , inherited6__rep_2 , )

	@property
	def context_dependent_shape_representation_representation_relation(self):
		attribute_eval = self
		return attribute_eval
	@context_dependent_shape_representation_representation_relation.setter
	def context_dependent_shape_representation_representation_relation( self, value ):
	# DERIVED argument
		raise AssertionError('Argument context_dependent_shape_representation_representation_relation is DERIVED. It is computed and can not be set to any value')

	def wr1(self):
		eval_wr1_wr = (self.self.representation_relationship.self.name  ==  'component 2d location')
		if not eval_wr1_wr:
			raise AssertionError('Rule wr1 violated')
		else:
			return eval_wr1_wr

