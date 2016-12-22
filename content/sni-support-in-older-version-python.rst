:title: SNI support in older version python
:slug: sni-support-in-older-version-python
:date: 2016-09-10 22:07:44
:tags: 
:category: Python
:author: arul
:lang: en
:summary: 
:status: draft
:disqus_identifier: python-sni-support-in-older-version-python

.. code-block:: text

    /usr/local/lib/python2.7/dist-packages/pip/_vendor/requests/packages/urllib3/util/ssl_.py:318: SNIMissingWarning: An HTTPS request has been made, but the SNI (Subject Name Indication) extension to TLS is not available on this platform. This may cause the server to present an incorrect TLS certificate, which can cause validation failures. You can upgrade to a newer version of Python to solve this. For more information, see https://urllib3.readthedocs.org/en/latest/security.html#snimissingwarning.

      SNIMissingWarning


    /usr/local/lib/python2.7/dist-packages/urllib3/util/ssl_.py:334: SNIMissingWarning: An HTTPS request has been made, but the SNI (Subject Name Indication) extension to TLS is not available on this platform. This may cause the server to present an incorrect TLS certificate, which can cause validation failures. You can upgrade to a newer version of Python to solve this. For more information, see https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings

      SNIMissingWarning
      

    python 2.7.9 and newer has support

    pip install urllib3[secure]

    https://urllib3.readthedocs.io/en/latest/user-guide.html#ssl-py2


         #include <Python.h>
                            ^
        compilation terminated.
        error: command 'x86_64-linux-gnu-gcc' failed with exit status 1


    sudo apt-get install python-dev




        c/_cffi_backend.c:15:17: fatal error: ffi.h: No such file or directory
         #include <ffi.h>
                         ^
        compilation terminated.
        error: command 'x86_64-linux-gnu-gcc' failed with exit status 1


    sudo apt-get install libffi-dev


    linux-x86_64-2.7/_openssl.c -o build/temp.linux-x86_64-2.7/build/temp.linux-x86_64-2.7/_openssl.o
        build/temp.linux-x86_64-2.7/_openssl.c:433:30: fatal error: openssl/opensslv.h: No such file or directory
         #include <openssl/opensslv.h>
                                      ^
        compilation terminated.
        error: command 'x86_64-linux-gnu-gcc' failed with exit status 1


    Command "/usr/bin/python -u -c "import setuptools, tokenize;__file__='/tmp/pip-build-SaV3BZ/cryptography/setup.py';exec(compile(getattr(tokenize, 'open', open)(__file__).read().replace('\r\n', '\n'), __file__, 'exec'))" install --record /tmp/pip-6rPu7I-record/install-record.txt --single-version-externally-managed --compile" failed with error code 1 in /tmp/pip-build-SaV3BZ/cryptography/
    ubuntu@ip-172-31-4-94:~$ sudo apt-get install libssl-dev
