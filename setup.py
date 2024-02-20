import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tarotNLP",
    version="0.1.0",
    author="David Dockhorn",
    author_email="ddtraveller@yahoo.com",
    description="This is code for playing tarot cards. Each card has a rich set of properties and there are many helpers to assist with associating cards with common symbols or esoteric references. The cards have been scored for positivity and emotions.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ddtraveller/tarot_cards",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)