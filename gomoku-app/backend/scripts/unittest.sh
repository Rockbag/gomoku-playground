#!/bin/bash

set -euo pipefail

if [ ! -f ./manage.py ]; then
    echo "Cannot find manage.py in the current directory. Please run this script from your directory that contains the manage.py file"
    exit 1
fi

./manage.py test --settings=backend.settings  --configuration=Test

