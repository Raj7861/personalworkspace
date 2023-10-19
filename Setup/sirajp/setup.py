from setuptools import find_packages, setup

setup(
    include_package_data=True,
    name='sirajp',
    version='0.0.1',
    description='sirajp python module',
    url='',
    author='siraj',
    author_email='siraj@gmail',
    packages=find_packages(),
    install_requires=['pandas', 'pytest'],
    long_description='sirajp python module',
    classifiers=["Programming Language :: Python :: 3", "Operating System :: OS Independent"],
)
