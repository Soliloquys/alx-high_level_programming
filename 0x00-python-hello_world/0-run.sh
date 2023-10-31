#!/bin/bash

# Check if the environment variable is set
if [ -z "$PYFILE" ]; then
  echo "Error: The PYFILE environment variable is not set."
  exit 1
fi

# Check if the Python script file exists
if [ ! -f "$PYFILE" ]; then
  echo "Error: The Python script file '$PYFILE' does not exist."
  exit 1
fi

python3 "$PYFILE"

