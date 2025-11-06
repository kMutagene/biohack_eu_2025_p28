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

## Run the tests

???
