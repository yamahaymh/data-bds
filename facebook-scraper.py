from facebook_scraper import get_posts
import fire_store

for post in get_posts (group='489801751369828',pages = 1):
   doc_ref = fire_store.doc_ref_collection.document(post['post_id'])
   doc_ref.set({
      'Noidung' : post['text']
   })

