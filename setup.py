"""
setup.py of this project
"""
from setuptools import setup


setup(
    name='pd_multiprocessing',
    version='1.0.1',
    uthor='Kyriakos Stavrakidis',
    author_email='kstavrakidis@gmail.com',
    description='Simple function to parallelize the mapping function of Pandas DataFrame',
    long_description=open('README.rst').read(),
    url='https://github.com/stavrakidis/pd_multiprocessing',
    license='LICENSE.txt',
    packages=['pd_multiprocessing', 'pd_multiprocessing.test'],
    install_requires=[
        'pandas>=0.22.0',
        'pytest>=3.4.1'
    ],
)
