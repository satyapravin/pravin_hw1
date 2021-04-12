import os

from setuptools import find_packages, setup


def read(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        return file.read()


def parse_requirements():
    """Parse requirements.txt for install_requires"""
    requirements = read('requirements.txt')
    return tuple(requirements.split('\n'))


setup(
    name='project_test',
    packages=find_packages(exclude=('tests', )),
    python_requires='~=3.7',
    install_requires=parse_requirements(),
)
