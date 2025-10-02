# Teilnehmer: DLWG und FARN

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
import uuid

# tasks = None
# backup_tasks = {}; Nutzen erschließt sich nicht


class Task:
    """ Klasse, die eine Aufgabe repräsentiert """
    priorities = {
        1: "niedrig",
        2: "mittel",
        3: "hoch"
    }
    format_code = "%d.%m.%Y"
    default_date = "31.12.9999"
    default_priority = 1

    def __init__(self, name=None, due_date=None, priority=None):
        """
            Instanziiert eine neue Aufgabe
            Args:
                name: Name der Aufgabe
                due_date: Fälligkeitsdatum als String; falls nicht angegeben, wird default_date der Klasse herangezogen
                priority: Dringlichkeit der Aufgabe; falls nicht angegeben oder unbekannt, wird default_priority gesetzt
            returns:
                None
        """
        self.id = int(uuid.uuid4())
        if name is None:
            self.name = "Platzhalter"
        else:
            self.name = name

        self.done = False
        self.set_due_date(due_date)
        if priority is None:
            self.set_priority(1)
        else:
            self.set_priority(priority)

    def set_done(self):
        """
            Setzt Aufgabe als erledigt
            Args:
                None
            Returns:
                None
        """
        self.done = True

    def set_priority(self, priority):
        """
            Ändern Priorität der Aufgabe, falls Priorität bekannt
            Args:
                priority: Neue Priorität
            Returns:
                None
        """
        if priority in Task.priorities:
            self.priority = priority
        else:
            self.priority = Task.default_priority

    def set_due_date(self, due_date=None):
        """
            Ändern des Fälligkeitsdatums
            Args:
                due_date: Neues Fälligkeitsdatum
            Returns:
                None

        """
        # Wenn due_date nicht gesetzt oder nicht zu datetime umwandelbar, default_date setzen
        if due_date is None:
            due_date = Task.default_date
        try:
            self.due_date = datetime.datetime.strptime(
                due_date, Task.format_code)
        except (ValueError, TypeError):
            self.due_date = datetime.datetime.strptime(
                Task.default_date, Task.format_code)

    def __str__(self):
        return f"""
        [{'x' if self.done else ' '}] Aufgabe {self.name} mit {str(self.id)} ist fällig am {datetime.datetime.strftime(self.due_date,Task.format_code)}
        und mit Priortät  {Task.priorities[self.priority]} zu behandeln.\n
        """


class TaskList:
    """ Klasse, die Aufgaben sammelt"""

    def __init__(self):
        """
            Instanziiert Taskliste und erstellt leeres dict self.tasks
        """
        self.tasks = {}

    def add_task(self, task: Task):
        """
            Fügt einen Task hinzu
            Args:
                task: Aufgabe, die hinzugefügt werden soll
            Returns:
                None
        """
        self.tasks[task.id] = task

    def get_task_count(self, done=None):
        """
            Gibt die Anzahl der noch zu erledigenden Aufgaben zurück
            Args:
                done: None, True oder False
            Returns:
                Anzahl aller Aufgaben oder
                Anzahl der Aufgaben, die
                    fertig sind, wenn done= True
                    offen sind, wenn done = False
                als int
            Raises:
                ValueError, wenn done weder None noch boolean

        """
        if done is None:
            return len(self.tasks)
        if isinstance(done, bool):
            return len([task for task in self.tasks.values() if task.done == done])
        raise (ValueError)

    def print_task_list(self, done=None):
        """
            Druckt die Taskliste je nach mode komplett (done==None)
            oder nur erledigte (done==True) /nicht erledigte (done==False)
            Args:
                done: None, True or False
            Returns:
                None
            Raises:
                ValueError, wenn done weder None noch boolean
        """

        if self.get_task_count() == 0:
            print("Keine Aufgaben in Aufgabenliste")
            return

        if done is None:
            for task in self.tasks.values():
                print(task)
        elif isinstance(done, bool):
            for task in self.tasks.values():
                if task.done == done:
                    print(task)
        else:
            raise (ValueError)

    def remove_task(self, task: Task, ):
        """
            Löscht einen Task anhand seiner ID
            Args:
                task_id
            Returns:
                None
        """
        del self.tasks[task.id]

    def mark_task_as_done(self, task: Task):
        """
            Markiert eine Aufgabe der Liste als erledigt
            Args:
                task_id
            Returns:
                None
            Raises:
                KeyError, wenn task.id nicht gefunden
        """
        if task.id in self.tasks:
            self.tasks[task.id].set_done()
        else:
            raise (KeyError("Aufgabe nicht in Liste"))

    def del_finished_tasks(self):
        """
            Entfernt Aufgaben aus der Liste, die als erledigt markiert sind
            Args:
                None
            Returns:
                None
        """
        for key in list(self.tasks.keys()):
            if self.tasks[key].done:
                del self.tasks[key]

    def __str__(self):
        return " ".join([task.__str__() for task in self.tasks.values()])


aufgabenliste = TaskList()

'''
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
'''

'''
def remove_task(task_id):
    global tasks
    if task_id in tasks:
        del tasks[task_id]
        return True
    return False
'''

'''
def mark_done(task_name):
    global tasks
    for task_id, task in tasks.items():
        if task[0] == task_name:
            task[3] = True
    return "Erledigt"
'''

'''
def show_tasks():
    global tasks
    for task_id, task in tasks.items():
        print(
            f"{task_id}: {task[0]} ({task[2]}) - bis {task[1]} - {'Erledigt' if task[3] else 'Offen'}")
'''


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


'''
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
'''


def get_task_count():
    return sum(1 for _ in tasks) if tasks else 0


'''add_task("Projekt abschließen", "25-05-2025", 1, task_id="hello")
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
'''

aufg1 = Task("Unikram", "27.10.2025", 2)
aufg2 = Task("Expose", "11.10.2025", 3)
ufgabenliste = TaskList()


aufgabenliste.add_task(aufg1)
aufgabenliste.add_task(aufg2)
aufgabenliste.print_task_list()
# aufgabenliste.remove_task(aufg1)
aufgabenliste.print_task_list(done=False)
aufgabenliste.mark_task_as_done(aufg2)
aufgabenliste.print_task_list()
aufg3 = Task("Weihnachten", "11.12.2025", "Test")
aufgabenliste.add_task(aufg3)
print("alle Tasks")
aufgabenliste.print_task_list()
print("nur offene")
aufgabenliste.print_task_list(done=False)
print("nur erledigte")
aufgabenliste.print_task_list(done=True)
aufgabenliste.del_finished_tasks()
print("Nach cleanup")
aufgabenliste.print_task_list()
