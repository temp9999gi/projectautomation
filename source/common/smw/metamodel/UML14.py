from __future__ import nested_scopes
import copy
from smw.metamodel.MetaMM import *
MMFullName='UML 14'
MMVersion='14'
MMName='UML'

class AggregationKind(MMEnumeration):
		ak_none=0
		ak_aggregate=1
		ak_composite=2
		description=[u'ak_none', u'ak_aggregate', u'ak_composite']
class CallConcurrencyKind(MMEnumeration):
		cck_sequential=0
		cck_guarded=1
		cck_concurrent=2
		description=[u'cck_sequential', u'cck_guarded', u'cck_concurrent']
class ChangeableKind(MMEnumeration):
		ck_changeable=0
		ck_frozen=1
		ck_addOnly=2
		description=[u'ck_changeable', u'ck_frozen', u'ck_addOnly']
class OrderingKind(MMEnumeration):
		ok_unordered=0
		ok_ordered=1
		description=[u'ok_unordered', u'ok_ordered']
class ParameterDirectionKind(MMEnumeration):
		pdk_in=0
		pdk_inout=1
		pdk_out=2
		pdk_return=3
		description=[u'pdk_in', u'pdk_inout', u'pdk_out', u'pdk_return']
class ScopeKind(MMEnumeration):
		sk_instance=0
		sk_classifier=1
		description=[u'sk_instance', u'sk_classifier']
class VisibilityKind(MMEnumeration):
		vk_public=0
		vk_protected=1
		vk_private=2
		vk_package=3
		description=[u'vk_public', u'vk_protected', u'vk_private', u'vk_package']
class LocationReference(MMEnumeration):
		description=[]
class PseudostateKind(MMEnumeration):
		pk_choice=0
		pk_deepHistory=1
		pk_fork=2
		pk_initial=3
		pk_join=4
		pk_junction=5
		pk_shallowHistory=6
		description=[u'pk_choice', u'pk_deepHistory', u'pk_fork', u'pk_initial', u'pk_join', u'pk_junction', u'pk_shallowHistory']
class Geometry(MMEnumeration):
		description=[]

class ElementImport(MMClass):
		__name__='ElementImport'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.importedElement!=None and \
					 self.package!=None

class Expression(MMClass):
		__name__='Expression'
		__userWellFormedRule__=MMSet()

class ProcedureExpression(Expression):
		__name__='ProcedureExpression'
		__userWellFormedRule__=MMSet()

class BooleanExpression(Expression):
		__name__='BooleanExpression'
		__userWellFormedRule__=MMSet()

class ObjectSetExpression(Expression):
		__name__='ObjectSetExpression'
		__userWellFormedRule__=MMSet()

class ArgListsExpression(Expression):
		__name__='ArgListsExpression'
		__userWellFormedRule__=MMSet()

class ElementResidence(MMClass):
		__name__='ElementResidence'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.container!=None and \
					 self.resident!=None

class TemplateParameter(MMClass):
		__name__='TemplateParameter'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.template!=None and \
					 self.parameter!=None

class Multiplicity(MMClass):
		__name__='Multiplicity'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.range.size()>=1

class MultiplicityRange(MMClass):
		__name__='MultiplicityRange'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.multiplicity!=None

class TypeExpression(Expression):
		__name__='TypeExpression'
		__userWellFormedRule__=MMSet()

class IterationExpression(Expression):
		__name__='IterationExpression'
		__userWellFormedRule__=MMSet()

class ActionExpression(Expression):
		__name__='ActionExpression'
		__userWellFormedRule__=MMSet()

class TemplateArgument(MMClass):
		__name__='TemplateArgument'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.binding!=None and \
					 self.modelElement!=None

class TimeExpression(Expression):
		__name__='TimeExpression'
		__userWellFormedRule__=MMSet()

class MappingExpression(Expression):
		__name__='MappingExpression'
		__userWellFormedRule__=MMSet()

class ModelElement(Element):
		__name__='ModelElement'
		__userWellFormedRule__=MMSet()

class Partition(ModelElement):
		__name__='Partition'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.activityGraph!=None

class Comment(ModelElement):
		__name__='Comment'
		__userWellFormedRule__=MMSet()

class LinkEnd(ModelElement):
		__name__='LinkEnd'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.instance!=None and \
					 self.link!=None and \
					 self.associationEnd!=None

class StateMachine(ModelElement):
		__name__='StateMachine'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.top!=None

class Argument(ModelElement):
		__name__='Argument'
		__userWellFormedRule__=MMSet()

class Guard(ModelElement):
		__name__='Guard'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.transition!=None

class TaggedValue(ModelElement):
		__name__='TaggedValue'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.type!=None and \
					 self.modelElement!=None

class Message(ModelElement):
		__name__='Message'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.receiver!=None and \
					 self.interaction!=None and \
					 self.sender!=None and \
					 self.action!=None

class AssociationEnd(ModelElement):
		__name__='AssociationEnd'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.association!=None and \
					 self.participant!=None

class InteractionInstanceSet(ModelElement):
		__name__='InteractionInstanceSet'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.context!=None and \
					 self.participatingStimulus.size()>=1

class Instance(ModelElement):
		__name__='Instance'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.classifier.size()>=1

class TagDefinition(ModelElement):
		__name__='TagDefinition'
		__userWellFormedRule__=MMSet()

class Object(Instance):
		__name__='Object'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.classifier.size()>=1

class SubsystemInstance(Instance):
		__name__='SubsystemInstance'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.classifier.size()>=1

class NodeInstance(Instance):
		__name__='NodeInstance'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.classifier.size()>=1

class UseCaseInstance(Instance):
		__name__='UseCaseInstance'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.classifier.size()>=1

class Constraint(ModelElement):
		__name__='Constraint'
		__userWellFormedRule__=MMSet()

class Transition(ModelElement):
		__name__='Transition'
		__userWellFormedRule__=MMSet()
		def getDescription(self):
				text=''
				if self.trigger:
						text=self.trigger.getDescription()
				if self.guard:
						text=text+'['+self.guard.expression.body+']'
				if self.effect:
						text=text+'/'+self.effect.script.body
				return text


		def wfrMetaModelMultiplicity(self):
					return self.target!=None and \
					 self.source!=None

class Action(ModelElement):
		__name__='Action'
		__userWellFormedRule__=MMSet()

class AttributeLink(ModelElement):
		__name__='AttributeLink'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.attribute!=None and \
					 self.value!=None

class EnumerationLiteral(ModelElement):
		__name__='EnumerationLiteral'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.enumeration!=None

class DestroyAction(Action):
		__name__='DestroyAction'
		__userWellFormedRule__=MMSet()

class GeneralizableElement(ModelElement):
		__name__='GeneralizableElement'
		__userWellFormedRule__=MMSet()
		def wfrCanNotGeneralizeItself(self):
				checked = []
				parents = []
				for i in self.generalization:
						parents.append(i)
						
				while len(parents) > 0:
						p = parents.pop()
						checked.append(p)
						p = p.parent
						if p == self:
								return 0
						addthese = p.generalization
						for i in addthese:
								if not i in checked and not i in parents:
										parents.append(i)
				return 1

		def wfrCanNotGeneralizeSameElementTwice(self):
				above = []
				for i in self.generalization:
						if i.parent in above:
								return 0
						above.append(i.parent)
				return 1


class AssociationEndRole(AssociationEnd):
		__name__='AssociationEndRole'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.association!=None and \
					 self.participant!=None

class Event(ModelElement):
		__name__='Event'
		__userWellFormedRule__=MMSet()

class StateVertex(ModelElement):
		__name__='StateVertex'
		__userWellFormedRule__=MMSet()

class Namespace(ModelElement):
		__name__='Namespace'
		__userWellFormedRule__=MMSet()

class Feature(ModelElement):
		__name__='Feature'
		__userWellFormedRule__=MMSet()

class ActionSequence(Action):
		__name__='ActionSequence'
		__userWellFormedRule__=MMSet()

class State(StateVertex):
		__name__='State'
		__userWellFormedRule__=MMSet()

class SendAction(Action):
		__name__='SendAction'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.signal!=None

class Parameter(ModelElement):
		__name__='Parameter'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.type!=None

class ExtensionPoint(ModelElement):
		__name__='ExtensionPoint'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.useCase!=None

class CollaborationInstanceSet(ModelElement):
		__name__='CollaborationInstanceSet'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.participatingInstance.size()>=1

class Relationship(ModelElement):
		__name__='Relationship'
		__userWellFormedRule__=MMSet()

class DataValue(Instance):
		__name__='DataValue'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.classifier.size()>=1

class BehavioralFeature(Feature):
		__name__='BehavioralFeature'
		__userWellFormedRule__=MMSet()

class UninterpretedAction(Action):
		__name__='UninterpretedAction'
		__userWellFormedRule__=MMSet()

class Link(ModelElement):
		__name__='Link'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.connection.size()>=2 and \
					 self.association!=None

class ActivityGraph(StateMachine):
		__name__='ActivityGraph'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.top!=None

class Interaction(ModelElement):
		__name__='Interaction'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.message.size()>=1 and \
					 self.context!=None

class ComponentInstance(Instance):
		__name__='ComponentInstance'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.classifier.size()>=1

class Package(GeneralizableElement ,Namespace):
		__name__='Package'
		__userWellFormedRule__=MMSet()

class Stimulus(ModelElement):
		__name__='Stimulus'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.sender!=None and \
					 self.receiver!=None and \
					 self.dispatchAction!=None

class Pseudostate(StateVertex):
		__name__='Pseudostate'
		__userWellFormedRule__=MMSet()

		def wfrPseudostate1(self):
				"An initial vertex can have at most one outgoing transition and no incoming transitions"
				return implies(self.kind == PseudostateKind.pk_initial,
											 self.outgoing.size()<=1 and self.incoming.isEmpty())

		def wftPseudostate2(self):
				"History vertices can have at most one outgoing transition"
				return implies(self.kind == PseudostateKind.pk_deepHistory or self.kind== PseudostateKind.pk_shallowHistory,
											 self.outgoing.size()<=1)

		

		
		

class CreateAction(Action):
		__name__='CreateAction'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.instantiation!=None

class Reception(BehavioralFeature):
		__name__='Reception'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.signal!=None

class Model(Package):
		__name__='Model'
		__userWellFormedRule__=MMSet()

class Classifier(GeneralizableElement ,Namespace):
		__name__='Classifier'
		__userWellFormedRule__=MMSet()
		def allFeatures(self):
				return self.feature
		
		def allOperations(self):
				return self.allFeatures().select(lambda f: f.oclIsKindOf(Operation))

		def allMethods(self):
				return self.allFeatures().select(lambda f: f.oclIsKindOf(Method))


class Stereotype(GeneralizableElement):
		__name__='Stereotype'
		__userWellFormedRule__=MMSet()

class Generalization(Relationship):
		__name__='Generalization'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.parent!=None and \
					 self.child!=None

class Collaboration(GeneralizableElement ,Namespace):
		__name__='Collaboration'
		__userWellFormedRule__=MMSet()

class CallAction(Action):
		__name__='CallAction'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.operation!=None

class CompositeState(State):
		__name__='CompositeState'
		__userWellFormedRule__=MMSet()
		def wfrCompositeState1(self):
				"A composite state can have at most one initial vertex"
				return self.subvertex.select(
						lambda v: v.oclIsKindOf(Pseudostate) and v.kind== PseudostateKind.pk_initial).size() <=1
		
		def wfrCompositeState2(self):
				"A composite state can have at most one deep history vertex"
				return self.subvertex.select(
						lambda v: v.oclIsKindOf(Pseudostate) and v.kind== PseudostateKind.pk_deepHistory).size() <=1

		def wfrCompositeState3(self):
				"A composite state can have at most one shallow history vertex"
				return self.subvertex.select(
						lambda v: v.oclIsKindOf(Pseudostate) and v.kind== PseudostateKind.pk_shallowHistory).size() <=1

		def wfrCompositeState4(self):
				"There have to be at least two composite substates in a concurrent composite state"
				return implies(self.isConcurrent,
											 self.subvertex.select(lambda v:
																						 v.oclIsKindOf(CompositeState)).size()>=2)

		def wfrCompositeState5(self):
				"A concurrent state can only have composite states as substates"
				return implies(self.isConcurrent,
											 self.subvertex.forAll(lambda s:
																						 s.oclIsKindOf(CompositeState)))

		def wfrCompositeState6(self):
				"The substates of a composite state are part of only that composite state"
				return self.subvertex.forAll(lambda s: s.container.asSet().size()==1 and s.container == self)



class Include(Relationship):
		__name__='Include'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.base!=None and \
					 self.addition!=None

class Method(BehavioralFeature):
		__name__='Method'
		__userWellFormedRule__=MMSet()
		def wfrHasSameSignature(self):
				op = self.specification
				if not op:
						return None
				if len(self.parameter) != len(op.parameter):
						return None
				x = 1
				for i in range(len(self.parameter)):
						pm, po = self.parameter[i], op.parameter[i]
						x = x and (pm.name == po.name)
						x = x and (pm.type.name == po.type.name)
						x = x and (pm.kind == po.kind)
				return x


		def wfrMetaModelMultiplicity(self):
					return self.specification!=None

class Node(Classifier):
		__name__='Node'
		__userWellFormedRule__=MMSet()

class ChangeEvent(Event):
		__name__='ChangeEvent'
		__userWellFormedRule__=MMSet()
		def getDescription(self):
				return self.changeExpression



class Extend(Relationship):
		__name__='Extend'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.extensionPoint.size()>=1 and \
					 self.base!=None and \
					 self.extension!=None

class TimeEvent(Event):
		__name__='TimeEvent'
		__userWellFormedRule__=MMSet()
		def getDescription(self):
				return self.when


class TerminateAction(Action):
		__name__='TerminateAction'
		__userWellFormedRule__=MMSet()

class Association(GeneralizableElement ,Relationship):
		__name__='Association'
		__userWellFormedRule__=MMSet()
		def wfrAssociation1(self):
				return self.allConnections().forAll(
						lambda r1,r2: implies(r1.name==r2.name,r1==r2))
		def wfrAssociation2(self):
				return self.allConnections().select(lambda c: c.aggregation != AggregationKind.ak_none).size()<=1
		def wfrAssociation3(self):
				return implies(self.allConnections().size()>=3,
											 self.allConnections().forAll(
						lambda c: c.aggregation == AggregationKind.ak_none))

		def allConnections(self):
				return self.connection
																						

		def wfrMetaModelMultiplicity(self):
					return self.connection.size()>=2

class ClassifierInState(Classifier):
		__name__='ClassifierInState'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.inState.size()>=1 and \
					 self.type!=None

class ReturnAction(Action):
		__name__='ReturnAction'
		__userWellFormedRule__=MMSet()

class Flow(Relationship):
		__name__='Flow'
		__userWellFormedRule__=MMSet()

class SimpleState(State):
		__name__='SimpleState'
		__userWellFormedRule__=MMSet()

class StructuralFeature(Feature):
		__name__='StructuralFeature'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.type!=None

class Dependency(Relationship):
		__name__='Dependency'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.supplier.size()>=1 and \
					 self.client.size()>=1

class UseCase(Classifier):
		__name__='UseCase'
		__userWellFormedRule__=MMSet()

class Actor(Classifier):
		__name__='Actor'
		__userWellFormedRule__=MMSet()

class SignalEvent(Event):
		__name__='SignalEvent'
		__userWellFormedRule__=MMSet()
		def getDescription(self):
				return self.signal.name


		def wfrMetaModelMultiplicity(self):
					return self.signal!=None

class CallEvent(Event):
		__name__='CallEvent'
		__userWellFormedRule__=MMSet()
		def getDescription(self):
				return self.operation.name


		def wfrMetaModelMultiplicity(self):
					return self.operation!=None

class Attribute(StructuralFeature):
		__name__='Attribute'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.type!=None

class Binding(Dependency):
		__name__='Binding'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.argument.size()>=1 and \
					 self.supplier.size()>=1 and \
					 self.client.size()>=1

class StubState(StateVertex):
		__name__='StubState'
		__userWellFormedRule__=MMSet()

class Class(Classifier):
		__name__='Class'
		__userWellFormedRule__=MMSet()
		def wfrClass1(self):
				"If a Class is concrete, all the Operations of the Class should have a realizing Method in the full descriptor [1.4,01.02.01,2-60]"
				return self.isAbstract or self.allOperations().forAll(lambda op: self.allMethods().exist(lambda m: m.specification.asSet().includes(op)))
				

class DataType(Classifier):
		__name__='DataType'
		__userWellFormedRule__=MMSet()

class SynchState(StateVertex):
		__name__='SynchState'
		__userWellFormedRule__=MMSet()

class FinalState(State):
		__name__='FinalState'
		__userWellFormedRule__=MMSet()

		def wfrFinalState1(self):
				"A final state cannot have any outgoing transitions"
				return self.outgoing.size()==0



class LinkObject(Object ,Link):
		__name__='LinkObject'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.classifier.size()>=1 and \
					 self.connection.size()>=2 and \
					 self.association!=None

class Operation(BehavioralFeature):
		__name__='Operation'
		__userWellFormedRule__=MMSet()

class ActionState(SimpleState):
		__name__='ActionState'
		__userWellFormedRule__=MMSet()

class ObjectFlowState(SimpleState):
		__name__='ObjectFlowState'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.type!=None

class Enumeration(DataType):
		__name__='Enumeration'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.literal.size()>=1

class ProgrammingLanguageDataType(DataType):
		__name__='ProgrammingLanguageDataType'
		__userWellFormedRule__=MMSet()

class Abstraction(Dependency):
		__name__='Abstraction'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.supplier.size()>=1 and \
					 self.client.size()>=1

class Permission(Dependency):
		__name__='Permission'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.supplier.size()>=1 and \
					 self.client.size()>=1

class Component(Classifier):
		__name__='Component'
		__userWellFormedRule__=MMSet()

class Artifact(Classifier):
		__name__='Artifact'
		__userWellFormedRule__=MMSet()

class ClassifierRole(Classifier):
		__name__='ClassifierRole'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.base.size()>=1

class AssociationRole(Association):
		__name__='AssociationRole'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.connection.size()>=2

class Interface(Classifier):
		__name__='Interface'
		__userWellFormedRule__=MMSet()

class Subsystem(Package ,Classifier):
		__name__='Subsystem'
		__userWellFormedRule__=MMSet()

class Signal(Classifier):
		__name__='Signal'
		__userWellFormedRule__=MMSet()

class Primitive(DataType):
		__name__='Primitive'
		__userWellFormedRule__=MMSet()

class SubmachineState(CompositeState):
		__name__='SubmachineState'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.submachine!=None

class CallState(ActionState):
		__name__='CallState'
		__userWellFormedRule__=MMSet()

class Usage(Dependency):
		__name__='Usage'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.supplier.size()>=1 and \
					 self.client.size()>=1

class SubactivityState(SubmachineState):
		__name__='SubactivityState'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.submachine!=None

class Exception(Signal):
		__name__='Exception'
		__userWellFormedRule__=MMSet()

class AssociationClass(Association ,Class):
		__name__='AssociationClass'
		__userWellFormedRule__=MMSet()

		def wfrMetaModelMultiplicity(self):
					return self.connection.size()>=2
TimeExpression.__subclasses__=[]
TimeExpression.__mm__={
		'language': (MMClass.kind__Attribute,Name,1,None,None,0),
		'body': (MMClass.kind__Attribute,String,1,None,None,0)
}

CallAction.__subclasses__=[]
CallAction.__mm__={
		'operation': (MMClass.kind__Association,Operation,1,'callAction',0,0),
		'recurrence': (MMClass.kind__Attribute,IterationExpression,1,None,None,0),
		'target': (MMClass.kind__Attribute,ObjectSetExpression,1,None,None,0),
		'isAsynchronous': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'script': (MMClass.kind__Attribute,ActionExpression,1,None,None,0),
		'stateExit': (MMClass.kind__Association,State,1,'exit',1,0),
		'transition': (MMClass.kind__Association,Transition,1,'effect',1,0),
		'message': (MMClass.kind__Association,Message,0,'action',1,0),
		'stateDoActivity': (MMClass.kind__Association,State,1,'doActivity',1,0),
		'state': (MMClass.kind__Association,State,1,'entry',1,0),
		'actionSequence': (MMClass.kind__Association,ActionSequence,1,'action',0,0),
		'stimulus': (MMClass.kind__Association,Stimulus,0,'dispatchAction',1,0),
		'actualArgument': (MMClass.kind__Composition,Argument,0,'action',1,1),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,1),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

AssociationEnd.__subclasses__=[AssociationEndRole]
AssociationEnd.__mm__={
		'isNavigable': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'ordering': (MMClass.kind__Attribute,OrderingKind,1,None,None,0),
		'aggregation': (MMClass.kind__Attribute,AggregationKind,1,None,None,0),
		'targetScope': (MMClass.kind__Attribute,ScopeKind,1,None,None,0),
		'multiplicity': (MMClass.kind__Attribute,Multiplicity,1,None,None,0),
		'changeability': (MMClass.kind__Attribute,ChangeableKind,1,None,None,0),
		'associationEndRole': (MMClass.kind__Association,AssociationEndRole,0,'base',1,0),
		'association': (MMClass.kind__Association,Association,1,'connection',0,0),
		'specification': (MMClass.kind__Association,Classifier,0,'specifiedEnd',0,0),
		'qualifier': (MMClass.kind__Composition,Attribute,0,'associationEnd',1,1),
		'linkEnd': (MMClass.kind__Association,LinkEnd,0,'associationEnd',1,0),
		'participant': (MMClass.kind__Association,Classifier,1,'association',0,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

PresentationElement.__subclasses__=[]
InteractionInstanceSet.__subclasses__=[]
InteractionInstanceSet.__mm__={
		'interaction': (MMClass.kind__Association,Interaction,1,'interactionInstanceSet',0,0),
		'context': (MMClass.kind__Association,CollaborationInstanceSet,1,'interactionInstanceSet',0,0),
		'participatingStimulus': (MMClass.kind__Association,Stimulus,0,'interactionInstanceSet',0,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

SubmachineState.__subclasses__=[SubactivityState]
SubmachineState.__mm__={
		'submachine': (MMClass.kind__Association,StateMachine,1,'submachineState',0,0),
		'isRegion': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isConcurrent': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'subvertex': (MMClass.kind__Composition,StateVertex,0,'container',1,0),
		'internalTransition': (MMClass.kind__Composition,Transition,0,'state',1,0),
		'classifierInState': (MMClass.kind__Association,ClassifierInState,0,'inState',0,0),
		'exit': (MMClass.kind__Composition,Action,1,'stateExit',1,0),
		'doActivity': (MMClass.kind__Composition,Action,1,'stateDoActivity',1,0),
		'entry': (MMClass.kind__Composition,Action,1,'state',1,0),
		'stateMachine': (MMClass.kind__Association,StateMachine,1,'top',1,0),
		'deferrableEvent': (MMClass.kind__Association,Event,0,'state',0,0),
		'incoming': (MMClass.kind__Association,Transition,0,'target',1,0),
		'container': (MMClass.kind__Association,CompositeState,1,'subvertex',0,0),
		'outgoing': (MMClass.kind__Association,Transition,0,'source',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

Instance.__subclasses__=[Object, SubsystemInstance, NodeInstance, UseCaseInstance, DataValue, ComponentInstance, LinkObject]
Instance.__mm__={
		'slot': (MMClass.kind__Composition,AttributeLink,0,'instance',1,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'participatingInstance',0,0),
		'stimulus': (MMClass.kind__Association,Stimulus,0,'argument',0,0),
		'classifier': (MMClass.kind__Association,Classifier,0,'instance',0,0),
		'stimulusSender': (MMClass.kind__Association,Stimulus,0,'sender',1,0),
		'linkEnd': (MMClass.kind__Association,LinkEnd,0,'instance',1,0),
		'componentInstance': (MMClass.kind__Association,ComponentInstance,1,'resident',0,0),
		'ownedLink': (MMClass.kind__Composition,Link,0,'owner',1,0),
		'ownedInstance': (MMClass.kind__Composition,Instance,0,'owner',1,0),
		'owner': (MMClass.kind__Association,Instance,1,'ownedInstance',0,0),
		'stimulusReceiver': (MMClass.kind__Association,Stimulus,0,'receiver',1,0),
		'playedRole': (MMClass.kind__Association,ClassifierRole,0,'conformingInstance',0,0),
		'attributeLink': (MMClass.kind__Association,AttributeLink,0,'value',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

CompositeState.__subclasses__=[SubmachineState, SubactivityState]
CompositeState.__mm__={
		'isRegion': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isConcurrent': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'subvertex': (MMClass.kind__Composition,StateVertex,0,'container',1,0),
		'internalTransition': (MMClass.kind__Composition,Transition,0,'state',1,0),
		'classifierInState': (MMClass.kind__Association,ClassifierInState,0,'inState',0,0),
		'exit': (MMClass.kind__Composition,Action,1,'stateExit',1,0),
		'doActivity': (MMClass.kind__Composition,Action,1,'stateDoActivity',1,0),
		'entry': (MMClass.kind__Composition,Action,1,'state',1,0),
		'stateMachine': (MMClass.kind__Association,StateMachine,1,'top',1,0),
		'deferrableEvent': (MMClass.kind__Association,Event,0,'state',0,0),
		'incoming': (MMClass.kind__Association,Transition,0,'target',1,0),
		'container': (MMClass.kind__Association,CompositeState,1,'subvertex',0,0),
		'outgoing': (MMClass.kind__Association,Transition,0,'source',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

CallState.__subclasses__=[]
CallState.__mm__={
		'isDynamic': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'dynamicArguments': (MMClass.kind__Attribute,ArgListsExpression,1,None,None,0),
		'dynamicMultiplicity': (MMClass.kind__Attribute,Multiplicity,1,None,None,0),
		'internalTransition': (MMClass.kind__Composition,Transition,0,'state',1,0),
		'classifierInState': (MMClass.kind__Association,ClassifierInState,0,'inState',0,0),
		'exit': (MMClass.kind__Composition,Action,1,'stateExit',1,0),
		'doActivity': (MMClass.kind__Composition,Action,1,'stateDoActivity',1,0),
		'entry': (MMClass.kind__Composition,Action,1,'state',1,0),
		'stateMachine': (MMClass.kind__Association,StateMachine,1,'top',1,0),
		'deferrableEvent': (MMClass.kind__Association,Event,0,'state',0,0),
		'incoming': (MMClass.kind__Association,Transition,0,'target',1,0),
		'container': (MMClass.kind__Association,CompositeState,1,'subvertex',0,0),
		'outgoing': (MMClass.kind__Association,Transition,0,'source',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

TagDefinition.__subclasses__=[]
TagDefinition.__mm__={
		'tagType': (MMClass.kind__Attribute,Name,1,None,None,0),
		'multiplicity': (MMClass.kind__Attribute,Multiplicity,1,None,None,0),
		'typedValue': (MMClass.kind__Association,TaggedValue,0,'type',1,0),
		'owner': (MMClass.kind__Association,Stereotype,1,'definedTag',0,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

Usage.__subclasses__=[]
Usage.__mm__={
		'supplier': (MMClass.kind__Association,ModelElement,0,'supplierDependency',0,0),
		'client': (MMClass.kind__Association,ModelElement,0,'clientDependency',0,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

Include.__subclasses__=[]
Include.__mm__={
		'base': (MMClass.kind__Association,UseCase,1,'include',0,0),
		'addition': (MMClass.kind__Association,UseCase,1,'includer',0,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

Method.__subclasses__=[]
Method.__mm__={
		'body': (MMClass.kind__Attribute,ProcedureExpression,1,None,None,0),
		'specification': (MMClass.kind__Association,Operation,1,'method',0,0),
		'isQuery': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'raisedSignal': (MMClass.kind__Association,Signal,0,'context',0,0),
		'parameter': (MMClass.kind__Composition,Parameter,0,'behavioralFeature',1,1),
		'ownerScope': (MMClass.kind__Attribute,ScopeKind,1,None,None,0),
		'owner': (MMClass.kind__Association,Classifier,1,'feature',0,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableFeature',0,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

Node.__subclasses__=[]
Node.__mm__={
		'deployedComponent': (MMClass.kind__Association,Component,0,'deploymentLocation',0,0),
		'instance': (MMClass.kind__Association,Instance,0,'classifier',0,0),
		'specifiedEnd': (MMClass.kind__Association,AssociationEnd,0,'specification',0,0),
		'feature': (MMClass.kind__Composition,Feature,0,'owner',1,1),
		'typedFeature': (MMClass.kind__Association,StructuralFeature,0,'type',1,0),
		'powertypeRange': (MMClass.kind__Association,Generalization,0,'powertype',1,0),
		'classifierInState': (MMClass.kind__Association,ClassifierInState,0,'type',1,0),
		'objectFlowState': (MMClass.kind__Association,ObjectFlowState,0,'type',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'base',0,0),
		'typedParameter': (MMClass.kind__Association,Parameter,0,'type',1,0),
		'createAction': (MMClass.kind__Association,CreateAction,0,'instantiation',1,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'representedClassifier',1,0),
		'association': (MMClass.kind__Association,AssociationEnd,0,'participant',1,0),
		'isRoot': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isLeaf': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isAbstract': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'specialization': (MMClass.kind__Association,Generalization,0,'parent',1,0),
		'generalization': (MMClass.kind__Association,Generalization,0,'child',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0),
		'ownedElement': (MMClass.kind__Composition,ModelElement,0,'namespace',1,0)
}

ChangeEvent.__subclasses__=[]
ChangeEvent.__mm__={
		'changeExpression': (MMClass.kind__Attribute,BooleanExpression,1,None,None,0),
		'transition': (MMClass.kind__Association,Transition,0,'trigger',1,0),
		'parameter': (MMClass.kind__Composition,Parameter,0,'event',1,1),
		'state': (MMClass.kind__Association,State,0,'deferrableEvent',0,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

Extend.__subclasses__=[]
Extend.__mm__={
		'condition': (MMClass.kind__Attribute,BooleanExpression,1,None,None,0),
		'extensionPoint': (MMClass.kind__Association,ExtensionPoint,0,'extend',0,1),
		'base': (MMClass.kind__Association,UseCase,1,'extender',0,0),
		'extension': (MMClass.kind__Association,UseCase,1,'extend',0,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

TimeEvent.__subclasses__=[]
TimeEvent.__mm__={
		'when': (MMClass.kind__Attribute,TimeExpression,1,None,None,0),
		'transition': (MMClass.kind__Association,Transition,0,'trigger',1,0),
		'parameter': (MMClass.kind__Composition,Parameter,0,'event',1,0),
		'state': (MMClass.kind__Association,State,0,'deferrableEvent',0,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

Object.__subclasses__=[LinkObject]
Object.__mm__={
		'slot': (MMClass.kind__Composition,AttributeLink,0,'instance',1,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'participatingInstance',0,0),
		'stimulus': (MMClass.kind__Association,Stimulus,0,'argument',0,0),
		'classifier': (MMClass.kind__Association,Classifier,0,'instance',0,0),
		'stimulusSender': (MMClass.kind__Association,Stimulus,0,'sender',1,0),
		'linkEnd': (MMClass.kind__Association,LinkEnd,0,'instance',1,0),
		'componentInstance': (MMClass.kind__Association,ComponentInstance,1,'resident',0,0),
		'ownedLink': (MMClass.kind__Composition,Link,0,'owner',1,0),
		'ownedInstance': (MMClass.kind__Composition,Instance,0,'owner',1,0),
		'owner': (MMClass.kind__Association,Instance,1,'ownedInstance',0,0),
		'stimulusReceiver': (MMClass.kind__Association,Stimulus,0,'receiver',1,0),
		'playedRole': (MMClass.kind__Association,ClassifierRole,0,'conformingInstance',0,0),
		'attributeLink': (MMClass.kind__Association,AttributeLink,0,'value',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

SubactivityState.__subclasses__=[]
SubactivityState.__mm__={
		'isDynamic': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'dynamicArguments': (MMClass.kind__Attribute,ArgListsExpression,1,None,None,0),
		'dynamicMultiplicity': (MMClass.kind__Attribute,Multiplicity,1,None,None,0),
		'submachine': (MMClass.kind__Association,StateMachine,1,'submachineState',0,0),
		'isRegion': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isConcurrent': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'subvertex': (MMClass.kind__Composition,StateVertex,0,'container',1,0),
		'internalTransition': (MMClass.kind__Composition,Transition,0,'state',1,0),
		'classifierInState': (MMClass.kind__Association,ClassifierInState,0,'inState',0,0),
		'exit': (MMClass.kind__Composition,Action,1,'stateExit',1,0),
		'doActivity': (MMClass.kind__Composition,Action,1,'stateDoActivity',1,0),
		'entry': (MMClass.kind__Composition,Action,1,'state',1,0),
		'stateMachine': (MMClass.kind__Association,StateMachine,1,'top',1,0),
		'deferrableEvent': (MMClass.kind__Association,Event,0,'state',0,0),
		'incoming': (MMClass.kind__Association,Transition,0,'target',1,0),
		'container': (MMClass.kind__Association,CompositeState,1,'subvertex',0,0),
		'outgoing': (MMClass.kind__Association,Transition,0,'source',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

TerminateAction.__subclasses__=[]
TerminateAction.__mm__={
		'recurrence': (MMClass.kind__Attribute,IterationExpression,1,None,None,0),
		'target': (MMClass.kind__Attribute,ObjectSetExpression,1,None,None,0),
		'isAsynchronous': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'script': (MMClass.kind__Attribute,ActionExpression,1,None,None,0),
		'stateExit': (MMClass.kind__Association,State,1,'exit',1,0),
		'transition': (MMClass.kind__Association,Transition,1,'effect',1,0),
		'message': (MMClass.kind__Association,Message,0,'action',1,0),
		'stateDoActivity': (MMClass.kind__Association,State,1,'doActivity',1,0),
		'state': (MMClass.kind__Association,State,1,'entry',1,0),
		'actionSequence': (MMClass.kind__Association,ActionSequence,1,'action',0,0),
		'stimulus': (MMClass.kind__Association,Stimulus,0,'dispatchAction',1,0),
		'actualArgument': (MMClass.kind__Composition,Argument,0,'action',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

SubsystemInstance.__subclasses__=[]
SubsystemInstance.__mm__={
		'slot': (MMClass.kind__Composition,AttributeLink,0,'instance',1,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'participatingInstance',0,0),
		'stimulus': (MMClass.kind__Association,Stimulus,0,'argument',0,0),
		'classifier': (MMClass.kind__Association,Classifier,0,'instance',0,0),
		'stimulusSender': (MMClass.kind__Association,Stimulus,0,'sender',1,0),
		'linkEnd': (MMClass.kind__Association,LinkEnd,0,'instance',1,0),
		'componentInstance': (MMClass.kind__Association,ComponentInstance,1,'resident',0,0),
		'ownedLink': (MMClass.kind__Composition,Link,0,'owner',1,0),
		'ownedInstance': (MMClass.kind__Composition,Instance,0,'owner',1,0),
		'owner': (MMClass.kind__Association,Instance,1,'ownedInstance',0,0),
		'stimulusReceiver': (MMClass.kind__Association,Stimulus,0,'receiver',1,0),
		'playedRole': (MMClass.kind__Association,ClassifierRole,0,'conformingInstance',0,0),
		'attributeLink': (MMClass.kind__Association,AttributeLink,0,'value',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

ElementImport.__subclasses__=[]
ElementImport.__mm__={
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'alias': (MMClass.kind__Attribute,Name,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'importedElement': (MMClass.kind__Association,ModelElement,1,'elementImport',0,0),
		'package': (MMClass.kind__Association,Package,1,'elementImport',0,0)
}

Association.__subclasses__=[AssociationClass, AssociationRole]
Association.__mm__={
		'connection': (MMClass.kind__Composition,AssociationEnd,0,'association',1,1),
		'associationRole': (MMClass.kind__Association,AssociationRole,0,'base',1,0),
		'link': (MMClass.kind__Association,Link,0,'association',1,0),
		'isRoot': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isLeaf': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isAbstract': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'specialization': (MMClass.kind__Association,Generalization,0,'parent',1,0),
		'generalization': (MMClass.kind__Association,Generalization,0,'child',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

ClassifierInState.__subclasses__=[]
ClassifierInState.__mm__={
		'inState': (MMClass.kind__Association,State,0,'classifierInState',0,0),
		'type': (MMClass.kind__Association,Classifier,1,'classifierInState',0,0),
		'instance': (MMClass.kind__Association,Instance,0,'classifier',0,0),
		'specifiedEnd': (MMClass.kind__Association,AssociationEnd,0,'specification',0,0),
		'feature': (MMClass.kind__Composition,Feature,0,'owner',1,0),
		'typedFeature': (MMClass.kind__Association,StructuralFeature,0,'type',1,0),
		'powertypeRange': (MMClass.kind__Association,Generalization,0,'powertype',1,0),
		'classifierInState': (MMClass.kind__Association,ClassifierInState,0,'type',1,0),
		'objectFlowState': (MMClass.kind__Association,ObjectFlowState,0,'type',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'base',0,0),
		'typedParameter': (MMClass.kind__Association,Parameter,0,'type',1,0),
		'createAction': (MMClass.kind__Association,CreateAction,0,'instantiation',1,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'representedClassifier',1,0),
		'association': (MMClass.kind__Association,AssociationEnd,0,'participant',1,0),
		'isRoot': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isLeaf': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isAbstract': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'specialization': (MMClass.kind__Association,Generalization,0,'parent',1,0),
		'generalization': (MMClass.kind__Association,Generalization,0,'child',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0),
		'ownedElement': (MMClass.kind__Composition,ModelElement,0,'namespace',1,0)
}

NodeInstance.__subclasses__=[]
NodeInstance.__mm__={
		'resident': (MMClass.kind__Association,ComponentInstance,0,'nodeInstance',1,0),
		'slot': (MMClass.kind__Composition,AttributeLink,0,'instance',1,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'participatingInstance',0,0),
		'stimulus': (MMClass.kind__Association,Stimulus,0,'argument',0,0),
		'classifier': (MMClass.kind__Association,Classifier,0,'instance',0,0),
		'stimulusSender': (MMClass.kind__Association,Stimulus,0,'sender',1,0),
		'linkEnd': (MMClass.kind__Association,LinkEnd,0,'instance',1,0),
		'componentInstance': (MMClass.kind__Association,ComponentInstance,1,'resident',0,0),
		'ownedLink': (MMClass.kind__Composition,Link,0,'owner',1,0),
		'ownedInstance': (MMClass.kind__Composition,Instance,0,'owner',1,0),
		'owner': (MMClass.kind__Association,Instance,1,'ownedInstance',0,0),
		'stimulusReceiver': (MMClass.kind__Association,Stimulus,0,'receiver',1,0),
		'playedRole': (MMClass.kind__Association,ClassifierRole,0,'conformingInstance',0,0),
		'attributeLink': (MMClass.kind__Association,AttributeLink,0,'value',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

Exception.__subclasses__=[]
Exception.__mm__={
		'reception': (MMClass.kind__Association,Reception,0,'signal',1,0),
		'occurrence': (MMClass.kind__Association,SignalEvent,0,'signal',1,0),
		'context': (MMClass.kind__Association,BehavioralFeature,0,'raisedSignal',0,0),
		'sendAction': (MMClass.kind__Association,SendAction,0,'signal',1,0),
		'instance': (MMClass.kind__Association,Instance,0,'classifier',0,0),
		'specifiedEnd': (MMClass.kind__Association,AssociationEnd,0,'specification',0,0),
		'feature': (MMClass.kind__Composition,Feature,0,'owner',1,0),
		'typedFeature': (MMClass.kind__Association,StructuralFeature,0,'type',1,0),
		'powertypeRange': (MMClass.kind__Association,Generalization,0,'powertype',1,0),
		'classifierInState': (MMClass.kind__Association,ClassifierInState,0,'type',1,0),
		'objectFlowState': (MMClass.kind__Association,ObjectFlowState,0,'type',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'base',0,0),
		'typedParameter': (MMClass.kind__Association,Parameter,0,'type',1,0),
		'createAction': (MMClass.kind__Association,CreateAction,0,'instantiation',1,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'representedClassifier',1,0),
		'association': (MMClass.kind__Association,AssociationEnd,0,'participant',1,0),
		'isRoot': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isLeaf': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isAbstract': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'specialization': (MMClass.kind__Association,Generalization,0,'parent',1,0),
		'generalization': (MMClass.kind__Association,Generalization,0,'child',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0),
		'ownedElement': (MMClass.kind__Composition,ModelElement,0,'namespace',1,0)
}

UseCaseInstance.__subclasses__=[]
UseCaseInstance.__mm__={
		'slot': (MMClass.kind__Composition,AttributeLink,0,'instance',1,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'participatingInstance',0,0),
		'stimulus': (MMClass.kind__Association,Stimulus,0,'argument',0,0),
		'classifier': (MMClass.kind__Association,Classifier,0,'instance',0,0),
		'stimulusSender': (MMClass.kind__Association,Stimulus,0,'sender',1,0),
		'linkEnd': (MMClass.kind__Association,LinkEnd,0,'instance',1,0),
		'componentInstance': (MMClass.kind__Association,ComponentInstance,1,'resident',0,0),
		'ownedLink': (MMClass.kind__Composition,Link,0,'owner',1,0),
		'ownedInstance': (MMClass.kind__Composition,Instance,0,'owner',1,0),
		'owner': (MMClass.kind__Association,Instance,1,'ownedInstance',0,0),
		'stimulusReceiver': (MMClass.kind__Association,Stimulus,0,'receiver',1,0),
		'playedRole': (MMClass.kind__Association,ClassifierRole,0,'conformingInstance',0,0),
		'attributeLink': (MMClass.kind__Association,AttributeLink,0,'value',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

MappingExpression.__subclasses__=[]
MappingExpression.__mm__={
		'language': (MMClass.kind__Attribute,Name,1,None,None,0),
		'body': (MMClass.kind__Attribute,String,1,None,None,0)
}

Constraint.__subclasses__=[]
Constraint.__mm__={
		'body': (MMClass.kind__Attribute,BooleanExpression,1,None,None,0),
		'constrainedElement': (MMClass.kind__Association,ModelElement,0,'constraint',0,1),
		'constrainedStereotype': (MMClass.kind__Association,Stereotype,1,'stereotypeConstraint',0,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

ReturnAction.__subclasses__=[]
ReturnAction.__mm__={
		'recurrence': (MMClass.kind__Attribute,IterationExpression,1,None,None,0),
		'target': (MMClass.kind__Attribute,ObjectSetExpression,1,None,None,0),
		'isAsynchronous': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'script': (MMClass.kind__Attribute,ActionExpression,1,None,None,0),
		'stateExit': (MMClass.kind__Association,State,1,'exit',1,0),
		'transition': (MMClass.kind__Association,Transition,1,'effect',1,0),
		'message': (MMClass.kind__Association,Message,0,'action',1,0),
		'stateDoActivity': (MMClass.kind__Association,State,1,'doActivity',1,0),
		'state': (MMClass.kind__Association,State,1,'entry',1,0),
		'actionSequence': (MMClass.kind__Association,ActionSequence,1,'action',0,0),
		'stimulus': (MMClass.kind__Association,Stimulus,0,'dispatchAction',1,0),
		'actualArgument': (MMClass.kind__Composition,Argument,0,'action',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

Transition.__subclasses__=[]
Transition.__mm__={
		'target': (MMClass.kind__Association,StateVertex,1,'incoming',0,0),
		'state': (MMClass.kind__Association,State,1,'internalTransition',0,0),
		'effect': (MMClass.kind__Composition,Action,1,'transition',1,0),
		'trigger': (MMClass.kind__Association,Event,1,'transition',0,0),
		'stateMachine': (MMClass.kind__Association,StateMachine,1,'transitions',0,0),
		'source': (MMClass.kind__Association,StateVertex,1,'outgoing',0,0),
		'guard': (MMClass.kind__Composition,Guard,1,'transition',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

Flow.__subclasses__=[]
Flow.__mm__={
		'source': (MMClass.kind__Association,ModelElement,0,'sourceFlow',0,0),
		'target': (MMClass.kind__Association,ModelElement,0,'targetFlow',0,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

SimpleState.__subclasses__=[ActionState, ObjectFlowState, CallState]
SimpleState.__mm__={
		'internalTransition': (MMClass.kind__Composition,Transition,0,'state',1,0),
		'classifierInState': (MMClass.kind__Association,ClassifierInState,0,'inState',0,0),
		'exit': (MMClass.kind__Composition,Action,1,'stateExit',1,0),
		'doActivity': (MMClass.kind__Composition,Action,1,'stateDoActivity',1,0),
		'entry': (MMClass.kind__Composition,Action,1,'state',1,0),
		'stateMachine': (MMClass.kind__Association,StateMachine,1,'top',1,0),
		'deferrableEvent': (MMClass.kind__Association,Event,0,'state',0,0),
		'incoming': (MMClass.kind__Association,Transition,0,'target',1,0),
		'container': (MMClass.kind__Association,CompositeState,1,'subvertex',0,0),
		'outgoing': (MMClass.kind__Association,Transition,0,'source',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

StructuralFeature.__subclasses__=[Attribute]
StructuralFeature.__mm__={
		'multiplicity': (MMClass.kind__Attribute,Multiplicity,1,None,None,0),
		'changeability': (MMClass.kind__Attribute,ChangeableKind,1,None,None,0),
		'targetScope': (MMClass.kind__Attribute,ScopeKind,1,None,None,0),
		'ordering': (MMClass.kind__Attribute,OrderingKind,1,None,None,0),
		'type': (MMClass.kind__Association,Classifier,1,'typedFeature',0,0),
		'ownerScope': (MMClass.kind__Attribute,ScopeKind,1,None,None,0),
		'owner': (MMClass.kind__Association,Classifier,1,'feature',0,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableFeature',0,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

Dependency.__subclasses__=[Usage, Binding, Abstraction, Permission]
Dependency.__mm__={
		'supplier': (MMClass.kind__Association,ModelElement,0,'supplierDependency',0,0),
		'client': (MMClass.kind__Association,ModelElement,0,'clientDependency',0,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

UseCase.__subclasses__=[]
UseCase.__mm__={
		'include': (MMClass.kind__Association,Include,0,'base',1,0),
		'includer': (MMClass.kind__Association,Include,0,'addition',1,0),
		'extensionPoint': (MMClass.kind__Composition,ExtensionPoint,0,'useCase',1,0),
		'extender': (MMClass.kind__Association,Extend,0,'base',1,0),
		'extend': (MMClass.kind__Association,Extend,0,'extension',1,0),
		'instance': (MMClass.kind__Association,Instance,0,'classifier',0,0),
		'specifiedEnd': (MMClass.kind__Association,AssociationEnd,0,'specification',0,0),
		'feature': (MMClass.kind__Composition,Feature,0,'owner',1,0),
		'typedFeature': (MMClass.kind__Association,StructuralFeature,0,'type',1,0),
		'powertypeRange': (MMClass.kind__Association,Generalization,0,'powertype',1,0),
		'classifierInState': (MMClass.kind__Association,ClassifierInState,0,'type',1,0),
		'objectFlowState': (MMClass.kind__Association,ObjectFlowState,0,'type',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'base',0,0),
		'typedParameter': (MMClass.kind__Association,Parameter,0,'type',1,0),
		'createAction': (MMClass.kind__Association,CreateAction,0,'instantiation',1,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'representedClassifier',1,0),
		'association': (MMClass.kind__Association,AssociationEnd,0,'participant',1,0),
		'isRoot': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isLeaf': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isAbstract': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'specialization': (MMClass.kind__Association,Generalization,0,'parent',1,0),
		'generalization': (MMClass.kind__Association,Generalization,0,'child',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0),
		'ownedElement': (MMClass.kind__Composition,ModelElement,0,'namespace',1,0)
}

Actor.__subclasses__=[]
Actor.__mm__={
		'instance': (MMClass.kind__Association,Instance,0,'classifier',0,0),
		'specifiedEnd': (MMClass.kind__Association,AssociationEnd,0,'specification',0,0),
		'feature': (MMClass.kind__Composition,Feature,0,'owner',1,0),
		'typedFeature': (MMClass.kind__Association,StructuralFeature,0,'type',1,0),
		'powertypeRange': (MMClass.kind__Association,Generalization,0,'powertype',1,0),
		'classifierInState': (MMClass.kind__Association,ClassifierInState,0,'type',1,0),
		'objectFlowState': (MMClass.kind__Association,ObjectFlowState,0,'type',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'base',0,0),
		'typedParameter': (MMClass.kind__Association,Parameter,0,'type',1,0),
		'createAction': (MMClass.kind__Association,CreateAction,0,'instantiation',1,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'representedClassifier',1,0),
		'association': (MMClass.kind__Association,AssociationEnd,0,'participant',1,0),
		'isRoot': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isLeaf': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isAbstract': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'specialization': (MMClass.kind__Association,Generalization,0,'parent',1,0),
		'generalization': (MMClass.kind__Association,Generalization,0,'child',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0),
		'ownedElement': (MMClass.kind__Composition,ModelElement,0,'namespace',1,0)
}

Action.__subclasses__=[CallAction, TerminateAction, ReturnAction, DestroyAction, ActionSequence, SendAction, UninterpretedAction, CreateAction]
Action.__mm__={
		'recurrence': (MMClass.kind__Attribute,IterationExpression,1,None,None,0),
		'target': (MMClass.kind__Attribute,ObjectSetExpression,1,None,None,0),
		'isAsynchronous': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'script': (MMClass.kind__Attribute,ActionExpression,1,None,None,0),
		'stateExit': (MMClass.kind__Association,State,1,'exit',1,0),
		'transition': (MMClass.kind__Association,Transition,1,'effect',1,0),
		'message': (MMClass.kind__Association,Message,0,'action',1,0),
		'stateDoActivity': (MMClass.kind__Association,State,1,'doActivity',1,0),
		'state': (MMClass.kind__Association,State,1,'entry',1,0),
		'actionSequence': (MMClass.kind__Association,ActionSequence,1,'action',0,0),
		'stimulus': (MMClass.kind__Association,Stimulus,0,'dispatchAction',1,0),
		'actualArgument': (MMClass.kind__Composition,Argument,0,'action',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

AssociationClass.__subclasses__=[]
AssociationClass.__mm__={
		'connection': (MMClass.kind__Composition,AssociationEnd,0,'association',1,0),
		'associationRole': (MMClass.kind__Association,AssociationRole,0,'base',1,0),
		'link': (MMClass.kind__Association,Link,0,'association',1,0),
		'isRoot': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isLeaf': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isAbstract': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'specialization': (MMClass.kind__Association,Generalization,0,'parent',1,0),
		'generalization': (MMClass.kind__Association,Generalization,0,'child',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0),
		'isActive': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'instance': (MMClass.kind__Association,Instance,0,'classifier',0,0),
		'specifiedEnd': (MMClass.kind__Association,AssociationEnd,0,'specification',0,0),
		'feature': (MMClass.kind__Composition,Feature,0,'owner',1,0),
		'typedFeature': (MMClass.kind__Association,StructuralFeature,0,'type',1,0),
		'powertypeRange': (MMClass.kind__Association,Generalization,0,'powertype',1,0),
		'classifierInState': (MMClass.kind__Association,ClassifierInState,0,'type',1,0),
		'objectFlowState': (MMClass.kind__Association,ObjectFlowState,0,'type',1,0),
		'typedParameter': (MMClass.kind__Association,Parameter,0,'type',1,0),
		'createAction': (MMClass.kind__Association,CreateAction,0,'instantiation',1,0),
		'association': (MMClass.kind__Association,AssociationEnd,0,'participant',1,0),
		'ownedElement': (MMClass.kind__Composition,ModelElement,0,'namespace',1,0)
}

Expression.__subclasses__=[TimeExpression, MappingExpression, ProcedureExpression, BooleanExpression, ObjectSetExpression, ArgListsExpression, TypeExpression, IterationExpression, ActionExpression]
Expression.__mm__={
		'language': (MMClass.kind__Attribute,Name,1,None,None,0),
		'body': (MMClass.kind__Attribute,String,1,None,None,0)
}

AttributeLink.__subclasses__=[]
AttributeLink.__mm__={
		'instance': (MMClass.kind__Association,Instance,1,'slot',0,0),
		'attribute': (MMClass.kind__Association,Attribute,1,'attributeLink',0,0),
		'linkEnd': (MMClass.kind__Association,LinkEnd,1,'qualifiedValue',0,0),
		'value': (MMClass.kind__Association,Instance,1,'attributeLink',0,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

SignalEvent.__subclasses__=[]
SignalEvent.__mm__={
		'signal': (MMClass.kind__Association,Signal,1,'occurrence',0,0),
		'transition': (MMClass.kind__Association,Transition,0,'trigger',1,0),
		'parameter': (MMClass.kind__Composition,Parameter,0,'event',1,0),
		'state': (MMClass.kind__Association,State,0,'deferrableEvent',0,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

EnumerationLiteral.__subclasses__=[]
EnumerationLiteral.__mm__={
		'enumeration': (MMClass.kind__Association,Enumeration,1,'literal',0,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

CallEvent.__subclasses__=[]
CallEvent.__mm__={
		'operation': (MMClass.kind__Association,Operation,1,'occurrence',0,0),
		'transition': (MMClass.kind__Association,Transition,0,'trigger',1,0),
		'parameter': (MMClass.kind__Composition,Parameter,0,'event',1,0),
		'state': (MMClass.kind__Association,State,0,'deferrableEvent',0,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

DestroyAction.__subclasses__=[]
DestroyAction.__mm__={
		'recurrence': (MMClass.kind__Attribute,IterationExpression,1,None,None,0),
		'target': (MMClass.kind__Attribute,ObjectSetExpression,1,None,None,0),
		'isAsynchronous': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'script': (MMClass.kind__Attribute,ActionExpression,1,None,None,0),
		'stateExit': (MMClass.kind__Association,State,1,'exit',1,0),
		'transition': (MMClass.kind__Association,Transition,1,'effect',1,0),
		'message': (MMClass.kind__Association,Message,0,'action',1,0),
		'stateDoActivity': (MMClass.kind__Association,State,1,'doActivity',1,0),
		'state': (MMClass.kind__Association,State,1,'entry',1,0),
		'actionSequence': (MMClass.kind__Association,ActionSequence,1,'action',0,0),
		'stimulus': (MMClass.kind__Association,Stimulus,0,'dispatchAction',1,0),
		'actualArgument': (MMClass.kind__Composition,Argument,0,'action',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

GeneralizableElement.__subclasses__=[Association, Package, Classifier, Stereotype, Collaboration, AssociationClass, AssociationRole, Subsystem, Model, Node, ClassifierInState, UseCase, Actor, Class, DataType, Component, Artifact, ClassifierRole, Interface, Signal, Enumeration, ProgrammingLanguageDataType, Primitive, Exception]
GeneralizableElement.__mm__={
		'isRoot': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isLeaf': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isAbstract': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'specialization': (MMClass.kind__Association,Generalization,0,'parent',1,0),
		'generalization': (MMClass.kind__Association,Generalization,0,'child',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

Attribute.__subclasses__=[]
Attribute.__mm__={
		'initialValue': (MMClass.kind__Attribute,Expression,1,None,None,0),
		'attributeLink': (MMClass.kind__Association,AttributeLink,0,'attribute',1,0),
		'associationEndRole': (MMClass.kind__Association,AssociationEndRole,0,'availableQualifier',0,0),
		'associationEnd': (MMClass.kind__Association,AssociationEnd,1,'qualifier',0,0),
		'multiplicity': (MMClass.kind__Attribute,Multiplicity,1,None,None,0),
		'changeability': (MMClass.kind__Attribute,ChangeableKind,1,None,None,0),
		'targetScope': (MMClass.kind__Attribute,ScopeKind,1,None,None,0),
		'ordering': (MMClass.kind__Attribute,OrderingKind,1,None,None,0),
		'type': (MMClass.kind__Association,Classifier,1,'typedFeature',0,0),
		'ownerScope': (MMClass.kind__Attribute,ScopeKind,1,None,None,0),
		'owner': (MMClass.kind__Association,Classifier,1,'feature',0,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableFeature',0,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

ProcedureExpression.__subclasses__=[]
ProcedureExpression.__mm__={
		'language': (MMClass.kind__Attribute,Name,1,None,None,0),
		'body': (MMClass.kind__Attribute,String,1,None,None,0)
}

BooleanExpression.__subclasses__=[]
BooleanExpression.__mm__={
		'language': (MMClass.kind__Attribute,Name,1,None,None,0),
		'body': (MMClass.kind__Attribute,String,1,None,None,0)
}

Binding.__subclasses__=[]
Binding.__mm__={
		'argument': (MMClass.kind__Composition,TemplateArgument,0,'binding',1,1),
		'supplier': (MMClass.kind__Association,ModelElement,0,'supplierDependency',0,0),
		'client': (MMClass.kind__Association,ModelElement,0,'clientDependency',0,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

StubState.__subclasses__=[]
StubState.__mm__={
		'referenceState': (MMClass.kind__Attribute,Name,1,None,None,0),
		'incoming': (MMClass.kind__Association,Transition,0,'target',1,0),
		'container': (MMClass.kind__Association,CompositeState,1,'subvertex',0,0),
		'outgoing': (MMClass.kind__Association,Transition,0,'source',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

AssociationEndRole.__subclasses__=[]
AssociationEndRole.__mm__={
		'collaborationMultiplicity': (MMClass.kind__Attribute,Multiplicity,1,None,None,0),
		'base': (MMClass.kind__Association,AssociationEnd,1,'associationEndRole',0,0),
		'availableQualifier': (MMClass.kind__Association,Attribute,0,'associationEndRole',0,0),
		'isNavigable': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'ordering': (MMClass.kind__Attribute,OrderingKind,1,None,None,0),
		'aggregation': (MMClass.kind__Attribute,AggregationKind,1,None,None,0),
		'targetScope': (MMClass.kind__Attribute,ScopeKind,1,None,None,0),
		'multiplicity': (MMClass.kind__Attribute,Multiplicity,1,None,None,0),
		'changeability': (MMClass.kind__Attribute,ChangeableKind,1,None,None,0),
		'associationEndRole': (MMClass.kind__Association,AssociationEndRole,0,'base',1,0),
		'association': (MMClass.kind__Association,Association,1,'connection',0,0),
		'specification': (MMClass.kind__Association,Classifier,0,'specifiedEnd',0,0),
		'qualifier': (MMClass.kind__Composition,Attribute,0,'associationEnd',1,0),
		'linkEnd': (MMClass.kind__Association,LinkEnd,0,'associationEnd',1,0),
		'participant': (MMClass.kind__Association,Classifier,1,'association',0,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

Class.__subclasses__=[AssociationClass]
Class.__mm__={
		'isActive': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'instance': (MMClass.kind__Association,Instance,0,'classifier',0,0),
		'specifiedEnd': (MMClass.kind__Association,AssociationEnd,0,'specification',0,0),
		'feature': (MMClass.kind__Composition,Feature,0,'owner',1,0),
		'typedFeature': (MMClass.kind__Association,StructuralFeature,0,'type',1,0),
		'powertypeRange': (MMClass.kind__Association,Generalization,0,'powertype',1,0),
		'classifierInState': (MMClass.kind__Association,ClassifierInState,0,'type',1,0),
		'objectFlowState': (MMClass.kind__Association,ObjectFlowState,0,'type',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'base',0,0),
		'typedParameter': (MMClass.kind__Association,Parameter,0,'type',1,0),
		'createAction': (MMClass.kind__Association,CreateAction,0,'instantiation',1,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'representedClassifier',1,0),
		'association': (MMClass.kind__Association,AssociationEnd,0,'participant',1,0),
		'isRoot': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isLeaf': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isAbstract': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'specialization': (MMClass.kind__Association,Generalization,0,'parent',1,0),
		'generalization': (MMClass.kind__Association,Generalization,0,'child',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0),
		'ownedElement': (MMClass.kind__Composition,ModelElement,0,'namespace',1,0)
}

DataType.__subclasses__=[Enumeration, ProgrammingLanguageDataType, Primitive]
DataType.__mm__={
		'instance': (MMClass.kind__Association,Instance,0,'classifier',0,0),
		'specifiedEnd': (MMClass.kind__Association,AssociationEnd,0,'specification',0,0),
		'feature': (MMClass.kind__Composition,Feature,0,'owner',1,0),
		'typedFeature': (MMClass.kind__Association,StructuralFeature,0,'type',1,0),
		'powertypeRange': (MMClass.kind__Association,Generalization,0,'powertype',1,0),
		'classifierInState': (MMClass.kind__Association,ClassifierInState,0,'type',1,0),
		'objectFlowState': (MMClass.kind__Association,ObjectFlowState,0,'type',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'base',0,0),
		'typedParameter': (MMClass.kind__Association,Parameter,0,'type',1,0),
		'createAction': (MMClass.kind__Association,CreateAction,0,'instantiation',1,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'representedClassifier',1,0),
		'association': (MMClass.kind__Association,AssociationEnd,0,'participant',1,0),
		'isRoot': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isLeaf': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isAbstract': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'specialization': (MMClass.kind__Association,Generalization,0,'parent',1,0),
		'generalization': (MMClass.kind__Association,Generalization,0,'child',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0),
		'ownedElement': (MMClass.kind__Composition,ModelElement,0,'namespace',1,0)
}

ObjectSetExpression.__subclasses__=[]
ObjectSetExpression.__mm__={
		'language': (MMClass.kind__Attribute,Name,1,None,None,0),
		'body': (MMClass.kind__Attribute,String,1,None,None,0)
}

SynchState.__subclasses__=[]
SynchState.__mm__={
		'bound': (MMClass.kind__Attribute,UnlimitedInteger,1,None,None,0),
		'incoming': (MMClass.kind__Association,Transition,0,'target',1,0),
		'container': (MMClass.kind__Association,CompositeState,1,'subvertex',0,0),
		'outgoing': (MMClass.kind__Association,Transition,0,'source',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

FinalState.__subclasses__=[]
FinalState.__mm__={
		'internalTransition': (MMClass.kind__Composition,Transition,0,'state',1,0),
		'classifierInState': (MMClass.kind__Association,ClassifierInState,0,'inState',0,0),
		'exit': (MMClass.kind__Composition,Action,1,'stateExit',1,0),
		'doActivity': (MMClass.kind__Composition,Action,1,'stateDoActivity',1,0),
		'entry': (MMClass.kind__Composition,Action,1,'state',1,0),
		'stateMachine': (MMClass.kind__Association,StateMachine,1,'top',1,0),
		'deferrableEvent': (MMClass.kind__Association,Event,0,'state',0,0),
		'incoming': (MMClass.kind__Association,Transition,0,'target',1,0),
		'container': (MMClass.kind__Association,CompositeState,1,'subvertex',0,0),
		'outgoing': (MMClass.kind__Association,Transition,0,'source',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

LinkObject.__subclasses__=[]
LinkObject.__mm__={
		'slot': (MMClass.kind__Composition,AttributeLink,0,'instance',1,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'participatingInstance',0,0),
		'stimulus': (MMClass.kind__Association,Stimulus,0,'argument',0,0),
		'classifier': (MMClass.kind__Association,Classifier,0,'instance',0,0),
		'stimulusSender': (MMClass.kind__Association,Stimulus,0,'sender',1,0),
		'linkEnd': (MMClass.kind__Association,LinkEnd,0,'instance',1,0),
		'componentInstance': (MMClass.kind__Association,ComponentInstance,1,'resident',0,0),
		'ownedLink': (MMClass.kind__Composition,Link,0,'owner',1,0),
		'ownedInstance': (MMClass.kind__Composition,Instance,0,'owner',1,0),
		'owner': (MMClass.kind__Association,Instance,1,'ownedInstance',0,0),
		'stimulusReceiver': (MMClass.kind__Association,Stimulus,0,'receiver',1,0),
		'playedRole': (MMClass.kind__Association,ClassifierRole,0,'conformingInstance',0,0),
		'attributeLink': (MMClass.kind__Association,AttributeLink,0,'value',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0),
		'connection': (MMClass.kind__Composition,LinkEnd,0,'link',1,0),
		'association': (MMClass.kind__Association,Association,1,'link',0,0)
}

Operation.__subclasses__=[]
Operation.__mm__={
		'concurrency': (MMClass.kind__Attribute,CallConcurrencyKind,1,None,None,0),
		'isRoot': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isLeaf': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isAbstract': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'specification': (MMClass.kind__Attribute,String,1,None,None,0),
		'callAction': (MMClass.kind__Association,CallAction,0,'operation',1,0),
		'method': (MMClass.kind__Association,Method,0,'specification',1,0),
		'occurrence': (MMClass.kind__Association,CallEvent,0,'operation',1,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'representedOperation',1,0),
		'isQuery': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'raisedSignal': (MMClass.kind__Association,Signal,0,'context',0,0),
		'parameter': (MMClass.kind__Composition,Parameter,0,'behavioralFeature',1,0),
		'ownerScope': (MMClass.kind__Attribute,ScopeKind,1,None,None,0),
		'owner': (MMClass.kind__Association,Classifier,1,'feature',0,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableFeature',0,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

ArgListsExpression.__subclasses__=[]
ArgListsExpression.__mm__={
		'language': (MMClass.kind__Attribute,Name,1,None,None,0),
		'body': (MMClass.kind__Attribute,String,1,None,None,0)
}

Event.__subclasses__=[ChangeEvent, TimeEvent, SignalEvent, CallEvent]
Event.__mm__={
		'transition': (MMClass.kind__Association,Transition,0,'trigger',1,0),
		'parameter': (MMClass.kind__Composition,Parameter,0,'event',1,0),
		'state': (MMClass.kind__Association,State,0,'deferrableEvent',0,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

ActionState.__subclasses__=[CallState]
ActionState.__mm__={
		'isDynamic': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'dynamicArguments': (MMClass.kind__Attribute,ArgListsExpression,1,None,None,0),
		'dynamicMultiplicity': (MMClass.kind__Attribute,Multiplicity,1,None,None,0),
		'internalTransition': (MMClass.kind__Composition,Transition,0,'state',1,0),
		'classifierInState': (MMClass.kind__Association,ClassifierInState,0,'inState',0,0),
		'exit': (MMClass.kind__Composition,Action,1,'stateExit',1,0),
		'doActivity': (MMClass.kind__Composition,Action,1,'stateDoActivity',1,0),
		'entry': (MMClass.kind__Composition,Action,1,'state',1,0),
		'stateMachine': (MMClass.kind__Association,StateMachine,1,'top',1,0),
		'deferrableEvent': (MMClass.kind__Association,Event,0,'state',0,0),
		'incoming': (MMClass.kind__Association,Transition,0,'target',1,0),
		'container': (MMClass.kind__Association,CompositeState,1,'subvertex',0,0),
		'outgoing': (MMClass.kind__Association,Transition,0,'source',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

StateVertex.__subclasses__=[StubState, SynchState, State, Pseudostate, CompositeState, SimpleState, FinalState, SubmachineState, SubactivityState, ActionState, ObjectFlowState, CallState]
StateVertex.__mm__={
		'incoming': (MMClass.kind__Association,Transition,0,'target',1,0),
		'container': (MMClass.kind__Association,CompositeState,1,'subvertex',0,0),
		'outgoing': (MMClass.kind__Association,Transition,0,'source',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

ElementResidence.__subclasses__=[]
ElementResidence.__mm__={
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'container': (MMClass.kind__Association,Component,1,'residentElement',0,0),
		'resident': (MMClass.kind__Association,ModelElement,1,'elementResidence',0,0)
}

Namespace.__subclasses__=[Package, Classifier, Collaboration, Subsystem, Model, Node, ClassifierInState, UseCase, Actor, Class, DataType, Component, Artifact, ClassifierRole, Interface, Signal, AssociationClass, Enumeration, ProgrammingLanguageDataType, Primitive, Exception]
Namespace.__mm__={
		'ownedElement': (MMClass.kind__Composition,ModelElement,0,'namespace',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

Feature.__subclasses__=[StructuralFeature, BehavioralFeature, Attribute, Method, Operation, Reception]
Feature.__mm__={
		'ownerScope': (MMClass.kind__Attribute,ScopeKind,1,None,None,0),
		'owner': (MMClass.kind__Association,Classifier,1,'feature',0,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableFeature',0,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

TemplateParameter.__subclasses__=[]
TemplateParameter.__mm__={
		'template': (MMClass.kind__Association,ModelElement,1,'templateParameter',0,0),
		'parameter': (MMClass.kind__Composition,ModelElement,1,'parameterTemplate',1,0),
		'defaultElement': (MMClass.kind__Association,ModelElement,1,'defaultedParameter',0,0)
}

ActionSequence.__subclasses__=[]
ActionSequence.__mm__={
		'action': (MMClass.kind__Composition,Action,0,'actionSequence',1,1),
		'recurrence': (MMClass.kind__Attribute,IterationExpression,1,None,None,0),
		'target': (MMClass.kind__Attribute,ObjectSetExpression,1,None,None,0),
		'isAsynchronous': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'script': (MMClass.kind__Attribute,ActionExpression,1,None,None,0),
		'stateExit': (MMClass.kind__Association,State,1,'exit',1,0),
		'transition': (MMClass.kind__Association,Transition,1,'effect',1,0),
		'message': (MMClass.kind__Association,Message,0,'action',1,0),
		'stateDoActivity': (MMClass.kind__Association,State,1,'doActivity',1,0),
		'state': (MMClass.kind__Association,State,1,'entry',1,0),
		'actionSequence': (MMClass.kind__Association,ActionSequence,1,'action',0,0),
		'stimulus': (MMClass.kind__Association,Stimulus,0,'dispatchAction',1,0),
		'actualArgument': (MMClass.kind__Composition,Argument,0,'action',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

State.__subclasses__=[CompositeState, SimpleState, FinalState, SubmachineState, SubactivityState, ActionState, ObjectFlowState, CallState]
State.__mm__={
		'internalTransition': (MMClass.kind__Composition,Transition,0,'state',1,0),
		'classifierInState': (MMClass.kind__Association,ClassifierInState,0,'inState',0,0),
		'exit': (MMClass.kind__Composition,Action,1,'stateExit',1,0),
		'doActivity': (MMClass.kind__Composition,Action,1,'stateDoActivity',1,0),
		'entry': (MMClass.kind__Composition,Action,1,'state',1,0),
		'stateMachine': (MMClass.kind__Association,StateMachine,1,'top',1,0),
		'deferrableEvent': (MMClass.kind__Association,Event,0,'state',0,0),
		'incoming': (MMClass.kind__Association,Transition,0,'target',1,0),
		'container': (MMClass.kind__Association,CompositeState,1,'subvertex',0,0),
		'outgoing': (MMClass.kind__Association,Transition,0,'source',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

ObjectFlowState.__subclasses__=[]
ObjectFlowState.__mm__={
		'isSynch': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'parameter': (MMClass.kind__Association,Parameter,0,'state',0,0),
		'type': (MMClass.kind__Association,Classifier,1,'objectFlowState',0,0),
		'internalTransition': (MMClass.kind__Composition,Transition,0,'state',1,0),
		'classifierInState': (MMClass.kind__Association,ClassifierInState,0,'inState',0,0),
		'exit': (MMClass.kind__Composition,Action,1,'stateExit',1,0),
		'doActivity': (MMClass.kind__Composition,Action,1,'stateDoActivity',1,0),
		'entry': (MMClass.kind__Composition,Action,1,'state',1,0),
		'stateMachine': (MMClass.kind__Association,StateMachine,1,'top',1,0),
		'deferrableEvent': (MMClass.kind__Association,Event,0,'state',0,0),
		'incoming': (MMClass.kind__Association,Transition,0,'target',1,0),
		'container': (MMClass.kind__Association,CompositeState,1,'subvertex',0,0),
		'outgoing': (MMClass.kind__Association,Transition,0,'source',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

SendAction.__subclasses__=[]
SendAction.__mm__={
		'signal': (MMClass.kind__Association,Signal,1,'sendAction',0,0),
		'recurrence': (MMClass.kind__Attribute,IterationExpression,1,None,None,0),
		'target': (MMClass.kind__Attribute,ObjectSetExpression,1,None,None,0),
		'isAsynchronous': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'script': (MMClass.kind__Attribute,ActionExpression,1,None,None,0),
		'stateExit': (MMClass.kind__Association,State,1,'exit',1,0),
		'transition': (MMClass.kind__Association,Transition,1,'effect',1,0),
		'message': (MMClass.kind__Association,Message,0,'action',1,0),
		'stateDoActivity': (MMClass.kind__Association,State,1,'doActivity',1,0),
		'state': (MMClass.kind__Association,State,1,'entry',1,0),
		'actionSequence': (MMClass.kind__Association,ActionSequence,1,'action',0,0),
		'stimulus': (MMClass.kind__Association,Stimulus,0,'dispatchAction',1,0),
		'actualArgument': (MMClass.kind__Composition,Argument,0,'action',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

Parameter.__subclasses__=[]
Parameter.__mm__={
		'defaultValue': (MMClass.kind__Attribute,Expression,1,None,None,0),
		'kind': (MMClass.kind__Attribute,ParameterDirectionKind,1,None,None,0),
		'state': (MMClass.kind__Association,ObjectFlowState,0,'parameter',0,0),
		'behavioralFeature': (MMClass.kind__Association,BehavioralFeature,1,'parameter',0,0),
		'event': (MMClass.kind__Association,Event,1,'parameter',0,0),
		'type': (MMClass.kind__Association,Classifier,1,'typedParameter',0,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

ExtensionPoint.__subclasses__=[]
ExtensionPoint.__mm__={
		'location': (MMClass.kind__Attribute,LocationReference,1,None,None,0),
		'extend': (MMClass.kind__Association,Extend,0,'extensionPoint',0,0),
		'useCase': (MMClass.kind__Association,UseCase,1,'extensionPoint',0,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

CollaborationInstanceSet.__subclasses__=[]
CollaborationInstanceSet.__mm__={
		'participatingInstance': (MMClass.kind__Association,Instance,0,'collaborationInstanceSet',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,1,'collaborationInstanceSet',0,0),
		'interactionInstanceSet': (MMClass.kind__Composition,InteractionInstanceSet,0,'context',1,0),
		'constrainingElement': (MMClass.kind__Association,ModelElement,0,'collaborationInstanceSet',0,0),
		'participatingLink': (MMClass.kind__Association,Link,0,'collaborationInstanceSet',0,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

Enumeration.__subclasses__=[]
Enumeration.__mm__={
		'literal': (MMClass.kind__Composition,EnumerationLiteral,0,'enumeration',1,1),
		'instance': (MMClass.kind__Association,Instance,0,'classifier',0,0),
		'specifiedEnd': (MMClass.kind__Association,AssociationEnd,0,'specification',0,0),
		'feature': (MMClass.kind__Composition,Feature,0,'owner',1,0),
		'typedFeature': (MMClass.kind__Association,StructuralFeature,0,'type',1,0),
		'powertypeRange': (MMClass.kind__Association,Generalization,0,'powertype',1,0),
		'classifierInState': (MMClass.kind__Association,ClassifierInState,0,'type',1,0),
		'objectFlowState': (MMClass.kind__Association,ObjectFlowState,0,'type',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'base',0,0),
		'typedParameter': (MMClass.kind__Association,Parameter,0,'type',1,0),
		'createAction': (MMClass.kind__Association,CreateAction,0,'instantiation',1,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'representedClassifier',1,0),
		'association': (MMClass.kind__Association,AssociationEnd,0,'participant',1,0),
		'isRoot': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isLeaf': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isAbstract': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'specialization': (MMClass.kind__Association,Generalization,0,'parent',1,0),
		'generalization': (MMClass.kind__Association,Generalization,0,'child',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0),
		'ownedElement': (MMClass.kind__Composition,ModelElement,0,'namespace',1,0)
}

ProgrammingLanguageDataType.__subclasses__=[]
ProgrammingLanguageDataType.__mm__={
		'expression': (MMClass.kind__Attribute,TypeExpression,1,None,None,0),
		'instance': (MMClass.kind__Association,Instance,0,'classifier',0,0),
		'specifiedEnd': (MMClass.kind__Association,AssociationEnd,0,'specification',0,0),
		'feature': (MMClass.kind__Composition,Feature,0,'owner',1,0),
		'typedFeature': (MMClass.kind__Association,StructuralFeature,0,'type',1,0),
		'powertypeRange': (MMClass.kind__Association,Generalization,0,'powertype',1,0),
		'classifierInState': (MMClass.kind__Association,ClassifierInState,0,'type',1,0),
		'objectFlowState': (MMClass.kind__Association,ObjectFlowState,0,'type',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'base',0,0),
		'typedParameter': (MMClass.kind__Association,Parameter,0,'type',1,0),
		'createAction': (MMClass.kind__Association,CreateAction,0,'instantiation',1,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'representedClassifier',1,0),
		'association': (MMClass.kind__Association,AssociationEnd,0,'participant',1,0),
		'isRoot': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isLeaf': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isAbstract': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'specialization': (MMClass.kind__Association,Generalization,0,'parent',1,0),
		'generalization': (MMClass.kind__Association,Generalization,0,'child',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0),
		'ownedElement': (MMClass.kind__Composition,ModelElement,0,'namespace',1,0)
}

Abstraction.__subclasses__=[]
Abstraction.__mm__={
		'mapping': (MMClass.kind__Attribute,MappingExpression,1,None,None,0),
		'supplier': (MMClass.kind__Association,ModelElement,0,'supplierDependency',0,0),
		'client': (MMClass.kind__Association,ModelElement,0,'clientDependency',0,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

Relationship.__subclasses__=[Include, Extend, Association, Flow, Dependency, Generalization, AssociationClass, AssociationRole, Usage, Binding, Abstraction, Permission]
Relationship.__mm__={
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

Permission.__subclasses__=[]
Permission.__mm__={
		'supplier': (MMClass.kind__Association,ModelElement,0,'supplierDependency',0,0),
		'client': (MMClass.kind__Association,ModelElement,0,'clientDependency',0,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

DataValue.__subclasses__=[]
DataValue.__mm__={
		'slot': (MMClass.kind__Composition,AttributeLink,0,'instance',1,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'participatingInstance',0,0),
		'stimulus': (MMClass.kind__Association,Stimulus,0,'argument',0,0),
		'classifier': (MMClass.kind__Association,Classifier,0,'instance',0,0),
		'stimulusSender': (MMClass.kind__Association,Stimulus,0,'sender',1,0),
		'linkEnd': (MMClass.kind__Association,LinkEnd,0,'instance',1,0),
		'componentInstance': (MMClass.kind__Association,ComponentInstance,1,'resident',0,0),
		'ownedLink': (MMClass.kind__Composition,Link,0,'owner',1,0),
		'ownedInstance': (MMClass.kind__Composition,Instance,0,'owner',1,0),
		'owner': (MMClass.kind__Association,Instance,1,'ownedInstance',0,0),
		'stimulusReceiver': (MMClass.kind__Association,Stimulus,0,'receiver',1,0),
		'playedRole': (MMClass.kind__Association,ClassifierRole,0,'conformingInstance',0,0),
		'attributeLink': (MMClass.kind__Association,AttributeLink,0,'value',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

Component.__subclasses__=[]
Component.__mm__={
		'residentElement': (MMClass.kind__Composition,ElementResidence,0,'container',1,0),
		'deploymentLocation': (MMClass.kind__Association,Node,0,'deployedComponent',0,0),
		'implementation': (MMClass.kind__Association,Artifact,0,'implementationLocation',0,0),
		'instance': (MMClass.kind__Association,Instance,0,'classifier',0,0),
		'specifiedEnd': (MMClass.kind__Association,AssociationEnd,0,'specification',0,0),
		'feature': (MMClass.kind__Composition,Feature,0,'owner',1,0),
		'typedFeature': (MMClass.kind__Association,StructuralFeature,0,'type',1,0),
		'powertypeRange': (MMClass.kind__Association,Generalization,0,'powertype',1,0),
		'classifierInState': (MMClass.kind__Association,ClassifierInState,0,'type',1,0),
		'objectFlowState': (MMClass.kind__Association,ObjectFlowState,0,'type',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'base',0,0),
		'typedParameter': (MMClass.kind__Association,Parameter,0,'type',1,0),
		'createAction': (MMClass.kind__Association,CreateAction,0,'instantiation',1,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'representedClassifier',1,0),
		'association': (MMClass.kind__Association,AssociationEnd,0,'participant',1,0),
		'isRoot': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isLeaf': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isAbstract': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'specialization': (MMClass.kind__Association,Generalization,0,'parent',1,0),
		'generalization': (MMClass.kind__Association,Generalization,0,'child',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0),
		'ownedElement': (MMClass.kind__Composition,ModelElement,0,'namespace',1,0)
}

Artifact.__subclasses__=[]
Artifact.__mm__={
		'implementationLocation': (MMClass.kind__Association,Component,0,'implementation',0,0),
		'instance': (MMClass.kind__Association,Instance,0,'classifier',0,0),
		'specifiedEnd': (MMClass.kind__Association,AssociationEnd,0,'specification',0,0),
		'feature': (MMClass.kind__Composition,Feature,0,'owner',1,0),
		'typedFeature': (MMClass.kind__Association,StructuralFeature,0,'type',1,0),
		'powertypeRange': (MMClass.kind__Association,Generalization,0,'powertype',1,0),
		'classifierInState': (MMClass.kind__Association,ClassifierInState,0,'type',1,0),
		'objectFlowState': (MMClass.kind__Association,ObjectFlowState,0,'type',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'base',0,0),
		'typedParameter': (MMClass.kind__Association,Parameter,0,'type',1,0),
		'createAction': (MMClass.kind__Association,CreateAction,0,'instantiation',1,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'representedClassifier',1,0),
		'association': (MMClass.kind__Association,AssociationEnd,0,'participant',1,0),
		'isRoot': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isLeaf': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isAbstract': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'specialization': (MMClass.kind__Association,Generalization,0,'parent',1,0),
		'generalization': (MMClass.kind__Association,Generalization,0,'child',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0),
		'ownedElement': (MMClass.kind__Composition,ModelElement,0,'namespace',1,0)
}

ClassifierRole.__subclasses__=[]
ClassifierRole.__mm__={
		'multiplicity': (MMClass.kind__Attribute,Multiplicity,1,None,None,0),
		'messageReceiver': (MMClass.kind__Association,Message,0,'receiver',1,0),
		'availableContents': (MMClass.kind__Association,ModelElement,0,'classifierRole',0,0),
		'message': (MMClass.kind__Association,Message,0,'sender',1,0),
		'conformingInstance': (MMClass.kind__Association,Instance,0,'playedRole',0,0),
		'base': (MMClass.kind__Association,Classifier,0,'classifierRole',0,0),
		'availableFeature': (MMClass.kind__Association,Feature,0,'classifierRole',0,0),
		'instance': (MMClass.kind__Association,Instance,0,'classifier',0,0),
		'specifiedEnd': (MMClass.kind__Association,AssociationEnd,0,'specification',0,0),
		'feature': (MMClass.kind__Composition,Feature,0,'owner',1,0),
		'typedFeature': (MMClass.kind__Association,StructuralFeature,0,'type',1,0),
		'powertypeRange': (MMClass.kind__Association,Generalization,0,'powertype',1,0),
		'classifierInState': (MMClass.kind__Association,ClassifierInState,0,'type',1,0),
		'objectFlowState': (MMClass.kind__Association,ObjectFlowState,0,'type',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'base',0,0),
		'typedParameter': (MMClass.kind__Association,Parameter,0,'type',1,0),
		'createAction': (MMClass.kind__Association,CreateAction,0,'instantiation',1,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'representedClassifier',1,0),
		'association': (MMClass.kind__Association,AssociationEnd,0,'participant',1,0),
		'isRoot': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isLeaf': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isAbstract': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'specialization': (MMClass.kind__Association,Generalization,0,'parent',1,0),
		'generalization': (MMClass.kind__Association,Generalization,0,'child',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0),
		'ownedElement': (MMClass.kind__Composition,ModelElement,0,'namespace',1,0)
}

BehavioralFeature.__subclasses__=[Method, Operation, Reception]
BehavioralFeature.__mm__={
		'isQuery': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'raisedSignal': (MMClass.kind__Association,Signal,0,'context',0,0),
		'parameter': (MMClass.kind__Composition,Parameter,0,'behavioralFeature',1,0),
		'ownerScope': (MMClass.kind__Attribute,ScopeKind,1,None,None,0),
		'owner': (MMClass.kind__Association,Classifier,1,'feature',0,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableFeature',0,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

UninterpretedAction.__subclasses__=[]
UninterpretedAction.__mm__={
		'recurrence': (MMClass.kind__Attribute,IterationExpression,1,None,None,0),
		'target': (MMClass.kind__Attribute,ObjectSetExpression,1,None,None,0),
		'isAsynchronous': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'script': (MMClass.kind__Attribute,ActionExpression,1,None,None,0),
		'stateExit': (MMClass.kind__Association,State,1,'exit',1,0),
		'transition': (MMClass.kind__Association,Transition,1,'effect',1,0),
		'message': (MMClass.kind__Association,Message,0,'action',1,0),
		'stateDoActivity': (MMClass.kind__Association,State,1,'doActivity',1,0),
		'state': (MMClass.kind__Association,State,1,'entry',1,0),
		'actionSequence': (MMClass.kind__Association,ActionSequence,1,'action',0,0),
		'stimulus': (MMClass.kind__Association,Stimulus,0,'dispatchAction',1,0),
		'actualArgument': (MMClass.kind__Composition,Argument,0,'action',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

Link.__subclasses__=[LinkObject]
Link.__mm__={
		'stimulus': (MMClass.kind__Association,Stimulus,0,'communicationLink',1,0),
		'connection': (MMClass.kind__Composition,LinkEnd,0,'link',1,0),
		'owner': (MMClass.kind__Association,Instance,1,'ownedLink',0,0),
		'playedRole': (MMClass.kind__Association,AssociationRole,0,'conformingLink',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'participatingLink',0,0),
		'association': (MMClass.kind__Association,Association,1,'link',0,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

AssociationRole.__subclasses__=[]
AssociationRole.__mm__={
		'multiplicity': (MMClass.kind__Attribute,Multiplicity,1,None,None,0),
		'base': (MMClass.kind__Association,Association,1,'associationRole',0,0),
		'message': (MMClass.kind__Association,Message,0,'communicationConnection',1,0),
		'conformingLink': (MMClass.kind__Association,Link,0,'playedRole',0,0),
		'connection': (MMClass.kind__Composition,AssociationEnd,0,'association',1,0),
		'associationRole': (MMClass.kind__Association,AssociationRole,0,'base',1,0),
		'link': (MMClass.kind__Association,Link,0,'association',1,0),
		'isRoot': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isLeaf': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isAbstract': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'specialization': (MMClass.kind__Association,Generalization,0,'parent',1,0),
		'generalization': (MMClass.kind__Association,Generalization,0,'child',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

Multiplicity.__subclasses__=[]
Multiplicity.__mm__={
		'range': (MMClass.kind__Composition,MultiplicityRange,0,'multiplicity',1,0)
}

Interface.__subclasses__=[]
Interface.__mm__={
		'instance': (MMClass.kind__Association,Instance,0,'classifier',0,0),
		'specifiedEnd': (MMClass.kind__Association,AssociationEnd,0,'specification',0,0),
		'feature': (MMClass.kind__Composition,Feature,0,'owner',1,0),
		'typedFeature': (MMClass.kind__Association,StructuralFeature,0,'type',1,0),
		'powertypeRange': (MMClass.kind__Association,Generalization,0,'powertype',1,0),
		'classifierInState': (MMClass.kind__Association,ClassifierInState,0,'type',1,0),
		'objectFlowState': (MMClass.kind__Association,ObjectFlowState,0,'type',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'base',0,0),
		'typedParameter': (MMClass.kind__Association,Parameter,0,'type',1,0),
		'createAction': (MMClass.kind__Association,CreateAction,0,'instantiation',1,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'representedClassifier',1,0),
		'association': (MMClass.kind__Association,AssociationEnd,0,'participant',1,0),
		'isRoot': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isLeaf': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isAbstract': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'specialization': (MMClass.kind__Association,Generalization,0,'parent',1,0),
		'generalization': (MMClass.kind__Association,Generalization,0,'child',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0),
		'ownedElement': (MMClass.kind__Composition,ModelElement,0,'namespace',1,0)
}

Subsystem.__subclasses__=[]
Subsystem.__mm__={
		'isInstantiable': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'elementImport': (MMClass.kind__Composition,ElementImport,0,'package',1,0),
		'isRoot': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isLeaf': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isAbstract': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'specialization': (MMClass.kind__Association,Generalization,0,'parent',1,0),
		'generalization': (MMClass.kind__Association,Generalization,0,'child',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0),
		'ownedElement': (MMClass.kind__Composition,ModelElement,0,'namespace',1,0),
		'instance': (MMClass.kind__Association,Instance,0,'classifier',0,0),
		'specifiedEnd': (MMClass.kind__Association,AssociationEnd,0,'specification',0,0),
		'feature': (MMClass.kind__Composition,Feature,0,'owner',1,0),
		'typedFeature': (MMClass.kind__Association,StructuralFeature,0,'type',1,0),
		'powertypeRange': (MMClass.kind__Association,Generalization,0,'powertype',1,0),
		'classifierInState': (MMClass.kind__Association,ClassifierInState,0,'type',1,0),
		'objectFlowState': (MMClass.kind__Association,ObjectFlowState,0,'type',1,0),
		'typedParameter': (MMClass.kind__Association,Parameter,0,'type',1,0),
		'createAction': (MMClass.kind__Association,CreateAction,0,'instantiation',1,0),
		'association': (MMClass.kind__Association,AssociationEnd,0,'participant',1,0)
}

ActivityGraph.__subclasses__=[]
ActivityGraph.__mm__={
		'partition': (MMClass.kind__Composition,Partition,0,'activityGraph',1,0),
		'context': (MMClass.kind__Association,ModelElement,1,'behavior',0,0),
		'transitions': (MMClass.kind__Composition,Transition,0,'stateMachine',1,0),
		'submachineState': (MMClass.kind__Association,SubmachineState,0,'submachine',1,0),
		'top': (MMClass.kind__Composition,State,1,'stateMachine',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

MultiplicityRange.__subclasses__=[]
MultiplicityRange.__mm__={
		'lower': (MMClass.kind__Attribute,Integer,1,None,None,0),
		'upper': (MMClass.kind__Attribute,UnlimitedInteger,1,None,None,0),
		'multiplicity': (MMClass.kind__Association,Multiplicity,1,'range',0,0)
}

TypeExpression.__subclasses__=[]
TypeExpression.__mm__={
		'language': (MMClass.kind__Attribute,Name,1,None,None,0),
		'body': (MMClass.kind__Attribute,String,1,None,None,0)
}

Interaction.__subclasses__=[]
Interaction.__mm__={
		'interactionInstanceSet': (MMClass.kind__Association,InteractionInstanceSet,0,'interaction',1,0),
		'message': (MMClass.kind__Composition,Message,0,'interaction',1,0),
		'context': (MMClass.kind__Association,Collaboration,1,'interaction',0,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

ComponentInstance.__subclasses__=[]
ComponentInstance.__mm__={
		'nodeInstance': (MMClass.kind__Association,NodeInstance,1,'resident',0,0),
		'resident': (MMClass.kind__Association,Instance,0,'componentInstance',1,0),
		'slot': (MMClass.kind__Composition,AttributeLink,0,'instance',1,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'participatingInstance',0,0),
		'stimulus': (MMClass.kind__Association,Stimulus,0,'argument',0,0),
		'classifier': (MMClass.kind__Association,Classifier,0,'instance',0,0),
		'stimulusSender': (MMClass.kind__Association,Stimulus,0,'sender',1,0),
		'linkEnd': (MMClass.kind__Association,LinkEnd,0,'instance',1,0),
		'componentInstance': (MMClass.kind__Association,ComponentInstance,1,'resident',0,0),
		'ownedLink': (MMClass.kind__Composition,Link,0,'owner',1,0),
		'ownedInstance': (MMClass.kind__Composition,Instance,0,'owner',1,0),
		'owner': (MMClass.kind__Association,Instance,1,'ownedInstance',0,0),
		'stimulusReceiver': (MMClass.kind__Association,Stimulus,0,'receiver',1,0),
		'playedRole': (MMClass.kind__Association,ClassifierRole,0,'conformingInstance',0,0),
		'attributeLink': (MMClass.kind__Association,AttributeLink,0,'value',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

Package.__subclasses__=[Subsystem, Model]
Package.__mm__={
		'elementImport': (MMClass.kind__Composition,ElementImport,0,'package',1,0),
		'isRoot': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isLeaf': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isAbstract': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'specialization': (MMClass.kind__Association,Generalization,0,'parent',1,0),
		'generalization': (MMClass.kind__Association,Generalization,0,'child',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0),
		'ownedElement': (MMClass.kind__Composition,ModelElement,0,'namespace',1,0)
}

Stimulus.__subclasses__=[]
Stimulus.__mm__={
		'argument': (MMClass.kind__Association,Instance,0,'stimulus',0,1),
		'playedRole': (MMClass.kind__Association,Message,0,'conformingStimulus',0,0),
		'sender': (MMClass.kind__Association,Instance,1,'stimulusSender',0,0),
		'communicationLink': (MMClass.kind__Association,Link,1,'stimulus',0,0),
		'receiver': (MMClass.kind__Association,Instance,1,'stimulusReceiver',0,0),
		'interactionInstanceSet': (MMClass.kind__Association,InteractionInstanceSet,0,'participatingStimulus',0,0),
		'dispatchAction': (MMClass.kind__Association,Action,1,'stimulus',0,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

ModelElement.__subclasses__=[AssociationEnd, InteractionInstanceSet, Instance, TagDefinition, Constraint, Transition, Action, AttributeLink, EnumerationLiteral, GeneralizableElement, Event, StateVertex, Namespace, Feature, Parameter, ExtensionPoint, CollaborationInstanceSet, Relationship, Link, Interaction, Stimulus, Partition, Comment, LinkEnd, StateMachine, Argument, Guard, TaggedValue, Message, AssociationEndRole, Object, SubsystemInstance, NodeInstance, UseCaseInstance, DataValue, ComponentInstance, LinkObject, CallAction, TerminateAction, ReturnAction, DestroyAction, ActionSequence, SendAction, UninterpretedAction, CreateAction, Association, Package, Classifier, Stereotype, Collaboration, AssociationClass, AssociationRole, Subsystem, Model, Node, ClassifierInState, UseCase, Actor, Class, DataType, Component, Artifact, ClassifierRole, Interface, Signal, Enumeration, ProgrammingLanguageDataType, Primitive, Exception, ChangeEvent, TimeEvent, SignalEvent, CallEvent, StubState, SynchState, State, Pseudostate, CompositeState, SimpleState, FinalState, SubmachineState, SubactivityState, ActionState, ObjectFlowState, CallState, StructuralFeature, BehavioralFeature, Attribute, Method, Operation, Reception, Include, Extend, Flow, Dependency, Generalization, Usage, Binding, Abstraction, Permission, ActivityGraph]
ModelElement.__mm__={
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

Signal.__subclasses__=[Exception]
Signal.__mm__={
		'reception': (MMClass.kind__Association,Reception,0,'signal',1,0),
		'occurrence': (MMClass.kind__Association,SignalEvent,0,'signal',1,0),
		'context': (MMClass.kind__Association,BehavioralFeature,0,'raisedSignal',0,0),
		'sendAction': (MMClass.kind__Association,SendAction,0,'signal',1,0),
		'instance': (MMClass.kind__Association,Instance,0,'classifier',0,0),
		'specifiedEnd': (MMClass.kind__Association,AssociationEnd,0,'specification',0,0),
		'feature': (MMClass.kind__Composition,Feature,0,'owner',1,0),
		'typedFeature': (MMClass.kind__Association,StructuralFeature,0,'type',1,0),
		'powertypeRange': (MMClass.kind__Association,Generalization,0,'powertype',1,0),
		'classifierInState': (MMClass.kind__Association,ClassifierInState,0,'type',1,0),
		'objectFlowState': (MMClass.kind__Association,ObjectFlowState,0,'type',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'base',0,0),
		'typedParameter': (MMClass.kind__Association,Parameter,0,'type',1,0),
		'createAction': (MMClass.kind__Association,CreateAction,0,'instantiation',1,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'representedClassifier',1,0),
		'association': (MMClass.kind__Association,AssociationEnd,0,'participant',1,0),
		'isRoot': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isLeaf': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isAbstract': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'specialization': (MMClass.kind__Association,Generalization,0,'parent',1,0),
		'generalization': (MMClass.kind__Association,Generalization,0,'child',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0),
		'ownedElement': (MMClass.kind__Composition,ModelElement,0,'namespace',1,0)
}

Partition.__subclasses__=[]
Partition.__mm__={
		'activityGraph': (MMClass.kind__Association,ActivityGraph,1,'partition',0,0),
		'contents': (MMClass.kind__Association,ModelElement,0,'partition',0,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

Pseudostate.__subclasses__=[]
Pseudostate.__mm__={
		'kind': (MMClass.kind__Attribute,PseudostateKind,1,None,None,0),
		'incoming': (MMClass.kind__Association,Transition,0,'target',1,0),
		'container': (MMClass.kind__Association,CompositeState,1,'subvertex',0,0),
		'outgoing': (MMClass.kind__Association,Transition,0,'source',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

CreateAction.__subclasses__=[]
CreateAction.__mm__={
		'instantiation': (MMClass.kind__Association,Classifier,1,'createAction',0,0),
		'recurrence': (MMClass.kind__Attribute,IterationExpression,1,None,None,0),
		'target': (MMClass.kind__Attribute,ObjectSetExpression,1,None,None,0),
		'isAsynchronous': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'script': (MMClass.kind__Attribute,ActionExpression,1,None,None,0),
		'stateExit': (MMClass.kind__Association,State,1,'exit',1,0),
		'transition': (MMClass.kind__Association,Transition,1,'effect',1,0),
		'message': (MMClass.kind__Association,Message,0,'action',1,0),
		'stateDoActivity': (MMClass.kind__Association,State,1,'doActivity',1,0),
		'state': (MMClass.kind__Association,State,1,'entry',1,0),
		'actionSequence': (MMClass.kind__Association,ActionSequence,1,'action',0,0),
		'stimulus': (MMClass.kind__Association,Stimulus,0,'dispatchAction',1,0),
		'actualArgument': (MMClass.kind__Composition,Argument,0,'action',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

Element.__subclasses__=[PresentationElement, ModelElement, AssociationEnd, InteractionInstanceSet, Instance, TagDefinition, Constraint, Transition, Action, AttributeLink, EnumerationLiteral, GeneralizableElement, Event, StateVertex, Namespace, Feature, Parameter, ExtensionPoint, CollaborationInstanceSet, Relationship, Link, Interaction, Stimulus, Partition, Comment, LinkEnd, StateMachine, Argument, Guard, TaggedValue, Message, AssociationEndRole, Object, SubsystemInstance, NodeInstance, UseCaseInstance, DataValue, ComponentInstance, LinkObject, CallAction, TerminateAction, ReturnAction, DestroyAction, ActionSequence, SendAction, UninterpretedAction, CreateAction, Association, Package, Classifier, Stereotype, Collaboration, AssociationClass, AssociationRole, Subsystem, Model, Node, ClassifierInState, UseCase, Actor, Class, DataType, Component, Artifact, ClassifierRole, Interface, Signal, Enumeration, ProgrammingLanguageDataType, Primitive, Exception, ChangeEvent, TimeEvent, SignalEvent, CallEvent, StubState, SynchState, State, Pseudostate, CompositeState, SimpleState, FinalState, SubmachineState, SubactivityState, ActionState, ObjectFlowState, CallState, StructuralFeature, BehavioralFeature, Attribute, Method, Operation, Reception, Include, Extend, Flow, Dependency, Generalization, Usage, Binding, Abstraction, Permission, ActivityGraph]
Reception.__subclasses__=[]
Reception.__mm__={
		'specification': (MMClass.kind__Attribute,String,1,None,None,0),
		'isRoot': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isLeaf': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isAbstract': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'signal': (MMClass.kind__Association,Signal,1,'reception',0,0),
		'isQuery': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'raisedSignal': (MMClass.kind__Association,Signal,0,'context',0,0),
		'parameter': (MMClass.kind__Composition,Parameter,0,'behavioralFeature',1,0),
		'ownerScope': (MMClass.kind__Attribute,ScopeKind,1,None,None,0),
		'owner': (MMClass.kind__Association,Classifier,1,'feature',0,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableFeature',0,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

Model.__subclasses__=[]
Model.__mm__={
		'elementImport': (MMClass.kind__Composition,ElementImport,0,'package',1,0),
		'isRoot': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isLeaf': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isAbstract': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'specialization': (MMClass.kind__Association,Generalization,0,'parent',1,0),
		'generalization': (MMClass.kind__Association,Generalization,0,'child',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0),
		'ownedElement': (MMClass.kind__Composition,ModelElement,0,'namespace',1,0)
}

Classifier.__subclasses__=[Node, ClassifierInState, UseCase, Actor, Class, DataType, Component, Artifact, ClassifierRole, Interface, Subsystem, Signal, AssociationClass, Enumeration, ProgrammingLanguageDataType, Primitive, Exception]
Classifier.__mm__={
		'instance': (MMClass.kind__Association,Instance,0,'classifier',0,0),
		'specifiedEnd': (MMClass.kind__Association,AssociationEnd,0,'specification',0,0),
		'feature': (MMClass.kind__Composition,Feature,0,'owner',1,0),
		'typedFeature': (MMClass.kind__Association,StructuralFeature,0,'type',1,0),
		'powertypeRange': (MMClass.kind__Association,Generalization,0,'powertype',1,0),
		'classifierInState': (MMClass.kind__Association,ClassifierInState,0,'type',1,0),
		'objectFlowState': (MMClass.kind__Association,ObjectFlowState,0,'type',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'base',0,0),
		'typedParameter': (MMClass.kind__Association,Parameter,0,'type',1,0),
		'createAction': (MMClass.kind__Association,CreateAction,0,'instantiation',1,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'representedClassifier',1,0),
		'association': (MMClass.kind__Association,AssociationEnd,0,'participant',1,0),
		'isRoot': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isLeaf': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isAbstract': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'specialization': (MMClass.kind__Association,Generalization,0,'parent',1,0),
		'generalization': (MMClass.kind__Association,Generalization,0,'child',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0),
		'ownedElement': (MMClass.kind__Composition,ModelElement,0,'namespace',1,0)
}

Comment.__subclasses__=[]
Comment.__mm__={
		'body': (MMClass.kind__Attribute,String,1,None,None,0),
		'annotatedElement': (MMClass.kind__Association,ModelElement,0,'comment',0,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

LinkEnd.__subclasses__=[]
LinkEnd.__mm__={
		'instance': (MMClass.kind__Association,Instance,1,'linkEnd',0,0),
		'link': (MMClass.kind__Association,Link,1,'connection',0,0),
		'qualifiedValue': (MMClass.kind__Composition,AttributeLink,0,'linkEnd',1,1),
		'associationEnd': (MMClass.kind__Association,AssociationEnd,1,'linkEnd',0,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

Primitive.__subclasses__=[]
Primitive.__mm__={
		'instance': (MMClass.kind__Association,Instance,0,'classifier',0,0),
		'specifiedEnd': (MMClass.kind__Association,AssociationEnd,0,'specification',0,0),
		'feature': (MMClass.kind__Composition,Feature,0,'owner',1,0),
		'typedFeature': (MMClass.kind__Association,StructuralFeature,0,'type',1,0),
		'powertypeRange': (MMClass.kind__Association,Generalization,0,'powertype',1,0),
		'classifierInState': (MMClass.kind__Association,ClassifierInState,0,'type',1,0),
		'objectFlowState': (MMClass.kind__Association,ObjectFlowState,0,'type',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'base',0,0),
		'typedParameter': (MMClass.kind__Association,Parameter,0,'type',1,0),
		'createAction': (MMClass.kind__Association,CreateAction,0,'instantiation',1,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'representedClassifier',1,0),
		'association': (MMClass.kind__Association,AssociationEnd,0,'participant',1,0),
		'isRoot': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isLeaf': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isAbstract': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'specialization': (MMClass.kind__Association,Generalization,0,'parent',1,0),
		'generalization': (MMClass.kind__Association,Generalization,0,'child',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0),
		'ownedElement': (MMClass.kind__Composition,ModelElement,0,'namespace',1,0)
}

IterationExpression.__subclasses__=[]
IterationExpression.__mm__={
		'language': (MMClass.kind__Attribute,Name,1,None,None,0),
		'body': (MMClass.kind__Attribute,String,1,None,None,0)
}

StateMachine.__subclasses__=[ActivityGraph]
StateMachine.__mm__={
		'context': (MMClass.kind__Association,ModelElement,1,'behavior',0,0),
		'transitions': (MMClass.kind__Composition,Transition,0,'stateMachine',1,0),
		'submachineState': (MMClass.kind__Association,SubmachineState,0,'submachine',1,0),
		'top': (MMClass.kind__Composition,State,1,'stateMachine',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

Stereotype.__subclasses__=[]
Stereotype.__mm__={
		'icon': (MMClass.kind__Attribute,Geometry,1,None,None,0),
		'baseClass': (MMClass.kind__Attribute,Name,1,None,None,0),
		'extendedElement': (MMClass.kind__Association,ModelElement,0,'stereotype',0,0),
		'definedTag': (MMClass.kind__Composition,TagDefinition,0,'owner',1,0),
		'stereotypeConstraint': (MMClass.kind__Composition,Constraint,0,'constrainedStereotype',1,0),
		'isRoot': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isLeaf': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isAbstract': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'specialization': (MMClass.kind__Association,Generalization,0,'parent',1,0),
		'generalization': (MMClass.kind__Association,Generalization,0,'child',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

ActionExpression.__subclasses__=[]
ActionExpression.__mm__={
		'language': (MMClass.kind__Attribute,Name,1,None,None,0),
		'body': (MMClass.kind__Attribute,String,1,None,None,0)
}

Argument.__subclasses__=[]
Argument.__mm__={
		'value': (MMClass.kind__Attribute,Expression,1,None,None,0),
		'action': (MMClass.kind__Association,Action,1,'actualArgument',0,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

Generalization.__subclasses__=[]
Generalization.__mm__={
		'discriminator': (MMClass.kind__Attribute,Name,1,None,None,0),
		'powertype': (MMClass.kind__Association,Classifier,1,'powertypeRange',0,0),
		'parent': (MMClass.kind__Association,GeneralizableElement,1,'specialization',0,0),
		'child': (MMClass.kind__Association,GeneralizableElement,1,'generalization',0,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

Guard.__subclasses__=[]
Guard.__mm__={
		'expression': (MMClass.kind__Attribute,BooleanExpression,1,None,None,0),
		'transition': (MMClass.kind__Association,Transition,1,'guard',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

TemplateArgument.__subclasses__=[]
TemplateArgument.__mm__={
		'binding': (MMClass.kind__Association,Binding,1,'argument',0,0),
		'modelElement': (MMClass.kind__Association,ModelElement,1,'templateArgument',0,0)
}

TaggedValue.__subclasses__=[]
TaggedValue.__mm__={
		'dataValue': (MMClass.kind__Attribute,String,1,None,None,0),
		'type': (MMClass.kind__Association,TagDefinition,1,'typedValue',0,0),
		'modelElement': (MMClass.kind__Association,ModelElement,1,'taggedValue',0,0),
		'referenceValue': (MMClass.kind__Association,ModelElement,0,'referenceTag',0,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

Message.__subclasses__=[]
Message.__mm__={
		'conformingStimulus': (MMClass.kind__Association,Stimulus,0,'playedRole',0,0),
		'receiver': (MMClass.kind__Association,ClassifierRole,1,'messageReceiver',0,0),
		'predecessor': (MMClass.kind__Association,Message,0,'successor',0,0),
		'successor': (MMClass.kind__Association,Message,0,'predecessor',0,0),
		'interaction': (MMClass.kind__Association,Interaction,1,'message',0,0),
		'sender': (MMClass.kind__Association,ClassifierRole,1,'message',0,0),
		'action': (MMClass.kind__Association,Action,1,'message',0,0),
		'communicationConnection': (MMClass.kind__Association,AssociationRole,1,'message',0,0),
		'message': (MMClass.kind__Association,Message,0,'activator',1,0),
		'activator': (MMClass.kind__Association,Message,1,'message',0,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'constrainingElement',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'constrainingElement',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0)
}

Collaboration.__subclasses__=[]
Collaboration.__mm__={
		'collaborationInstanceSet': (MMClass.kind__Association,CollaborationInstanceSet,0,'collaboration',1,0),
		'representedOperation': (MMClass.kind__Association,Operation,1,'collaboration',0,0),
		'interaction': (MMClass.kind__Composition,Interaction,0,'context',1,0),
		'constrainingElement': (MMClass.kind__Association,ModelElement,0,'collaboration',0,0),
		'representedClassifier': (MMClass.kind__Association,Classifier,1,'collaboration',0,0),
		'usedCollaboration': (MMClass.kind__Association,Collaboration,0,'collaboration',0,0),
		'collaboration': (MMClass.kind__Association,Collaboration,0,'usedCollaboration',0,0),
		'isRoot': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isLeaf': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'isAbstract': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'specialization': (MMClass.kind__Association,Generalization,0,'parent',1,0),
		'generalization': (MMClass.kind__Association,Generalization,0,'child',1,0),
		'name': (MMClass.kind__Attribute,Name,1,None,None,0),
		'visibility': (MMClass.kind__Attribute,VisibilityKind,1,None,None,0),
		'isSpecification': (MMClass.kind__Attribute,Boolean,1,None,None,0),
		'sourceFlow': (MMClass.kind__Association,Flow,0,'source',0,0),
		'elementImport': (MMClass.kind__Association,ElementImport,0,'importedElement',1,0),
		'stereotype': (MMClass.kind__Association,Stereotype,0,'extendedElement',0,0),
		'presentation': (MMClass.kind__Composition,PresentationElement,0,'subject',0,0),
		'templateArgument': (MMClass.kind__Association,TemplateArgument,0,'modelElement',1,0),
		'classifierRole': (MMClass.kind__Association,ClassifierRole,0,'availableContents',0,0),
		'namespace': (MMClass.kind__Association,Namespace,1,'ownedElement',0,0),
		'constraint': (MMClass.kind__Association,Constraint,0,'constrainedElement',0,0),
		'elementResidence': (MMClass.kind__Association,ElementResidence,0,'resident',1,0),
		'partition': (MMClass.kind__Association,Partition,0,'contents',0,0),
		'taggedValue': (MMClass.kind__Composition,TaggedValue,0,'modelElement',1,0),
		'behavior': (MMClass.kind__Association,StateMachine,0,'context',1,0),
		'templateParameter': (MMClass.kind__Composition,TemplateParameter,0,'template',1,0),
		'comment': (MMClass.kind__Association,Comment,0,'annotatedElement',0,0),
		'parameterTemplate': (MMClass.kind__Association,TemplateParameter,1,'parameter',1,0),
		'supplierDependency': (MMClass.kind__Association,Dependency,0,'supplier',0,0),
		'clientDependency': (MMClass.kind__Association,Dependency,0,'client',0,0),
		'targetFlow': (MMClass.kind__Association,Flow,0,'target',0,0),
		'referenceTag': (MMClass.kind__Association,TaggedValue,0,'referenceValue',0,0),
		'defaultedParameter': (MMClass.kind__Association,TemplateParameter,0,'defaultElement',1,0),
		'ownedElement': (MMClass.kind__Composition,ModelElement,0,'namespace',1,0)
}

import string
		
def newMultiplicity(lower=1,upper=1):
		m=Multiplicity()
		m.range.insert(MultiplicityRange(lower=lower,upper=upper))
		return m

def newAssociation(classifier1,classifier2,name=None):
		if not name:
				name=''
		as=Association(name=name,namespace=classifier1.namespace)
		ae1=AssociationEnd(participant=classifier1,
											 association=as,
											 multiplicity=newMultiplicity(1,1),
											 isNavigable=1)
				
		ae2=AssociationEnd(participant=classifier2,
											 association=as,
											 multiplicity=newMultiplicity(1,1),
											 isNavigable=1)

		return as

def newAssociationRole(classifierrole1,classifierrole2,name=None):
		if not name:
				name='unnamed'
		baseAss=classifierrole1.base[0].association[0].association #FIXME
		asr=AssociationRole(base=baseAss,name=name,namespace=classifierrole1.namespace)
		aer1=AssociationEndRole(association=asr,
														participant=classifierrole1,
														base=baseAss.connection[0],
														multiplicity=newMultiplicity(1,1),
														isNavigable=1)
		aer2=AssociationEndRole(association=asr,
														participant=classifierrole2,
														base=baseAss.connection[1],
														multiplicity=newMultiplicity(1,1),
														isNavigable=1)

		return asr
def collectAssociations(clf,assoc=None):
		"""Method for collecting all AssociationEnds from a classifier and all
		its superclasses.
		"""
		if not assoc:
				assoc=[]
		assoc+=clf.association
		for g in clf.generalization:
				assoc+=g.parent.association
				if g.parent.generalization:
						return collectAssociations(g.parent,assoc)
		else:
				return assoc

def newLink(instance1,instance2,name=None):
		"""Creates a new link between two instances, there must exist an
		association between the base classifiers (or superclasses of these)
		for the link to map onto, otherwise it will return None and no Link
		is created.
		returns the new Link
		"""
		if not name:
				name='unnamed'
		baseAss=None

		assocs1=MMSet()
		assocs2=MMSet()

		assocs1=collectAssociations(instance1.classifier[0])
		assocs2=collectAssociations(instance2.classifier[0])
		for a in assocs1:
				for b in assocs2:
						if not a == b and a.association == b.association:
								baseAss=a.association
								break

		if not baseAss:
				return None
		
		link=Link(name=name,association=baseAss,namespace=instance1.namespace)

		if baseAss.connection[0].participant == instance1.classifier[0]:
				le1=LinkEnd(instance=instance1,link=link,
										associationEnd=baseAss.connection[0])
				le2=LinkEnd(instance=instance2,link=link,
										associationEnd=baseAss.connection[1])
		else:
				le1=LinkEnd(instance=instance1,link=link,
										associationEnd=baseAss.connection[1])
				le2=LinkEnd(instance=instance2,link=link,
										associationEnd=baseAss.connection[0])
		
		return link

def fromMultiplicityToString(multiplicity):
		"""
		fromMultiplicityToString creates a string from a multiplicity instance that
		will be displayed in the editor, i.e. 2..7 .

		Example: 
			testlist='2..7'
			a=fromStringToMultiplicity(testlist)
			b=fromMultiplicityToString(a)
			assert('2..7'==b)
		"""
		
		outString=""
	 
		for i in multiplicity.range:
				lower=i.lower
				upper=i.upper

				if upper==-1:
						upper="*"

				if outString:
						outString = outString +","

				if lower==0 and upper=="*":
						outString=outString+"*"
				else:
						if lower!=upper:
								outString=outString+str(lower)+".."+str(upper)
						else:
								outString=outString+str(lower)
		
		return outString


def fromStringToMultiplicity(s):

		"""
		fromStringToMultiplicity creates an Multiplicity instance from
		a given string containing a multiplicity range such as '1..5', '*' or
		'2..5,7..10'

		Example:
		 testlist='2..	7,	10.. 29, 23..2'
		 m=fromStringToMultiplicity(testlist)
		 assert(m.range[0].lower==2 and m.range[0].upper==7)
		 assert(m.range[1].lower==10 and m.range[1].upper==29)
		 assert(m.range[2].lower==2 and m.range[2].upper==23)
		 
		It returns None if the string is empty or contains an invalid
		multiplicty range.		
		"""

		s=string.replace(s," ","")
		list=string.split(s,",")

		if len(list)==0:
				return None

		m=Multiplicity()

		for temp in list:														 
				r=string.split(temp,"..")
 
				#If only	element x in list, lower=x and upper=x
				if len(r)==1:		 
						r.append(r[0])

			 # r[0]=string.strip(r[0])
				if r[0]=='*':
						r[0]=0
						r.append(-1)
				else:
						try:
								r[0]=int(r[0])
						except ValueError:
								return None
			
				if r[1]=='*':
						r[1]=-1
				else:
						try:
								r[1]=int(r[1])
						except ValueError:
								return None

				
				if r[1] != -1 and r[0] > r[1] or r[0]==-1:
						r[0],r[1]=r[1],r[0] #Swap

					 
				if len(r)==3 and r[1]!=-1: #if input is i.e(*..5) swap to (5..*)
						r[0]=r[1]
						r[1]=r[2]
				
				m.range.insert(MultiplicityRange(lower=r[0],upper=r[1]))
				#for loop ends
	 
				
		#creates a new multiplicity instance with the given multiplicities sorted!		
		return m

def fromAttributeToString(attr):
		"""
		fromAttributeToString takes the attributes from the Attribute instance and
		converts them into a string. This string is then used for proper output in the
		class diagram, i.e. ([visibility][name]:[type]=[body]), +x:int=5...

		Example:
		
		attr=Attribute()
		attr.name=\"theAttr\"
		myExp=Expression()
		myExp.body=\"Hello World!\"
		myExp.language=\"\"
		attr.initialValue=myExp
		clfier=Classifier(name=\"String\")
		attr.type=clfier
		attr.visibility=VisibilityKind.vk_protected
		
		assert(fromAttributeToString(attr)==\"#theAttr:String=Hello World!\")
		"""
		
		s=""
		if attr.visibility == VisibilityKind.vk_public:
				s=s+"+"
		elif attr.visibility == VisibilityKind.vk_private:
				s=s+"-"
		elif attr.visibility == VisibilityKind.vk_protected:
				s=s+"#"
		elif attr.visibility == VisibilityKind.vk_package:
				s=s+"~"

		if attr.name:
				s=s+attr.name
		if attr.type:
				s=s+":"+attr.type.name
		if attr.initialValue and attr.initialValue.body:
				s=s+"="+attr.initialValue.body
		
		if s=='+':
				return None
		else:
				return s

#kusung write
def getAttributeInfo(attr):
		visibility, name, typeName, initialValueBody='', '', '', ''
		
		if attr.visibility == VisibilityKind.vk_public:
				visibility = "public"
		elif attr.visibility == VisibilityKind.vk_private:
				visibility = "private"
		elif attr.visibility == VisibilityKind.vk_protected:
				visibility = "protected"
		elif attr.visibility == VisibilityKind.vk_package:
				visibility = "package"

		if attr.name:
				name = attr.name
		if attr.type:
				typeName = attr.type.name

		if attr.initialValue and attr.initialValue.body:
				initialValueBody = attr.initialValue.body
				
		return (visibility, name, typeName, initialValueBody)
##		if s=='+':
##				return None
##		else:
##				return (visibility, name, typeName, initialValueBody)

def fromBehavioralFeatureToString(bf):
	'''
	fromBehaviorToString takes the name, parameters, type (and kind), etc. from
	the BehavioralFeature instance for output to be printed in the diagram...

	Example:
	op=Operation(name="add")
	op.parameter.insert(Parameter(name="x",type=t))
	op.parameter.insert(Parameter(kind=ParameterDirectionKind.pdk_return, type=t))
	op.parameter.insert(Parameter(name="y",type=t))
	op.visibility=VisibilityKind.vk_private
	assert(fromBehavioralFeatureToString(op)=="-add(x:int,y:int):int")

	According to specifications if a BehavioralFeature returns nothing (i.e. void)
	the return type should be omitted.
	'''

	
	s=""
	if bf.visibility == VisibilityKind.vk_public:
			s=s+"+"
	elif bf.visibility == VisibilityKind.vk_private:
			s=s+"-"
	elif bf.visibility == VisibilityKind.vk_protected:
			s=s+"#"
	elif bf.visibility == VisibilityKind.vk_package:
			s=s+"~"
	first=1
	end="" #according to "the bible" it should be nothing
	s=s+bf.name+"("
	for p in bf.parameter:
			if p.kind==ParameterDirectionKind.pdk_return and p.type and not p.type.name == "void":						
					end+=":"+p.type.name

			if not first and p.name and p.kind!=ParameterDirectionKind.pdk_return:
					s=s+','

			if p.name and p.kind!=ParameterDirectionKind.pdk_return:			 
					s=s+p.name
					first=0

			if p.type and p.type.name!="" and p.name and p.kind!=ParameterDirectionKind.pdk_return:
					s=s+":"+p.type.name
											 
	s=s+")"+end
							
	return s

def getBehavioralFeatureInfo(bf):
	visibility, name, parameterString, returnTypeName = '', '', '', ''
	if bf.visibility == VisibilityKind.vk_public:
			visibility='public'
	elif bf.visibility == VisibilityKind.vk_private:
			visibility='private'
	elif bf.visibility == VisibilityKind.vk_protected:
			visibility='protected'
	elif bf.visibility == VisibilityKind.vk_package:
			visibility='package'
			
	#  -insert(inID:String,inName:Integer):String
	first=1
	end="" 			#according to "the bible" it should be nothing
	
	name = bf.name
	s=""
	for p in bf.parameter:
		if p.kind==ParameterDirectionKind.pdk_return and p.type \
		   and not p.type.name == "void":
				end+=":"+p.type.name
				returnTypeName = p.type.name

		if not first and p.name and p.kind!=ParameterDirectionKind.pdk_return:
				s=s+','

		if p.name and p.kind!=ParameterDirectionKind.pdk_return:
				s=s+p.name
				first=0

		if p.type and p.type.name!="" and p.name and p.kind!=ParameterDirectionKind.pdk_return:
				s=s+":"+p.type.name
	parameterString = s

	return (visibility, name, parameterString, returnTypeName)

def fromParameterToString(p):
	'''fromParameterToString returns the textual representation of
	   a parameter according to the specification.

	Example:
	t2=Class(name="String")
	p=Parameter(name="name",type=t2)
	exp=Expression()
	exp.body="Hello World"
	p.kind=ParameterDirectionKind.pdk_inout
	p.defaultValue=exp
	assert(fromParameterToString(p)=="in-out name:String=Hello World")
	'''
	
	s=""
	if p.kind==ParameterDirectionKind.pdk_in:
			s+="in "
	elif p.kind==ParameterDirectionKind.pdk_inout:
			s+="in-out "
	elif p.kind==ParameterDirectionKind.pdk_out:
			s+="out "
	elif p.kind==ParameterDirectionKind.pdk_return:
			s+="return "
	if p.name!="":
			s+=p.name
	if p.type:
			if p.type.name!="":
					s+=":"
			s+=p.type.name
			
	if p.defaultValue and p.defaultValue.body !="":
			s+="="+p.defaultValue.body
			
	return s

def fromOrderingToString(ae):
		"""fromOrderingToString gets the orderingkind from an associationEnd
		so that it will be easier to print relevant output to the screen..."""
		s=""
		if ae.ordering==OrderingKind.ok_ordered:
				return "{ordered}"
		else:
				return s


def fromVisibilityToString(ae):
		"""fromVisibilityToString takes an AssociationEnd Rolename as the argument
		and returns the given visibility of the name e.g +specification=public..."""
		s=""
		
		if ae.visibility == VisibilityKind.vk_public:
				s=s+"+"
		elif ae.visibility == VisibilityKind.vk_private:
				s=s+"-"
		elif ae.visibility == VisibilityKind.vk_protected:
				s=s+"#"
				
		return s



def fromFQPToElement(s,model):
		"""fromFQPToElement takes a FullyQualifiedPath in the form of a string and a model and
		returns a reference to that particular element (if it exists).

		If the element does not exist, it returns None.
		"""
		if not model:
				return None
		
		names=string.split(s,"::")

		for e in model.ownedElement:
		
				if e.name==names[0] and len(names)==1:
	
						return e
				elif len(names)>1:
	
						if e.name==names[0]:
	
								names=names[1:]
								return fromFQPToElement(string.join(names,"::"),e)
		#out of elements..
		return None

def convertSimpleToCompositeState(state):
				assert(isinstance(state,SimpleState))
 
				# this is a really dirty hack
				# and it is not undoable
				state.__setclass__(CompositeState)
				state.subvertex=[]
				
				state.isConcurrent=0
				state.isRegion=0

				return state
