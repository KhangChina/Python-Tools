import requests


host_input= 'gmo.jp'
finded_host = [] #list
def findSubByDomain (sub, host):
    domain = f"https://{sub}.{host}"
    print(f'Test => {domain}')
    try:
        requests.get(domain)
        finded_host.append(domain)
        #ghi kết quả vào file
        report = open("report.txt", "a")
        with open('report.txt', mode='a') as report_file:
            report_file.write(domain+'\n')
        
        #print(f'Found: {domain}')
    except requests.ConnectionError:
        # print(f'Not Found: {domain}')
        pass

def get_current_ipv6():
    """Get the current external IPv6 address or return None if no connection to the IPify service is possible"""
    try:
        return requests.get("https://ident.me").text
    except requests.exceptions.ConnectionError as ex:
        return None
# Usage example
 # Prints e.g. 2a01:4f9:c010:278::1
print("MyIP: " +get_current_ipv6())

with open('sub.txt', mode='r') as sub_file:
     #Chuyển đổi danh sách trong file thành list
    list_Sub = sub_file.read().splitlines()
    #Duyệt list
    print('-----------Scanner Started-----------')
    for line in list_Sub:
        findSubByDomain(line,host_input)
    print('---------- Scanning Finished Report---------')
    print(*finded_host, sep = "\n")

