# biohack_eu_2025_p28
Work done during the #BioHackEU 2025 on project 28: Towards a robust validation service for data and metadata in ARC RO-Crates

## Setup

Clone the repo:
```
git clone git@github.com:kMutagene/biohack_eu_2025_p28.git
cd biohack_eu_2025_p28
```

Install the submodules:
```
git submodule update --init --recursive
cd ro-crate-schema-tools
npm install
cd ..
```

## Build the profile documentation

```
node ro-crate-schema-tools/generate-soss-docs.js isa-ro-crate/profile-crate/ro-crate-metadata.json isa-ro-crate/profile-text.md isa-ro-crate/profile-crate/profile-documentation.md
```

## Run the validation

Copy the following script into a file `ro-crate-schema-tools/testmycrate.js`:

```js
const path = require("path");
const fs = require("fs");
const ROCrate = require("ro-crate");
const { SossValidator } = require("./lib/soss-validator");

const rocProfileCratePath = path.join(
    __dirname,
    "../isa-ro-crate/profile-crate/ro-crate-metadata.json"
);

const sampleCratePath = path.join(
    __dirname,
    "../isa-ro-crate/examples/minimal-arc-ro-crate/ro-crate-metadata.json"
);


let rocrateProfileCrate;
let sampleCrate;

console.log("--- SETUP ---");
// Load RO-Crate profile crate
console.log("Loading RO-Crate profile crate from:", rocProfileCratePath);
const profileData = fs.readFileSync(rocProfileCratePath, "utf8");
const profileJson = JSON.parse(profileData);
rocrateProfileCrate = new ROCrate.ROCrate(profileJson, { array: true, link: true });

// Load sample target crate
const sampleCrateData = fs.readFileSync(sampleCratePath, "utf8");
const targetJson = JSON.parse(sampleCrateData);
sampleCrate = new ROCrate.ROCrate(targetJson, { array: true, link: true });

const validator = new SossValidator(rocrateProfileCrate);
validator.parseRules();
var results = validator.validateCrate(sampleCrate).then((results) => {
    console.log("Validation Results:");
    console.log(JSON.stringify(results, null, 2));
    console.log("error count: ", results.error.length)
    console.log("success count: ", results.success.length)
});
```

(**_TODO: move this script to the top level rather than a submodule folder_**)

```bash
cd ro-crate-schema-tools/
npm install
node testmycrate.js  # the file we just created
```

## Development notes

See [dev-notes.md](dev-notes.md)
