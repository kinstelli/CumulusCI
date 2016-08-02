from setuptools import setup

setup(
    name='cumulusci',
    version='2.0-prealpha',
    py_modules=['cumulusci'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        cumulusci=cli.cumulusci:cli
        cumulusci2=newcli.cumulusci:cli
    ''',
)
