from setuptools import setup

setup(
    name='Mytest',
    version='1.0',
    description='A useful module',
    author='Govind',
    author_email='example@example.com',
    packages=['mytest'],  #same as name
    data_files=[('mytest', ['mytest/test.csv', 'mytest/test.cfg', 'mytest/test.bin'])]   
)
