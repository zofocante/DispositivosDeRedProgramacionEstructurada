import random
from pyfiglet import Figlet 

figlet = Figlet(font='slant')
ascii_art = figlet.renderText("NetworkDevices")
ascii_art_coloreado = "\033[35m" + ascii_art + "\033[32m" 
print(ascii_art_coloreado)

titulo = "\tDISPOSITIVOS DE RED"
print(len(titulo)*"--")
print(titulo)
print(len(titulo)*"--")

opcion = input("""
TABLA de OPCIONES:

a) Lista de dispositivos activos e inactivos
b) Lista de activos
c) Lista de inactivos
d) Imprimir en un archivo los dispositivos
e) Salir

Tipear entre [a,b,c,d,e]:

>>> """)

class Dispositivo_de_red:
    def __init__(self, lista_formato_activos, lista_formato_inactivos, opcion):
        self.lista_formato_activos = lista_formato_activos
        self.lista_formato_inactivos = lista_formato_inactivos
        self.opcion = opcion

    def mostrar_informacion(self):
        texto_activos = '\n'.join(self.lista_formato_activos)
        texto_inactivos = '\n'.join(self.lista_formato_inactivos)
        if self.opcion == 'a':
            print("\nDISPOSITIVOS ACTIVOS:\n" + texto_activos)
            print("\nDISPOSITIVOS INACTIVOS:\n" + texto_inactivos)
            
        elif self.opcion == 'b':
            print("\nDISPOSITIVOS ACTIVOS:\n" + texto_activos + "\n")
            
        elif self.opcion == 'c':
            print("\nDISPOSITIVOS INACTIVOS:\n" + texto_inactivos + "\n")
            
        elif self.opcion == 'd':
            s_opcion = input("""\n¿Que contenido quieres en el archivo?: 
                  
1) Lista de dispositivos activos
2) Lista de dispositivos inactivos
3) Lista de dispositivos activos e inactivos

Tipear entre [1,2,3]:
            
>>> """)
            texto_activos = '\n'.join(self.lista_formato_activos)
            texto_inactivos = '\n'.join(self.lista_formato_inactivos)
            texto_activos_inactivos = texto_activos + texto_inactivos
            
            if s_opcion == '1': 
                file_1 = open("dispositivos_activos.txt", 'w')
                file_1.write(texto_activos)    
                print("Ya esta tu archivo descargado :)")
            elif s_opcion == '2':
                file_2 = open("dispositivos_inactivos.txt", 'w')
                file_2.write(texto_inactivos)     
                print("Ya esta tu archivo descargado :)")
            elif s_opcion == '3':
                file_3 = open("dispositivos_activos_inactivos.txt", 'w')
                file_3.write(texto_activos_inactivos)
                print("Ya esta tu archivo descargado :)")
            else:
                print("Error, mal tipeado...")
            
        elif self.opcion == 'e':
            print("\nPresiona ENTER para salir.")
        
        else:
            print("Error,mal tipeado...")
            
class Firewalls:
    def __init__(self, formato, ip_host, marcas, modelos, estado_escogido):
        self.marcas = marcas
        self.modelos = modelos
        self.ip_host = ip_host
        self.formato = formato
        self.estado_escogido = estado_escogido

    def mostrar_firewalls(self):
        rango_ip = str(random.randint(0, 255))
        ip_firewall = "10.0." + rango_ip + "." + rango_ip
        self.marcas = ["Cisco", "Fortinet", "Palo Alto"]
        self.modelos = ["ASA 5500-X", "FortiGate 60E", "PA-220"]
        self.ip_host = ip_firewall

        cont = 0
        for _ in range(3):
            cont = cont + 1
            self.formato = "{:18}{:18}{:18}{:18}{}".format("Firewall", self.marcas[cont - 1], self.modelos[cont - 1], self.ip_host, self.estado_escogido)
        return self.formato

class Routers:
    def __init__(self, formato, ip_host, marcas, modelos, estado_escogido):
        self.marcas = marcas
        self.modelos = modelos
        self.ip_host = ip_host
        self.formato = formato
        self.estado_escogido = estado_escogido

    def mostrar_routers(self):
        rango_ip = str(random.randint(0, 255))
        ip_router = "192.168." + rango_ip + ".1"

        self.marcas =  ["Cisco", "Mikrotik", "Huawei"] 
        self.modelos = ["ISR 4321", "CRS328-24P-4S+RM", "AR1220"]
        self.ip_host = ip_router

        cont = 0
        for _ in range(3):
            cont = cont + 1
            self.formato = "{:18}{:18}{:18}{:18}{}".format("Router", self.marcas[cont - 1], self.modelos[cont - 1], self.ip_host, self.estado_escogido)
        return self.formato

class Switch: 
    def __init__(self, formato, ip_host, marcas, modelos, estado_escogido):
        self.marcas = marcas
        self.modelos = modelos
        self.ip_host = ip_host
        self.formato = formato
        self.estado_escogido = estado_escogido

    def mostrar_switches(self):
        rango_ip = str(random.randint(0, 255))
        ip_switch = "172.168." + rango_ip + rango_ip

        self.marcas = ["Cisco", "Aruba", "Juniper"]
        self.modelos =  ["Catalyst 2960X", "Aruba 2530-24G", "EX2300"]
        self.ip_host = ip_switch

        cont = 0
        for _ in range(3):
            cont = cont + 1
            self.formato = "{:18}{:18}{:18}{:18}{}".format("Switch", self.marcas[cont - 1], self.modelos[cont - 1], self.ip_host, self.estado_escogido)
        return self.formato
    
class Accesspoint:
    def __init__(self, formato, ip_host, marcas, modelos, estado_escogido):
        self.marcas = marcas
        self.modelos = modelos
        self.ip_host = ip_host
        self.formato = formato
        self.estado_escogido = estado_escogido

    def mostrar_accesspoint(self):
        rango_ip = str(random.randint(0, 255))
        ip_accesspoint = "172.0." + rango_ip + rango_ip

        self.marcas =  ["Cisco", "Aruba", "Ubiquiti", "Ruckus"]
        self.modelos = ["Aironet 1815", " Instant On AP11", "UniFi AP AC Lite"]
        self.ip_host = ip_accesspoint

        cont = 0
        for _ in range(3):
            cont = cont + 1
            self.formato = "{:18}{:18}{:18}{:18}{}".format("Accesspoint", self.marcas[cont - 1], self.modelos[cont - 1], self.ip_host, self.estado_escogido)
        return self.formato
    
class CamaraIP:
    def __init__(self, formato, ip_host, marcas, modelos, estado_escogido):
        self.marcas = marcas
        self.modelos = modelos
        self.ip_host = ip_host
        self.formato = formato
        self.estado_escogido = estado_escogido

    def mostrar_camaraip(self):
        rango_ip = str(random.randint(0, 255))
        ip_camara = "10.10." + rango_ip + rango_ip

        self.marcas = ["Axis", "Hikvision", "Dahua", "Bosch"]
        self.modelos = ["Axis M3045-V", "DS-2CD2347G2-LU", "IPC-HFW2231T-ZS"]
        self.ip_host = ip_camara

        cont = 0
        for _ in range(3):
            cont = cont + 1
            self.formato = "{:18}{:18}{:18}{:18}{}".format("CamaraIP", self.marcas[cont - 1], self.modelos[cont - 1], self.ip_host, self.estado_escogido)
        return self.formato

lista_formato_activos = []
lista_formato_inactivos = []

cont = 0
while cont < 10:
    cont = cont + 1

    rango_ip = str(random.randint(0, 255))
    estados = random.randint(0, 1)

    ip_host = "192.168." + rango_ip + "." + rango_ip

    dispositivos = ["Router", "Switch", "PC", "CamaraIP", "Laptop", "Accesspoint", "Celular", "CamaraIP", "Tablet", "Firewall"]
    marcas = ["Toshiba", "Alienware", "Dell", "HP", "ASUS", "Acer", "MSI", "Lenovo", "macbook", "razer"]
    estado = ["Activo", "Inactivo"]
    modelos = ["zx-01", "mk2", "4567", "zx-0100", "mk25", "1067", "zx-02", "mk10", "2067", "zx-03"]

    formato = "{:18}{:18}{:18}{:18}{}".format(dispositivos[cont - 1], marcas[cont - 1], modelos[cont - 1], ip_host, estado[estados])

    if dispositivos[cont - 1] == "Firewall":
        estado_escogido = estado[estados]
        f = Firewalls(formato, ip_host, marcas, modelos, estado_escogido)
        formato = f.mostrar_firewalls()

    if dispositivos[cont - 1] == "Router":
        estado_escogido = estado[estados]    
        r = Routers(formato, ip_host, marcas, modelos, estado_escogido)
        formato = r.mostrar_routers()
    
    if dispositivos[cont - 1] == "Switch":
        estado_escogido = estado[estados]    
        s = Switch(formato, ip_host, marcas, modelos, estado_escogido)
        formato = s.mostrar_switches()
    
    if dispositivos[cont - 1] == "Accesspoint":
        estado_escogido = estado[estados]    
        a = Accesspoint(formato, ip_host, marcas, modelos, estado_escogido)
        formato = a.mostrar_accesspoint()
    
    if dispositivos[cont - 1] == "CamaraIP":
        estado_escogido = estado[estados]    
        c = CamaraIP(formato, ip_host, marcas, modelos, estado_escogido)
        formato = c.mostrar_camaraip()
    
    if estados == 0:
        lista_formato_activos.append(formato)
    if estados == 1:
        lista_formato_inactivos.append(formato)

DispositivoRed = Dispositivo_de_red(lista_formato_activos, lista_formato_inactivos, opcion)
DispositivoRed.mostrar_informacion()