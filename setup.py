from setuptools import setup, find_packages

setup(
    name='nooCrypto',
    version='1.0.4',
    url='https://github.com/noosphere-tech/nooCrypto',  # Optional
    author='Noosphere Foundation',  # Optional
    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    packages=find_packages(),  # Required
    install_requires=['coincurve', 'PyQt5', 'cryptography'],  # Optional
)
