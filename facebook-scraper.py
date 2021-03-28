from facebook_scraper import get_posts
import fire_store
import regex_data as rg

group1='2023588204354732' #BĐS Đồng Tháp có giá trị lớn
group2='489801751369828'  # Nhà đất Đồng Tháp
group3='279200489509507'  # Nhà đất Tp Cao Lãnh

for post in get_posts (group=group1,pages = 1):

   text = post['text']
   postid = post['post_id']
   time = post['time']
   url = "https://www.facebook.com/groups/"+group1+"/permalink/"+str(postid)

   if rg.canmua(text):
      None
   else:
   # docs= fire_store.doc_ref_collection.stream()
      if postid != None:
         doc_ref = fire_store.doc_ref_collection.document(postid)
         doc_ref.set({
            '0_Thời gian': time,
            '1_Giá' : rg.gia(text),
            '3_SĐT' : rg.sdt(text),
            '2_Kích thước' : rg.kichthuoc(text),
            '4_Noidung' : text,
            '5_URL': url
         })
      else:
         None
      