from setuptools import setup, find_packages

setup(
    name="lluminate-llamasearch",
    version="0.1.0",
    description="A powerful tool for working with lluminate data",
    author="LlamaSearch AI",
    author_email="nikjois@llamasearch.ai",
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
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)

# Updated in commit 5 - 2025-04-04 17:41:25

# Updated in commit 13 - 2025-04-04 17:41:26

# Updated in commit 21 - 2025-04-04 17:41:26

# Updated in commit 29 - 2025-04-04 17:41:26

# Updated in commit 5 - 2025-04-05 14:41:50

# Updated in commit 13 - 2025-04-05 14:41:50
