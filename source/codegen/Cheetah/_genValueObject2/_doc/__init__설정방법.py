"""
All of FAQTsPython Knowledge BaseSnippets Folder 
Did You Find This Entry Useful?
    
17 of 18 people (94%) answered Yes
Recently 9 of 10 people (90%) answered Yes

 

Python Cookbook (lots of great snippets!),  
Entry
Using __init__.py
Jul 5th, 2000 09:59
Nathan Wallace, Hans Nowak, Snippet 27, Andrew Kuchling
"""



"""
Packages: modules_and_packages
"""

"""
Frank McGeough writes:
>I want to define new modules. These reside
>in subdirectories under the PythonPath. They
>seem to require an __init__.py. 

 Terminology note: it's *packages* that reside in
subdirectories, and require an __init__.py file.  Modules are simply
*.py files that reside somewhere along the Python path.  Packages are a
way to group related modules together.

> If I just put a
>blank one in the directory this seems to work
>fine. It seems like this file is to allow general
>definitions that are shared by the module. Is
>this correct? What would typically go in there?

 An empty __init__.py works fine; this simply indicates that
the subdirectory is a package, not just an ordinary directory.  

 'from <package> import *' won't do anything in this simplest
case.  If you want to be able to do 'from <package> import *', 
you must set a variable named __all__ in __init__.py; this variable
must be a list of strings.  In this case, __init__.py could contain
just:

__all__ = ['func1', 'func2', 'var1', 'class1']

'from <package> import *' would then add the objects named func1,
func2, var1, and class1.  (Note that some people consider wanton use
of 'from foo import *' to be poor style.  I'm very hard-line on the
practice, and think that using it is almost always a mistake.)

 Finally, you can put any code you like in __init__.py; it can
precompute complicated variables, import other packages or modules, or do
anything.  For example, if you wanted to look for optional subpackages,
you could code this:
"""

__all__ = []
for subpackage in ['A', 'B', 'C']:
    try: 
 exec 'import ' + subpackage
 __all__.append( subpackage )
    except ImportError:
 pass

"""
 This tries to import each of A,B,C, and, if no ImportError
exception was raised, adds the name to __all__.

 GvR's notes on the package support are available at
http://www.python.org/doc/essays/packages.html
"""

Faqts.com brought to you by PowWeb Inc. 
