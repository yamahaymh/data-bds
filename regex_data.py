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