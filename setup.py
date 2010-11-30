#from setuptools import setup, find_packages
from setuptools import setup
import sys, os

version = '0.2.4'
#here = os.path.dirname(__file__)
#def read(fname):
#    return open(os.path.join(os.path.dirname(__file__), fname)).read()
#def md2stx(s):
#    import re
#    s = re.sub(':\n(\s{8,10})', r'::\n\1', s)
#    return s

setup(name='python-donecal',
      version=version,
      description="Python interface for the donecal.com restful HTTP API",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='donecal rest api donecal.com',
      author='Peter Bengtsson',
      author_email='mail@peterbe.com',
      url='http://donecal.com/help/API#Python',
      license='BSD',
      packages=[
        'donecal',
      ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'anyjson',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
