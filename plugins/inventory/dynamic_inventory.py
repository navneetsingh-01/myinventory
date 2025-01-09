import os
import json
from ansible.plugins.inventory import BaseInventoryPlugin, Constructable, Cacheable
from ansible.errors import AnsibleError

extra_vars = json.loads(os.getenv("ANSIBLE_EXTRA_VARS", "{}"))
target_host = extra_vars.get("hosts", [])

class InventoryModule(BaseInventoryPlugin, Constructable, Cacheable):
    NAME = "dynamic_inventory_webhook"

    def verify_file(self, path):
        """Verify if the file is a valid configuration file for this plugin"""
        valid = super(InventoryModule, self).verify_file(path)
        if valid:
            if path.endswith((".yaml", ".yml")):
                return True
        return False

    def parse(self, inventory, loader, path, cache=True):
        """Parse the inventory file and populate the inventory"""
        super(InventoryModule, self).parse(inventory, loader, path)

        print(extra_vars)

        self.inventory.add_host(target_host)