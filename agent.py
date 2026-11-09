import socket, time

MONITOR_IP = "10.0.0.1"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(f"[*] Agent started. Sending periodic status updates to {MONITOR_IP}...")

try:
    while True:
        sock.sendto(b"HEARTBEAT_STATUS: OK", (MONITOR_IP, UDP_PORT))
        time.sleep(1)
except KeyboardInterrupt:
    print("\n[*] Agent shutting down.")
