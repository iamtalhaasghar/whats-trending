import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="whatstrending",
    version="0.0.1",
    author="Talha Asghar",
    author_email="talhaasghar.contact@simplelogin.fr",
    description="Python CLI tool to scrap latest twitter trends without using twitter api.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iamtalhaasghar/whats-trending",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=["beautifulsoup4"],
    entry_points={'console_scripts': ['whatstrending = whatstrending:whatstrending.main']},
	
	
)
