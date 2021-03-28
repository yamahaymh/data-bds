import fire_store
danhsach =[]
docs= fire_store.doc_ref_collection.stream()

for doc in docs:
    danhsach.append(doc.id)
print(danhsach)
len(danhsach)