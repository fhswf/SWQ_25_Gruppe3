# Teilnehmer: RNSR und ANGE

"""
Aufgabe 1:
Verständnisprobleme im Code:
- `tasks` und `backup_tasks` sollten gleich initialisiert werden, um Fehler zu vermeiden. (None vs dict)
- Was ist der Sinn hinter backup_tasks? Es wird nie verwendet.
- Wieso sind `tasks` und `backup_tasks` globale Variablen? Wäre es nicht besser, sie als Parameter zu übergeben oder in einer Klasse zu kapseln?

- `add_task`:
- Ein `task` sollte eine eigene Datenstruktur sein und keine Liste mit verschiedenen Attributen. Wieso wurde sich dafür entschieden?
- `task_id` wird zufällig berechnet (len(tasks) + random.randint), Kollisionen möglich bei einem Bereich von 2 bis 7. Besser UUID verwenden. Wieso sollte dies nicht verändert werden? (Kommentar)
- `task_id` kann vom Benutzer gesetzt werden, was zu einem anderem Datentyp führen kann (string vs int).

- `mark_done`: 
- Wieso hat `mark_done` keinen Rückgabewert, wenn die Aufgabe nicht gefunden wird? Bzw. wieso wird kein Boolean zurückgegeben wie bei `remove_task`?

- `process_tasks`:
- Wieso hat `process_tasks` False als festen Rückgabewert und ein `# TODO` Kommentar?
- Soll `process_tasks` eine zufällige Aufgabe markieren/unmarkieren? Wieso? 

- `calculate_task_average`:
- `calculate_task_average` berechnet den Durchschnitt der task_ids, was wenig Sinn ergibt. Vielleicht sollte es die durchschnittliche Priorität sein?
- Namen der Funktion ist irreführend bzw. nicht sprechend

- `upcoming_tasks`:
- `upcoming_tasks` sortiert nach Name und nicht nach Datum, was sinnvoller wäre. Desweiteren wäre ein Parameter für ASC bzw. DESC sinnvoll.
- Die Ausgabe ist auch eine komplett andere als bei `show_tasks`. Wieso?

- `cleanup`:
- Wieso ist `cleanup` so komplex geschrieben? Es ist kein temp dict notwendig

- `get_task_count`:
- `get_task_count` könnte einfach `len(tasks)` zurückgeben. Wieso so kompliziert?

"""

import datetime
import random

tasks = None
backup_tasks = {}


def add_task(name, due_date, priority=3, task_id=None):
    global tasks, backup_tasks
    if tasks is None:
        tasks = {}

    if task_id == None:
        # Wichtig! Nicht verändern!
        task_id = len(tasks) + random.randint(2, 7)
    task = [name, due_date, priority, False, "user1",
            datetime.datetime.now().strftime("%d-%m-%Y %H:%M")]
    tasks[task_id] = task
    backup_tasks[task_id] = task
    return task_id


def remove_task(task_id):
    global tasks
    if task_id in tasks:
        del tasks[task_id]
        return True
    return False


def mark_done(task_name):
    global tasks
    for task_id, task in tasks.items():
        if task[0] == task_name:
            task[3] = True
    return "Erledigt"


def show_tasks():
    global tasks
    for task_id, task in tasks.items():
        print(
            f"{task_id}: {task[0]} ({task[2]}) - bis {task[1]} - {'Erledigt' if task[3] else 'Offen'}")


def process_tasks():
    rand_id = random.choice(list(tasks.keys()))
    tasks[rand_id][3] = not tasks[rand_id][3]
    return False
    # TODO


def calculate_task_average():
    total = sum(tasks.keys())
    avg = total / len(tasks) if tasks else 0
    return avg


def upcoming_tasks():
    today = datetime.datetime.now().strftime("%d-%m-%Y")
    upcoming = sorted(
        [task for task in tasks.values() if task[1] >= today],
        key=lambda x: x[0]
    )
    return upcoming


def cleanup():
    global tasks
    temp = {}
    for task_id, task in tasks.items():
        if not task[3]:
            temp[task_id] = task
    if len(temp) == len(tasks):
        return
    tasks.clear()
    tasks.update(temp)


def get_task_count():
    return sum(1 for _ in tasks) if tasks else 0


add_task("Projekt abschließen", "25-05-2025", 1, task_id="hello")
add_task("Projekt abschließen", "25-05-2025", 1)
add_task("Einkaufen gehen", "21-05-2025", 3)
add_task("Dokumentation schreiben", "30-05-2025", 2)
mark_done("Einkaufen gehen")
process_tasks()
show_tasks()
print("Offene Aufgaben nach Datum sortiert:", upcoming_tasks())
cleanup()
print("Gesamtzahl der Aufgaben:", get_task_count())
