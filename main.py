
from typing import List, Dict

# Globální seznam úkolů
ukoly: List[Dict[str, str]] = []

def hlavni_menu() -> None:
    """
    Zobrazí hlavní menu aplikace pro správu úkolů.
    Umožní uživateli vybrat jednu z následujících možností:
    - Přidat nový úkol
    - Zobrazit všechny úkoly
    - Odstranit úkol
    - Ukončit program
    """
    while True:
        print("\nSprávce úkolů - Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")
        volba: str = input("Vyberte možnost (1-4): ")

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("\nKonec programu.")
            break
        else:
            print("\nNeplatná volba, zkuste to znovu.")

def pridat_ukol() -> None:
    """
    Umožní uživateli zadat nový úkol.
    Získá název a popis od uživatele a přidá jej do seznamu úkolů.
    Kontroluje, že název i popis nejsou prázdné.
    """
    while True:
        nazev: str = input("\nZadejte název úkolu: ").strip()
        if not nazev:
            print("\nNázev úkolu nesmí být prázdný.")
            continue

        popis: str = input("Zadejte popis úkolu: ").strip()
        if not popis:
            print("\nPopis úkolu nesmí být prázdný.")
            continue

        ukoly.append({'nazev': nazev, 'popis': popis})
        print(f"Úkol '{nazev}' byl přidán.")
        break

def zobrazit_ukoly() -> None:
    """
    Vypíše všechny uložené úkoly ze seznamu.
    Pokud žádné úkoly neexistují, vypíše odpovídající zprávu.
    """
    if not ukoly:
        print("\nŽádné úkoly nebyly nalezeny.")
    else:
        print("\nSeznam úkolů:")
        for i, u in enumerate(ukoly, 1):
            print(f"{i}. {u['nazev']} - {u['popis']}")

def odstranit_ukol() -> None:
    """
    Umožní uživateli odstranit úkol podle čísla.
    Zobrazí seznam úkolů a vyžádá si číslo úkolu ke smazání.
    Kontroluje platnost vstupu a zobrazí odpovídající zprávy.
    """
    if not ukoly:
        print("\nSeznam úkolů je prázdný, není co odstranit.")
        return

    zobrazit_ukoly()
    while True:
        try:
            cislo: int = int(input("\nZadejte číslo úkolu, který chcete odstranit: "))
            if 1 <= cislo <= len(ukoly):
                odebrany: Dict[str, str] = ukoly.pop(cislo - 1)
                print(f"Úkol '{odebrany['nazev']}' byl odstraněn.")
                break
            else:
                print("\nNeplatné číslo úkolu. Zkuste to znovu.")
        except ValueError:
            print("\nProsím, zadejte platné číslo.")

# Spuštění programu
if __name__ == "__main__":
    hlavni_menu()

