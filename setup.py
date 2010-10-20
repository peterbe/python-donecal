from setuptools import setup, find_packages
import sys, os

version = '0.2'
long_description = open('README.md').read().strip() + "\n\n"
def md2stx(s):
    import re
    s = re.sub(':\n(\s{8,10})', r'::\n\1', s)
    return s
long_description = md2stx(long_description)
            

setup(name='python-donecal',
      version=version,
      description="Python interface for the donecal.com restful HTTP API",
      long_description=long_description,
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='donecal rest api donecal.com',
      author='Peter Bengtsson',
      author_email='mail@peterbe.com',
      url='http://donecal.com/help/API#Python',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'anyjson',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
