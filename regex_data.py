import re
noidung = 0

def gia (noidung):
    try:
        gia = re.search(r"\d+\s*[,.-;]*\s*\d*\s*(ty|tỷ|ti|tỉ|trieu|triệu|tr|đ|đong|đồng|vnd)\b",noidung,re.IGNORECASE)
        return gia.group()
    except:
        None
    
def sdt (noidung):
    try:
        sdt = re.search(r"\b0([-_.,\s]*?\d){9}\b",noidung,re.IGNORECASE)
        return sdt.group()
    except:
        None

def kichthuoc (noidung):
    try:
        kichthuoc = re.search(r"\d.*[x\*X]\s*\d+.*",noidung,re.IGNORECASE)
        return kichthuoc.group()
    except:
        None

def canmua (noidung):
    try:
        canmua = re.search(r"tìm|cần tìm|can tim|cần tim|can tìm|càn tìm|càn tim|cân tim|cân tìm|cần mua|can mua|cân mua|càn mua|cần mu|cần nền|can nen|càn nen|cân nen|can nền|can nèn|can nên|cần thuê|thuê|can thue|cân thue|cần nhà|can nhà|cân nhà|càn nhà|cần nhà|mua dat|mua đất|muadat|mua đát'",noidung,re.IGNORECASE)
        return canmua.group()
    except:
        None