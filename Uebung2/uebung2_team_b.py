# Teilnehmer: RNSR und ANGE

"""
Dieses Modul enthält die Klassen `Task` und `TaskManager` zur Verwaltung von Aufgaben.
Es umfasst Funktionen zum Hinzufügen, Löschen, Bearbeiten und Anzeigen von Aufgaben.
"""

import uuid
import datetime

# pylint: disable=W0105, R0913, C0114


"""
Aufgabe 1:
Verständnisprobleme im Code:
- `tasks` und `backup_tasks` sollten gleich initialisiert werden, um Fehler zu vermeiden.
 (None vs dict)
- Was ist der Sinn hinter backup_tasks? Es wird nie verwendet.
- Wieso sind `tasks` und `backup_tasks` globale Variablen?
 Wäre es nicht besser, sie als Parameter zu übergeben oder in einer Klasse zu kapseln?

- `add_task`:
- Ein `task` sollte eine eigene Datenstruktur sein und keine Liste mit verschiedenen Attributen.
 Wieso wurde sich dafür entschieden?
- `task_id` wird zufällig berechnet (len(tasks) + random.randint),
 Kollisionen möglich bei einem Bereich von 2 bis 7. Besser UUID verwenden.
Wieso sollte dies nicht verändert werden? (Kommentar)
- `task_id` kann vom Benutzer gesetzt werden, was zu einem anderem Datentyp führen kann 
(string vs int).

- `mark_done`: 
- Wieso hat `mark_done` keinen Rückgabewert, wenn die Aufgabe nicht gefunden wird?
 Bzw. wieso wird kein Boolean zurückgegeben wie bei `remove_task`?

- `process_tasks`:
- Wieso hat `process_tasks` False als festen Rückgabewert und ein `# TODO` Kommentar?
- Soll `process_tasks` eine zufällige Aufgabe markieren/unmarkieren? Wieso? 

- `calculate_task_average`:
- `calculate_task_average` berechnet den Durchschnitt der task_ids, was wenig Sinn ergibt.
 Vielleicht sollte es die durchschnittliche Priorität sein?
- Namen der Funktion ist irreführend bzw. nicht sprechend

- `upcoming_tasks`:
- `upcoming_tasks` sortiert nach Name und nicht nach Datum, was sinnvoller wäre. 
Desweiteren wäre ein Parameter für ASC bzw. DESC sinnvoll.
- Die Ausgabe ist auch eine komplett andere als bei `show_tasks`. Wieso?

- `cleanup`:
- Wieso ist `cleanup` so komplex geschrieben? Es ist kein temp dict notwendig

- `get_task_count`:
- `get_task_count` könnte einfach `len(tasks)` zurückgeben. Wieso so kompliziert?

"""


"""
Aufgabe 2: 

Positive Aspekte:
- Funktionen sind thematisch klar getrennt (add, remove, mark_done, show, cleanup, ...).
- Der Code ist lauffähig und demonstriert grundlegende Funktionalität.
- Nutzung von Standardbibliotheken (datetime, random).
- Testaufrufe am Ende der Datei erleichtern erstes Verständnis.

Negative Aspekte:
- Globale Variablen (tasks, backup_tasks) → erschwert Testbarkeit und Wartbarkeit.
- Aufgaben werden als Liste gespeichert → unverständlich, was Index 0,1,2,... bedeutet.
- Keine Typannotationen oder Docstrings → Verständlichkeit und Lesbarkeit leiden.
- Keine Fehlerbehandlung bei ungültigen Eingaben (z. B. nicht existierende Task-IDs).
- Inkonsistente Datentypen für task_id (mal String, mal int).
- Methoden wie calculate_task_average oder process_tasks haben unklare 
bzw. fragwürdige Funktionalität.
- Vermischung von deutscher und englischer Sprache (Kommentar vs. Variablen und Funktionsnamen).
- Datum wird als String verglichen → fehleranfällig und nicht robust.

Verbesserungsvorschläge:
- Einführung einer Task-Klasse oder Nutzung von Dictionaries mit klaren Schlüsseln 
(name, due_date, priority, ...).
- Entfernen globaler Variablen → stattdessen Übergabe von Datenstrukturen 
oder Nutzung einer TaskManager-Klasse.
- Einheitliche und sprechende Benennungen in Englisch oder Deutsch.
- Nutzung von datetime-Objekten statt Strings für Datumsvergleiche.
- Hinzufügen von Docstrings und Typannotationen für bessere Lesbarkeit.
- Fehlerbehandlung für ungültige Eingaben (z. B. Exception oder Rückgabewert).
- Konsistente Handhabung von Task-IDs (eindeutig, nur int oder nur string).
- Entfernen oder Überarbeiten unklarer Funktionen 
(z. B. calculate_task_average, process_tasks).
- Ergänzen von Unit-Tests, um Robustheit und Wartbarkeit zu erhöhen.
- Nutzung der main-Funktion für das Modul.

"""


class Task:
    """
    Repräsentiert eine Aufgabe mit Name, Fälligkeitsdatum, Priorität, zugewiesenem Benutzer 
    und Status.

    Attribute:
        name (str): Name der Aufgabe.
        due_date (datetime.datetime): Fälligkeitsdatum der Aufgabe.
        priority (int): Prioritätslevel der Aufgabe (Standard: 3).
        assigned_to (str): Benutzer, dem die Aufgabe zugewiesen ist (Standard: "user1").
        task_id (str): Eindeutige Kennung der Aufgabe.
        is_done (bool): Gibt an, ob die Aufgabe erledigt ist.
        created_at (datetime.datetime): Zeitpunkt der Erstellung der Aufgabe.

    Methoden:
        mark_done():
            Markiert die Aufgabe als erledigt.

        __repr__():
            Gibt eine String-Repräsentation der Aufgabe zurück, 
            inkl. Name, Priorität, Fälligkeitsdatum und Status.
    """

    def __init__(self, name: str, due_date: datetime.datetime, task_id: str, priority: int = 3,
                 assigned_to: str = "user1"):
        self.name = name
        self.due_date = due_date
        self.priority = priority
        self.is_done = False
        self.assigned_to = assigned_to
        self.task_id = task_id
        self.created_at = datetime.datetime.now()

    def mark_done(self):
        """
        Markiert die aktuelle Aufgabe als erledigt.
        """
        self.is_done = True

    def __repr__(self):
        status = "Erledigt" if self.is_done else "Offen"
        return f"{self.name} ({self.priority}) " + \
               f"- bis {self.due_date.strftime('%d-%m-%Y')} - {status}"


class TaskManager:
    """
    TaskManager verwaltet Aufgaben mit Fälligkeitsdatum, Priorität und Status.

    Methoden:
        - add_task(name, due_date, priority=3, task_id=None): Fügt eine neue Aufgabe 
        hinzu und gibt die Task-ID zurück.
        - remove_task(task_id): Entfernt eine Aufgabe anhand ihrer ID.
        - mark_done_by_id(task_id): Markiert eine Aufgabe als erledigt anhand ihrer ID.
        - mark_done_by_name(task_name): Markiert eine Aufgabe als erledigt anhand ihres Namens.
        - show_tasks(): Gibt alle Aufgaben mit ihren Details aus.
        - toggle_task_status(task_id): Wechselt den Erledigt-Status einer Aufgabe.
        - calculate_average_priority(): Berechnet die durchschnittliche Priorität aller Aufgaben.
        - upcoming_tasks(): Gibt alle noch nicht abgelaufenen Aufgaben 
        sortiert nach Fälligkeitsdatum zurück.
        - cleanup(): Entfernt alle erledigten Aufgaben aus der Liste.
        - get_task_count(): Gibt die Anzahl der aktuellen Aufgaben zurück.

    Attribute:
        - tasks (dict[str, Task]): Dictionary mit allen Aufgaben, indiziert nach Task-ID.
    """

    def __init__(self):
        self.tasks: dict[str, Task] = {}

    def add_task(self, name: str, due_date: str, priority: int = 3,
                 task_id: str | None = None) -> str:
        """
        Fügt eine neue Aufgabe hinzu.
        :param name: Aufgabenname
        :param due_date: Fälligkeitsdatum im Format 'DD-MM-YYYY'
        :param priority: Wichtigkeit (1 = hoch, 3 = niedrig)
        :param task_id: Optional eine feste ID, sonst wird automatisch eine generiert
        :return: Task-ID
        """
        # Datum in datetime umwandeln
        try:
            due_date_obj = datetime.datetime.strptime(due_date, "%d-%m-%Y")
        except Exception as exc:
            raise ValueError(
                "Ungültiges Datum. Bitte im Format 'DD-MM-YYYY' eingeben.") from exc

        if task_id is None:
            task_id = str(uuid.uuid4())

        if task_id in self.tasks:
            raise ValueError("Task-ID existiert bereits.")

        task = Task(name, due_date_obj, task_id, priority)
        self.tasks[task_id] = task
        return task.task_id

    def remove_task(self, task_id: str) -> bool:
        """Löscht eine Aufgabe anhand ihrer ID."""
        return self.tasks.pop(task_id, None) is not None

    def mark_done_by_id(self, task_id: str) -> bool:
        """Markiert eine Aufgabe als erledigt (per ID statt Name)."""
        if task_id in self.tasks:
            self.tasks[task_id].mark_done()
            return True
        return False

    def mark_done_by_name(self, task_name: str) -> bool:
        """Markiert eine Aufgabe als erledigt (per Name statt ID)."""
        for task in self.tasks.values():
            if task.name == task_name:
                task.mark_done()
                return True
        return False

    def show_tasks(self) -> None:
        """Gibt alle Aufgaben aus."""
        for task_id, task in self.tasks.items():
            print(f"{task_id}: {task}")

    def toggle_task_status(self, task_id: str) -> bool:
        """Wechselt den Erledigt-Status einer Aufgabe."""
        if task_id in self.tasks:
            self.tasks[task_id].is_done = not self.tasks[task_id].is_done
            return True
        return False

    def calculate_average_priority(self) -> float:
        """Berechnet die durchschnittliche Priorität aller Aufgaben."""
        if not self.tasks:
            return 0.0
        total_priority = sum(task.priority for task in self.tasks.values())
        return total_priority / len(self.tasks)

    def upcoming_tasks(self) -> list[Task]:
        """Gibt alle noch nicht abgelaufenen Aufgaben sortiert nach Fälligkeitsdatum zurück."""
        today = datetime.datetime.today()
        upcoming = [task for task in self.tasks.values()
                    if task.due_date >= today]
        return sorted(upcoming, key=lambda t: t.due_date)

    def cleanup(self) -> None:
        """Entfernt erledigte Aufgaben."""
        self.tasks = {tid: task
                      for tid, task in self.tasks.items() if not task.is_done}

    def get_task_count(self) -> int:
        """Zählt die Aufgaben."""
        return len(self.tasks)


if __name__ == "__main__":

    manager = TaskManager()

    manager.add_task("Projekt abschließen", "25-05-2025", 1, task_id="hello")
    done_task_id = manager.add_task("Projekt abschließen", "25-05-2025", 1)
    manager.add_task("Einkaufen gehen", "21-05-2025", 3)
    manager.add_task("Dokumentation schreiben", "30-05-2025", 2)

    manager.mark_done_by_id(done_task_id)
    manager.mark_done_by_name("Einkaufen gehen")

    manager.show_tasks()

    print("Offene Aufgaben nach Datum sortiert:", manager.upcoming_tasks())

    manager.cleanup()

    print("Gesamtzahl der Aufgaben:", manager.get_task_count())


"""
************* Module Uebung2-TeamB
Uebung2/Uebung2-TeamB.py:6:0: C0301: Line too long (104/100) (line-too-long)
Uebung2/Uebung2-TeamB.py:8:0: C0301: Line too long (144/100) (line-too-long)
Uebung2/Uebung2-TeamB.py:11:0: C0301: Line too long (132/100) (line-too-long)
Uebung2/Uebung2-TeamB.py:12:0: C0301: Line too long (194/100) (line-too-long)
Uebung2/Uebung2-TeamB.py:13:0: C0301: Line too long (104/100) (line-too-long)
Uebung2/Uebung2-TeamB.py:16:0: C0301: Line too long (148/100) (line-too-long)
Uebung2/Uebung2-TeamB.py:23:0: C0301: Line too long (149/100) (line-too-long)
Uebung2/Uebung2-TeamB.py:27:0: C0301: Line too long (139/100) (line-too-long)
Uebung2/Uebung2-TeamB.py:54:0: C0301: Line too long (103/100) (line-too-long)
Uebung2/Uebung2-TeamB.py:59:0: C0301: Line too long (115/100) (line-too-long)
Uebung2/Uebung2-TeamB.py:60:0: C0301: Line too long (112/100) (line-too-long)
Uebung2/Uebung2-TeamB.py:77:0: C0301: Line too long (124/100) (line-too-long)
Uebung2/Uebung2-TeamB.py:91:0: C0301: Line too long (101/100) (line-too-long)
Uebung2/Uebung2-TeamB.py:98:0: C0301: Line too long (103/100) (line-too-long)
Uebung2/Uebung2-TeamB.py:1:0: C0103: Module name "Uebung2-TeamB" doesn't conform to snake_case naming style (invalid-name)
Uebung2/Uebung2-TeamB.py:39:0: W0105: String statement has no effect (pointless-string-statement)
Uebung2/Uebung2-TeamB.py:72:0: C0413: Import "import uuid" should be placed at the top of the module (wrong-import-position)
Uebung2/Uebung2-TeamB.py:73:0: C0413: Import "import datetime" should be placed at the top of the module (wrong-import-position)
Uebung2/Uebung2-TeamB.py:76:0: C0115: Missing class docstring (missing-class-docstring)
Uebung2/Uebung2-TeamB.py:77:4: R0913: Too many arguments (6/5) (too-many-arguments)
Uebung2/Uebung2-TeamB.py:86:4: C0116: Missing function or method docstring (missing-function-docstring)
Uebung2/Uebung2-TeamB.py:94:0: C0115: Missing class docstring (missing-class-docstring)

-----------------------------------
Your code has been rated at 7.18/10
"""


"""
- Uebung2/Uebung2-TeamB.py:6:0 - Notwendig für die Bearbeitung von Aufgabe 1 und 2,
jedoch hätte man auch Zeilen auf 80 char begrenzen können.
Die Grenzen der Zeilenlänge sind jedoch nicht mehr allzu relevant,
da viele Editoren und IDEs dies automatisch umbrechen und aufgrund entsprechend großer Bildschirme.
- Uebung2/Uebung2-TeamB.py:1:0: C0103: - Stimmen wir zu, 
der Dateiname sollte pythonic sein, also uebung2_team_b.py
- Uebung2/Uebung2-TeamB.py:39:0: W0105: - Betrifft Bearbeitung von Aufgabe 1 und 2, keine Bedeutung 
- Uebung2/Uebung2-TeamB.py:72:0: C0413: - Aufgrund Bearbeitungsvorgaben, 
stehen die Imports nicht am Anfang der Datei.
Können verschoben werden, sind dann jedoch weiter vom Code entfernt aufgrund der Aufaben 1 und 2.
- Uebung2/Uebung2-TeamB.py:76:0: C0115: - Beschreibung der Klasse könnte ergänzt werden, 
ist jedoch selbsterklärend.
- Uebung2/Uebung2-TeamB.py:77:4: - Das stimmt, jedoch sind die Argumente notwendig für 
z.B. spätere Funktionalitäten (Angabe eines Users, bei der Erstellung einer Aufgabe)
- Uebung2/Uebung2-TeamB.py:86:4: C0116: - Beschreibung der Methode könnte ergänzt werden
- Uebung2/Uebung2-TeamB.py:94:0: C0115: - Beschreibung der Klasse könnte ergänzt werden, 
ist jedoch selbsterklärend.
"""
