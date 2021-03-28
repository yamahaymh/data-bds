import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('e:/data-bds/data-bds-firebase-adminsdk-fedtv-972503e67a.json')
# Up len git
# cred = credentials.Certificate('data-bds-firebase-adminsdk-fedtv-972503e67a.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

# Them du lieu collectio len firestore
doc_ref_collection = db.collection(u'Bandat')
