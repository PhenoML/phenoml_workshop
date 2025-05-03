#!/bin/bash

# Check if environment variables are set
if [ -z "$MEDPLUM_CLIENT_ID" ] || [ -z "$MEDPLUM_CLIENT_SECRET" ]; then
  echo "Error: Required environment variables not set."
  echo "Please set MEDPLUM_CLIENT_ID and MEDPLUM_CLIENT_SECRET before running this script."
  echo "Example:"
  echo "  export MEDPLUM_CLIENT_ID=your_client_id"
  echo "  export MEDPLUM_CLIENT_SECRET=your_client_secret"
  exit 1
fi


curl -X POST https://api.medplum.com/oauth2/token \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "grant_type=client_credentials&client_id=$MEDPLUM_CLIENT_ID&client_secret=$MEDPLUM_CLIENT_SECRET"
