# Reproduce:
1. `poetry install --no-root`
2. `poetry run mypy repro.py`

# Output
```
repro.py:5: note: Revealed type is "def (fo: Union[typing.IO[Any], fastavro.io.json_decoder.AvroJSONDecoder], reader_schema: Union[builtins.str, builtins.list[Any], builtins.dict[Any, Any], None] =, return_record_name: builtins.bool =, return_record_name_override: builtins.bool =, handle_unicode_errors: builtins.str =) -> fastavro._read.reader"
repro.py:7: error: Variable "fastavro.reader" is not valid as a type  [valid-type]
repro.py:7: note: See https://mypy.readthedocs.io/en/stable/common_issues.html#variables-vs-type-aliases
repro.py:8: error: fastavro.reader? has no attribute "schema"  [attr-defined]
Found 2 errors in 1 file (checked 1 source file)
```
