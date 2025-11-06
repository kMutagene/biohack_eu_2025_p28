import argparse
import os
import arctrl
from arctrl.py.Core.data_map import DataMap , DataContext
import re
import frictionless
from junit_xml import TestSuite, TestCase

def init_filebased_frictionless_schema(basepath: str, datacontext: DataContext) -> frictionless.Metadata:
    #create automatically resource with schema
    automaticResource = frictionless.describe(datacontext.FilePath, basepath=basepath)
    #update type to any
    for i in range(len(automaticResource.schema.fields)):
        fieldName = automaticResource.schema.fields[i].name
        automaticResource.schema.fields[i] = frictionless.fields.AnyField(name=fieldName)
    #update files
    return automaticResource

def validate_datamap(basepath:str, datamap: DataMap) -> TestSuite:

    datamap_filepath = os.path.join(basepath, datamap.FileName())

    datamapTestcase = TestCase(datamap_filepath, "Arctrl", allow_multiple_subelements=True)

    entries = {}
    patternColumn = re.compile("^col=([0-9]+)+$")

    if not datamapTestcase.is_error():        
        for datacontext in datamap.DataContexts:
            data_context_path = os.path.join(basepath, datacontext.FilePath)
            if datacontext.Format == "text/csv":
                #check existence
                if not datacontext.FilePath in entries:
                    entries[datacontext.FilePath] = {
                            "location": data_context_path,
                            "testcase": TestCase(data_context_path, "Frictionless", allow_multiple_subelements=True)
                        }
                    try:
                        if os.path.exists(data_context_path):
                            #create automatically resource with schema
                            automaticResource = init_filebased_frictionless_schema(basepath, datacontext)
                            entries[datacontext.FilePath]["resource"] = automaticResource
                        else:
                            raise FileNotFoundError(datacontext.FilePath)
                    except Exception as ex:
                        entries[datacontext.FilePath]["testcase"].add_error_info(str(ex),None,type(ex).__name__)
                #if exists without errors
                if not entries[datacontext.FilePath]["testcase"].is_error():
                    try:
                        if datacontext.SelectorFormat == "https://datatracker.ietf.org/doc/html/rfc7111":
                            if (colMatch := patternColumn.match(datacontext.Selector)):
                                column = int(colMatch.group(1))
                                value = datacontext.GetValue()
                                fieldName = entries[datacontext.FilePath]["resource"].schema.fields[column].name
                                if value.IsAnOntology:
                                    if value.Text in ["double","decimal","float"]:                            
                                        entries[datacontext.FilePath]["resource"].schema.fields[column] = frictionless.fields.NumberField(name=fieldName)
                                    elif value.Text in ["integer", "long", "int", "short", "byte"]:                            
                                        entries[datacontext.FilePath]["resource"].schema.fields[column] = frictionless.fields.IntegerField(
                                            name=fieldName)
                                    elif value.Text in ["positiveInteger"]:                            
                                        entries[datacontext.FilePath]["resource"].schema.fields[column] = frictionless.fields.IntegerField(
                                            name=fieldName, constraints={"minimum": 1})
                                    elif value.Text in ["nonNegativeInteger", "unsignedLong", "unsignedInt", "unsignedShort", "unsignedByte"]:                            
                                        entries[datacontext.FilePath]["resource"].schema.fields[column] = frictionless.fields.IntegerField(
                                            name=fieldName, constraints={"minimum": 0})
                                    elif value.Text in ["nonPositiveInteger"]:                            
                                        entries[datacontext.FilePath]["resource"].schema.fields[column] = frictionless.fields.IntegerField(
                                            name=fieldName, constraints={"maximum": 0})
                                    elif value.Text in ["negativeInteger"]:                            
                                        entries[datacontext.FilePath]["resource"].schema.fields[column] = frictionless.fields.IntegerField(
                                            name=fieldName, constraints={"maximum": -1})
                                    elif value.Text in ["string", "normalizedString", "token"]:
                                        entries[datacontext.FilePath]["resource"].schema.fields[column] = frictionless.fields.StringField(
                                            name=fieldName)
                                    elif value.Text in ["language"]:
                                        entries[datacontext.FilePath]["resource"].schema.fields[column] = frictionless.fields.StringField(
                                            name=fieldName, constraints={"pattern": "[a-zA-Z]{1,8}(-[a-zA-Z0-9]{1,8})*"})
                                    elif value.Text in ["boolean"]:
                                        entries[datacontext.FilePath]["resource"].schema.fields[column] = frictionless.fields.BooleanField(name=fieldName)
                                    elif value.Text in ["dateTime"]:
                                        entries[datacontext.FilePath]["resource"].schema.fields[column] = frictionless.fields.DateTimeField(name=fieldName)
                                    elif value.Text in ["time"]:
                                        entries[datacontext.FilePath]["resource"].schema.fields[column] = frictionless.fields.TimeField(name=fieldName)
                                    elif value.Text in ["date"]:
                                        entries[datacontext.FilePath]["resource"].schema.fields[column] = frictionless.fields.DateField(name=fieldName)
                                    elif value.Text in ["gYear"]:
                                        entries[datacontext.FilePath]["resource"].schema.fields[column] = frictionless.fields.YearField(name=fieldName)
                                    elif value.Text in ["gYearMonth"]:
                                        entries[datacontext.FilePath]["resource"].schema.fields[column] = frictionless.fields.YearmonthField(name=fieldName)
                                    elif value.Text in ["duration", "yearMonthDuration", "dayTimeDuration"]:
                                        entries[datacontext.FilePath]["resource"].schema.fields[column] = frictionless.fields.DurationField(name=fieldName)
                                    else:
                                        raise NotImplementedError(value.Text)
                                elif value.IsAnInt:
                                    entries[datacontext.FilePath]["resource"].schema.fields[column] = frictionless.fields.IntegerField(name=fieldName)
                                elif value.IsAFloat:
                                    entries[datacontext.FilePath]["resource"].schema.fields[column] = frictionless.fields.NumberField(name=fieldName)
                                elif value.IsNumerical:
                                    entries[datacontext.FilePath]["resource"].schema.fields[column] = frictionless.fields.NumberField(name=fieldName) 
                                elif value.IsText:
                                    entries[datacontext.FilePath]["resource"].schema.fields[column] = frictionless.fields.StringField(name=fieldName) 
                                else:
                                    raise NotImplementedError(value)
                        else:
                            raise NotImplementedError(datacontext.SelectorFormat)
                    except Exception as ex:
                        entries[datacontext.FilePath]["testcase"].add_failure_info(str(ex),None,type(ex).__name__)
            else:
                # raise NotImplementedError(datacontext.Format)
                pass
        for id, entry in entries.items():
            try:
                validationResult = entry["resource"].validate()
                if not validationResult.valid:
                    for task in validationResult.tasks:
                        for error in task.errors:
                            entry["testcase"].add_failure_info(error.description, error.message, error.type)            
            except Exception as ex:
                entries[datacontext.FilePath]["testcase"].add_error_info(str(ex),None,type(ex).__name__)
    return TestSuite(datamap_filepath,[datamapTestcase] + [entry["testcase"] for entry in entries.values()])

def aggregate_datamaps(arc: arctrl.ARC) -> list[DataMap]:
    datamaps : list[DataMap] = []
    for assay in arc.Assays:
        if assay.DataMap is not None:
            datamaps.append(assay.DataMap)
    for study in arc.Studies:
        if study.DataMap is not None:
            datamaps.append(study.DataMap)
    for workflow in arc.Workflows:
        if workflow.DataMap is not None:
            datamaps.append(workflow.DataMap)
    for runs in arc.Runs:
        if runs.DataMap is not None:
            datamaps.append(runs.DataMap)
    return datamaps

def main():

    parser = argparse.ArgumentParser(
        description="Reads an arc and attempts to validate whether contained data described by a datamap is valid."
    )

    parser.add_argument("--arc-path", "-i", help="Path to the input ARC root folder")
    parser.add_argument("--out-path", "-o", help="path of the junit xml output file")

    args = parser.parse_args()

    arc : arctrl.ARC = arctrl.ARC.load(args.arc_path)
    arc.MakeDataFilesAbsolute()

    datamaps : list[DataMap] = aggregate_datamaps(arc)

    basePath = os.path.dirname(args.arc_path)

    testsuites: list[TestSuite] = []

    for datamap in datamaps:
        response = validate_datamap(basePath,datamap)
        testsuites.append(response)
        
    with open(args.out_path,"w") as f:
        f.write(TestSuite.to_xml_string(testsuites))

if __name__ == "__main__":
    main()