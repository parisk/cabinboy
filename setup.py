from setuptools import setup
from setuptools import find_packages

setup(
    name='cabinboy',
    version='0.2.0',
    description='run tasks in your code base with astounding easiness.',
    url='https://github.com/parisk/cabinboy',
    author='Paris Kasidiaris',
    author_email='paris@sourcelair.com',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['cb=cabinboy.cli:run'],
    },
    install_requires=[
        'pyyaml==3.12',
        'delegator.py==0.0.13',
        'crayons==0.1.2',
        'click==6.7',
    ]
)
