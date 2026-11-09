# Network Monitoring and Alert System (SDN)

## Architecture & Problem Statement
This project implements a dynamic Network Monitoring and Alert System using UDP sockets and Software-Defined Networking (SDN). The system monitors network device availability and dynamically applies traffic-management policies when nodes fail.

*   **Topology:** Mininet single-switch topology with 3 hosts (`sudo mn --topo=single,3`).
*   **Monitor (Host 1):** Acts as the central server, tracking UDP heartbeats from agents.
*   **Agents (Host 2 & 3):** Send lightweight UDP status updates every 1 second.
*   **SDN Integration:** If a node stops responding for 5 seconds (simulating link failure or crash), the Monitor dynamically pushes an OpenFlow rule to the Open vSwitch to drop all traffic from the faulty IP, protecting the network from rogue behavior.

## How to Run the Demo
1. Start Mininet: `sudo mn --topo=single,3 --mac`
2. Open host terminals: `xterm h1 h2 h3`
3. Start agents on Host 2 & 3: `python3 agent.py`
4. Start monitor on Host 1: `python3 monitor.py`

## Robustness & Dynamic Policy Testing
1. While the system is running, press `Ctrl+C` on `h3` to simulate a service failure.
2. Observe `h1`: After 5 seconds, an alert is generated and an SDN policy is pushed.
3. Verify the block: Run `h3 ping -c 3 h1` in the Mininet CLI to confirm 100% packet loss, proving the dynamic SDN quarantine rule is active.
