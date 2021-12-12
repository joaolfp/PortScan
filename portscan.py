import socket

def header():
    print("""
 ########:::'#######::'########::'########:::::'######:::'######:::::'###::::'##::: ##:
 ##.... ##:'##.... ##: ##.... ##:... ##..:::::'##... ##:'##... ##:::'## ##::: ###:: ##:
 ##:::: ##: ##:::: ##: ##:::: ##:::: ##::::::: ##:::..:: ##:::..:::'##:. ##:: ####: ##:
 ########:: ##:::: ##: ########::::: ##:::::::. ######:: ##:::::::'##:::. ##: ## ## ##:
 ##.....::: ##:::: ##: ##.. ##:::::: ##::::::::..... ##: ##::::::: #########: ##. ####:
 ##:::::::: ##:::: ##: ##::. ##::::: ##:::::::'##::: ##: ##::: ##: ##.... ##: ##:. ###:
 ##::::::::. #######:: ##:::. ##:::: ##:::::::. ######::. ######:: ##:::: ##: ##::. ##:
..::::::::::.......:::..:::::..:::::..:::::::::......::::......:::..:::::..::..::::..::
""")
    print("")
    print("About: To check open ports on a particular host")
    print("Author: Joao Lucas")
    print("Language: Python")
    print("GitHub: https://github.com/joaolfp/PortScan")
    print("")

def menu(value):
    if value == "1":
       addFields()
    elif value == "2":
       quantityPorts()
    else:
       print("Option not found")   

def setupClient(host, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.5)
    code = client.connect_ex((host, int(port)))
    
    if code == 0:
        print("Port Success")
    else:
        print("Port Failed")
        
def addFields():
    host = input("Host: ")
    port = input("Port: ")
    
    setupClient(host, port)
    
def quantityPorts():
    host = input("Host: ")
    quantity = input("Quantity ports: ")		
    ports = range(int(quantity))
    
    for port in ports:
        setupClient(host, port)
        
if __name__ == "__main__":
    header()
    print("------------------------------")
    print("1 - Add by fields")
    print("2 - Add by quantity ports") 
    value = input("Choose an option: ")
    print("")
    menu(value)