#!/bin/bash

# Check if environment variables are set
if [ -z "$PHENOML_CLIENT_ID" ] || [ -z "$PHENOML_CLIENT_SECRET" ]; then
  echo "Error: Required environment variables not set."
  echo "Please set PHENOML_CLIENT_ID and PHENOML_CLIENT_SECRET before running this script."
  echo "Example:"
  echo "  export PHENOML_CLIENT_ID=your_client_id"
  echo "  export PHENOML_CLIENT_SECRET=your_client_secret"
  exit 1
fi

# Set API base URL or use default
PHENOML_API_BASE_URL=${PHENOML_API_BASE_URL:-"https://experiment-test.app.pheno.ml"}

# Remove trailing slash if present
PHENOML_API_BASE_URL=${PHENOML_API_BASE_URL%/}

basic_auth=$(echo -n "${PHENOML_CLIENT_ID}:${PHENOML_CLIENT_SECRET}" | base64)

echo "Authenticating with PhenoML API at $PHENOML_API_BASE_URL..."

# Use actual environment variables rather than string literals with $ inside
curl --request POST "$PHENOML_API_BASE_URL/auth/token" \
  --header "accept: application/json" \
  --header "authorization: Basic $basic_auth"
