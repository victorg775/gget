from setuptools import setup, find_packages

long_description = read('README.md')

setup(
    name='gget',
    version='0.0.1',
    license='MIT',
    author='Laura Luebbert',
    author_email='lauraluebbert@caltech.edu',
    description='Query Ensembl for genes using free form search words (gget search) or fetch FTP download links by species (gget FetchTP).',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author_email='email@example.com',
    packages=find_packages(),
    url='https://github.com/lauraluebbert/gget',
    keywords='gget',
)
