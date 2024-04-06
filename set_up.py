from setuptools import find_packages, setup
from typing import List # type: ignore


hyphen_e = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function returns a list of requirements

    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
    
    if hyphen_e in requirements:
        requirements.remove(hyphen_e)

    return requirements

setup(
    name = 'Project Zero',
    version='0.0.1',
    author = 'Abhinay',
    author_email='prasannaabhinayarcot@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')
)