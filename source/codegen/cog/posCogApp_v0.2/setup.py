from distutils.core import setup
setup(
    name = 'posCog',
    version = '1.0',
    url = 'http://xxx.com/cog',
    author = 'kusung',
    author_email = 'kusung@xxx.com',
    description =
        'posdata code generation tool: A code generator for executing Python snippets in source files.',

    packages = [
        'posCogApp',
        ],

    scripts = [
        'scripts/test_posCogApp.py',
        ],
    )