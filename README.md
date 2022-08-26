# splunkes_snmptrap
Send SplunkES incidents to OpenNMS via snmp.

## Setup 
1. Install OpenNMS
2. Modify eventconf:
/etc/opennms/eventconf.xml
Needs the first `<event>...</event>` segment to define how the event is supposed to look.
3. Compile mib file on OpenNMS server:
"Configure OpenNMS" -> "SNMP MIB Compiler" -> "Upload MIB" -> "Compile Mib"
4. Reboot opennms server

5. Install snmptrap on the SplunkES server (e.g. yum install net-snmp-utils)

5. Add Splunk-ES-MIB.mib file on the SplunkES server, path should be:
/usr/share/snmp/mibs/Splunk-ES-MIB.mib

6. Test sending a trap manually from the SplunkES server, e.g.:
/usr/bin/snmptrap -v 2c -c public opennms-server-ip "" Splunk-ES-MIB::splunkIncidentAlertNotification splunkIncidentAlertTitle s "SplunkES: Portscan detected" splunkIncidentAlertText s "Portscan from IP 10.10.10.10 on 123 unique IPs."

7. Register a script for sending snmptraps on your SplunkES server:
add the content of 'commands.conf' to '/opt/splunk/etc/apps/SplunkEnterpriseSecuritySuite/local/commands.conf'

8. Copy snmptrap.py to /opt/splunk/etc/apps/SplunkEnterpriseSecuritySuite/bin

9. Define the IP adress of the OpenNMS server in snmptrap.py

10. You should be able to send traps from the SplunkES WebGUI with:
| script snmptrap 'traptitle' 'traptext'
