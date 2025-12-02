def ip_address(ip):
    new_address = ""
    split_ip = ip.split(".")
    separator = "[.]"
    new_address = separator.join(split_ip)
    return new_address

IPaddress = input("Enter IP address: ")
ipAddress = ip_address(IPaddress)
print(ipAddress)