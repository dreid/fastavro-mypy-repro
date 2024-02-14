# Reproduce:
1. `poetry install --no-root`
2. `poetry run mypy repro.py`

# Output
```
❯ poetry run mypy --no-incremental --cache-dir=/dev/null repro.py
repro.py:8: note: Revealed type is "def (fo: Union[typing.IO[Any], fastavro.io.json_decoder.AvroJSONDecoder], reader_schema: Union[builtins.str, builtins.list[Any], builtins.dict[Any, Any], None] =, return_record_name: builtins.bool =, return_record_name_override: builtins.bool =, handle_unicode_errors: builtins.str =) -> fastavro._read.reader"
repro.py:10: error: Variable "fastavro.reader" is not valid as a type  [valid-type]
repro.py:10: note: See https://mypy.readthedocs.io/en/stable/common_issues.html#variables-vs-type-aliases
repro.py:13: note: Revealed type is "def (fo: Union[typing.IO[Any], fastavro.io.json_decoder.AvroJSONDecoder], reader_schema: Union[builtins.str, builtins.list[Any], builtins.dict[Any, Any], None] =, return_record_name: builtins.bool =, return_record_name_override: builtins.bool =, handle_unicode_errors: builtins.str =) -> fastavro._read.reader"
repro.py:15: error: Variable "fastavro.read.reader" is not valid as a type  [valid-type]
repro.py:15: note: See https://mypy.readthedocs.io/en/stable/common_issues.html#variables-vs-type-aliases
repro.py:18: note: Revealed type is "def (fo: Union[typing.IO[Any], fastavro.io.json_decoder.AvroJSONDecoder], reader_schema: Union[builtins.str, builtins.list[Any], builtins.dict[Any, Any], None] =, return_record_name: builtins.bool =, return_record_name_override: builtins.bool =, handle_unicode_errors: builtins.str =) -> fastavro._read.reader"
repro.py:23: note: Revealed type is "def (fo: Union[typing.IO[Any], fastavro.io.json_decoder.AvroJSONDecoder], reader_schema: Union[builtins.str, builtins.list[Any], builtins.dict[Any, Any], None] =, return_record_name: builtins.bool =, return_record_name_override: builtins.bool =, handle_unicode_errors: builtins.str =, return_named_type: builtins.bool =, return_named_type_override: builtins.bool =) -> fastavro._read_py.reader"
Found 2 errors in 1 file (checked 1 source file)
```
