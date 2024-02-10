def map_name_and_ip(n):
    ip_to_name = {}
    for _ in range(n):
        parts = input().split()
        name, ip = parts[0], parts[1]
        ip = ip.rstrip(';')
        ip_to_name[ip] = name
    return ip_to_name

def ip_commands(m, ip_to_name):
    for _ in range(m):
        command, ip = input().split()
        if ip.endswith(';'):
            ip = ip[:-1]
        name = ip_to_name[ip]
        print(f"{command} {ip}; #{name}")

n, m = map(int, input().split())

ip_to_name = map_name_and_ip(n)

ip_commands(m, ip_to_name)
