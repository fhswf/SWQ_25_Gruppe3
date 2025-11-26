# Übung 6: Code-Qualitätsanalyse mit SonarQube

## Lernziele

In dieser Übung lernen Sie:
- Die Einrichtung und Nutzung von SonarQube zur statischen Code-Analyse
- Die Integration von SonarQube in GitHub Actions
- Die Interpretation von SonarQube-Analyseergebnissen
- Die systematische Behebung von Code-Qualitätsproblemen
- Die Analyse von Test Coverage in größeren Projekten

---

## Teil 1: SonarQube-Analyse mit Python

**Geschätzte Bearbeitungszeit: 60-75 Minuten**

### Schritt 1: Projekt erstellen (5 Minuten)

1. Loggen Sie Sich bei Github ein
2. Navigieren Sie zu https://github.com/SonarQube-Org-Example/SonarQube-Example-Template und klicken Sie rechts oben auf "Use this template" -> "Create a new repository"
3. Wählen Sie als "Owner" die FHSWF-Organisation, vergeben den Namen `SWQ25_G<Nummer>_T<Nummer>_SonarQube` (ersetzen Sie `<Nummer>` durch Ihre Gruppen-/Teamnummer, z.B. `SWQ25_G4_T1_SonarQube` und machen Sie daraus ein **öffentliches Repository**

### Schritt 2: SonarQube-Projekt anlegen (10 Minuten)

1. **Login in SonarQube**
   - Öffnen Sie https://sonarqube.fh-swf.cloud/
   - Melden Sie sich mit Ihren GitHub-Zugangsdaten an

2. **Neues Projekt erstellen**
   - Klicken Sie oben rechts auf **"Create Project"**
   - Wählen Sie **"Locall project"** (lokales Projekt)
   - Geben Sie folgende Informationen ein:
     - **Project display name**: `SWQ25_G<Nummer>_T<Nummer>_SonarQube` (z.B. `SWQ25_G4_T1_SonarQube`)
     - **Project key**: (derselbe Name wie oben)
     - **Main branch name**: `main`
   - Klicken Sie auf **"Next"**
   - Wählen Sie "Follows the instance's default"
   - Klicken Sie auf **"Create project"**

3. **Token generieren**
   - Wählen Sie **"With GitHub Actions"**
   - Erstellen Sie die Secrets in Ihrem Respository so wie angegeben (inkl. Token-Generierung). Bitte beachten:
      - Das generierte Token wird nur einmal angezeigt! Direkt kopieren!
      - Die Anleitung zum Anlegen der Secrets finden Sie auch unten in Schritt 3
   - Bei "Create Workflow YAML file" wählen Sie **"Python"** und als OS **Linux**
   - SonarQube zeigt Ihnen nun Anweisungen zur Integration
      - Die Änderungen können Sie ohne Codespaces direkt in GitHub durchführen, mit Codespaces arbeiten oder das Repository auschecken, verändern und die Änderungen pushen

### Schritt 3: GitHub Actions konfigurieren (15 Minuten)

1. **GitHub Secrets einrichten**
   - Öffnen Sie Ihr GitHub-Repository im Browser
   - Navigieren Sie zu **Settings** → **Secrets and variables** → **Actions**
   - Klicken Sie auf **"New repository secret"**
   - Erstellen Sie folgende Secrets:

     **SONAR_TOKEN**:
     - Name: `SONAR_TOKEN`
     - Value: Der zuvor kopierte SonarQube-Token
     - **ACHTUNG**: Fügen Sie den Token ohne Newline/Zeilenumbruch ein! Kopieren Sie ihn direkt aus SonarQube.
     
     **SONAR_HOST_URL**:
     - Name: `SONAR_HOST_URL`
     - Value: `https://sonarqube.fh-swf.cloud`
     - **ACHTUNG**: Auch hier keine Zeilenumbrüche!

2. **Properties-Datei erstellen**
   - Erstellen Sie die `sonar-project.properties` Datei in Ihrem Repository und fügen Sie die von SonarQube angegebene Zeile ein

3. **Workflow-Datei erstellen**
   - Klicken Sie auf "Actions" in Ihrem Repository
   - Wählen Sie ganz oben "Skip this and set up a workflow yourself ->"
   - Fügen Sie den YAML-Content aus SonarQube ein und entfernen Sie die Kommentarzeichen weiter unten in der Datei, damit der Build abbricht, wenn das Quality Gate rot ist
   - Fügen Sie folgenden Trigger hinzu, damit Sie den Build manuell starten können:

   ```yaml
   on:
     push:
       branches:
         - main
     workflow_dispatch:  # <-- Diese Zeile hinzufügen
   ```

4. **Änderungen committen und pushen**

### Schritt 4: Build manuell starten (5 Minuten)

**Ihr Build sollte nach der Erstellung des Workflos automatisch starten. Ist dies nicht der Fall, starten Sie den Build manuell:**

1. **GitHub Actions aufrufen**
   - Gehen Sie in Ihrem Repository auf den Tab **"Actions"**
   - Links sehen Sie die Liste der Workflows
   - Klicken Sie auf den Workflow (z.B. "Build")

2. **Manuellen Build starten**
   - Oben rechts sehen Sie den Button **"Run workflow"**
   - Klicken Sie darauf
   - Wählen Sie den Branch `main`
   - Klicken Sie auf **"Run workflow"**
   - Der Build startet und Sie können den Fortschritt verfolgen

3. **Build-Ergebnis prüfen**
   - Warten Sie, bis der Build abgeschlossen ist (grüner Haken = erfolgreich)
   - Bei Problemen können Sie die Logs einsehen, indem Sie auf den Build-Job klicken

### Schritt 5: Ergebnisse in SonarQube analysieren (15 Minuten)

1. **SonarQube-Dashboard öffnen**
   - Gehen Sie zurück zu https://sonarqube.fh-swf.cloud/
   - Klicken Sie auf Ihr Projekt `SWQ25_G<Nummer>_T<Nummer>_SonarQube`

2. **Übersicht verstehen**
   - **Reliability** (Zuverlässigkeit): Bugs, die zu unerwartetem Verhalten führen
   - **Security** (Sicherheit): Sicherheitslücken und Sicherheits-Hotspots
   - **Maintainability** (Wartbarkeit): Code Smells, die die Wartung erschweren
   - **Coverage** (Testabdeckung): Anteil des getesteten Codes
   - **Duplications** (Duplikate): Code-Duplikate

3. **Issues strukturiert ansehen**
   - Klicken Sie im linken Menü auf **"Issues"**
   - Verwenden Sie die Filter oben:
     - **Severity**: Blocker, Critical, Major, Minor, Info
     - **Type**: Bug, Vulnerability, Code Smell
     - **Status**: Open, Confirmed, Resolved
   - Sortieren Sie nach **Severity** (schwerwiegendste zuerst)

4. **Issue-Details verstehen**
   - Klicken Sie auf ein Issue
   - Lesen Sie die Beschreibung
   - Klicken Sie auf **"Why is this an issue?"** - dies erklärt:
     - Warum der Code problematisch ist
     - Welche Risiken bestehen
     - Wie das Problem behoben werden kann
   - Unter **"How can I fix it?"** finden Sie oft Code-Beispiele

**Aufgaben zur Analyse:**
1. Wie viele Issues wurden insgesamt gefunden? Notieren Sie die Anzahl nach Typ (Bugs, Vulnerabilities, Code Smells).
2. Welches Issue hat die höchste Severity (Blocker)? Was ist das Problem?
3. Suchen Sie ein Issue mit Severity "Critical". Lesen Sie "Why is this an issue?" - erklären Sie kurz, warum dies ein Problem ist.

### Schritt 6: Code-Problem provozieren (10 Minuten)

1. **Datei bearbeiten**
   - Öffnen Sie die Datei `src/S2115.py`
   - Suchen Sie das "non-compliant" return statement (sollte als Kommentar markiert sein)
   - Kommentieren Sie die Zeile **aus** (fügen Sie ein `#` am Zeilenanfang hinzu)

2. **Änderung committen und pushen**

3. **Build-Fehler beobachten**
   - Gehen Sie zu **Actions** in GitHub
   - Der Build sollte automatisch starten (durch den Push)
   - **Der Build schlägt fehl** - dies ist gewollt!
   - Klicken Sie auf den fehlgeschlagenen Build
   - Schauen Sie sich die Logs an - wo ist der Fehler?

4. **Ergebnis in SonarQube**
   - Gehen Sie zu SonarQube
   - Das neue Issue sollte nun sichtbar sein
   - Analysieren Sie, welches neue Problem hinzugekommen ist

### Schritt 7: Problem beheben (5 Minuten)

1. **Code korrigieren**
   - Öffnen Sie erneut `src/S2115.py`
   - **Löschen** Sie die auskommentierte (non-compliant) Zeile komplett
   - Speichern Sie die Datei

2. **Änderung committen**

3. **Build-Erfolg verifizieren**
   - Warten Sie, bis der Build durchläuft (grüner Haken)
   - Prüfen Sie in SonarQube, dass das Issue verschwunden ist

### Schritt 8: Security-Issue beheben (15 Minuten)

1. **Blocker-Issue identifizieren**
   - In SonarQube, filtern Sie nach **Severity: Blocker**
   - Suchen Sie das Issue: **"Add password protection to this database"**
   - Lesen Sie "Why is this an issue?" - verstehen Sie das Sicherheitsproblem

2. **Erster Fix-Versuch (falsch)**
   - Öffnen Sie die entsprechende Datei
   - Setzen Sie das Passwort direkt im Code auf `"passwort"`:
     ```python
     password="passwort"
     ```
   - Committen und pushen Sie die Änderung
   - Build läuft durch - aber schauen Sie in SonarQube!

3. **Neues Problem in SonarQube**
   - Ein neues Security-Issue sollte erscheinen
   - Das Passwort sollte **nicht** im Code gespeichert werden
   - Lesen Sie "Why is this an issue?" für dieses neue Problem

4. **Korrekter Fix**
   - Das Passwort muss aus einer System Property geladen werden
   - Ändern Sie den Code wie folgt:
     ```python
     import os
     password = os.getenv('DB_PASSWORD')
     ```
   - Committen und pushen Sie die Änderung

5. **Ergebnis prüfen**
   - Build sollte durchlaufen
   - In SonarQube: Das Blocker-Issue sollte verschwunden sein
   - Möglicherweise erscheint ein Minor-Issue zum Fehlerhandling - das ist akzeptabel

### Schritt 9: Alle verbleibenden Issues beheben (>15 Minuten)

**Aufgabe:**
Beheben Sie nun systematisch alle verbleibenden Issues in SonarQube. Gehen Sie dabei wie folgt vor:

1. **Priorisierung**
   - Beheben Sie Issues in dieser Reihenfolge:
     1. Blocker
     2. Critical
     3. Major
     4. Minor
     5. Info

2. **Vorgehen pro Issue**
   - Lesen Sie die Beschreibung und "Why is this an issue?"
   - Verstehen Sie das Problem
   - Implementieren Sie den Fix
   - Committen und pushen Sie die Änderung
   - Warten Sie auf den Build
   - Verifizieren Sie in SonarQube

3. **Ziel**
   - Reduzieren Sie die Issues auf 0 (falls möglich)
   - Erreichen Sie mindestens ein "A" Rating für Reliability und Security
   - Verbessern Sie das Maintainability-Rating

---

## Teil 2: Test Coverage mit Spring PetClinic (Optional)

**Geschätzte Bearbeitungszeit: 30-45 Minuten**

### Schritt 1: Repository forken (5 Minuten)

1. **Fork erstellen**
   - Öffnen Sie https://github.com/spring-projects/spring-petclinic
   - Klicken Sie oben rechts auf **"Fork"**
   - Wählen Sie die **FHSWF-Organisation** als Ziel
   - Benennen Sie das Repository: `SWQ25_G<Nummer>_T<Nummer>_PetClinic` (z.B. `SWQ25_G4_T1_PetClinic`)
   - Stellen Sie sicher, dass das Repository **public** ist
   - Klicken Sie auf **"Create fork"**

### Schritt 2: Workflows entfernen (2 Minuten)

1. **Workflows-Ordner löschen**
   - Löschen Sie den bestehenden Ordner `.github` oder den Unterordener `workflows`

   Dies stellt sicher, dass keine vorhandenen GitHub Actions mehr ausgeführt werden.

### Schritt 3: SonarQube-Projekt anlegen (8 Minuten)

1. **Neues Projekt in SonarQube**
   - Gehen Sie zu https://sonarqube.fh-swf.cloud/
   - Erstellen Sie ein neues Projekt mit **"Manually"**
   - **Project display name**: `SWQ25_G<Nummer>_T<Nummer>_PetClinic`
   - **Project key**: (wie oben)
   - **Main branch name**: `main`

2. **Analysis Method wählen**
   - Wählen Sie **"With GitHub Actions"**
   - Wählen Sie als Build-Tool: **"Maven"**

3. **Workflow-Datei erstellen** (analog zu oben)
   - SonarQube zeigt Ihnen eine beispielhafte Workflow-Datei
   - **Wichtig**: Passen Sie die Java-Version an:
     - Ändern Sie `java-version: '17'` (oder was auch immer angezeigt wird)
     - Zu: `java-version: '25'`
   - Fügen Sie den manuellen Trigger hinzu (wie bei Aufgabe 1)
   - Erstellen Sie die Action wie in Aufgabe 1

4. **GitHub Secrets einrichten**
   - Erstellen Sie die Secrets `SONAR_TOKEN` und `SONAR_HOST_URL` wie in Teil 1
   - **Achtung**: Keine Newlines in den Secrets!

### Schritt 4: Build starten und analysieren (15 Minuten)

**Sollte der Build nicht automatisch gestartet werden, starten Sie Ihn manuell**

1. **Manuellen Build starten**
   - Gehen Sie zu **Actions** in GitHub
   - Klicken Sie auf **"Run workflow"** und starten Sie den Build
   - Der Build dauert einige Minuten (Maven muss Dependencies laden)

2. **Ergebnis in SonarQube**
   - Warten Sie, bis die Analyse abgeschlossen ist
   - Öffnen Sie Ihr PetClinic-Projekt in SonarQube

3. **Coverage-Übersicht**
   - Im Dashboard sehen Sie die **Coverage**-Metrik
   - Klicken Sie auf **"Coverage"** im linken Menü
   - Sie sehen nun eine Übersicht der Testabdeckung

### Schritt 5: Coverage strukturiert analysieren (10+ Minuten)

**Coverage-Dashboard verstehen:**

Die Test Coverage zeigt an, welcher Anteil Ihres Codes durch automatisierte Tests abgedeckt ist. SonarQube unterscheidet dabei:

1. **Overall Coverage**
   - Gesamtabdeckung über alle Dateien
   - Wird als Prozentsatz angezeigt
   - Ein höherer Wert bedeutet mehr getesteten Code

2. **Line Coverage**
   - Zeigt an, wie viele Codezeilen von Tests ausgeführt wurden
   - Grüne Zeilen: wurden getestet
   - Rote Zeilen: wurden nicht getestet

3. **Branch Coverage**
   - Betrifft Kontrollstrukturen (if/else, switch, etc.)
   - Zeigt, ob alle möglichen Ausführungspfade getestet wurden
   - Wichtig für vollständige Testabdeckung

**Coverage nach Datei/Package analysieren:**

1. **Coverage-Ansicht öffnen**
   - Klicken Sie im Projekt auf den Tab **"Measures"**
   - Wählen Sie links **"Coverage"**
   - Sie sehen nun eine Baumstruktur nach Packages

2. **Farbcodierung verstehen**
   - **Dunkelgrün** (>80%): Sehr gute Abdeckung
   - **Hellgrün** (50-80%): Mittlere Abdeckung
   - **Orange** (30-50%): Geringe Abdeckung
   - **Rot** (<30%): Sehr geringe oder keine Abdeckung

3. **Details pro Datei**
   - Klicken Sie auf ein Package, um die enthaltenen Klassen zu sehen
   - Klicken Sie auf eine Klasse, um den Code mit Abdeckung zu sehen
   - Im Code:
     - **Grüne Zeilen**: Durch Tests abgedeckt
     - **Rote Zeilen**: Nicht durch Tests abgedeckt
     - **Gelbe Markierungen** bei Bedingungen: Nur teilweise getestete Branches

4. **Uncovered Code identifizieren**
   - Filtern Sie nach **"Uncovered Lines"** oder **"Uncovered Conditions"**
   - Identifizieren Sie kritische Code-Bereiche ohne Tests
   - Priorisieren Sie:
     - Business-Logik
     - Sicherheitsrelevanter Code
     - Fehlerbehandlung

**Aufgaben zur Coverage-Analyse:**

1. **Allgemeine Metriken**
   - Wie hoch ist die Overall Coverage des Projekts?
   - Wie viele Lines of Code gibt es insgesamt?
   - Wie viele Lines werden durch Tests abgedeckt?

2. **Package-Analyse**
   - Welches Package hat die höchste Coverage?
   - Welches Package hat die niedrigste Coverage?
   - Warum könnte es sinnvoll sein, dass manche Packages niedrigere Coverage haben (z.B. Model-Klassen vs. Service-Klassen)?

3. **Detail-Analyse**
   - Wählen Sie eine Klasse mit mittlerer Coverage (50-80%)
   - Öffnen Sie den Code in SonarQube
   - Identifizieren Sie 3 nicht getestete Code-Bereiche
   - Überlegen Sie: Welche dieser Bereiche sollten priorisiert getestet werden? Warum?

4. **Branch Coverage**
   - Finden Sie eine Methode mit unvollständiger Branch Coverage
   - Wie viele Branches gibt es?
   - Wie viele sind getestet?
   - Welcher Ausführungspfad wird nicht getestet?

5. **Best Practices**
   - Spring PetClinic ist ein Demo-Projekt. Welche Coverage würden Sie für ein Produktionsprojekt empfehlen?
   - Welche Arten von Code müssen nicht zwingend zu 100% getestet werden?
   - Wann ist eine hohe Branch Coverage besonders wichtig?

**Tipps zur Interpretation:**

- **100% Coverage bedeutet nicht 100% Qualität**: Tests können existieren, aber unzureichend sein
- **Fokus auf kritischen Code**: Nicht alles muss gleich hoch abgedeckt sein
- **Trendanalyse**: Wichtiger als ein einzelner Wert ist die Entwicklung über Zeit
- **Uncovered Code in Exception-Handling**: Oft schwer zu testen, aber wichtig für Produktionsstabilität
