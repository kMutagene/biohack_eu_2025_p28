Here is where a human description of the workflow should go

## Types of entities (specializations of Classes) and expected Properties


### <a id="class-propertyvalue"></a> Class: PropertyValue

#### IRI: #PropertyValue  

A general profile for key-value pairs.

Instances of this type MAY be present in the crate.

| Min Count | Max Count |
| --------- | --------- |
| N/A | N/A |

| Property | Required | Description | Range | Value |
| -------- | -------- | ----------- | ----- | ----- |
| @type | Yes |  |  | http://schema.org/PropertyValue |
| <a href="#property-additionaltype">additionalType <a href="#property-additionaltype" target="_blank" rel="noopener">ⓘ</a></a> | Yes | A PropertyValue MUST have additionalType with the type of the property |  |  |
| <a href="#property-name">name <a href="#property-name" target="_blank" rel="noopener">ⓘ</a></a> | Yes | The PropertyValue must have a name |  |  |
| <a href="#property-value">value <a href="#property-value" target="_blank" rel="noopener">ⓘ</a></a> | Yes | The PropertyValue SHOULD have a value |  |  |

## All Properties

### <a id="property-additionaltype"></a> Property: additionalType <a href="http://schema.org/additionalType" target="_blank" rel="noopener">ⓘ</a>

ID: #Property_additionalType_pv

| Description | Range | Occurs in Domain(s) |
| ----------- | ----------- | ----------- |
| A PropertyValue MUST have additionalType with the type of the property |  | <a href="#class-propertyvalue">PropertyValue</a> |
### <a id="property-name"></a> Property: name <a href="http://schema.org/name" target="_blank" rel="noopener">ⓘ</a>

ID: #Property_name_pv

| Description | Range | Occurs in Domain(s) |
| ----------- | ----------- | ----------- |
| The PropertyValue must have a name |  | <a href="#class-propertyvalue">PropertyValue</a> |
### <a id="property-value"></a> Property: value <a href="http://schema.org/value" target="_blank" rel="noopener">ⓘ</a>

ID: #Property_value_pv

| Description | Range | Occurs in Domain(s) |
| ----------- | ----------- | ----------- |
| The PropertyValue SHOULD have a value |  | <a href="#class-propertyvalue">PropertyValue</a> |


## Item Lists



<a id="example-1-hasexample"></a>

## Example-1: #hasExample


### <a id="artifact-isa-ro-crate-example"></a> Artifact: ISA RO-Crate Example

<pre>
 {
  "@id": "https://git.nfdi4plants.org/venn/Ru_ChlamyHeatstress/-/package_files/35699/download",
  "@type": "File",
  "name": "ISA RO-Crate Example",
  "encodingFormat": "application/json",
  "about": {
    "@id": "https://github.com/nfdi4plants/isa-ro-crate-profile/tree/1.0.0-draft.2/profile/"
  }
}
</pre>


