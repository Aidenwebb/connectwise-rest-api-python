import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.version_info <= (2, 4):
    error = 'Requires Python Version 2.5 or above... exiting'
    print >> sys.stderr, error
    sys.exit(1)

with open("README.rst", "r") as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as f:
    requirements = f.read()

with open('test_requirements.txt', 'r') as f:
    test_requirements = f.read()

setup(
    name='pyRESTcw',
    version='0.0.13',
    packages=['test', 'connectwise', 'connectwise.time', 'connectwise.time.entries',
              'connectwise.company',
              'connectwise.company.contacts', 'connectwise.company.companies',
              'connectwise.company.configurations',
              'connectwise.service', 'connectwise.service.boards', 'connectwise.service.tickets',
              'connectwise.service.boardstatuses', 'connectwise.service.priorities'],
    description='Python client library for Connectwise REST API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    scripts=[],
    url="https://github.com/Aidenwebb/connectwise-rest-api-python",
    licence="Apache 2.0",
    platforms="Posix; MacOS X; Windows",
    setup_requirements=requirements,
    install_requirements=requirements,
    tests_require=test_requirements,
    classifiers=['Development Status :: 3 - Alpha',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: Apache Software License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.2',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.6',
                 'Topic :: Internet',
                 ]
)
