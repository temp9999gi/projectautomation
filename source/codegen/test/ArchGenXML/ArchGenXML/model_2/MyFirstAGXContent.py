# -*- coding: utf-8 -*-
#
# File: MyFirstAGXContent.py
#
# Copyright (c) 2006 by []
# Generator: ArchGenXML Version 1.5.0
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from Products.model_2.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    TextField(
        name='MyTextField',
        widget=TextAreaWidget(
            label='Mytextfield',
            label_msgid='model_2_label_MyTextField',
            i18n_domain='model_2',
        )
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

MyFirstAGXContent_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class MyFirstAGXContent(BaseContent):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'MyFirstAGXContent'

    meta_type = 'MyFirstAGXContent'
    portal_type = 'MyFirstAGXContent'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 1
    #content_icon = 'MyFirstAGXContent.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "MyFirstAGXContent"
    typeDescMsgId = 'description_edit_myfirstagxcontent'

    _at_rename_after_creation = True

    schema = MyFirstAGXContent_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(MyFirstAGXContent, PROJECTNAME)
# end of class MyFirstAGXContent

##code-section module-footer #fill in your manual code here
##/code-section module-footer



