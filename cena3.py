def montagem_elenco():
    print("🎙️ CENA 3 — Montando o elenco")
    elenco = ["AJ", "Regina", "Elphaba", "Simba"]
    elenco.append("Janis")
    elenco.remove("Regina")
    for personagem in elenco:
        print(personagem)
    print()
