# Rough idea

1. Create Datamap for excel example dataset
2. Translate Datamap into frictionless schema
3. Validate using excel validator

## Example dataset

- File: [bca-protein-titration.xlsx](bca-protein-titration.xlsx)
- Assay: Titration to determine sample protein content
- Measurement device: Tecan Spark Control

### Notes

- file is pretty untidy
- upper part (row ≤33) and row 44
  - metadata
  - somewhat key:value pairs
  - some keys are key:values themselves
  - some keys with / without ": "
- table range A31:M44
  - actual measurement data
  - here: absorbance at 562 nm (as determined by B23 E25, F25)

## Datamap

- https://github.com/nfdi4plants/ARC-specification/blob/release/ISA-XLSX.md#datamap-table-sheets
- 

## Fragment identifiers for excel datasets

https://github.com/nfdi4plants/spreadsheet-fragment-identifiers

## Frictionless + Excel Validator

- Frictionless: https://framework.frictionlessdata.io/docs/guides/validating-data.html
- Excel Validator: https://pypi.org/project/excel-validator/

