import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="porthole",
    version="0.0.1",
    author="emuggie",
    author_email="emuggie@gmail.com",
    description="Simple OS monitoring server and client tool.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/emuggie/porthole",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
    ],
    entry_points = {
        'console_scripts' : [
            'porthole=porthole.script'
        ]
    },
    python_requires='>=2.7',
)