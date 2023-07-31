#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
]

extra_requirements = {
    'bsddb3': ["bsddb3"],
}

setup(
    name='pyquicksum',
    version='1.0.0',
    description='Quickly group by and sum up columns',
    long_description=readme + '\n\n' + history,
    author="Steven Willis",
    author_email='onlynone@gmail.com',
    url='https://gitlab.com/onlynone/pyquicksum',
    packages=[
        'quicksum',
    ],
    package_dir={'quicksum':
                 'quicksum'},
    entry_points={
        'console_scripts': [
            'quicksum = quicksum.main:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    extras_require=extra_requirements,
    license="BSD",
    zip_safe=False,
    keywords='quicksum',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
)
