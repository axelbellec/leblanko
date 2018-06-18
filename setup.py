from setuptools import setup, find_packages

to_exclude = ["leblanko.cli", "tests"]

setup(
    name="Leblanko",
    version="0.1",
    description="Simple CLI tool to extract table names from SQL query files.",
    author="Axel Bellec",
    author_email="axel.bellec@outlook.fr",
    packages=find_packages(exclude=to_exclude),
    include_package_data=True,
    entry_points={"console_scripts": ["leblanko = leblanko.cli:main"]},
    zip_safe=False,
)
