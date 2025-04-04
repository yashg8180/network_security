'''
this fiel is essential part of packing and 
distributui python project .it is used by setuptools 
(or distutiliin older python versions ) to defient the configuration
of your project such as its metadata dependencies and more
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    this function will return list of requirements
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            # read lines
            lines=file.readlines()
            # process each line
            for line in lines:
                requirement=line.strip()
                # ignore empty and -e .
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

# print(get_requirements())
setup(
    name="networksecurity",
    version="0.0.1",
    author="YASH",
    author_email="xyz@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()

)