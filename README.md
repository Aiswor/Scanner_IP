# README

## English Version

### Network Scanner

This script scans a given network by performing a ping to each host within the specified subnet.

### Features:
1. Asks the user for the network IP.
2. Asks the user for the subnet mask.
3. Uses multi-threading to efficiently scan all hosts in the network.
4. Displays active hosts that respond to the ping request.

### How to Use:

Run the script using Python:
```bash
python3 script.py
```
Then, input the network IP and the subnet mask in long format (e.g., 24 for a /24 network).

### Notes:
- Script designed for Linux systems.
- Requires Python 3.
- Ensure you have the necessary permissions to send ICMP requests (may require `sudo`).

---

## Versión en Español

### Escáner de Red

Este script escanea una red determinada realizando un ping a cada host dentro de la subred especificada.

### Características:
1. Solicita al usuario la IP de la red.
2. Solicita la máscara de subred en formato largo.
3. Usa multi-threading para escanear todos los hosts de manera eficiente.
4. Muestra los hosts activos que responden al ping.

### Cómo usarlo:

Ejecuta el script usando Python:
```bash
python3 script.py
```
Luego, ingresa la IP de la red y la máscara de subred en formato largo (por ejemplo, 24 para una red /24).

### Notas:
- Script diseñado para sistemas Linux.
- Requiere Python 3.
- Asegúrate de tener los permisos necesarios para enviar solicitudes ICMP (puede requerir `sudo`).

