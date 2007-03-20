#!/usr/bin/env python2.2

from __future__ import nested_scopes
import copy
import re
import os
import sys
import string
import types
import unittest
import pymerase
from  pymerase.util import NameMangling

class TestNameMangling(unittest.TestCase):

  def testNullMangler(self):
    #tests mangle
    nullMangler = NameMangling.nullMangler()
    self.failUnless(nullMangler.mangle("test") == "test", "Mangle: test didn't equal test")

    #tests createGetter
    self.failUnless(nullMangler.createGetter("createGetter") == "getcreateGetter", "CreateGetter didn't equal")
    self.failUnless(nullMangler.createGetter("**createGetter") == "get**createGetter", "CreateGetter didn't equal")

    #tests createSetter
    self.failUnless(nullMangler.createSetter("createSetter") == "setcreateSetter", "CreateSetter didn't equal")
    self.failUnless(nullMangler.createSetter("**createSetter") == "set**createSetter", "CreateSetter didn't equal")
    
    #tests createAppender
    self.failUnless(nullMangler.createAppender("createAppender") == "appendcreateAppender", "CreateAppender didn't equal")
    self.failUnless(nullMangler.createAppender("**createAppender") == "append**createAppender", "CreateAppender didn't equal")

  def testCapWord(self):
    capword= NameMangling.CapWord()
    #tests lower -> uppercase
    self.failUnless(capword.mangle("checkinguppercase") == "Checkinguppercase")
    self.failUnless(capword.mangle("1upperCase") == "1upperCase")

    #test CapWord()
    self.failUnless(capword.mangle("upper_case") == "UpperCase")
    self.failUnless(capword.mangle("with spaces_Are Cool_") == "WithSpacesAreCool")
    self.failUnless(capword.mangle("_upper_ caSe") == "UpperCaSe")
    self.failUnless(capword.mangle("**upper_ 3case")  == "**upper3case")
    self.failUnless(capword.mangle("3upper_3case")  == "3upper3case")

  def testUnderscore_word(self):
    underscore = NameMangling.underscore_word()
    #tests for underscore words
    self.failUnless(underscore.mangle("Under_Scored_Word_") == "under_scored_word")
    self.failUnless(underscore.mangle("UNDER SCORE WORD") == "under_scored_word")
    self.failUnless(underscore.mangle("Under_3Scored") == "under_3_scored")
    self.failUnless(underscore.mangle("under_scored_word") == "under_scored_word")
    self.failUnless(underscore.mangle("UnderScoreWord") == "under_score_word")
    self.failUnless(underscore.mangle("3Upper 3Case")  == "3_upper_3_Case")

  def testEnglishWord(self):
    english = NameMangling.EnglishWord()
    #tests English words
    self.failUnless(english.mangle("capitalized_words") == "Capitalized words")
    self.failUnless(english.mangle("CapitalizeWords") == "Capitalize words")
    self.failUnless(english.mangle("Capitalize_2_words") == "Capitalize 2 words")
    self.failUnless(english.mangle("tHIS is english") == "This is english")
    self.failUnless(english.mangle("3Upper_3case")  == "3 upper 3case")

  def testLowercaseword(self):
    lowercase = NameMangling.lowercaseword()
    #tests Lowercasewords
    self.failUnless(lowercase.mangle("*$LOWER_case") == "*$lower_case")
    self.failUnless(lowercase.mangle("WITH_SPACES_LOWER") == "with_spaces_lower")
    self.failUnless(lowercase.mangle("Lower_3Case") == "lower_3case")
    self.failUnless(lowercase.mangle("THIS IS SPACED") == "this is spaced")
    self.failUnless(lowercase.mangle("3Upper_3CaSe")  == "3upper_3case")

  def testRelationalKey(self):
    relation = NameMangling.RelationalKey()
    #test primaryKey
    self.failUnless(cmp(map(relation.getPrimaryKey, re.split(", ", "helpk, JOHNK, PuNPK, Pumpkin, pkorn, popPk")), re.split(", ", "helpk, JOHNK_pk, PuNPK, Pumpkin_pk, pkorn_pk, popPk")) == 0)
    self.failUnless(cmp(map(relation.getPrimaryKey, re.split(", ", "fkab, houseFK, fake, helpfK, popPk")), re.split (", ", "fkab_pk, housepk, fake_pk, helppk, popPk")) == 0)

    #test foreighKey
    self.failUnless(cmp(map(relation.getForeignKey, re.split(", ", "helpk, JOHNK, PuNPK, Pumpkin, pkorn, popPk")), re.split("," , "helpfk, JOHNK_fk, PuNfk, Pumpkin_fk, pkorn_fk, popfk")) == 0)
    self.failUnless(cmp(map(relation.getForeignKey, re.split(", ", "fkab, houseFK, fake, helpfK, popPk")), re.split(", ", "fkab_fk, houseFK, fake_fk, helpfK, popfk")) == 0)

def suite():
  return unittest.defaultTestLoader.loadTestsFromTestCase(TestNameMangling)

if __name__ == "__main__":
  unittest.main(defaultTest="suite") 
