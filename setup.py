from setuptools import setup

setup(
    name='palletize',
    version='0.1.2',
    description='Extract dominant colors from image using K-means',
    url='https://github.com/despawnerer/palletize',
    author='Aleksei Voronov',
    author_email='despawn@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    python_modules=['palletize'],
    scripts=['bin/palletize'],
    install_requires=[
        'numpy>=1.11',
        'scipy>=0.18',
        'pillow>=3.0'
    ]
)
