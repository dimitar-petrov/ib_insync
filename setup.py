import os
import sys
import codecs
from setuptools import setup

if sys.version_info < (3, 6, 0):
    raise RuntimeError("ib_insync requires Python 3.6 or higher")

here = os.path.abspath(os.path.dirname(__file__))
with codecs.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ib_insync',
    version='0.8.2',
    description='Python sync/async framework for Interactive Brokers API',
    long_description=long_description,
    url='https://github.com/erdewit/ib_insync',
    author='Ewald R. de Wit',
    author_email='ewald.de.wit@gmail.com',
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Office/Business :: Financial :: Investment',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='ibapi asyncio jupyter interactive brokers async',
    packages=['ib_insync']
)
