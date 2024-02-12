IP_PRINCIPAL = input("Ingrese la IP principal: ")
NUMERO_SUBREDES = input("Ingrese la cantidad de subredes: ")

NUMERO_SUBREDES = int(NUMERO_SUBREDES)

n = 0
bits_adicionales = 0

while bits_adicionales < NUMERO_SUBREDES:
  n += 1
  
  bits_adicionales = 2**n

nueva_mascara_subred = 24 + n

#dividir la ip principal en subredes
subredes = []

# Encontrar la posición del último punto
ultimo_punto_index = IP_PRINCIPAL.rfind('.')

# Cortar el string hasta la posición del último punto
ip_red = IP_PRINCIPAL[:ultimo_punto_index]

bits_por_red = int(256 / bits_adicionales)

octeto_4 = 0
for red in range(1, NUMERO_SUBREDES + 1):
  subred = {}

  ip_subred = f"{ip_red}.{octeto_4}"
  primera_ip = f"{ip_red}.{octeto_4 + 1}"
  
  octeto_4 += bits_por_red

  if red >= NUMERO_SUBREDES:
    octeto_4 = 256
  
  ultima_ip = f"{ip_red}.{octeto_4 - 2}"
  broadcast = f"{ip_red}.{octeto_4 - 1}"

  subred["ip_subred"] = ip_subred
  subred["primera_ip"] = primera_ip
  subred["ultima_ip"] = ultima_ip
  subred["broadcast"] = broadcast

  subredes.append(subred)

for subred in subredes:
  print(f"Subred: {subred['ip_subred']}")
  print(f"Primera IP: {subred['primera_ip']}")
  print(f"Última IP: {subred['ultima_ip']}")
  print(f"Broadcast: {subred['broadcast']}")
  print('-----------------------')

  print('\n')
