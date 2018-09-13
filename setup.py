from setuptools import setup

setup(
    name='Open API specification editor',
    version='0.1.0',
    py_modules=['oas'],
    install_requires=[
        'Click',
        'PyYaml'
    ],
    entry_points='''
        [console_scripts]
        oas-edit=oasedit:cli
    ''',
)
