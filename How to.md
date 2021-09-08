# Installing from PyPI
The most common usage of 'pip' is to install from the Python Package Index using a requirement specifier.
Generally speaking, a requirement specifier is composed of a project name followed by an optional version
specifier. PEP 440 contains a full specification of the currently supported specifiers.

Examples:
To install the latest version of “SomeProject” on Windows
$ py -m pip install "SomeProject"

A specific version:
$ py -m pip install "SomeProject==1.4"

Install greater than or equal to one version and less than another:
$ py -m pip install "SomeProject>=1,<2"
To install a version that's “compatible” with a certain version
$ py -m pip install "SomeProject~=1.4.2"
In this case, this means to install any version “==1.4.*” version that’s also “>=1.4.2”.


# Source Distributions vs Wheels
'pip' can install from either Source Distributions (sdist) or Wheels, but if both are present on
PyPI, 'pip' will prefer a compatible wheel. You can override pip`s default behavior by e.g. using its –no-binary option.

Wheels are a pre-built distribution format that provides faster installation compared to Source Distributions (sdist),
especially when a project contains compiled extensions.

If 'pip' does not find a wheel to install, it will locally build a wheel and cache it for future installs, instead of rebuilding the source distribution in the future.

# Upgrading packages
Upgrade an already installed SomeProject to the latest from PyPI.
$ py -m pip install --upgrade SomeProject
Installing to the User Site
To install packages that are isolated to the current user, use the --user flag:
$ py -m pip install --user SomeProject

Note: '--user' flag has no effect when inside a virtual environment - all installation commands will affect the virtual environment.