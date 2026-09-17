from setuptools import setup, find_packages

setup(
    name="fs_tools",
    version="1.0.0",
    author="Ildar Bikmamatov",
    author_email="ildar@bayrell.org",
    description="Filesystem tools and MCP",
    packages=find_packages(),
    python_requires=">3.8",
    install_requires=[
        "mcp>=2.0"
    ],
    scripts=[
        "bin/fs_tools",
    ]
)