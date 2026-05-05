import urllib.request, json
from urllib.error import HTTPError

req = urllib.request.Request(
    'http://localhost:7860/simulate/create', 
    data=json.dumps({'num_ems':2,'num_fire':2,'num_police':2,'num_dispatcher':1,'grid_size':32,'seed':42,'weather_dynamic':True,'cascade_enabled':True,'curriculum_level':2,'max_steps':500, 'city': 'procedural'}).encode('utf-8'), 
    headers={'Content-Type': 'application/json'}
)

try:
    res = urllib.request.urlopen(req)
    print("Success:", res.read().decode())
except HTTPError as e:
    print("Error:", e.code)
    print(e.read().decode())
except Exception as e:
    print("Exception:", e)
