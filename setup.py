from setuptools import setup, find_packages
import hubo


setup(
    name='hubo',
    version=hubo.__version__,
    packages=find_packages(exclude=['*.tests']),
    scripts=[],

    install_requires=[
        'pillow', 'easygui',
    ],

    author='lordpeara',
    author_email='lordpeara@gmail.com',
    description='hubo\'s playground for softlangding python',
    license='GPL',
    keywords='',
    url='http://github.com/lordpeara/hubo',

    zip_safe=False,
    include_package_data=True,

    classifiers=[],
)
