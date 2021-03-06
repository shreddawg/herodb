from setuptools import setup, find_packages
setup(
    name = "herodb",
    version = "0.2.9",
    packages = find_packages(exclude="test"),
	install_requires = ['dulwich>=0.8.3', 'bottle>=0.10.9', 'requests>=1.1.0'],
	setup_requires=['nose>=1.0'],
	test_suite = 'nose.collector',
	zip_safe = True,
	
	# metadata for upload to PyPI
	author = "Dave White",
	author_email = "dwhite@yieldbot.com",
	description = "A simple key/value store using git as the backing store.",
	license = "PSF",
	keywords = "git key value store database",
	url = "https://github.com/yieldbot/herodb",
    entry_points={
        'console_scripts': ['herodb_mirror = herodb.mirror:mirror']
    },
)
