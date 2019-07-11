from setuptools import find_packages, setup

with open('bsvbip32/__init__.py', 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.strip().split('= ')[1].strip("'")
            break

setup(
    name='bsvbip32',
    version=version,
    description='BIP32 Hierarchical Deterministic wallet functions - extends bitsv.',
    long_description=open('README.rst', 'r').read(),
    author='AustEcon',
    author_email='AustEcon0922@gmail.com',
    maintainer='AustEcon',
    maintainer_email='AustEcon0922@gmail.com',
    url='https://github.com/AustEcon/bsvbip32',
    download_url='https://github.com/AustEcon/bsvbip32/tarball/{}'.format(version),
    license='MIT',

    keywords=[
        'bitcoinsv',
        'bsv',
        'bitcoin sv',
        'cryptocurrency',
        'payments',
        'tools',
        'wallet',
        'bip32',
        'bitsv'
    ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
    ],

    install_requires=['coincurve>=4.3.0', 'requests', 'cashaddress==1.0.4', 'pycoin==0.80', 'bitcoinx'],
    extras_require={
        'cli': ('appdirs', 'click', 'privy', 'tinydb'),
        'cache': ('lmdb', ),
    },
    tests_require=['pytest'],

    packages=find_packages(),
    entry_points={},
)
