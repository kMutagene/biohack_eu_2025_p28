# Validation Datamap/Frictionless

Using Datamap to create Frictionless Schema and validate data

This project had 4 goals:

1. extract the necessary information from an ARC datamap to validate the data file it describes (in the scope of the project limited to csv)
2. map the datamap descriptor to a frictionless table schema
3. map the frictionless output to junit (to display the results in a ci process)
4. package the tool as a docker container that can be used in a CI/CD runner

all of the goals were reached. 

the python tool in `datamap-validation\app` parses an ARC, aggregates all data maps, creates an ephemeral fritionless table schema from them and then validates the described files against it.
The tool's output is a junit xml report.
It is hosted as a docker container at https://hub.docker.com/r/mutagene/datamap-validation/tags.
A test run where it was used in the PLANTdataHUB to validate files in a CI process can be seen here: https://git.nfdi4plants.org/kMutagene/bruh/-/pipelines/17494/test_report?job_name=My+own+stuff

## Datamap

- https://github.com/nfdi4plants/ARC-specification/blob/release/ISA-XLSX.md#datamap-table-sheets


## Frictionless

- https://pypi.org/project/frictionless/

## Example data

- ArcPrototype : https://git.nfdi4plants.org/muehlhaus/ArcPrototype/