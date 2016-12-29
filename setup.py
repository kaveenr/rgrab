import platform
try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
setup(
    name="rgrab",
    version="0.1",
    description="Download Images form reddit sub-reddits",
    keywords=["Reddit", "Image", "Download"],
    author="KaveenR",
    author_email="u.k.k.rodrigo@gmail.com",
    url="http://kaveenrodrigo.com",
    scripts=['rgrab'],
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Environment :: Console",
        "Programming Language :: Python :: 2 :: Only",
        "Topic :: Utilities"]
)
