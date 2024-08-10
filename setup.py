from setuptools import find_packages, setup

setup(
    name= "financebot",
    version="0.0.1",
    author="kiranmai",
    author_email="kiranmaiboda@gmail.com",
    packages=find_packages(),
    install_requries=["langchain","langchain-openai","langchain-astradb","datasets","pypdf","python-dotenv","flask"] 
)