import socket, time, os

UDP_IP = "0.0.0.0"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
sock.settimeout(2.0)

nodes = {"10.0.0.2": time.time(), "10.0.0.3": time.time()}
blocked_nodes = []

print("[*] Network Monitor Started. Listening for agent status updates...")

while True:
    try:
        data, addr = sock.recvfrom(1024)
        ip = addr[0]
        nodes[ip] = time.time()
        print(f"[LOG] Status Update received from {ip} at {time.ctime()}")
    except socket.timeout:
        pass 

    current_time = time.time()
    for ip, last_seen in nodes.items():
        if (current_time - last_seen) > 5.0 and ip not in blocked_nodes:
            print(f"\n[ALERT] Device {ip} is UNREACHABLE! Link failure detected.")
            print(f"[SDN INTEGRATION] Applying dynamic policy: Blocking {ip} at switch s1.")
            os.system(f"sudo ovs-ofctl add-flow s1 ip,nw_src={ip},actions=drop")
            blocked_nodes.append(ip)
            print(f"[POLICY] Traffic from {ip} is now dropped.\n")
