# Nothilfe Tracker

Dieses Projekt trackt die Anzahl der Anträge zu der Soforthilfe für Studierende und Fachschüler*innen. [Link](https://www.einmalzahlung200.de/eppsg-de)
Da das BMBF netterweise deine Infobox mit der Anzahl der erfoglreichen Anträge und ausgezahlten Anträge auf der Seite hat, wollte ich das mal tracken.

## Hast du zu viel Zeit?
Vermutlich, aber ich wollte sowieso mal ein bisschen mit Python, Docker und cron spielen.
Also habe ich mir das mal angeschaut und ein kleines Script geschrieben, dass die Anzahl der Anträge trackt und in eine CSV schreibt.

## Wie funktioniert das?


Was Python angeht ist die Sache an sich recht einfach: Mit `requests` wird die Seite angefragt und mit `lxml` der ganze HTML-Unfug in etwas schöneres geparst.
Dann kann man mit `xpath` die Elemente in der Infobox finden und auslesen. Dabei bringt man den Text (!) in ein schöneres Format und schreibt ihn in die CSV.
Damit das ganze schöner aussieht, habe ich mir eine `data` Klasse erstellt. Die kann man dann sehr einfach mit `pandas` als CSV exportieren.
Ansonsten ist noch eine kleine `Logger` Klasse vorhanden, mit der ich mir anschauen kann, was passiert.

Das Script läuft in einem Docker Container und wird mit einem Cronjob alle 15 Minuten (von der vollen Stunde) ausgeführt.

## Wie kann ich das installieren?

Du brauchst nur Docker und Docker Compose. Dann kannst du einfach das Repository klonen und mit `docker-compose up -d --build` den Container starten.
Die Daten findest du dann, wenn du mit `docker exec -it tracker /bin/bash` die interaktive Docker Konsole startest in `data/data.csv`.

## Hast du schon deine 200€ bekommen?

**Ja**, am 16.03.2023 um 14:12 war das Geld auf meinem Konto! Beantragt habe ich am 15.03.2023 um 07:38.