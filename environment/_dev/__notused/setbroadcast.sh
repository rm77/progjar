sysctl -w net.ipv4.icmp_echo_ignore_broadcasts=0
sysctl -w net.ipv4.conf.all.bc_forwarding=1
sysctl -w net.ipv4.conf.progjar-network.bc_forwarding=1
