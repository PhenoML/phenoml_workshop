#!/bin/bash

# Check if environment variables are set
if [ -z "$CANVAS_CLIENT_ID" ] || [ -z "$CANVAS_CLIENT_SECRET" ]; then
  echo "Error: Required environment variables not set."
  echo "Please set CANVAS_CLIENT_ID and CANVAS_CLIENT_SECRET before running this script."
  echo "Example:"
  echo "  export CANVAS_CLIENT_ID=your_client_id"
  echo "  export CANVAS_CLIENT_SECRET=your_client_secret"
  exit 1
fi

# Set API base URL or use default
CANVAS_API_BASE_URL=${CANVAS_API_BASE_URL:-"https://xpc-dev.canvasmedical.com"}

# Remove trailing slash if present
CANVAS_API_BASE_URL=${CANVAS_API_BASE_URL%/}

echo "Authenticating with Canvas API at $CANVAS_API_BASE_URL..."

# Use actual environment variables rather than string literals with $ inside
curl --request POST "$CANVAS_API_BASE_URL/auth/token/" \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'grant_type=client_credentials' \
--data-urlencode "client_id=$CANVAS_CLIENT_ID" \
--data-urlencode "client_secret=$CANVAS_CLIENT_SECRET"
