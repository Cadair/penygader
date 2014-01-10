from setuptools import setup, find_packages
setup(
    name = "penygader",
    version = "0.1",
    packages = find_packages(),

    install_requires = ['matplotlib>1.3'],

    # metadata for upload to PyPI
    author = "Stuart Mumford",
    description = "Cadair's top collection of tools",
    license = "BSD",
    url = "http://github.com/Cadair/penygader",   # project home page, if any
)
