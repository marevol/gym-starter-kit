#!/usr/bin/env python

from setuptools import setup

setup(
    name="gym-starter-kit",
    version="0.0.3",
    packages=['gymkit',
              'gymkit.agent'],
    author="Shinsuke Sugaya",
    author_email="shinsuke@yahoo.co.jp",
    license="Apache Software License",
    description=("Gym Starter Kit: A running environment for developing OpenAI Gym agents."),
    keywords="machine learning",
    url="https://github.com/marevol/gym-starter-kit",
    download_url='https://github.com/marevol/gym-starter-kit/tarball/0.0.3',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache Software License",
    ],
    install_requires=[
        'gym>=0.7.0'
    ],
    entry_points={
        "console_scripts": [
            "gym-start=gymkit:main",
        ],
    },
)
