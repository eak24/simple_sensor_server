from setuptools import setup

setup(name='thermograph',
      version='0.0.0dev',
      description='A server with temperature readings',
      long_description=open('README.md').read(),
      url='https://github.com/ethan92429/ThermoGraph',
      author='Maelstrom Mining',
      author_email='maelstrommining@gmail.com',
      license='MIT',
      packages=['thermograph'],
      install_requires=[
          'flask', 'w1thermsensor'
      ],
      zip_safe=False)