# How to Deploy a Private Package
The private package mylib.gcp_cloud_util.gcp_cloud_util encapsulates the interaction with google-cloud packages (storage, pubsub, firestore etc.) in order to simplify its reusable usage.

## Create a source distribution
```
python setup.py sdist
```

## Cloud Function: Need to copy package locally
### GCP Ref: https://cloud.google.com/functions/docs/writing/specifying-dependencies-python
```
cd [CLOUD_FUNCTION_FOLDER]
```

### Install Package: pip install --target=DEPENDENCY_FOLDER PACKAGE_DEPENDENCY_FOLDER
```
pip install --upgrade --target=gcputil [PATH]\my_lib\gcp\dist\gcputil-0.1.tar.gz
```

## Use package
```
from gcp_cloud_util.gcp_cloud_util import gcp_cloud_util
```
