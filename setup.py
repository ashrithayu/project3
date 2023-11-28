from setuptools import setup, find_packages

setup(
    name='project_3',
    version='0.1',
    packages=find_packages(),
    package_data={'project_3': ['*.ipynb']},
    install_requires=[ 'pandas', 'matplotlib','seaborn' ]
                                
)