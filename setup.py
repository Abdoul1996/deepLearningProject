from setuptools import find_packages, setup 

def get_requirements(file_path:str)->List[str]:
     """
    Reads the requirements file and returns a list of requirements.

    Args:
    file_path (str): Path to the requirements file.

    Returns:
    List[str]: A list of requirements.
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements 

setup(
    name="Xray",  # Name of your project
    version="0.0.1",  # Version number
    author="Abdoul Abdillahi",  # Author's name
    author_email="aabdillahid@gmail.com",  # Author's email
    install_requires=get_requirements(),  # Requirements file
    packages=find_packages()  # Automatically find all packages in the project
)