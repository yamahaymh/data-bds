from facebook_scraper import get_posts
import fire_store
import regex_data as rg
from algoliasearch.search_client import SearchClient

group1='2023588204354732' #BĐS Đồng Tháp có giá trị lớn
group2='489801751369828'  # Nhà đất Đồng Tháp
group3='279200489509507'  # Nhà đất Tp Cao Lãnh

for post in get_posts (group=group2,pages = 1):

   text = post['text']
   postid = post['post_id']
   time = post['time']
   url = "https://www.facebook.com/groups/"+group2+"/permalink/"+str(postid)
   # Loại bỏ cần mua không thực hiện
   if rg.canmua(text):
      None
   else:
      # Nếu postid khác rỗng thì thực hiện lệnh:
      if postid != None:
         # Up firecloud
         doc_ref = fire_store.doc_ref_collection.document(postid)
         doc_ref.set({
            '0_Thời gian': time,
            '1_Giá' : rg.gia(text),
            '3_SĐT' : rg.sdt(text),
            '2_Kích thước' : rg.kichthuoc(text),
            '4_Noidung' : text,
            '5_URL': url
         })
         
         # Push Algolia
         client = SearchClient.create('7HGG4UE4R4','a231a7cc19ce990e955a6b8db62c3fa5')
         index = client.init_index('bds')

         records = {
            "objectID": str(postid),
            "4_Noidung": text
         }
         index.save_objects(records)
      #Nếu postid rỗng thì ko làm gì.
      else:
         None
      