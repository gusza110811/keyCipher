from setuptools import setup, find_packages

setup(
    name='keyCipher',
    version='0.1',
    packages=find_packages(),
    description='A Python library for key-based encoding and decoding.',
    long_description=open('README.md').read() + ", no longer description available",
    license='GNU',
    author='Gusza1108 / Gusza110811 / Sarunphat',
    author_email='auguz1108@email.com',
    url='https://github.com/gusza110811/keyCipher',
    keywords=['encryption', 'decryption', 'key-based'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU License',
        'Operating System :: OS Independent',
    ],
)
