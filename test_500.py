import urllib.request, json
from urllib.error import HTTPError

req = urllib.request.Request(
    'https://rajadityaaaaaa-file2-openenv.hf.space/simulate/create', 
    data=json.dumps({'num_ems':2,'num_fire':2,'num_police':2,'num_dispatcher':1,'grid_size':32,'seed':42,'weather_dynamic':True,'cascade_enabled':True,'curriculum_level':2,'max_steps':500, 'city': 'procedural', 'deception_prob': 0.3}).encode('utf-8'), 
    headers={'Content-Type': 'application/json'}
)

try:
    response = urllib.request.urlopen(req)
    print("Success:", response.read().decode())
except HTTPError as e:
    print("Error:", e.code, e.read().decode())
