# Copyright: (c) 2024, Dell Technologies

"""NTP operations"""

# pylint: disable=duplicate-code

import os
from PyPowerStore import powerstore_conn

CONN = powerstore_conn.PowerStoreConn(
    username=os.getenv("POWERSTORE_USERNAME", "<username>"),
    password=os.getenv("POWERSTORE_PASSWORD", "<password>"),
    server_ip=os.getenv("POWERSTORE_SERVER_IP", "<server_ip>"),
    verify=True,  # SECURITY: Always verify SSL certificates in production
    timeout=180.0,
)

# Getting NTP list
ntp_list = CONN.config_mgmt.get_ntp_list()
print(ntp_list)

# Getting NTP instance details
ntp_details = CONN.config_mgmt.get_ntp_details(ntp_id=ntp_list[0]["id"])
print(ntp_details)

# Modifying the NTP addresses
modify_dict = {"addresses": ["XX.XX.XX.XX", "XX.XX.XX.YY"]}

resp_modify = CONN.config_mgmt.modify_ntp_details(
    ntp_id=ntp_list[0]["id"], modify_parameters=modify_dict,
)
print(resp_modify)
