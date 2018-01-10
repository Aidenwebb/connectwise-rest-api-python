import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.version_info <= (2, 4):
    error = 'Requires Python Version 2.5 or above... exiting'
    print >> sys.stderr, error
    sys.exit(1)


requirements = [
    'certifi==2017.7.27.1',
    'chardet==3.0.4',
    'idna==2.6',
    'requests==2.18.4',
    'urllib3==1.22',
]

setup(
    name='pyRESTcw',
    version='0.0.9a-dev',
    packages=['test', 'connectwise', 'connectwise.time', 'connectwise.time.entries', 'connectwise.company',
              'connectwise.company.contacts', 'connectwise.company.companies', 'connectwise.company.configurations',
              'connectwise.service', 'connectwise.service.boards', 'connectwise.service.tickets',
              'connectwise.service.boardstatuses', 'connectwise.service.priorities'],
    description='Python client library for Connectwise REST API',
    scripts=[],
    url="",
    licence="Apache 2.0",
    platforms="Posix; MacOS X; Windows",
    setup_requirements = requirements,
    install_requirements = requirements,
classifiers=['Development Status :: 5 - Alpha',
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