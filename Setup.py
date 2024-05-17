from setuptools import find_packages,setup
from typing import List

Hypen_e_dot='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open("requirements.txt") as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/n"," ")for req in requirements]
        
        if Hypen_e_dot in requirements:
            requirements.remove(Hypen_e_dot)
    return requirements
setup(
name='mlproject',
version='0.0.1',
author='ayush',
author_email='ayushpoonmia2003@gmail.com',
pakages=find_packages(),
install_requires=get_requirements('requirements.txt')
)