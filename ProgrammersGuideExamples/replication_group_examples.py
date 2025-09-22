# Copyright: (c) 2024, Dell Technologies

"""Replication Group operations"""

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
print(CONN)

# Get Replication Group list
repl_group_list = CONN.protection.get_replication_groups()
print(repl_group_list)

# Get Replication Group details
repl_group_details = CONN.protection.get_replication_group_details(
    repl_group_list[0]["id"],
)
print(repl_group_details)

# Get Replication Group by name
repl_group_details = CONN.protection.get_replication_group_details_by_name(
    repl_group_list[0]["name"],
)
print(repl_group_details)
