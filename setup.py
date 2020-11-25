import setuptools

setuptools.setup(
    name="fbutils",
    version="0.0.1",
    author="Hamish Gibbs",
    author_email="Hamish.Gibbs@lshtm.ac.uk",
    description="Personal utilities for managinf Facebook Data For Good data.",
    url="https://github.com/hamishgibbs/fbutils_py",
    py_modules=['fbutils'],
    install_requires=[
          'pyquadkey2',
          'shapely'
      ],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
