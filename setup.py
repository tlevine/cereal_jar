from distutils.core import setup

from jar import __version__

setup(name='jar',
      author='Thomas Levine',
      author_email='_@thomaslevine.com',
      description='Save things in [cookie] jar format',
      url='https://github.com/tlevine/jar',
      packages=['jar'],
      install_requires = [],
      tests_require = ['nose'],
      version=__version__,
      license='AGPL',
)
