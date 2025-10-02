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
- Methoden wie calculate_task_average oder process_tasks haben unklare bzw. fragwürdige Funktionalität.
- Vermischung von deutscher und englischer Sprache (Kommentar vs. Variablen und Funktionsnamen).
- Datum wird als String verglichen → fehleranfällig und nicht robust.

Verbesserungsvorschläge:
- Einführung einer Task-Klasse oder Nutzung von Dictionaries mit klaren Schlüsseln (name, due_date, priority, ...).
- Entfernen globaler Variablen → stattdessen Übergabe von Datenstrukturen oder Nutzung einer TaskManager-Klasse.
- Einheitliche und sprechende Benennungen in Englisch oder Deutsch.
- Nutzung von datetime-Objekten statt Strings für Datumsvergleiche.
- Hinzufügen von Docstrings und Typannotationen für bessere Lesbarkeit.
- Fehlerbehandlung für ungültige Eingaben (z. B. Exception oder Rückgabewert).
- Konsistente Handhabung von Task-IDs (eindeutig, nur int oder nur string).
- Entfernen oder Überarbeiten unklarer Funktionen (z. B. calculate_task_average, process_tasks).
- Ergänzen von Unit-Tests, um Robustheit und Wartbarkeit zu erhöhen.
- Nutzung der main-Funktion für das Modul.

"""

import uuid
import datetime


class Task:
    def __init__(self, name: str, due_date: datetime.datetime, task_id: str, priority: int = 3, assigned_to: str = "user1"):
        self.name = name
        self.due_date = due_date
        self.priority = priority
        self.is_done = False
        self.assigned_to = assigned_to
        self.task_id = task_id
        self.created_at = datetime.datetime.now()

    def mark_done(self):
        self.is_done = True

    def __repr__(self):
        status = "Erledigt" if self.is_done else "Offen"
        return f"{self.name} ({self.priority}) - bis {self.due_date.strftime('%d-%m-%Y')} - {status}"


class TaskManager:
    def __init__(self):
        self.tasks: dict[str, Task] = {}

    def add_task(self, name: str, due_date: str, priority: int = 3, task_id: str | None = None) -> str:
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
