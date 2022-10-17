import http.client
import json
import os

config_dir = "/app/configs/"

os.makedirs(config_dir, exist_ok=True)
if os.path.exists("/app/configs"):
    print("config folder created")
else:
    print("config folder creation error")

conn = http.client.HTTPConnection(os.environ["CONSUL_HOST"] + ":" + os.environ["CONSUL_PORT"])
payload = ""
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "X-Consul-Token": os.environ["CONSUL_ACL_TOKEN"],
    "Referer": "http://" + os.environ["CONSUL_HOST"] + ":" + os.environ["CONSUL_PORT"] + "/v1/kv/",
    "Accept-Language": "en-GB,en;q=0.9,en-US;q=0.8",
}
conn.request("GET", "/v1/kv/" + os.environ["CONSUL_CONFIG"] + "/?keys", payload, headers)
res = conn.getresponse()
config_file_list = res.read()
config_file_list = config_file_list.decode("utf-8")
config_file_list = json.loads(config_file_list)

print(config_file_list)

headers["Referer"] = (
    "http://" + os.environ["CONSUL_HOST"] + ":" + os.environ["CONSUL_PORT"] + "/v1/kv/" + os.environ["CONSUL_CONFIG"]
)

for config_file_path in config_file_list:
    config_file_name = config_file_path.split("/")[-1]
    conn.request("GET", "/v1/kv/" + config_file_path + "?raw", payload, headers)
    config_file_data = conn.getresponse()
    config_file_data = config_file_data.read().decode("utf-8")
    target_file = os.path.join(config_dir, config_file_name)

    with open(target_file, "w", encoding="utf-8") as fw:
        fw.writelines(config_file_data)
        print(f"Downloaded {config_file_name} at {target_file}")
