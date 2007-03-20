"""
SMW The System Modeling Workbench 
Copyright 2001,2002 by Ivan Porres iporres@abo.fi

The System Modeling Workbench is a collection of tools for creating,
editing and transforming software models.

MODELER

We recomend that you start using the SMW Modeler in order to get
familiar with SMW. 

MODELS

From the programmer's point of view, each supported modeling language
is represented by a metamodel module. A metamodel module contains a
Python class for each model element. These classes have the same
attributes and associations with the same name as in the metamodel of
the modeling language.	Since the model elements are represented as
Python classes, we can create a model by instantiating new objects and
manipulating its associations.

METAMODELS 

SMW provides the following metamodels

	 Language Module 
	 UML 1.1	smw.metamodel.UML11
	 UML 1.3	smw.metamodel.UML13
	 UML 1.4	smw.metamodel.UML14

You should import the appropiate module, i.e.:

 from smw.metamodel import UML14

LICENSE

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.
 
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
GNU General Public License for more details.

"""
