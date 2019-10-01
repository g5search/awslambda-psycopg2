from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name = 'g5-lambda-psycopg2',
  packages = ['g5-lambda-psycopg2'],
  version = '0.1.1',
  license='MIT',
  description = 'Fork of awslambda-psycopg2',
  long_description = long_description,
  long_description_content_type='text/markdown',
  author = 'G5Dev',
  author_email = 'g5dev@g5searchmarketing.com',
  url = 'https://github.com/G5/awslambda-psycopg2',
  download_url = 'https://github.com/G5/awslambda-psycopg2/archive/master.zip',
  keywords = ['aws', 'lambda', 'psycopg2'],
  install_requires=[],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
  ],
)
