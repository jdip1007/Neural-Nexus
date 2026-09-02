---
title: Networking
created: 2026-09-02
updated: 2026-09-02
type: concept
classification: technology.networking
domain: technology
tags: [networking, technology, ethernet, protocols]
sources: []
confidence: high
status: active
reviewed: 2026-09-02
backlinks: []
---

# Networking

Networking is the practice of connecting computers and other devices to share resources and communicate with each other. It encompasses both the physical hardware (cables, routers, switches) and the software protocols that enable data transmission.

## Overview

Networks form the backbone of modern computing, enabling everything from local file sharing to global internet connectivity. Understanding networking principles is essential for system administrators, developers, and IT professionals.

## Types of Networks

### Local Area Networks (LAN)
- Connects devices within a limited area (home, office, building)
- Typically uses Ethernet cables or Wi-Fi
- Managed by local network administrators
- High speed and low latency

### Wide Area Networks (WAN)
- Spans large geographical areas
- Connects multiple LANs together
- Uses leased lines, satellites, or internet connections
- Examples: Internet, corporate networks across cities

### Metropolitan Area Networks (MAN)
- Spans a metropolitan area
- Larger than LAN but smaller than WAN
- Often operated by telecommunications companies
- High-speed backbone for city-wide connectivity

### Personal Area Networks (PAN)
- Connects devices within personal space
- Short-range wireless connections
- Examples: Bluetooth, NFC connections
- Used for connecting personal devices

## Network Protocols

### TCP/IP Suite
- **Transmission Control Protocol (TCP)**: Reliable, connection-oriented data transfer
- **Internet Protocol (IP)**: Addressing and routing of packets
- **User Datagram Protocol (UDP)**: Fast, connectionless data transfer
- **HTTP/HTTPS**: Web communication protocols
- **FTP**: File transfer protocol

### Ethernet Standards
- **10BASE-T**: 10 Mbps over twisted pair
- **100BASE-TX**: Fast Ethernet at 100 Mbps
- **1000BASE-T**: Gigabit Ethernet at 1 Gbps
- **10GBASE-T**: 10 Gigabit Ethernet
- **CANBUS**: Controller Area Network for vehicles

### Wireless Protocols
- **Wi-Fi (IEEE 802.11)**: Wireless local area networking
- **Bluetooth**: Short-range personal area networking
- **5G**: Fifth-generation cellular technology
- **LTE**: Long-Term Evolution for mobile broadband

## Network Topologies

### Bus Topology
- Single cable connects all devices
- Simple and inexpensive
- Limited scalability
- Single point of failure

### Star Topology
- All devices connect to central hub/switch
- Easy to manage and troubleshoot
- Scalable
- Central point of failure

### Ring Topology
- Devices connected in circular fashion
- Equal access for all devices
- Difficult to troubleshoot
- Single failure affects entire network

### Mesh Topology
- Multiple interconnections between devices
- High redundancy and reliability
- Complex and expensive
- Self-healing capabilities

## Network Devices

### Routers
- Connect different networks
- Use IP addresses for routing
- Operate at Layer 3 (Network layer)
- Examples: Home routers, enterprise routers

### Switches
- Connect devices within same network
- Use MAC addresses for switching
- Operate at Layer 2 (Data Link layer)
- Examples: Ethernet switches, managed switches

### Hubs
- Simple connection points
- Broadcast traffic to all ports
- Deprecated in modern networks
- Low cost but inefficient

### Access Points
- Provide wireless connectivity
- Convert wired to wireless signals
- Manage wireless clients
- Examples: Wi-Fi access points

## Network Security

### Firewalls
- Monitor and control network traffic
- Filter incoming and outgoing packets
- Can be hardware or software-based
- Examples: pfSense, Cisco ASA, Windows Firewall

### VPNs (Virtual Private Networks)
- Create secure connections over public networks
- Encrypt data for privacy
- Enable remote access to private networks
- Examples: OpenVPN, IPsec, WireGuard

### Intrusion Detection/Prevention
- Monitor network for suspicious activity
- Alert administrators or automatically block threats
- Use signatures and anomaly detection
- Examples: Snort, Suricata

## Network Troubleshooting

### Common Issues
- **Connectivity problems**: Physical cable issues, misconfigured IP addresses
- **Performance issues**: Bandwidth limitations, network congestion
- **Security breaches**: Unauthorized access, malware propagation
- **Configuration errors**: Incorrect settings, misconfigured devices

### Diagnostic Tools
- **ping**: Test basic connectivity
- **traceroute**: Trace path to destination
- **ipconfig/ifconfig**: Display network configuration
- **netstat**: Show network connections and statistics
- **Wireshark**: Detailed packet analysis

## Related Pages

- [[Dave's Garage]] - Networking tutorials and projects
- [[Ethernet]] - Specific networking technology
- [[Programming]] - Network programming and protocols
- [[Technology]] - Broader technology concepts
- [[Security]] - Network security best practices

## External Resources

- [Network Fundamentals (Cisco)](https://www.cisco.com/c/en/us/training-events/training-certifications/certifications/associate/ccna.html)
- [CompTIA Network+](https://www.comptia.org/training/resources/exam-objectives/network)
- [Network Uptime](https://www.networkup.com/)
- [Packet Pushers](https://packetpushers.net/)
- [Network World](https://www.networkworld.com/)

---
*Created: 2026-09-02 20:50:40*