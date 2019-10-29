csv2json.py converts an input CSV file to JSON.
```sh
  python csv2json.py IQP_JSON11.csv
```

Input CSV file has a header row. Multivalued properties have a numbered suffix
and they will be stored in a list as a value in a dictionary with property as the key.

Checkout sample input file `IQP_JSON11.csv` and output file `convertedTo.json`.
```sh
python -m json.tool convertedTo.json >> pretty.json
```
