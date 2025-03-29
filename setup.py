from setuptools import setup, find_packages

setup(
    name="lluminate",
    version="0.1.0",
    description="A powerful tool for working with lluminate data",
    author="LlamaSearch AI",
    author_email="info@llamasearch.ai",
    url=f"https://github.com/hypocrite/lluminate",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.0",
        "numpy>=1.19.0",
        "pandas>=1.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "black>=20.8b1",
            "flake8>=3.8.0",
        ],
    },
)
