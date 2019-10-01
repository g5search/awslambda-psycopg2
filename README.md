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
