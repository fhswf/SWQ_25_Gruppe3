# Teilnehmer: XXXX und FARN

'''
    A1

    Anmerkungen FARN
    - Sehr wenige Kommentare
    - Bildung der task_id kritisch, weil nicht eindeutig
    - Möglichkeit, id von außen mitzugeben, ist ungünstig
    - Realisierung der Entität task als Liste ist intransparent und umständlich

    - die Funktion process_tasks ist sehr schwer nachzuvollziehen. Was soll sie leisten?
    durch das TODO ist auch unklar, ob sie überhaupt schon fertig.

    - undurchsichtige Funktionsnamen. Was machen die Funktionen überhaupt?
    - wofür wird die Variable backup_tasks benötigt? Sie wird deklariert und das Dictionary wird auch gefüllt, aber niemals geleert oder abgefragt
    - Jeder Task, wird demselben "User" zugewiesen; warum?
    - die Funktion mark_done arbeitet - warum auch immer - anhand des Tasknamens und nicht anhand der id. Der Name muss nicht eindeutig sein. Im Zweifel werden hier zu viele Tasks als erledigt markiert.
    - Welchen Mehrwert, hat der Rückgabewert der mark_done-Funktion?
    - Die Zuordnung der Status findet nur im print-Statement der Funktion show_tasks statt. Was, wenn andere/künftige Funktionen die Status auch auflösen müssen?
    - Welchen Zweck hat die Funktion calculate_task_average? Schlecht dokumentiert. Wird hier tatsächlich die "durchschnittliche Task-ID" berechnet? Welchen Nutzen hat das?
-
    Was macht der Code?
    1) add_task
       - erstellt einen Task, der als Liste gespeichert wird. Die "Attribute" des Tasks sind in einer bestimmten Reihenfolge in einer Liste gespeichert
       - bildet eine task_id, wenn keine von außen mitgegeben wurde,
       - die Werte unter den Indizes, die offenber für "erledigt" und den Benutzer stehen, werden standardmäßig vorbelegt mit False und "user1"
       - die Liste/der Task wird im dict tasks und backup_tasks gespeichert, wobei die task_id als Schlüssel fungiert
       - die task_id wird zurückgegeben

    2) remove_task
        - etnfernt den task anhand der id den task aus dem task-dict
        - gibt True zurück, wenn task enthalten war und gelöscht wurde, ansonsten false

    3) mark_done
        - der zu markierende Task wird anhand des Namens identifiziert
        - iteriert über jedes Element des task_dict und macht dann für jede Liste Folgendes
            - wenn der erste Eintrag der Liste mir dem Namen übereinstimmt, wird der vierte Eintrag der Liste auf True gesetzt
        - gibt immer "Erledigt" zurück
    4) show_tasks
        - iteriert über das tasks-dict
        - gibt für jedes Element einen f-String aus
        - innerhalb der Ausgabe wird noch entschieden, wie die numerischen Status aufgelöst werden
    5) process_tasks
        - negiert für einen beliebigen task im task_dict den Wert unter Index 3 (Status)
        - damit wird ein beliebiger Task von offen auf erledigt oder anders herum gesetzt
        - gibt False zurück
    6) calculate_task_avergae
        - berechnet die durchschnittliche task_id und gibt diese zurück
    7) upcoming_tasks
        - gibt eine Liste an Tasks, sortiert nach Namen zurück, deren Fälligkeitsdatum größer oder gleich heute ist.
            Der Datumsvergleich passiert aber lexikografisch
    8) clean_up()
        - legt ein neues dict namens temp an
        - iteriert über das task_dict und prüft für jeden task, ob er unter index 3 False gespeichert hat (Offene Fälle)
            - wenn das der Fall ist, wird der Fall in das neue dict geschrieben
        - das ursprüngliche taks_dict wird geleert
        - das task_dict wird allen Einträgen aus temp wieder gefüllt 
    9) get_task_count()
        - gibt die Anzahl an Elementen im task_dict zurück
        - das passiert indem per Iteration über das dict für jedes Element 1 zurückgegeben wird und diese aufsummiert werden

    Welche Stellen machen den Code unverständlich?

    - Zu wenig und mangelhafte Kommentare
    - unpassende Datentypen, z.B. ein task als Liste
    - einmalige Benutzung von #TODO
        - einerseits ist an der Stelle des Vorkommens nicht klar, worin das todo noch besteht
        - andererseits wirkt das als wäre der Rest des Codes fertig, was weitere Fragen aufwirft, 
    

    A2

    Negativ zu bewertende Aspekt
        - Funktionalität
            - Ohne die Spezifikation zu kennen, kann davon ausgegangen werden, dass
            viele Funktionen nicht so arbeiten, wie sie sollten.
            - So kann nicht sinnvoll gewollt sein, dass alle Todos mit demselben Namen
            mit einem Schritt auf erledigt gesetzt werden
            - ein weiteres Beispiel ist die "Filterung" der kommenden Task anhand des Datum,
            das als String formatiert ist. 
        - Zuverlässigkeit / Robustheit
            - das System ist fehleranfällig
            - es gibt keinerlei Ausnahmebehandlungen, welche sich anbieten würden, alleine weil
            es z.B. bei Erstellung von tasks Eingaben von außen geben kann
            - so gibt es bspw. die Funktion calculate_ask_average. Wenngleich deren Sinn sich nicht erschließt,
            funktioniert sie nicht zuverlässig, weil taks_ids auch nicht numerisch sein können

        Verständlichkeit, Struktur, Transparenz
        - positiv zu bemerken ist, dass die Funktionsnamen grundsätzlich sprechend benannt sind,
        auch wenn sie nicht immer das machen, was sie vorgeben zu tun
        - ebenfalls positiv zu bemerken ist, dass es eine Gliederung in Funktionen gibt
        - es mangelt an Verständlichkeit einerseits augrund von fehlenden Kommentaren,
        andererseits aufgrund von umständlichen Strukturen. Hier ist noch einmal die Implementierung
        eines Tasks als Liste zu nennen. Nur durch lesen des Codes kann man erahnen, welche Taskeigenschaft
        unter welchem Index zu finden ist. Wenn man dies durchschaut hat, muss man es sich nur noch merken können.
        Eine Klasse könnte hier helfen

        Wartbarkeit
        - die Wartbarkeit ist mangelhaft. Der gesamte Quelltext muss angepasst werden,
        wenn sie die Struktur eines tasks ändert. 
        - auch hier könnte ein objektorientierter Ansatz helfen
    '''
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
show_tasks()
print("___________________")
process_tasks()
show_tasks()
print("Offene Aufgaben nach Datum sortiert:", upcoming_tasks())
cleanup()
print("Gesamtzahl der Aufgaben:", get_task_count())
