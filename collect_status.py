#!/usr/bin/env python
import pynetbox
import urllib3
import config

urllib3.disable_warnings()


NETBOX_URL = "https://demo.netbox.dev/"
NETBOX_TOKEN = config.api_key

nb = pynetbox.api(url=NETBOX_URL, token=NETBOX_TOKEN)
nb.http_session.verify = False

devices = list(nb.dcim.devices.all())

status_cond = list(nb.dcim.devices.filter(tenant="noc", status="active"))
for device in status_cond:
    if device:
        print(
            "\n"
            "Name:\t{devname}"
            "\nTenant:\t{devtenant}"
            "\nManufacturer:\t{devmanufacturer}"
            "\nModel:\t{devmodel}"
            "\nOSversion:\t{devcustomfield}"
            "\nStatus:\t{devstatus}"
            "\nSite:\t{devsite}".format(
                devname=device.name,
                devtenant=device.tenant,
                devstatus=device.status["label"],
                devsite=device.site,
                devmodel=device.device_type["model"],
                devmanufacturer=device.device_type["manufacturer"]["display"],
                devcustomfield=device.custom_fields["sw_version"],
            )
        )