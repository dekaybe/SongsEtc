import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='ArtistSongsLyrics',  
     version='0.4',
     author="Dave Brown",
     author_email="dave.k.flowers@gmail.com",
     description="Oooo the way you move me baby",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/dekaybe/SongsEtc",
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     package_dir={"": "src"},
     packages=setuptools.find_packages(where="src"),
     python_requires=">=3.6",
 )
