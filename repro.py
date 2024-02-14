from __future__ import annotations

import fastavro

reveal_type(fastavro.reader)

def x(reader: fastavro.reader) -> None:
    print(reader.schema)

with open("foo.avro", "rb") as f:
    x(fastavro.reader(f))
