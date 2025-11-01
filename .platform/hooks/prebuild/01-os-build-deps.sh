#!/bin/bash
set -e
# Essential compilers/headers for many Python wheels (cryptography, numpy/scipy fallbacks, etc.)
yum install -y gcc gcc-c++ make
yum install -y libffi-devel openssl-devel
# If you use psycopg2 or similar:
# yum install -y postgresql-devel