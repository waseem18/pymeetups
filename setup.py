import os
from setuptools import setup, find_packages


setup(
    name = "pymeetups",
    version = "1.1.1",
    author = "Wasim Thabraze",
    author_email = "wasim@thabraze.me",
    description = "Find information about future Pycon conferences and meetups through your terminal",
    license = "MIT",
    keywords = "pymeetups",
    install_requires = ['Click',
                        'google-auth-httplib2',
                        'google-api-python-client',
                        'texttable'
                        ],
    url = "https://github.com/waseem18/pymeetups",
    packages=find_packages(include=['pymeetups']),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'pymeetups=pymeetups.cli:main',
        ],
    },
    long_description="Find information about future Pycon conferences and meetups through your terminal",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python :: 3.5',
    ],
)
