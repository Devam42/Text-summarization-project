import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__="0.0.0"

REPO_NAME = "Text-summarization-project"
AUTHOR_USER_NAME = "Devam42"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "dkathane42@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for NLP app",
    Long_decription=long_description,
    Long_description_content="text/markdown",
    url=f"http://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"http://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",      
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)