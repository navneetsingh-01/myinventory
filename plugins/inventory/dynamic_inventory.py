import os
import json

extra_vars = json.loads(os.getenv("ANSIBLE_EXTRA_VARS", "{}"))
target_hosts = extra_vars.get("hosts", [])

def generate_inventory(hosts):
    return {
        "all": {
            "hosts": hosts
        }
    }

if __name__ == "__main__":
    inventory = generate_inventory(target_hosts)
    print(json.dumps(inventory))