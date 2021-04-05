from algoliasearch.search_client import SearchClient

client = SearchClient.create('7HGG4UE4R4','a231a7cc19ce990e955a6b8db62c3fa5')
index = client.init_index('bds')

records = [
    {'name': 'Tom Cruise'},
    {'name': 'Scarlett Johansson'}
]
index.save_objects(records,  {'autoGenerateObjectIDIfNotExist': True})