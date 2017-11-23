from setuptools import setup

setup(
    name='cabinboy',
    version='0.1.0',
    description='run tasks in your code base with astounding easiness.',
    url='https://github.com/parisk/cabinboy',
    author='Paris Kasidiaris',
    author_email='paris@sourcelair.com',
    license='MIT',
    entry_points={
        'console_scripts': ['cb=cb:run'],
    },
    install_requires=[
        'pyyaml==3.12',
        'delegator.py==0.0.13',
        'crayons==0.1.2',
        'click==6.7',
    ]
)
