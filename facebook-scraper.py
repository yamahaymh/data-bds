from facebook_scraper import get_posts
import fire_store
import regex_data as rg

for post in get_posts (group='489801751369828',pages = 1):

   text = post['text']
   postid = post['post_id']
  # docs= fire_store.doc_ref_collection.stream()
   if postid != None:
      doc_ref = fire_store.doc_ref_collection.document(postid)
      doc_ref.set({
         'Giá' : rg.gia(text),
         'SĐT' : rg.sdt(text),
         'Kích thước' : rg.kichthuoc(text),
         'Noidung' : text
      })
   else:
      None
      