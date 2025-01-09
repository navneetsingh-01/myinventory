import os
import json

extra_vars = json.loads(os.getenv("ANSIBLE_EXTRA_VARS", "{}"))
target_hosts = extra_vars.get("hosts", [])
environment = extra_vars.get("environment", "unknown")

def generate_inventory(hosts, env):
    return {
        "all": {
            "hosts": hosts,
            "vars": {
                "environment": env
            }
        }
    }

if __name__ == "__main__":
    inventory = generate_inventory(target_hosts, environment)
    print(json.dumps(inventory))