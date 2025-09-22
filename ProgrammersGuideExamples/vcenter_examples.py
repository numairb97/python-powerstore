# Copyright: (c) 2024, Dell Technologies

"""Vcenter Operations"""

# pylint: disable=invalid-name,duplicate-code

import os
from PyPowerStore import powerstore_conn

CONN = powerstore_conn.PowerStoreConn(
    username=os.getenv("POWERSTORE_USERNAME", "<username>"),
    password=os.getenv("POWERSTORE_PASSWORD", "<password>"),
    server_ip=os.getenv("POWERSTORE_SERVER_IP", "<IP>"),
    verify=True,  # SECURITY: Always verify SSL certificates in production
    application_type="<Application>",
    timeout=180.0,
)
print(CONN)

# Get Vcenter list
vcenters_list = CONN.config_mgmt.get_vcenters()
print(vcenters_list)

# Get Vcenter details by vcenter_id
vcenter_details = CONN.config_mgmt.get_vcenter_details(
    vcenter_id=vcenters_list[0]["id"],
)
print(vcenter_details)

# Register VASA provider
param_dict = {
    "vasa_provider_credentials": {
        "username": "<<admin_user>>",
        "password": "<<admin_password>>",
    },
}

vcenter_details = CONN.config_mgmt.modify_vcenter(
    vcenter_id=vcenters_list[0]["id"], modify_param_dict=param_dict,
)
print(vcenter_details)

# Add vCenter
add_dict = {
    "address": "vcenter IP/hostname",
    "username": "vcenter username",
    "password": "vcenter password",
    "vasa_provider_credentials": {
        "username": "<<admin_user>>",
        "password": "<<admin_password>>",
    },
}

vcenter_id = CONN.config_mgmt.add_vcenter(add_params=add_dict)
print(vcenter_id)

# Remove a vCenter
remove_vasa = True
print(
    CONN.config_mgmt.remove_vcenter(
        vcenter_id=vcenters_list[0]["id"], delete_vasa_provider=remove_vasa,
    ),
)
