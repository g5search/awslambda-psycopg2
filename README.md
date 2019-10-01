psycopg2 Python Library for AWS Lambda
======================================

This is a custom compiled psycopg2 C library for Python. Due to AWS Lambda
missing the required PostgreSQL libraries in the AMI image, we needed to
compile psycopg2 with the PostgreSQL `libpq.so` library statically linked
libpq library instead of the default dynamic link.

### How to use

This project only exists for python 3.7. The subsequent pypi package will only support python 3.7 as well.
It only includes the `with_ssl_support` version. Since that will generally be required for AWS lambda usage.

### Building from source
Go to the original package if you wish to modify this from source

### Usage
Same as normal psycopg2. `import psycopg2` and use related libraries as needed.

### Modifications
If you need to make changes to the import or update the library make sure to test with the docker image
`docker build .` should rebuild the image and test the latest change.


You'll also need to make sure you update the versions in the `Dockerfile` and in the `setup.py`
