"""
    DFIRTrack

    OpenAPI 3 - Documentation of DFIRTrack API  # noqa: E501

    The version of the OpenAPI document: v2.0.0
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "dfirtrack-api-client"
VERSION = "2.2.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="DFIRTrack",
    author="OpenAPI Generator community",
    author_email="team@openapitools.org",
    url="https://github.com/dfirtrack/dfirtrack-api-python-client",
    keywords=["OpenAPI", "OpenAPI-Generator", "DFIRTrack"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    OpenAPI 3 - Documentation of DFIRTrack API  # noqa: E501
    """
)
