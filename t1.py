import requests



base_url = 'http://127.0.0.1:8080'
data = dict(header="some_header",
            discrpt="some_disc",
            owner_id="some_id")
res = requests.post(base_url + '/add/', json=data)
print(res.json())

res2 = requests.get(base_url + f'/get/{res.json()["adv_id"]}')
print(res2.json())

print('Update test')
data2 = dict(adv_id=res.json()["adv_id"], header="updated_header")
requests.put(base_url + '/put/', json=data2)

res2 = requests.get(base_url + f'/get/{res.json()["adv_id"]}')
print(res2.json())


requests.delete(base_url + f'/delete/{res.json()["adv_id"]}')

res2 = requests.get(base_url + f'/get/{res.json()["adv_id"]}')
print(res2.json())


# tuid = add_adv(header="some_header",
#                 discrpt="some_disc",
#                 owner_id="some_id")
# print(get_adv(tuid))
# delete_adv(tuid)
# print(get_adv(tuid))
