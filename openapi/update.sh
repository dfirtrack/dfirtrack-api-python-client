#!/bin/bash

#Get current OpenAPI definition file from the DFIRTrack repo
rm openapi_dfirtrack.yml
wget https://raw.githubusercontent.com/stuhli/dfirtrack/develop/dfirtrack_api/openapi/openapi_dfirtrack.yml .
