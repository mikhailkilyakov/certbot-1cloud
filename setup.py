from setuptools import setup
from setuptools import find_packages

from certbot_1cloud import __version__

install_requires = [
    'acme>=0.29.0',
    'certbot>=0.39.0',
    'requests>=2.22.0',
    'mock',
    'setuptools',
    'zope.interface'
]

data_files = [
    ('/etc/letsencrypt', ['1cloud.ini'])
]

with open('README.md', 'r') as f:
    full_description = f.read()

setup(
    name='certbot-1cloud',
    version=__version__,
    description='1cloud DNS authenticator plugin for Certbot',
    full_description=full_description,
    author='Mikhail Kilyakov',
    author_email='mikhail.kilyakov@gmail.com',
    license='MIT',
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    classifiers=[
        'Environment :: Plugins',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Security',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Networking',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],
    install_requires=install_requires,
    data_files=data_files,
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'certbot.plugins': [
            'dns = certbot_1cloud.dns:Authenticator'
        ]
    },
    test_suite='certbot_1cloud'
)
