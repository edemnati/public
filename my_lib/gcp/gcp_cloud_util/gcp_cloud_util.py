import os

class gcp_util:
    def get_projectid(self,projectid=None):
        if projectid is None:
            env_var=['GCP_PROJECT','GOOGLE_CLOUD_PROJECT']
            for v in env_var:
                try:
                    my_projectid=os.environ.get(v)
                    print('OK')
                    break
                except:
                    pass  
            try: 
               my_projectid
            except:
                print("Error: Failed to get projectid from environment variables")  
                raise
        else:
            my_projectid=projectid
        
        return my_projectid

class gcp_storage:
    def __init__(self,projectid=None,sa_path=None):
        from google.cloud import storage
        self.storage=storage
        
        util=gcp_util()
        self.projectid=util.get_projectid(projectid)
        
        if sa_path:
            os.environ['GOOGLE_APPLICATION_CREDENTIALS']=sa_path
            self.sa_path=sa_path
    
    def get_projectid(self):
        return self.projectid
    

    def connect(self,bucketid):    
        #Open connection
        try:
            #if self.sa_path:
            #    self.pubsub_client = self.pubsub_v1.PublisherClient.from_service_account_file(self.sa_path)
            #else
            storage_client = self.storage.Client(project=self.projectid)
            self.bucketid=bucketid
            self.bucket = storage_client.get_bucket(self.bucketid) 
            print('Connected to Cloud storage:  Project/Bucket: {}/{}'.format(self.projectid,self.bucketid))
            message="Connected to Cloud storage"
        except Exception as ex:
            print("Error: Cloud storage connection failed to Project/Bucket: {}/{}".format(self.projectid,bucketid))
            raise
            message="Eror connecting to Cloud storage"
        
        return message
        
    def upload_from_string(self,filename,dataset):
        blob = self.bucket.blob( filename ) 
        blob.upload_from_string( dataset) 
        return blob.public_url

    def download_as_string(self,filename):
        blob = self.bucket.blob( filename ) 
        return blob.download_as_string() 

class gcp_pubsub:
    def __init__(self,projectid=None,sa_path=None):
        from google.cloud import pubsub_v1
        self.pubsub_v1=pubsub_v1
        
        util=gcp_util()
        self.projectid=util.get_projectid(projectid)
        
        if sa_path:
            os.environ['GOOGLE_APPLICATION_CREDENTIALS']=sa_path
            self.sa_path=sa_path
    
    def get_projectid(self):
        return self.projectid
    
    def connect(self,topic):    
        #Open connection
        try:
            #if self.sa_path:
            #    self.pubsub_client = self.pubsub_v1.PublisherClient.from_service_account_file(self.sa_path)
            #    self.topic = self.pubsub_client.topic_path(self.projectid, topic) #topic = 'projects/' + PROJECTID + '/topics/' + topic
            #else
            self.pubsub_client = self.pubsub_v1.PublisherClient()
            self.topic = self.pubsub_client.topic_path(self.projectid, topic) #topic = 'projects/' + PROJECTID + '/topics/' + topic
            print('Connected to Cloud pubsub:  Project/topic: {}/{}'.format(self.projectid,self.topic))
            message="Connected to Cloud PubSub"
        except :
            print("Error: Cloud pubsub connection failed to Project/topic: {}/{}".format(self.projectid,topic))
            raise
            message="Eror connecting to Cloud PubSub"
        
        return message
 
    def publish_message(self,data,**kwargs):
        params={}
        if len(kwargs)>0:
            for key, value in kwargs.items():
                params[key]=value
        response = self.pubsub_client.publish(topic=self.topic,data=data,**params)
        
        return response

class gcp_firestore:
    def __init__(self,projectid=None,sa_path=None):
        import firebase_admin
        from firebase_admin import credentials
        from firebase_admin import firestore
        #from google.cloud import firestore
        self.firestore=firestore
        self.credentials=credentials
        self.firebase_admin=firebase_admin
        
        util=gcp_util()
        self.projectid=util.get_projectid(projectid)
        
        if sa_path:
            os.environ['GOOGLE_APPLICATION_CREDENTIALS']=sa_path
            self.sa_path=sa_path
        else:
            self.sa_path=None
    
    def get_projectid(self):
        return self.projectid
    
    def connect(self):    
        #Connect to firestore
        my_firestore=''
        try:
            # Use the application default credentials
            
            if (not len(self.firebase_admin._apps)):
                if self.sa_path:
                    # Use a service account
                    cred = credentials.Certificate(self.sa_path)
                else:
                    cred = self.credentials.ApplicationDefault()
                
                self.firebase_admin.initialize_app(cred, {
                  'projectId': self.projectid,
                })
            
            my_firestore = self.firestore.client() #project=self.projectid
            message="Connected to Cloud firestore"
        except:
            print("Error: firestore connection failed to Project: {}".format(self.projectid))
            raise    
            message="Eror connecting to Cloud firestore"
        
        return message,my_firestore


