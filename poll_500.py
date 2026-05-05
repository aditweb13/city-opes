import urllib.request, json, time
from urllib.error import HTTPError
req = urllib.request.Request(
    'https://rajadityaaaaaa-file2-openenv.hf.space/simulate/create', 
    data=json.dumps({'num_ems':2,'num_fire':2,'num_police':2,'num_dispatcher':1,'grid_size':32,'seed':42,'weather_dynamic':True,'cascade_enabled':True,'curriculum_level':2,'max_steps':500,'city':'procedural'}).encode('utf-8'), 
    headers={'Content-Type': 'application/json'}
)
for i in range(30):
    try:
        res = urllib.request.urlopen(req)
        if res.status == 200:
            print(res.read())
            break
    except HTTPError as e:
        print("HTTP Error:", e.code, e.reason)
        if e.code == 500:
            print(e.read())
            break
    except Exception as e:
        print("Waiting...")
    time.sleep(5)
