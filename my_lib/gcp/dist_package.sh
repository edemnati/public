#!/bin/sh -x

echo "----------------------------------"
echo "Deploy package : gcp_cloud_util"

python setup.py sdist

read -p "Press enter to close..." x