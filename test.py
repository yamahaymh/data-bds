import re
noidung = '''
Đường Nguyễn Thái Học (phường Hòa Thuận) đoạn hàng me, rẽ trái vào đường nhà trọ Quốc Huy (đường dal rộng 4m) khoảng 100m. Khu vực an ninh, chiếu sáng và điện nước đầy đủ
Diện tích 5x35, có 100m đất ở đô thị.
Giá 2 ti
Liên hệ chính chủ: 0918496963 (Tài)

'''
gia = re.search(r"(\d+\s*[,.;]*\s*\d*\s*)(ty|tỷ|ti|tỉ|trieu|triệu|tr|đ|đong|đồng|vnd)\b",noidung,re.IGNORECASE)
print(gia.group())