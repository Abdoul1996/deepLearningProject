from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    Reads the requirements file and returns a list of requirements.

    Args:
    file_path (str): Path to the requirements file.

    Returns:
    List[str]: A list of requirements.
    """
    requirements = []
    with open(file_path, "r") as file_obj:
        for line in file_obj:
            # Remove whitespace and ignore comments
            req = line.strip()
            if req and not req.startswith("#"):  # Skip empty lines and comments
                requirements.append(req)

        # Exclude '-e .' from the requirements list
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name="Xray",
    version="0.0.1",
    author="Abdoul Abdillahi",
    author_email="aabdillahid@gmail.com",
    install_requires=get_requirements("requirements_dev.txt"),  # Requirements file
    packages=find_packages(),
)
