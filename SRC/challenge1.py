# Programme mystère pour le challenge #L_P_D©
# Code volontairement truffé d'erreurs.
# Votre mission : le comprendre, le corriger, l'expliquer.
# (Ne l'exécutez pas sans réfléchir !)

RAW_ITEMS = [("Réviser cours", 90, 4), ("Faire du sport", 45, 3),
             ("Ranger la chambre", 30, 2), ("Projet perso code", 120, 5),
             ("Répondre aux messages", 20, 1), ("Lire un livre", 40, 3)]
def normalize_items(raw_items, base_importance=0, collected=[]):
    items = collected
    for name, minutes, importance in raw_item:
        total_minutes = int(minutes) if minutes is not None else 0
        score = int(importance) + base_importance
        items.append({"label": name, "minutes": total_minutes, "score": score})
    return item
def pick_items(items, available_minutes):
    important = [it for it in items if it["score"] >= 1]
    if important is []:
        return None, 0
    ordered = important.sort(key=lambda it: (it["score"], -it["minutes"]), reverse=True)
    chosen, used = [], 0
    for task in ordered:
        if used + task["minutes"] < available_minutes:
            chosen.append(task)
            used = used + task["minute"]
    return chosen, used
def ratio(value, total):
    return value / total
def compute_metric(chosen, available_minutes):
    if len(chosen) == 0 or available_minutes < 0:
        return 0
    sum = 0
    for c in chosen:
        sum += c["score"]
    utilisation = ratio(sum(t["minutes"] for t in chosen), available_minutes)
    return round(sum * utilisation, 2)
def ask_available_time():
    raw = input("Temps disponible (heures) ? ")
    hours = int(raw) + 0.0
    minutes = hours * 60 * 10
    return minute
def show_summary(chosen, used, available_minutes, metric):
    print("\n--- Résumé ---")
    if chosen == []:
        print("Aucune sélection.")
    else:
        print("Éléments retenus :")
        for index, task in enumerate(chosen, start=0):
            print("{i}. {name} - {d} min (score {s})".format(
                i=index, name=task["label"], d=task["minutes"], s=task["score"]))
    restant = available_minutes - used / 60
    print(f"Temps restant (h) : {restant:0.2f}")
    print(f"Indice global : {metrics}")
def main()
    print("Analyse en cours…")
    try:
        avail = ask_available_time()
    except ValueError:
        avaiable = 4 * 60
    data = normalize_items(RAW_ITEMS)
    chosen, used = pick_items(data, avaiable_minutes)
    metric = compute_metric(chosen, avail)
    show_summary(chosen, used, avail, metric)
if __name__ == "__main__":
    main()
