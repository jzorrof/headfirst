from distutils.core import setup
'''
settings
1.python3 setup sdist
2.sudo python3 setup install
'''
setup(
        name = 'nester',
        version = '1.3.0',
        py_modules = ['nester'],
        author = 'Joe',
        author_email = 'jzorrof@gmail.com',
        url = 'http://fanzhong.me',
        description = 'A simple printer of nested lists',
    )
