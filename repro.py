from __future__ import annotations

import fastavro
import fastavro.read
from fastavro._read import reader
from fastavro._read_py import reader as py_reader

reveal_type(fastavro.reader)

def x(reader: fastavro.reader) -> None:
    ...

reveal_type(fastavro.read.reader)

def y(reader: fastavro.read.reader) -> None:
    ...

reveal_type(reader)

def z(reader: reader) -> None:
    ...

reveal_type(py_reader)

def zz(reader: py_reader) -> None:
    ...
