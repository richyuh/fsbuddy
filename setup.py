from setuptools import setup

setup(
    name="filesystemcleaner",
    version="0.1.0",
    entry_points={
        "console_scripts": [
            "fscleaner=main:main",
        ]
    },
    python_requires=">=3.8",
)
