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
    'requests<=2.11.1',
]

setup(
    name='connectwise',
    version='0.0.2a-dev',
    description='Python client library for Connectwise REST API',
    scripts=[],
    url="",
    packages=["connectwise"],
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
                   'Topic :: Internet',
                   ]

)