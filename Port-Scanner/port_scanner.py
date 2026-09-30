
import socket
import threading
from datetime import datetime
all_results = []
lock = threading.Lock()  


def scan_one_port(host, port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  

    try:
        result = sock.connect_ex((host, port))

        if result == 0:
          
            try:
                service_name = socket.getservbyport(port)
            except:
                service_name = "unknown"
            status = "open"
        else:
         
            service_name = ""
            status = "closed"

    except socket.timeout:
        status = "timeout"
        service_name = ""

    except socket.gaierror:
       
        status = "error"
        service_name = "host not found"

    sock.close()
    with lock:
        all_results.append((host, port, status, service_name))
        if status == "open":
            print(f"[+] {host}:{port} OPEN - {service_name}")
        elif status == "timeout":
            print(f"[!] {host}:{port} TIMEOUT")
        elif status == "error":
            print(f"[x] {host}:{port} ERROR - {service_name}")
def get_host_list(host_input):
   
    host_input = host_input.strip()

    if "-" in host_input:
        start_ip, end_ip = host_input.split("-")
        start_ip = start_ip.strip()
        end_ip = end_ip.strip()

        ip_parts = start_ip.split(".")
        base_ip = ip_parts[0] + "." + ip_parts[1] + "." + ip_parts[2]

        start_number = int(ip_parts[3])
        end_number = int(end_ip.split(".")[3])

        host_list = []
        for i in range(start_number, end_number + 1):
            host_list.append(base_ip + "." + str(i))

        return host_list
    else:

        return [host_input]


def save_to_file(filename, results):
   
    file = open(filename, "w")
    file.write("Port Scan Results\n")
    file.write("Date: " + str(datetime.now()) + "\n")
    file.write("-" * 30 + "\n")

    for host, port, status, service in results:
        line = host + ":" + str(port) + " - " + status.upper()
        if service:
            line += " (" + service + ")"
        file.write(line + "\n")

    file.close()
    print(f"\nResult saved: {filename}")


def main():
    print("=== TCP Port Scanner ===\n")
    host_input = input("Add host or host range (like 127.0.0.1): ")
    start_port = int(input("Start port: "))
    end_port = int(input("End port: "))
    hosts = get_host_list(host_input)

    print(f"\nScanning {len(hosts)} host(s), port {start_port} se {end_port} tak...\n")
    threads = []

    for host in hosts:
        for port in range(start_port, end_port + 1):
            t = threading.Thread(target=scan_one_port, args=(host, port))
            threads.append(t)
            t.start()
    for t in threads:
        t.join()

    print("\nScan complete!")

    open_count = 0
    closed_count = 0
    for r in all_results:
        if r[2] == "open":
            open_count += 1
        elif r[2] == "closed":
            closed_count += 1

    print(f"Total: {open_count} open, {closed_count} closed")

    save_to_file("scan_results.txt", all_results)

if __name__ == "__main__":
    main()
