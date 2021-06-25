#!/bin/bash

#Get current OpenAPI definition file from the DFIRTrack repo
rm openapi_dfirtrack.yml
wget https://raw.githubusercontent.com/dfirtrack/dfirtrack/develop/dfirtrack_api/openapi/openapi_dfirtrack.yml .
