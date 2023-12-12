from setuptools import setup, find_packages

setup(
    name="Gun_Violence",  
    version="0.1.0",  
    author="Manoj Kumar Singade",  
    author_email="msingade@mail.yu.edu",  
    description="This project conducts a detailed analysis of gun violence incidents across the United States and examines their correlation with firearm background checks, aiming to unearth patterns and inform policy decisions.",  
    long_description=open("Readme.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Manojkumar8899/testingfinalproject",  
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
        "pandas>=1.2.0",
        "beautifulsoup4>=4.9.3",
        "numpy>=1.20.0",
        "matplotlib>=3.3.4",
        "seaborn>=0.11.1",
        "scipy>=1.6.0",
    ],
    python_requires=">=3.6",  # Minimum Python version required

    # Additional metadata for PyPI
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
