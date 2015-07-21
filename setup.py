from setuptools import setup, find_packages # Always prefer setuptools over distutils

setup(
    name= 'Gitopen',
    version='1.2.1',
    description="Open your git-remote url in your browser",
    url='https://github.com/guinslym/gitopen',
    author='Guinslym',
    author_email='guinslym@gmail.com',
    py_modules=['gitopen'],
    license='GNU GPLv2',
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'        
    ],
    keywords='git repo repoitory gitbucket',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=[
        'Click',
        'blessings'
        ],
    entry_points='''
        [console_scripts]
        gitopen=gitopen:cli
        ''',       
)
