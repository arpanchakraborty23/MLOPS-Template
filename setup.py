from setuptools import setup,find_packages
from typing import List

Hypen_dot_e='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path,'r') as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/n","") for req in requirements]

        if Hypen_dot_e in requirements:
            requirements.remove(Hypen_dot_e)
    return requirements

__version__='0.0.1'
Repo_name= 'demo'
package_name='demo'
Author='Arpanchakraborty23'
Author_email='arpanchakraborty500@gmail.com'

setup(
    name=package_name,
    version=__version__,
    author=Author,
    author_email=Author_email,
  
    
    long_description_content='text/markdown',
    url=f"https//:github.com/{Author}/{Repo_name}",
    packages=find_packages(),
    install_requries=get_requirements('requirementes.txt')
)
