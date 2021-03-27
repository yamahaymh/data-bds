from facebook_scraper import get_posts
import fire_store
import regex_data as rg

for post in get_posts (group='489801751369828',pages = 1):

   text = post['text']

   doc_ref = fire_store.doc_ref_collection.document(post['post_id'])
   doc_ref.set({
      'Giá' : rg.gia(text),
      'SĐT' : rg.sdt(text),
      'Kích thước' : rg.kichthuoc(text),
      'Noidung' : text

   })