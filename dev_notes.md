# dev notes on RO-Crate validation with SoSS+ schema

## Guidance needed on writing the profile

A technical tutorial for writing profiles would be useful - and documentation on how to run the validation outside of the tests. It's hard to figure out exactly how things should be designed, though we have had a go.

## Severity levels

e.g. MUST/SHOULD/MAY or Violation/Warning/Info in SHACL. Are these supported?

## Errors recorded as "info" rather than error

If the `name` property is removed from one of the `ParameterValue` entities in the example, the validation output includes:

```
...
"#Property_name_pv": {
      "#ParameterValue_software_ProteomIqon": {
        "info": [
          {
            "message": "Entity #ParameterValue_software_ProteomIqon is missing required property name"
          }
        ]
      }
    },
...
error count:  0
success count:  1
```

## 2. Can't get checks working for ro-crate-metadata.json or root data entity

Our experiments with this have been deleted, but this also seems to be a problem when testing the Workflow RO-Crate profile on the workflow example. All the checks fail on Eli's machine...

<details>
<summmary>View log</summary>
```
--- SETUP ---
Loading RO-Crate profile crate from: /home/eli/manchester/bh2025/biohack_eu_2025_p28/ro-crate-schema-tools/profiles/workflow/profile-crate/ro-crate-metadata.json
Parsing 27 schema entities from profile crate
Found 8 class rules in the SoSS+ profile
Found 17 property rules in the SoSS+ profile
Found 2 item list rules in the SoSS+ profile
Found 0 term set rules in the SoSS+ profile
Parsing 27 schema entities from profile crate
Found 8 class rules in the SoSS+ profile
Found 17 property rules in the SoSS+ profile
Found 2 item list rules in the SoSS+ profile
Found 0 term set rules in the SoSS+ profile
Validating entity: ro-crate-metadata.json
Checking class rule: RO-Crate Metadadata Descriptor for entity ro-crate-metadata.json -types CreativeWork with required types: http://schema.org/CreativeWork debug
Entity ro-crate-metadata.json matches required types http://schema.org/CreativeWork for rule RO-Crate Metadadata Descriptor
Validating entity: ./
Checking class rule: Root Data Entity for entity ./ -types Dataset with required types: http://schema.org/Dataset debug
Entity ./ matches required types http://schema.org/Dataset for rule Root Data Entity
Validating entity: example_workflow.cwl
Checking class rule: Main Workflow for entity example_workflow.cwl -types File, SoftwareSourceCode, ComputationalWorkflow with required types: http://schema.org/MediaObject, http://schema.org/SoftwareSourceCode, https://bioschemas.org/ComputationalWorkflow debug
Entity example_workflow.cwl matches required types http://schema.org/MediaObject, http://schema.org/SoftwareSourceCode, https://bioschemas.org/ComputationalWorkflow for rule Main Workflow
Validating entity: diagram.svg
Checking class rule: Main Workflow Diagram for entity diagram.svg -types File, ImageObject with required types: http://schema.org/ImageObject, http://schema.org/MediaObject debug
Entity diagram.svg matches required types http://schema.org/ImageObject, http://schema.org/MediaObject for rule Main Workflow Diagram
Validating entity: ./
Checking class rule: RO-Crate Metadadata Descriptor for entity ./ -types Dataset with required types: http://schema.org/CreativeWork debug
Validating entity: ro-crate-preview.html
Checking class rule: RO-Crate Metadadata Descriptor for entity ro-crate-preview.html -types CreativeWork with required types: http://schema.org/CreativeWork debug
Entity ro-crate-preview.html matches required types http://schema.org/CreativeWork for rule RO-Crate Metadadata Descriptor
Validating entity: ./
Validating entity: https://w3id.org/workflowhub/workflow-ro-crate/1.0
Checking class rule: RO-Crate Metadadata Descriptor for entity https://w3id.org/workflowhub/workflow-ro-crate/1.0 -types CreativeWork, Profile with required types: http://schema.org/CreativeWork debug
Entity https://w3id.org/workflowhub/workflow-ro-crate/1.0 matches required types http://schema.org/CreativeWork for rule RO-Crate Metadadata Descriptor
Validating entity: example_workflow.cwl
Checking class rule: RO-Crate Metadadata Descriptor for entity example_workflow.cwl -types File, SoftwareSourceCode, ComputationalWorkflow with required types: http://schema.org/CreativeWork debug
Validating entity: diagram.svg
Checking class rule: RO-Crate Metadadata Descriptor for entity diagram.svg -types File, ImageObject with required types: http://schema.org/CreativeWork debug
Validating entity: README.md
Checking class rule: RO-Crate Metadadata Descriptor for entity README.md -types File with required types: http://schema.org/CreativeWork debug
Validating entity: https://w3id.org/workflowhub/workflow-ro-crate#cwl
Checking class rule: RO-Crate Metadadata Descriptor for entity https://w3id.org/workflowhub/workflow-ro-crate#cwl -types ComputerLanguage with required types: http://schema.org/CreativeWork debug
Validating entity: ro-crate-metadata.json
Checking class rule: Root Data Entity for entity ro-crate-metadata.json -types CreativeWork with required types: http://schema.org/Dataset debug
Validating entity: ./
Validating entity: ro-crate-preview.html
Checking class rule: Root Data Entity for entity ro-crate-preview.html -types CreativeWork with required types: http://schema.org/Dataset debug
Validating entity: https://w3id.org/workflowhub/workflow-ro-crate/1.0
Checking class rule: Root Data Entity for entity https://w3id.org/workflowhub/workflow-ro-crate/1.0 -types CreativeWork, Profile with required types: http://schema.org/Dataset debug
Validating entity: example_workflow.cwl
Checking class rule: Root Data Entity for entity example_workflow.cwl -types File, SoftwareSourceCode, ComputationalWorkflow with required types: http://schema.org/Dataset debug
Validating entity: diagram.svg
Checking class rule: Root Data Entity for entity diagram.svg -types File, ImageObject with required types: http://schema.org/Dataset debug
Validating entity: README.md
Checking class rule: Root Data Entity for entity README.md -types File with required types: http://schema.org/Dataset debug
Validating entity: https://w3id.org/workflowhub/workflow-ro-crate#cwl
Checking class rule: Root Data Entity for entity https://w3id.org/workflowhub/workflow-ro-crate#cwl -types ComputerLanguage with required types: http://schema.org/Dataset debug
Validating entity: ro-crate-metadata.json
Checking class rule: Main Workflow for entity ro-crate-metadata.json -types CreativeWork with required types: http://schema.org/MediaObject, http://schema.org/SoftwareSourceCode, https://bioschemas.org/ComputationalWorkflow debug
Validating entity: ./
Checking class rule: Main Workflow for entity ./ -types Dataset with required types: http://schema.org/MediaObject, http://schema.org/SoftwareSourceCode, https://bioschemas.org/ComputationalWorkflow debug
Validating entity: ro-crate-preview.html
Checking class rule: Main Workflow for entity ro-crate-preview.html -types CreativeWork with required types: http://schema.org/MediaObject, http://schema.org/SoftwareSourceCode, https://bioschemas.org/ComputationalWorkflow debug
Validating entity: https://w3id.org/workflowhub/workflow-ro-crate/1.0
Checking class rule: Main Workflow for entity https://w3id.org/workflowhub/workflow-ro-crate/1.0 -types CreativeWork, Profile with required types: http://schema.org/MediaObject, http://schema.org/SoftwareSourceCode, https://bioschemas.org/ComputationalWorkflow debug
Validating entity: example_workflow.cwl
Validating entity: diagram.svg
Checking class rule: Main Workflow for entity diagram.svg -types File, ImageObject with required types: http://schema.org/MediaObject, http://schema.org/SoftwareSourceCode, https://bioschemas.org/ComputationalWorkflow debug
Validating entity: README.md
Checking class rule: Main Workflow for entity README.md -types File with required types: http://schema.org/MediaObject, http://schema.org/SoftwareSourceCode, https://bioschemas.org/ComputationalWorkflow debug
Validating entity: https://w3id.org/workflowhub/workflow-ro-crate#cwl
Checking class rule: Main Workflow for entity https://w3id.org/workflowhub/workflow-ro-crate#cwl -types ComputerLanguage with required types: http://schema.org/MediaObject, http://schema.org/SoftwareSourceCode, https://bioschemas.org/ComputationalWorkflow debug
Validating entity: ro-crate-metadata.json
Checking class rule: Main Workflow Description for entity ro-crate-metadata.json -types CreativeWork with required types: http://schema.org/MediaObject, http://schema.org/SoftwareSourceCode, http://schema.org/HowTo debug
Validating entity: ./
Checking class rule: Main Workflow Description for entity ./ -types Dataset with required types: http://schema.org/MediaObject, http://schema.org/SoftwareSourceCode, http://schema.org/HowTo debug
Validating entity: ro-crate-preview.html
Checking class rule: Main Workflow Description for entity ro-crate-preview.html -types CreativeWork with required types: http://schema.org/MediaObject, http://schema.org/SoftwareSourceCode, http://schema.org/HowTo debug
Validating entity: https://w3id.org/workflowhub/workflow-ro-crate/1.0
Checking class rule: Main Workflow Description for entity https://w3id.org/workflowhub/workflow-ro-crate/1.0 -types CreativeWork, Profile with required types: http://schema.org/MediaObject, http://schema.org/SoftwareSourceCode, http://schema.org/HowTo debug
Validating entity: example_workflow.cwl
Checking class rule: Main Workflow Description for entity example_workflow.cwl -types File, SoftwareSourceCode, ComputationalWorkflow with required types: http://schema.org/MediaObject, http://schema.org/SoftwareSourceCode, http://schema.org/HowTo debug
Validating entity: diagram.svg
Checking class rule: Main Workflow Description for entity diagram.svg -types File, ImageObject with required types: http://schema.org/MediaObject, http://schema.org/SoftwareSourceCode, http://schema.org/HowTo debug
Validating entity: README.md
Checking class rule: Main Workflow Description for entity README.md -types File with required types: http://schema.org/MediaObject, http://schema.org/SoftwareSourceCode, http://schema.org/HowTo debug
Validating entity: https://w3id.org/workflowhub/workflow-ro-crate#cwl
Checking class rule: Main Workflow Description for entity https://w3id.org/workflowhub/workflow-ro-crate#cwl -types ComputerLanguage with required types: http://schema.org/MediaObject, http://schema.org/SoftwareSourceCode, http://schema.org/HowTo debug
Validating entity: ro-crate-metadata.json
Checking class rule: README File for entity ro-crate-metadata.json -types CreativeWork with required types: http://schema.org/CreativeWork, http://schema.org/MediaObject debug
Validating entity: ./
Checking class rule: README File for entity ./ -types Dataset with required types: http://schema.org/CreativeWork, http://schema.org/MediaObject debug
Validating entity: ro-crate-preview.html
Checking class rule: README File for entity ro-crate-preview.html -types CreativeWork with required types: http://schema.org/CreativeWork, http://schema.org/MediaObject debug
Validating entity: https://w3id.org/workflowhub/workflow-ro-crate/1.0
Checking class rule: README File for entity https://w3id.org/workflowhub/workflow-ro-crate/1.0 -types CreativeWork, Profile with required types: http://schema.org/CreativeWork, http://schema.org/MediaObject debug
Validating entity: example_workflow.cwl
Checking class rule: README File for entity example_workflow.cwl -types File, SoftwareSourceCode, ComputationalWorkflow with required types: http://schema.org/CreativeWork, http://schema.org/MediaObject debug
Validating entity: diagram.svg
Checking class rule: README File for entity diagram.svg -types File, ImageObject with required types: http://schema.org/CreativeWork, http://schema.org/MediaObject debug
Validating entity: README.md
Checking class rule: README File for entity README.md -types File with required types: http://schema.org/CreativeWork, http://schema.org/MediaObject debug
Validating entity: https://w3id.org/workflowhub/workflow-ro-crate#cwl
Checking class rule: README File for entity https://w3id.org/workflowhub/workflow-ro-crate#cwl -types ComputerLanguage with required types: http://schema.org/CreativeWork, http://schema.org/MediaObject debug
Validating entity: ro-crate-metadata.json
Checking class rule: Test Directory for entity ro-crate-metadata.json -types CreativeWork with required types: http://schema.org/Dataset debug
Validating entity: ./
Checking class rule: Test Directory for entity ./ -types Dataset with required types: http://schema.org/Dataset debug
Entity ./ matches required types http://schema.org/Dataset for rule Test Directory
Validating entity: ro-crate-preview.html
Checking class rule: Test Directory for entity ro-crate-preview.html -types CreativeWork with required types: http://schema.org/Dataset debug
Validating entity: https://w3id.org/workflowhub/workflow-ro-crate/1.0
Checking class rule: Test Directory for entity https://w3id.org/workflowhub/workflow-ro-crate/1.0 -types CreativeWork, Profile with required types: http://schema.org/Dataset debug
Validating entity: example_workflow.cwl
Checking class rule: Test Directory for entity example_workflow.cwl -types File, SoftwareSourceCode, ComputationalWorkflow with required types: http://schema.org/Dataset debug
Validating entity: diagram.svg
Checking class rule: Test Directory for entity diagram.svg -types File, ImageObject with required types: http://schema.org/Dataset debug
Validating entity: README.md
Checking class rule: Test Directory for entity README.md -types File with required types: http://schema.org/Dataset debug
Validating entity: https://w3id.org/workflowhub/workflow-ro-crate#cwl
Checking class rule: Test Directory for entity https://w3id.org/workflowhub/workflow-ro-crate#cwl -types ComputerLanguage with required types: http://schema.org/Dataset debug
Validating entity: ro-crate-metadata.json
Checking class rule: Examples Directory for entity ro-crate-metadata.json -types CreativeWork with required types: http://schema.org/Dataset debug
Validating entity: ./
Checking class rule: Examples Directory for entity ./ -types Dataset with required types: http://schema.org/Dataset debug
Entity ./ matches required types http://schema.org/Dataset for rule Examples Directory
Validating entity: ro-crate-preview.html
Checking class rule: Examples Directory for entity ro-crate-preview.html -types CreativeWork with required types: http://schema.org/Dataset debug
Validating entity: https://w3id.org/workflowhub/workflow-ro-crate/1.0
Checking class rule: Examples Directory for entity https://w3id.org/workflowhub/workflow-ro-crate/1.0 -types CreativeWork, Profile with required types: http://schema.org/Dataset debug
Validating entity: example_workflow.cwl
Checking class rule: Examples Directory for entity example_workflow.cwl -types File, SoftwareSourceCode, ComputationalWorkflow with required types: http://schema.org/Dataset debug
Validating entity: diagram.svg
Checking class rule: Examples Directory for entity diagram.svg -types File, ImageObject with required types: http://schema.org/Dataset debug
Validating entity: README.md
Checking class rule: Examples Directory for entity README.md -types File with required types: http://schema.org/Dataset debug
Validating entity: https://w3id.org/workflowhub/workflow-ro-crate#cwl
Checking class rule: Examples Directory for entity https://w3id.org/workflowhub/workflow-ro-crate#cwl -types ComputerLanguage with required types: http://schema.org/Dataset debug
Validating entity: ro-crate-metadata.json
Checking class rule: Main Workflow Diagram for entity ro-crate-metadata.json -types CreativeWork with required types: http://schema.org/ImageObject, http://schema.org/MediaObject debug
Validating entity: ./
Checking class rule: Main Workflow Diagram for entity ./ -types Dataset with required types: http://schema.org/ImageObject, http://schema.org/MediaObject debug
Validating entity: ro-crate-preview.html
Checking class rule: Main Workflow Diagram for entity ro-crate-preview.html -types CreativeWork with required types: http://schema.org/ImageObject, http://schema.org/MediaObject debug
Validating entity: https://w3id.org/workflowhub/workflow-ro-crate/1.0
Checking class rule: Main Workflow Diagram for entity https://w3id.org/workflowhub/workflow-ro-crate/1.0 -types CreativeWork, Profile with required types: http://schema.org/ImageObject, http://schema.org/MediaObject debug
Validating entity: example_workflow.cwl
Checking class rule: Main Workflow Diagram for entity example_workflow.cwl -types File, SoftwareSourceCode, ComputationalWorkflow with required types: http://schema.org/ImageObject, http://schema.org/MediaObject debug
Validating entity: diagram.svg
Validating entity: README.md
Checking class rule: Main Workflow Diagram for entity README.md -types File with required types: http://schema.org/ImageObject, http://schema.org/MediaObject debug
Validating entity: https://w3id.org/workflowhub/workflow-ro-crate#cwl
Checking class rule: Main Workflow Diagram for entity https://w3id.org/workflowhub/workflow-ro-crate#cwl -types ComputerLanguage with required types: http://schema.org/ImageObject, http://schema.org/MediaObject debug
Validation Results:
{
  "error": [],
  "success": [
    {
      "message": "Found 1 valid instances of http://schema.org/CreativeWork (expected between 1 and 1)",
      "rule": "#RO-Crate_Metadata_Descriptor"
    },
    {
      "message": "Found 1 valid instances of http://schema.org/Dataset (expected between 1 and 1)",
      "rule": "#Root_Data_Entity"
    },
    {
      "message": "Found 1 valid instances of http://schema.org/MediaObject, http://schema.org/SoftwareSourceCode, https://bioschemas.org/ComputationalWorkflow (expected between 1 and 9007199254740991)",
      "rule": "#Class_MainWorkflow"
    },
    {
      "message": "Found 0 valid instances of http://schema.org/MediaObject, http://schema.org/SoftwareSourceCode, http://schema.org/HowTo (expected between 0 and 1)",
      "rule": "#Class_MainWorkflow_Description"
    },
    {
      "message": "Found 0 valid instances of http://schema.org/CreativeWork, http://schema.org/MediaObject (expected between 0 and 1)",
      "rule": "#class_CreativeWork_README"
    },
    {
      "message": "Found 0 valid instances of http://schema.org/Dataset (expected between 0 and 1)",
      "rule": "#class_Dataset_Test_Directory"
    },
    {
      "message": "Found 0 valid instances of http://schema.org/Dataset (expected between 0 and 1)",
      "rule": "#class_Dataset_Examples_Directory"
    },
    {
      "message": "Found 1 valid instances of http://schema.org/ImageObject, http://schema.org/MediaObject (expected between 0 and 9007199254740991)",
      "rule": "#Class_ImageObject_Diagram"
    }
  ],
  "rules": {
    "#RO-Crate_Metadata_Descriptor": {
      "ro-crate-metadata.json": {
        "property-success": [
          {
            "message": "Property \"@id\" validation succeeded for entity ro-crate-metadata.json"
          },
          {
            "message": "Property \"about\" validation succeeded for entity ro-crate-metadata.json"
          }
        ]
      },
      "ro-crate-preview.html": {
        "property-errors": [
          {
            "message": "Property \"@id\" validation failed for entity ro-crate-preview.html"
          }
        ],
        "property-success": [
          {
            "message": "Property \"about\" validation succeeded for entity ro-crate-preview.html"
          }
        ]
      },
      "https://w3id.org/workflowhub/workflow-ro-crate/1.0": {
        "property-errors": [
          {
            "message": "Property \"@id\" validation failed for entity https://w3id.org/workflowhub/workflow-ro-crate/1.0"
          },
          {
            "message": "Property \"about\" validation failed for entity https://w3id.org/workflowhub/workflow-ro-crate/1.0"
          }
        ]
      }
    },
    "#Root_Data_Entity": {
      "./": {
        "property-success": [
          {
            "message": "Property \"description\" validation succeeded for entity ./"
          },
          {
            "message": "Property \"datePublished\" validation succeeded for entity ./"
          },
          {
            "message": "Property \"license\" validation succeeded for entity ./"
          },
          {
            "message": "Property \"mainEntity\" validation succeeded for entity ./"
          },
          {
            "message": "Property \"conformsTo\" validation succeeded for entity ./"
          },
          {
            "message": "Property \"name\" validation succeeded for entity ./"
          }
        ]
      }
    },
    "#Class_MainWorkflow": {
      "example_workflow.cwl": {
        "property-success": [
          {
            "message": "Property \"programmingLanguage\" validation succeeded for entity example_workflow.cwl"
          },
          {
            "message": "Property \"subjectOf\" validation succeeded for entity example_workflow.cwl"
          },
          {
            "message": "Property \"image\" validation succeeded for entity example_workflow.cwl"
          }
        ]
      }
    },
    "#RO-Crate_Metadata_Descriptor.id": {
      "ro-crate-preview.html": {
        "info": [
          {
            "message": "Entity ro-crate-preview.html property @id values do not match expected fixed value ro-crate-metadata.json"
          }
        ]
      },
      "https://w3id.org/workflowhub/workflow-ro-crate/1.0": {
        "info": [
          {
            "message": "Entity https://w3id.org/workflowhub/workflow-ro-crate/1.0 property @id values do not match expected fixed value ro-crate-metadata.json"
          }
        ]
      }
    },
    "#RO-Crate_Metadata_Descriptor.about": {
      "https://w3id.org/workflowhub/workflow-ro-crate/1.0": {
        "info": [
          {
            "message": "Entity https://w3id.org/workflowhub/workflow-ro-crate/1.0 is missing required property about"
          }
        ]
      }
    },
    "#property_Dataset_Test_Directory.id": {
      "./": {
        "info": [
          {
            "message": "Entity ./ property @id values do not match expected fixed value test/"
          }
        ]
      }
    },
    "#class_Dataset_Test_Directory": {
      "./": {
        "property-errors": [
          {
            "message": "Property \"@id\" validation failed for entity ./"
          }
        ]
      }
    },
    "#property_Dataset_Examples_Directory.id": {
      "./": {
        "info": [
          {
            "message": "Entity ./ property @id values do not match expected fixed value examples/"
          }
        ]
      }
    },
    "#class_Dataset_Examples_Directory": {
      "./": {
        "property-errors": [
          {
            "message": "Property \"@id\" validation failed for entity ./"
          }
        ]
      }
    }
  }
}
error count:  0
success count:  8
```
</details>
