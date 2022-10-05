from setuptools import find_packages, setup

setup(
    name="ia2",
    packages=find_packages(),
    version="1.0.0",
    description="Anonomiza",
    author="Romi",
    author_email="romailanda@gmail.com",
    url="https://gitlab.com/romailanda/ia2-refactor",
    install_requires=[
        "jsonschema==4.5.1",
        "pre-commit==2.20.0",
        "fire==0.4.0",
        "more-itertools==8.13.0",
        "pandas==1.4.2",
        "matplotlib==3.5.2",
        "seaborn==0.11.2",
    ],
    package_data={"": ["*.yml", "*.yaml"]},
    include_package_data=True,
    classifiers=["Programming Language :: Python :: 3"],
)