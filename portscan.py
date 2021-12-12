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
       add_fields()
    elif value == "2":
       quantity_ports()
    else:
       print("Option not found")   

def setup_client(host, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.5)
    code = client.connect_ex((host, int(port)))
    
    if code == 0:
        print("Port Success")
    else:
        print("Port Failed")
        
def add_fields():
    host = input("Host: ")
    port = input("Port: ")
    
    setup_client(host, port)
    
def quantity_ports():
    host = input("Host: ")
    quantity = input("Quantity ports: ")		
    ports = range(int(quantity))
    
    for port in ports:
        setup_client(host, port)
        
if __name__ == "__main__":
    header()
    print("------------------------------")
    print("1 - Add by fields")
    print("2 - Add by quantity ports") 
    value = input("Choose an option: ")
    print("")
    menu(value)