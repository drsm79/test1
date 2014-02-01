from setuptools import setup
import os

buildnum = os.environ.get('TRAVIS_BUILD_NUMBER', 'local')

setup(
    name='test1',
    version='1.1.{0}'.format(buildnum),
    description='Test 2',
    author_email='simon@cloudant.com',
    long_description=__doc__,
    packages=['test1'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'test1 = test1.bar:bar'
        ]
    }
)
