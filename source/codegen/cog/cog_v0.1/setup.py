from distutils.core import setup

setup (# Distribution meta-data
       name = "posCog",
       version = "1.0",
       description = "posdata code generation tool",
       py_modules = ['posCog', 'voMain', 'voCommonUtil','cogCommonUtil'] # Description of modules and packages in the distribution
      )