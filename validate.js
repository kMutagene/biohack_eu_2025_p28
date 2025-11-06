#!/usr/bin/env node
/**
 * Generate documentation from a SOSS+ profile crate
 *
 * This script loads a SOSS+ profile crate and creates a data structure
 * that can be used by a template to generate documentation.
 */

// THIS SCRIPT DOES NOT WORK - SEE README INSTEAD TO SET UP

import { ROCrate } from "ro-crate";
import fs from "fs";
import path from "path";
import { SossValidator } from './ro-crate-schema-tools/lib/soss-validator.js';
import { execSync } from "child_process";
import { fileURLToPath } from 'url';

function main() {    // Create a validator with the profile crate
    console.log("--- SETUP ---");
    // Load RO-Crate profile crate
    let rocrateProfileCrate, sampleCrate

    let thisFile = fileURLToPath(import.meta.url)
    let dir = path.dirname(thisFile)
    const rocProfileCratePath = path.join(
        dir,
        "isa-ro-crate/profile-crate/ro-crate-metadata.json"
    );
    const sampleCratePath = path.join(
        dir,
        "isa-ro-crate/examples/minimal-arc-ro-crate/ro-crate-metadata.json"
    );

    console.log("Loading RO-Crate profile crate from:", rocProfileCratePath);
    const profileData = fs.readFileSync(rocProfileCratePath, "utf8");
    const profileJson = JSON.parse(profileData);
    rocrateProfileCrate = new ROCrate(profileJson, { array: true, link: true });

    // Load sample target crate
    const sampleCrateData = fs.readFileSync(sampleCratePath, "utf8");
    const targetJson = JSON.parse(sampleCrateData);
    sampleCrate = new ROCrate(targetJson, { array: true, link: true });

    const validator = new SossValidator(rocProfileCratePath);
    validator.parseRules();

    const targetCrate = new ROCrate({ array: true, link: true });
    var results = validator.validateCrate(targetCrate);

    console.log(JSON.stringify(results, null, 2));
}

main()
