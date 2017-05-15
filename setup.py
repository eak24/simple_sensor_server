from setuptools import setup

setup(name='simple_sensor_server',
      version='0.0.0dev',
      description='A server with temperature readings',
      long_description=open('README.md').read(),
      url='https://github.com/ethan92429/simple_sensor_server',
      author='Maelstrom Mining',
      author_email='maelstrommining@gmail.com',
      license='MIT',
      packages=['simple_sensor_server'],
      install_requires=[
          'flask', 'w1thermsensor'
      ],
      zip_safe=False)