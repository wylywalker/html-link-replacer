from setuptools import setup, find_packages

setup(
    name="html-link-replacer",
    version="1.0.0",
    description="A GUI application for replacing links in HTML content",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "tkinter",
    ],
    entry_points={
        "console_scripts": [
            "html-link-replacer=html_link_replacer:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
) 