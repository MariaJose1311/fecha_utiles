from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="fecha-utils",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    author="Maria Jose Suarez",
    author_email="mariajosesuarez013@gmail.com",
    description="Una librería para operaciones con fechas",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MariaJose1311/fecha_utils",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
