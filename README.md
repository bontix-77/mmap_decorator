UTF-8 Safe File Chunk Reader

This repository contains a Python script for reading large text files in UTF-8 safe chunks using mmap. The script allows you to efficiently process very large files without loading the entire file into memory.

Features

Reads files in chunks of a specified size.

Handles UTF-8 encoding safely to avoid splitting multibyte characters.

Works efficiently with very large files.

Simple decorator interface to process each chunk with a custom function.

Requirements

Python 3.6+

Standard Python libraries: os, mmap, codecs, functools

No additional dependencies are required.

Usage

Clone the repository:

git clone <repository_url>
cd <repository_folder>


Edit the path variable in the script to point to your file:

path = "/path/to/your/large_file.fasta"


Define a function to process each chunk of text. Decorate it with @mmap_chunks_utf8_safe:

from script_name import mmap_chunks_utf8_safe

@mmap_chunks_utf8_safe(path, chunk_size=10000)
def process_chunk(chunk):
    print("Chunk length:", len(chunk))
    print(chunk)


Call your decorated function:

process_chunk()


The function will be called once for each UTF-8 safe chunk of the file.

Example

For a FASTA file, each chunk could be processed like this:

@mmap_chunks_utf8_safe(path, chunk_size=10000)
def process_chunk(chunk):
    sequences = chunk.split(">")  # Split by FASTA header
    for seq in sequences:
        if seq:
            print("Sequence length:", len(seq))

Notes

The chunk_size parameter controls how many bytes are read at a time. Adjust based on your system memory and file size.

The decorator ensures that multi-byte UTF-8 characters are not broken across chunks.

If the file does not exist, a FileNotFoundError is raised.

License

This project is licensed under the MIT License.
