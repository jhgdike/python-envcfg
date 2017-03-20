from setuptools import setup, find_packages


setup(
    name='python-envcfg',
    version='0.0.1',
    author='Tao Wang',
    author_email='jhgdike@gmail.com',
    description='Accessing environment variables with a portable function.',
    platforms=['Any'],
    url='https://github.com/jhgdike/python-envcfg',
    license='MIT',
    packages=find_packages(),
    keywords=['env', 'config'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries',
    ]
)
