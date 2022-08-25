# splunkes_snmptrap
Send SplunkES incidents to OpenNMS via snmp.

## Setup 
1. Install OpenNMS
2. Modify eventconf:
/etc/opennms/eventconf.xml
Needs the first <event>...</event> segment to define how the event is supposed to look.
3. Compile mib file on OpenNMS server:
"Configure OpenNMS" -> "SNMP MIB Compiler" -> "Upload MIB" -> "Compile Mib"
4. Reboot opennms server

5. Add Splunk-ES-MIB.mib file on the snmp client, path should be:
/var/lib/opennms/mibs/compiled/Splunk-ES-MIB.mib
6. Test sending a trap from the snmp client, e.g.:
/usr/bin/snmptrap -v 2c -c public localhost "" Splunk-ES-MIB::splunkIncidentAlertNotification splunkIncidentAlertTitle s "SplunkES: Portscan detected" splunkIncidentAlertText s "Portscan from IP 10.10.10.10 on 123 unique IPs."
