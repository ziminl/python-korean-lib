from setuptools import setup

setup(
    name='pyhangul',
    version='1.0.0',
    description='A Python library for Hangul processing',
    author='z',
    author_email='ziminl@ziminl.com',
    url='https://github.com/ziminl/python-korean-lib',
    packages=['hangul4deno'],
    install_requires=[
        'numpy',
        'pandas'
    ],
)
