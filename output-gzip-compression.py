#!/usr/bin/python3
"""AWS S3 Gzip compression utility."""

import os
import sys
import gzip
import shutil
import hashlib
import logging


"""
AWS S3 Gzip compression utility

Author: Dmitriy Sukharev
Modified: 2013-09-11
-------

Synchronizes directory with gzipped content of Amazon S3 bucket with local
one to avoid redundant synchronization requests when files were not changed,
but MD5 sums of Gzipped files are different. This script is part of article
http://sukharevd.net/gzipping-website-in-amazon-s3-bucket.html
"""

"""
Algorithm:
  Precondition: last compressed publication is in the last_publication
                directory, sha512sum is in file sha512.digest
  1. Read sha512.digest into dictionary
  2. For each file in output directory:
     -- If sha512 differ or dictionary doesn't contain hash sum, update
        last_publication directory with gzipped version of the file.
  3. Rewrite sha512.digest
"""

if len(sys.argv) != 3:
    logging.error(f"Usage: {sys.argv[0]} <output_dir> <publication_dir>")
    sys.exit(0)

OUTPUT_DIR = sys.argv[1]
PUBLICATION_DIR = sys.argv[2]
HASH_SUM_FILE = sys.argv[2] + "/SHA512SUM"
GZIPPED_EXTENSIONS = ("html", "js", "css", "xml")


def read_hash_codes(filename):
    """Read Hash Codes."""
    hashes_dict = {}
    try:
        with open(filename, encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                split = line.split()
                assert len(split) == 2
                hashes_dict[split[1]] = split[0]
            file.close()
            return hashes_dict
    except Exception:
        return {}


def update_gzipped_publications(output_dir, publication_dir):
    """Update Gzipped Publications."""
    for root, _subs, files in os.walk(output_dir):
        for f in files:
            filename = os.path.join(root, f)
            relpath = os.path.relpath(filename, output_dir)

            if relpath.endswith(GZIPPED_EXTENSIONS):
                # can be a problem if files are big:
                current_hash = hashlib.sha512(
                    open(filename, encoding="utf-8").read().encode("utf-8")
                ).hexdigest()
                if not (relpath in hashes and hashes[relpath] == current_hash):
                    publicated_file = os.path.join(publication_dir, relpath)
                    directory_of_file = os.path.dirname(publicated_file)
                    if not os.path.exists(directory_of_file):
                        os.makedirs(directory_of_file)
                    with gzip.open(publicated_file, "w") as fw:
                        with open(filename, mode="rb") as fr:
                            blocksize = 65536
                            buf = fr.read(blocksize)
                            while len(buf) > 0:
                                fw.write(buf)
                                buf = fr.read(blocksize)
                    hashes[relpath] = current_hash
                    logging.info(f"Gzipped: {filename}")
            else:
                publicated_file = os.path.join(publication_dir, relpath)
                directory_of_file = os.path.dirname(publicated_file)
                if not os.path.exists(directory_of_file):
                    os.makedirs(directory_of_file)
                shutil.copy(filename, directory_of_file)


def rewrite_hash_codes(hash_sum_file, given_hashes):
    """Rewrite Hash Codes."""
    with open(hash_sum_file, "w", encoding="utf-8") as fw:
        for key in given_hashes:
            fw.write(given_hashes[key] + "  " + key + "\n")


hashes = read_hash_codes(os.path.abspath(HASH_SUM_FILE))
update_gzipped_publications(
    os.path.abspath(OUTPUT_DIR), os.path.abspath(PUBLICATION_DIR)
)
rewrite_hash_codes(os.path.abspath(HASH_SUM_FILE), hashes)
