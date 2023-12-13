#WRITTEN BY: Ted Charles Brown
#ONLY FOR USE WITH PYPI

# IN PARENT DIRECTORY TO API
# python setup.py sdist bdist_wheel
# twine upload dist/*

from setuptools import setup, find_packages

setup(
    name='PixeraPy',
    version='0.367.2',
    packages=find_packages(),
    description='Python package for AVStumpfl, Pixera API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Tedcharlesbrown/Pixera-TCB/tree/main/01-Custom/03-API',
    author='Ted Charles Brown',
    author_email='tedcharlesbrown@gmail.com',
    license='MIT',
    install_requires=[
        "requests"
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)