import mmap
import os
import codecs
from functools import wraps

def mmap_chunks_utf8_safe(file_path, chunk_size):
    """
    Reads a file in UTF-8 safe chunks using mmap sequentially.
    Guaranteed to process the entire file, even very large files.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not os.path.isfile(file_path):
                raise FileNotFoundError(f"File not found: {file_path}")

            decoder = codecs.getincrementaldecoder('utf-8')()

            with open(file_path, "rb") as f:
                mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
                print(mm.size())
                try:
                    while True:
                        chunk_bytes = mm.read(chunk_size)
                        if not chunk_bytes:
                            break

                        text_chunk = decoder.decode(chunk_bytes, final=False)
                        if text_chunk:
                            func(text_chunk, *args, **kwargs)

                    # Flush any remaining bytes
                    final_text = decoder.decode(b"", final=True)
                    if final_text:
                        func(final_text, *args, **kwargs)

                finally:
                    mm.close()
        return wrapper
    return decorator


path = "/home/alexander-bontempo/Desktop/TFM_christ/scanprosite/scanprosite_clean_last.fasta" #change the path to point to your file

@mmap_chunks_utf8_safe(path, chunk_size=10000)
def process_chunk(chunk):  #here goes your function  just add (chunk) as parameter. Im you function you can handle chunk as a text.
    print("Chunk length:", len(chunk))
    print(chunk)


process_chunk()
