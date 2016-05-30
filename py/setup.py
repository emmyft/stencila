'''
Setup script for the Stencila Python package.

To create binary package wheel:
    python setup.py bdist_wheel

The Python Packaging User Guide recommends using setuptools and bdist_wheel (
https://python-packaging-user-guide.readthedocs.org/en/latest/current.html)
'''
import subprocess
from setuptools import setup, Extension

setup(
    name='stencila',
    version=subprocess.check_output('../version.sh', shell=True),

    author='Nokome Bentley',
    author_email='nokome@stenci.la',

    url='http://stenci.la',
    license='GPLv3',

    packages=[
        'stencila'
    ],

    ext_modules=[
        Extension(
            'stencila.extension',
            sources=[
                'stencila/extension.cpp',

                'stencila/component.cpp',
                'stencila/context.cpp',
                'stencila/sheet.cpp',
                'stencila/spread.cpp',
                'stencila/stencil.cpp',
            ],
            include_dirs=[
                '../cpp',
                '../cpp/requires/boost',
                '../cpp/requires/websocketpp'
            ],
            extra_compile_args=[
                '--std=c++11', '-Wno-unused-local-typedefs'
            ],
            library_dirs=[
                '../cpp/library',
                '../cpp/requires/boost/lib'
            ],
            libraries=[
                'stencila',
                'boost_python',
                'ssl',
                'curl'
            ]
        ),
    ],

    scripts=[
        'scripts/stencila-py'
    ]
)
