#Deploy a Private Package

###GCP Ref: https://cloud.google.com/functions/docs/writing/specifying-dependencies-python
##Deploy package
python setup.py sdist

##Install Package

##Use package
from gcp_cloud_util.gcp_cloud_util import gcp_cloud_util

##Cloud Function: Need to copy package locally
> cd CLOUD_FUNCTION_FOLDER

##pip install --target=DEPENDENCY_FOLDER PACKAGE_DEPENDENCY_FOLDER
> pip install --upgrade --target=gcputil C:\Users\ezzat\githubrepository\my_lib\gcp\dist\gcputil-0.1.tar.gz