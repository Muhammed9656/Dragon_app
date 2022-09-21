from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in dragon_app/__init__.py
from dragon_app import __version__ as version

setup(
	name="dragon_app",
	version=version,
	description="STUDY",
	author="MUHAMMED",
	author_email="muhammedibnuarif3@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
