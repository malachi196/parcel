from setuptools import setup, find_packages
setup(
    name='parcel',
    version='1.0.0',
    author='@malachi196',
    author_email='malachiaaronwilson@gmail.com',
    description='Parcel is a python module made for the purpose of "Packaging Python Programs Properly". Creation rights go to @malachi196 on github',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)