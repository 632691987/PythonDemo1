db_config = {
    "ip": "1234",
    "port": 5500,
    "uid": "admin",
    "password": "1q2w3e4R"
}


print(db_config["ip"])


db_config["vincentceng"] = "1212121" ## 动态添加
print(db_config)

for key, val in db_config.items():
    print(key, "=", val)

for key in db_config.keys():
    print(key, "=", db_config[key])