import hashlib
import sys
import pydantic

class MetaBlob(pydantic.BaseModel):
    blake2b: str

b2b = hashlib.blake2b()
with open(sys.argv[1], 'rb') as f:
    for chunk in iter(lambda: f.read(8192), b""):
        b2b.update(chunk)

print (MetaBlob(**{"blake2b": b2b.hexdigest()}).json())
