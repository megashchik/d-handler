from xml.etree.ElementInclude import include
from setuptools import setup, find_packages


setup(
    name='d-handler',
    version='0.0.1',
    description='simple util to create and control processes',
    long_description='simple util to create and control processes',
    packages=find_packages(),
    url='https://github.com/megashchik/daemon-handler',
    author='Ivan Chizhikov',
    author_email='megashchik@gmail.com',
    license='Apache 2 License'
)