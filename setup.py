from setuptools import setup, find_packages
import os

setup(
    name="DSSS_Homework_2",  
    version="0.1",
    packages=find_packages(),
    install_requires=["numpy","matplotlib"],  
    description="A short description of your package",
    long_description=open("README.md").read() if os.path.isfile("README.md") else "",
    long_description_content_type="text/markdown",
    author="Meenal",
    author_email="meenal.baberwal@fau.de",
    url="https://github.com/meenal30-stack/DSSS_Homework_2.git",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
