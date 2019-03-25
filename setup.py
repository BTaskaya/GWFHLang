from pathlib import Path
from setuptools import setup, find_packages

current_dir = Path(__file__).parent.resolve()

with open(current_dir / 'README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="gwfhlang",
    version="0.1.1",
    packages=find_packages(),
    author="BTaskaya",
    author_email="batuhanosmantaskaya@gmail.com",
    description = "Programming language that runs on ArkheVM",
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url="https://github.com/BTaskaya/GWFHLang"
)
