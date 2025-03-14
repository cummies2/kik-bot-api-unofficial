from codecs import open
from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

setup(
    name='kik_unofficial',
    version='0.4',
    description='Python API for writing unoffical kik bots that act like humans',
    # long_description="",
    url='https://github.com/tomer8007/kik-bot-api-unofficial',
    download_url="https://github.com/tomer8007/kik-bot-api-unofficial/tarball/master",
    author='Tomer',
    author_email='tomer8007@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ],
    keywords=['kik', 'bot', 'kikbot', 'kik-messenger-platform', 'api', 'unofficial', 'python',],
    packages=find_packages(exclude=['docs', 'test']),
    install_requires=[
        'pbkdf2', 'rsa', 'lxml', 'bs4', 'protobuf>=4.21.0', 'requests', 'pillow', 'pyDes',
    ],
    extras_require={
        'dev': [],
        'test': [],
    },
    package_data={
        'kik_unofficial': [],
    },
    entry_points={
        'console_scripts': [
            'kikapi=kik_unofficial.cmdline:execute',
        ],
    },
)
