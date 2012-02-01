
from setuptools import setup, find_packages

REQUIREMENTS = (
    'django>=1.3',
)

from djbootstrap import VERSION

setup(
    name="djbootstrap",
    version=VERSION,
    author="Aaron Madison",
    description="Kickstart your django app with twitter bootstrap.",
    long_description=open('README', 'r').read(),
    url="https://github.com/madisona/djbootstrap",
    packages=find_packages(exclude=["example"]),
    include_package_data=True,
    install_requires=REQUIREMENTS,
    zip_safe=False,
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
)
