# Deploy a Private Package

### GCP Ref: https://cloud.google.com/functions/docs/writing/specifying-dependencies-python
## Deploy package
python setup.py sdist

## Install Package

## Use package
from gcp_cloud_util.gcp_cloud_util import gcp_cloud_util

## Cloud Function: Need to copy package locally
> cd CLOUD_FUNCTION_FOLDER

## pip install --target=DEPENDENCY_FOLDER PACKAGE_DEPENDENCY_FOLDER
> pip install --upgrade --target=gcputil C:\Users\ezzat\githubrepository\my_lib\gcp\dist\gcputil-0.1.tar.gz



#############Environment variables #############
#-----------------------------#
## App Engine
#-----------------------------#
## Ref: https://cloud.google.com/appengine/docs/standard/python3/runtime#environment_variables

	Environment variables
	The following environment variables are set by the runtime:

	Environment variable	Description
	GAE_APPLICATION	The ID of your App Engine application.
	GAE_DEPLOYMENT_ID	The ID of the current deployment.
	GAE_ENV	The App Engine environment. Set to standard.
	GAE_INSTANCE	The ID of the instance on which your service is currently running.
	GAE_MEMORY_MB	The amount of memory available to the application process, in MB.
	GAE_RUNTIME	The runtime specified in your app.yaml file.
	GAE_SERVICE	The service name specified in your app.yaml file. If no service name is specified, it is set to default.
	GAE_VERSION	The current version label of your service.
	GOOGLE_CLOUD_PROJECT	The GCP project ID associated with your application.
	NODE_ENV	Set to production when your service is deployed.
	PORT	The port that receives HTTP requests.

#-----------------------------#
## Cloud Function
#-----------------------------#
# Ref:https://cloud.google.com/functions/docs/env-var
	Environment variables set automatically
	This section lists environment variables that are set automatically.

	Node.js 6, Node.js 8, Python 3.7 and Go 1.11
	The following environment variables are set automatically for the Node.js 6, Node.js 8, Python 3.7 and Go 1.11 runtimes. Subsequent Cloud Functions runtimes use a more limited set of environment variables, as described in Node.js 10 and subsequent runtimes.

	Key	Description
	ENTRY_POINT	Reserved: The function to be executed.
	GCP_PROJECT	Reserved: The current GCP project ID.
	GCLOUD_PROJECT	Reserved: The current GCP project ID (deprecated).
	GOOGLE_CLOUD_PROJECT	Reserved: Not set but reserved for internal use.
	FUNCTION_TRIGGER_TYPE	Reserved: The trigger type of the function.
	FUNCTION_NAME	Reserved: The name of the function resource.
	FUNCTION_MEMORY_MB	Reserved: The maximum memory of the function.
	FUNCTION_TIMEOUT_SEC	Reserved: The execution timeout in seconds.
	FUNCTION_IDENTITY	Reserved: The current identity (service account) of the function.
	FUNCTION_REGION	Reserved: The function region (example: us-central1).
