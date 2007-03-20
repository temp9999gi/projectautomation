class XMI1_0:
	XMI_CONTENT = "XMI.content"
	OWNED_ELEMENT = "Foundation.Core.Namespace.ownedElement"
	def __init__(self):
		pass

class XMI1_1(XMI1_0):
	# XMI version specific stuff goes there

	tagDefinitions = None

	NAME = 'UML:ModelElement.name'
	OWNED_ELEMENT = "UML:Namespace.ownedElement"

	MODEL = 'UML:Model'

	# Collaboration
	COLLAB = 'Behavioral_Elements.Collaborations.Collaboration'
	CLASS = 'UML:Class'
	PACKAGE = 'UML:Package'

	# To match up a CR with the right start state, we look out for the context
	MULTIPLICITY = 'UML:StructuralFeature.multiplicity'
	ATTRIBUTE = 'UML:Attribute'
	DATATYPE = 'UML:DataType'
	FEATURE = 'UML:Classifier.feature'
	TYPE = 'UML:StructuralFeature.type'
	CLASSIFIER = 'UML:Classifier'
	ASSOCIATION = 'UML:Association'
	AGGREGATION = 'UML:AssociationEnd.aggregation'
	ASSOCEND = 'UML:AssociationEnd'
	ASSOCENDTYPE = 'UML:AssociationEnd.type'
	ASSOCEND_PARTICIPANT = 'UML:AssociationEnd.participant'
	OPERATION = "UML:Operation"
	METHOD_PARAMETER = "UML:Parameter"
	MULTRANGE = 'UML:MultiplicityRange'

	MULT_MIN = 'UML:MultiplicityRange.lower'
	MULT_MAX = 'UML:MultiplicityRange.upper'

	GENERALIZATION = "UML:Generalization"
	GEN_CHILD = "UML:Generalization.child"
	GEN_PARENT = "UML:Generalization.parent"
	GEN_ELEMENT = "UML:Class"

	ATTRIBUTE_INIT_VALUE = "UML:Attribute.initialValue"
	ATTRIBUTE_EXPRESSION ="UML:Expression"
	EXPRESSION = ["UML:Expression","UML2:OpaqueExpression"]
	PARAM_DEFAULT = "UML:Parameter.defaultValue"

	TAG_DEFINITION = "UML:TagDefinition"

	TAGGED_VALUE_MODEL = "UML:ModelElement.taggedValue"
	TAGGED_VALUE = "UML:TaggedValue"
	TAGGED_VALUE_TAG = "UML:TaggedValue.tag"
	TAGGED_VALUE_VALUE = "UML:TaggedValue.value"

	MODELELEMENT = "UML:ModelElement"
	STEREOTYPE_MODELELEMENT = "UML:ModelElement.stereotype"

	STEREOTYPE = "UML:Stereotype"
	ISABSTRACT = "UML:GeneralizableElement.isAbstract"
	INTERFACE = "UML:Interface"

	ABSTRACTION = "UML:Abstraction"

	DEPENDENCY = "UML:Dependency"
	DEP_CLIENT = "UML:Dependency.client"
	DEP_SUPPLIER = "UML:Dependency.supplier"

	ASSOCIATION_CLASS = 'UML:AssociationClass'
	BOOLEAN_EXPRESSION = ["UML:BooleanExpression","UML2:OpaqueExpression"]

	#State Machine

	STATEMACHINE = "UML:StateMachine","UML2:StateMachine"
	STATEMACHINE_CONTEXT = "UML:StateMachine.context"
	STATEMACHINE_TOP = "UML:StateMachine.top"
	COMPOSITESTATE = "UML:CompositeState"
	COMPOSITESTATE_SUBVERTEX = "UML:CompositeState.subvertex"
	SIMPLESTATE = "UML:SimpleState","UML2:State"
	PSEUDOSTATE = "UML:Pseudostate", "UML2:PseudoState", "UML2:Pseudostate"
	PSEUDOSTATE_KIND = "kind"
	FINALSTATE = "UML:FinalState","UML2:FinalState"
	STATEVERTEX_OUTGOING = "UML:StateVertex.outgoing","UML2:Vertex.outgoing"
	STATEVERTEX_INCOMING = "UML:StateVertex.incoming","UML2:Vertex.incoming"
	TRANSITION = "UML:Transition","UML2:Transition"
	STATEMACHINE_TRANSITIONS = "UML:StateMachine.transitions"
	TRANSITON_TARGET = "UML:Transition.target","UML2:Transition.target"
	TRANSITION_SOURCE = "UML:Transition.source","UML2:Transition.source"
	TRANSITION_EFFECT = "UML:Transition.effect","UML2:Transition.effect"
	TRANSITION_GUARD = "UML:Transition.guard", "UML2:Transition.guard"
	OWNED_BEHAVIOR = "UML2:BehavioredClassifier.ownedBehavior"

	ACTION_SCRIPT = "UML:Action.script"
	ACTION_EXPRESSION = "UML:ActionExpression"
	ACTION_EXPRESSION_BODY = "UML:ActionExpression.body"

	DIAGRAM = "UML:Diagram"
	DIAGRAM_OWNER = "UML:Diagram.owner"
	DIAGRAM_SEMANTICMODEL_BRIDGE = "UML:Uml1SemanticModelBridge"
	DIAGRAM_SEMANTICMODEL_BRIDGE_ELEMENT = "UML:Uml1SemanticModelBridge.element"
	ACTOR = "UML:Actor"

	UML2TYPE = 'UML2:TypedElement.type'
	
	def __init__(self):
		XMI1_0.__init__


