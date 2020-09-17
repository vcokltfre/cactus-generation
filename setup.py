from distutils.core import setup

setup(
        name="cactus-generation",
        version="1.0",
        description="Singlechunk Minecraft cactus generation in Python",
        long_description=open("README.md").read(),
        author="vcokltfre",
        author_email="vcokltfre@gmail.com",
        url="http://github.com/vcokltfre/cactus-generation",
        py_modules=[
            "cactus",
            ],
        )