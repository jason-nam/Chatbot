"""
Setup package file
"""

from setuptools import setup

setup(
    name="chatbot",
    version="0.1",
    install_requires=[
        "numpy",
        "matplotlib",
        "pandas",
        "pyyaml",
        # "unittest",
        "tensorflow",
        "tensorflow_datasets",
    ],
    extras_require={
        "convokit": ["convokit"],
        "tensorflow with gpu": ["tensorflow-gpu"],
    },
)