from setuptools import setup

#to get all info and description of the project we are reading the README file
with open("README.md","r",encoding="utf-8") as fh:
    long_description=fh.read()

AUTHOR_NAME='NOYONIKA MUKHERJEE'
SRC_REPO='src' #define my local package name
LIST_OF_REQUIREMENTS=['streamlit']

setup(
    name=SRC_REPO,
    version='0.0.1',
    author=AUTHOR_NAME,
    author_email='noyonikacarmel@gmail.com',
    description='A small package for movies recommendation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    #url='give url of your project eg if you have committed to GITHUB'
    package=[SRC_REPO],
    python_requires='>=3.7',
    install_requires=LIST_OF_REQUIREMENTS,
)