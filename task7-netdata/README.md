Task 7: Monitor System Resources Using Netdata
Objective

Install and run Netdata using Docker to visualize system and application performance metrics in real time.

Tools Used

Netdata – Free, open-source monitoring tool

Docker – For containerized deployment

Steps Performed

Run Netdata in Docker

docker run -d \
  --name=netdata \
  -p 19999:19999 \
  --cap-add=SYS_PTRACE \
  --security-opt apparmor=unconfined \
  netdata/netdata


Access the Dashboard

Open browser and visit: http://localhost:19999

Metrics Observed

CPU usage

RAM usage

Disk read/write speed

Network inbound/outbound traffic

System load

Explore Alerts & Logs

Alerts: Available from the Health tab in the dashboard.

Logs (via container shell):

docker exec -it netdata /bin/bash
cat /var/log/netdata/error.log

Screenshot

![alt text](netdata_dashboard.png-1.png)

Conclusion

Netdata provides an easy-to-use, web-based interface for real-time system monitoring. Running it in Docker makes it portable and quick to set up.