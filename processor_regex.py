import re

def classify_with_regex(log_message):
    regex_patterns = {
        r"nova.osapi_compute.wsgi.server \[req-([a-f0-9\- \].\"]+)GET \/v2\/54fadb412c4e40cdbaed9335e4c35a9e\/servers\/detail HTTP\/1.1\" ([a-z:0-9\- \].\" A-Z]*)": "HTTP Status",
        r"nova.metadata.wsgi.server \[([-a-z\] 0-9.,]+)\"GET \/openstack\/201([0-9])-([0-9]+)-([0-9]+)([a-z_. \/]+)HTTP\/1.1\" ([A-Za-z 0-9:.]*)": "HTTP Status",
        r"Backup completed successfully\.?": "System Notification",
        r"Backup ended at 2025-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}\.?": "System Notification",
        r"Disk cleanup completed successfully\.?": "System Notification",
        r"User User([0-9]+) logged out\.?": "User Action",
        r"File data_([0-9]{4})\.csv uploaded successfully by user User([0-9]{3})\.?": "System Notification",
        r"nova.osapi_compute.wsgi.server \[req-([a-zA-Z: 0-9.-]*)] 10.11.10.1 \"POST \/v2\/e9746973ac574cf56b8a9e88576a7608\/os-server-external-events HTTP\/1.1\"([a-zA-z0-9 -:]*)": "HTTP Status",
        r"nova.compute.claims \[req-([a-zA-Z: 0-9.-]*)] \[instance: ([a-zA-Z: 0-9.-]*)] ([a-zA-Z: 0-9.-]*), ([a-zA-Z: 0-9.-]*)": "Resource Usage",
        r"System reboot initiated by user User([0-9]{3})\.?": "System Notification",
        r"Backup started at 2025-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}\.?": "System Notification",
        r"nova.metadata.wsgi.server \[([-a-z0-9 ]*)] 10.11.21.1([0-9,.]*) \"GET \/latest\/meta-data\/block-device-mapping\/([ a-z]*)HTTP\/1.1\" ([sStatus codeHTTP:-]*)200 len: 124 time: 0.([0-9]*)": "HTTP Status",
        r"nova.metadata.wsgi.server \[([-a-z0-9 ]*)] 10.11.21.1([0-9,.]*) \"GET \/latest\/meta-data\/([placement \/]*)HTTP\/1.1\" ([ status HTTP cdoeRCODE:-]*)200 len: ([-a-z0-9 ]*): 0.([0-9]*)": "HTTP Status",
        r"nova.compute.claims \[req-([0-9a-f\-]*) ([0-9a-f]*) ([0-9a-f]*) - - -\] \[instance: ([0-9a-f\-]*)\] Attempting claim: memory 2048 MB, disk 20 GB, vcpus 1 CPU": "Resource Usage",
        r"nova.compute.claims \[req-([0-9a-f\-]*) ([0-9a-f]*) ([0-9a-f]*) - - -\] \[instance: ([0-9a-f\-]*)\] Total disk: 15 GB, used: 0.00 GB": "Resource Usage",
        r"/nova.compute.claims \[req-([0-9a-f\-]*) ([0-9a-f]*) ([0-9a-f]*) - - -\] \[instance: ([0-9a-f\-]*)\] Total vcpu: 16 VCPU, used: 0.00 VCPU/gm": "Resource Usage",
        r"nova.compute.claims \[req-([0-9a-f\-]*) ([0-9a-f]*) ([0-9a-f]*) - - -\] \[instance: ([0-9a-f\-]*)\] vcpu limit not specified, defaulting to unlimited": "Resource Usage",
        r"nova.compute.claims \[req-([0-9a-f\-]*) ([0-9a-f]*) ([0-9a-f]*) - - -\] \[instance: ([0-9a-f\-]*)\] disk limit not specified, defaulting to unlimited": "Resource Usage",
        r"([A-Za-z ]*)health check([A-Za-z ]*)\.?": "Error",
        r"nova.metadata.wsgi.server \[([a-z0-9 -]*)\] 10.11.21.1([0-9,.]*) \"GET \/openstack\/2013-10-17\/user_data HTTP\/1.1\" ([RCODE status:codeHTTP-]*)404 len: 176 time: 0.([0-9]*)": "HTTP Status",
        r"nova.compute.resource_tracker \[req-([0-9a-f\-]*) - - - - -\] Final resource view: name=.* phys_ram=[0-9]+MB used_ram=[0-9]+MB phys_disk=[0-9]+GB used_disk=[0-9]+GB total_vcpus=[0-9]+ used_vcpus=[0-9]+ pci_stats=\[\]": "Resource Usage",
        r"nova.compute.resource_tracker \[req-([0-9a-f\-]*) - - - - -\] Total usable vcpus: [0-9]+, total allocated vcpus: [0-9]+": "Resource Usage",
        r"Account with ID .* created by.*": "User Action",
        r"User User([0-9]+) logged in\.?": "User Action",
        r"Backup started at [0-9]{2}:[0-9]{2}\.?": "System Notification",
        r"System updated to version [0-9]+\.[0-9]+\.[0-9]+\.?": "System Notification"
,r"File .* uploaded successfully by user .*": "System Notification"
,r"System reboot initiated ?by user User?[0-9]+\.?": "System Notification"


    }

    for pattern, label in regex_patterns.items():
        if re.search(pattern, log_message, re.IGNORECASE):
            return label
    return None

# Example test
if __name__ == "__main__":
    print(classify_with_regex("User User123 logged in."))                                 # User Action
    print(classify_with_regex("Backup started at 12:08."))                                # System Notification
    print(classify_with_regex("Backup completed successfully."))                          # System Notification
    print(classify_with_regex("System updated to version 1.0.8."))                        # System Notification
    print(classify_with_regex("File file1.txt uploaded successfully by user user1"))      # System Notification
    print(classify_with_regex("Disk cleanup completed successfully."))                    # System Notification
    print(classify_with_regex("System reboot initiatedby user user1."))                   # System Notification
    print(classify_with_regex("Hey Bro"))                                                 # None
    print(classify_with_regex("Account with ID A0098234 created by Dhaval"))              # User Action
    print(classify_with_regex("User User494 logged out."))                                # User Action