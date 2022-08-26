# Script for sending snmp traps to OpenNMS
#
# Usage:
# | snmptrap <alerttitle> <alerttext>
#
# Example:
# | script snmptrap "New Domain Admin" "User x1malicious added to group "domain admins" by a1compromised."

import sys
import os

# This is the server the snmptrap is sent to.
openNMS_server = "localhost"

# First two arguments to the script call are the title and the text
alert_title = sys.argv[1]
alert_text = sys.argv[2]

# Assemble the snmptrap command we will send to the openNMS server
# Boilerplate and servername
trap_command = f"/usr/bin/snmptrap -v 2c -c public {openNMS_server} 0 "
# Define the mib file we are using
trap_command += f"Splunk-ES-MIB::splunkIncidentAlertNotification "
# Add a title for the alert (bolded)
trap_command += f"splunkIncidentAlertTitle s '{alert_title}' "
# Add the text of the alert
trap_command += f"splunkIncidentAlertText s '{alert_text}' "
# Add logging
trap_command += " > /tmp/snmptrap.log 2>&1"
 
# Write the command to a temp file for debugging
debug = True
if debug:
        with open("/tmp/test_snmpcmd.log", "w") as outfile:
             outfile.write(trap_command)

# Execute the snmptrap command
# Note: we execute partially user-controlled code without security checks.
# This can lead to unwanted privilege escalation/GUI->server escape.
# Make sure to either include more input sanitation or to only led trusted users execute this script.
os.system(trap_command)
