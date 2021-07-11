import socket

print('Wellcom to Port Scanner... ')
print('='*50)

hostname=input('Enter domain: ')

ip=socket.gethostbyname(hostname)

ip_range_start=int(input("IP range (Start): "))

ip_range_end=int(input("IP range (End): "))

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

for port in range(ip_range_start,(ip_range_end)+1):
    print('Scanning port {0}: {1}'.format(ip,port))
    
    r=s.connect_ex((ip,port))
    if r==0:
        print('PORT {0} is open... '.format(port))
