import random

# Personajes jugables
personajes_jugables = [
    {"nombre": "Harry Potter", "atributos": (100, 22, 12)},
    {"nombre": "Hermione Granger", "atributos": (90, 25, 10)},
    {"nombre": "Ron Weasley", "atributos": (95, 18, 14)}
]

# Enemigos
enemigos = [
    {"nombre": "Lord Voldemort", "atributos": (110, 27, 8)},
    {"nombre": "Bellatrix Lestrange", "atributos": (95, 26, 10)},
    {"nombre": "Lucius Malfoy", "atributos": (90, 21, 11)}
]

# Acciones posibles del enemigo
acciones = ["hechizar", "proteger"]

# Mostrar personajes jugables
print("🧙‍♂️ Personajes disponibles:")
for i in range(len(personajes_jugables)):
    p = personajes_jugables[i]
    print(f"{i + 1}. {p['nombre']} - Vida: {p['atributos'][0]}, Ataque: {p['atributos'][1]}, Defensa: {p['atributos'][2]}")

# Elegir personaje del jugador
jugador_idx = int(input("Elige tu mago (1-3): ")) - 1
jugador = personajes_jugables[jugador_idx]
jugador_vida = jugador["atributos"][0]
jugador_ataque = jugador["atributos"][1]
jugador_defensa = jugador["atributos"][2]

# Elegir enemigo aleatorio
enemigo = random.choice(enemigos)
enemigo_vida = enemigo["atributos"][0]
enemigo_ataque = enemigo["atributos"][1]
enemigo_defensa = enemigo["atributos"][2]

print(f"\n🧟‍♂️ Te enfrentarás a: {enemigo['nombre']}")

# Variables de combate
turno = 1
contador_ataques = 0
poder_disponible = False

# Bucle de combate
while jugador_vida > 0 and enemigo_vida > 0:
    print(f"\n🔄 --- Turno {turno} ---")
    print(f"✨ Tu vida: {jugador_vida} | Vida de {enemigo['nombre']}: {enemigo_vida}")

    print("\n¿Qué harás?")
    print("1. Hechizo de ataque: Bombarda 💥")
    print("2. Hechizo de protección: Protego 🛡️")
    if contador_ataques >= 5:
        print("3. PODER ESPECIAL: Avada Kedavra 🔥")
        poder_disponible = True
    else:
        poder_disponible = False

    eleccion = int(input("Elige acción (1-2" + (" o 3" if poder_disponible else "") + "): "))

    if eleccion == 1:
        accion_jugador = "ataque"
        contador_ataques += 1
        hechizo_jugador = "Hechizo de ataque: Bombarda 💥"
    elif eleccion == 2:
        accion_jugador = "defensa"
        hechizo_jugador = "Hechizo de protección: Protego 🛡️"
    elif eleccion == 3 and poder_disponible:
        accion_jugador = "especial"
        hechizo_jugador = "PODER ESPECIAL: Explosión de Fénix 🔥🔥🔥"
        contador_ataques = 0
    else:
        accion_jugador = "fallo"
        hechizo_jugador = "No hiciste nada 😴"

    accion_enemigo = random.choice(acciones)
    if accion_enemigo == "hechizar":
        hechizo_enemigo = "Hechizo de ataque: Sectumsempra 💢"
    else:
        hechizo_enemigo = "Hechizo de protección: Expectro Patronum 🦌"

    # Mostrar acciones
    print(f"\n✨ Tú usaste: {hechizo_jugador}")
    print(f"😈 {enemigo['nombre']} usó: {hechizo_enemigo}")

    # Resolver efectos
    if accion_jugador == "ataque" and accion_enemigo == "hechizar":
        enemigo_vida -= max(0, jugador_ataque - enemigo_defensa)
        jugador_vida -= max(0, enemigo_ataque - jugador_defensa)
    elif accion_jugador == "ataque" and accion_enemigo == "proteger":
        print(f"{enemigo['nombre']} bloqueó tu ataque con Expectro Patronum. 🦌")
    elif accion_jugador == "defensa" and accion_enemigo == "hechizar":
        print("¡Bloqueaste el hechizo del enemigo con Protego! 🛡️")
    elif accion_jugador == "defensa" and accion_enemigo == "proteger":
        print("Ambos se protegieron. Turno sin daño. ⚔️")
    elif accion_jugador == "especial" and accion_enemigo == "hechizar":
        enemigo_vida -= max(0, (jugador_ataque * 2) - enemigo_defensa)
        jugador_vida -= max(0, enemigo_ataque - jugador_defensa)
    elif accion_jugador == "especial" and accion_enemigo == "proteger":
        enemigo_vida -= max(0, jugador_ataque - enemigo_defensa)
        jugador_vida -= max(0, enemigo_ataque - jugador_defensa)
        print(f"{enemigo['nombre']} se protegió del PODER ESPECIAL. Recibió la mitad del daño del PODER ESPECIAL122. 🦸‍♂️")
    elif accion_jugador == "fallo":
        jugador_vida -= max(0, enemigo_ataque - jugador_defensa)

    turno += 1

# Resultado final
print("\n⚡ Fin del duelo mágico ⚡")
if jugador_vida <= 0 and enemigo_vida <= 0:
    print("¡Ambos magos han caído! Empate. 💀")
elif jugador_vida <= 0:
    print(f"¡{enemigo['nombre']} te ha derrotado! 😵")
else:
    print(f"¡Has vencido a {enemigo['nombre']}! 🎉")
