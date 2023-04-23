# SchildNRW-WebUntis-Umwandler
Ein Umwanlder, der Daten aus SchildNRW passend für den Import nach WebUntis aufbereitet.

Ich habe mir die Mühe gemacht ein kleines Programm zu basteln, was Sie unterstützen kann, die für WebUntis verwertbaren Schüler:innen und Daten aus Schild nach WebUntis zu übertragen, also aus Schild NRW zu exportieren und in WebUntis importieren.

Das Programm nimmt sich einen Export von Schild, wandelt mehrere Spalten so um, dass sie in dem Format angelegt werden, wie WebUnits sie braucht und speichert das Ergebnis als neue Datei mit dem aktuellen Datum und der Uhrzeit in einem Unterordner wieder ab.
Dazu muss die .csv im selben Ordner liegen wie die .exe Datei. Das Programm sucht immer nach der neuesten .csv in diesem Ordner und nimmt diese als Datenquelle.

Voraussetzungen:
1. Ein Auswahfilter (Filter I) in SchildNRW, der wie folgt eingestellt ist:
Unten bei Laufbahninfo: Schuljahr das aktuelle Schuljahr auswählen
Oben rechts bei Status: Aktiv, Abschluss und Abgänger anwählen
-> Sie sollten diesen Filter speichern, damit Sie ihn später über Auswahl - Vorhandene Filter laden .. wieder verwenden können.

2. Ein Export aus SchildNRW als Text/Excel Export, jedoch unbedingt mit der manuell eingegebenen Dateiendung .csv.
Als Seperator ist ";" zu wählen.
Erforderliche Daten (idealerweise auch in dieser Reihenfolge): Interne ID-Nummer, Nachname, Vorname, Klasse, Geburtsdatum, Geschlecht, vorrauss. Abschluss, Aufnahmedatum, Entlassdatum, Volljährig, Schulpflicht erfüllt, Status
Optionale Daten: E-mail (privat), Telefon-Nr., Fax-Nr., Straße, Postleitzahl, Ortsname
Hinweise:
Es wird nicht funktionieren, wenn Sie die Datei als Excel-Datei exportieren und diese als .csv abspeichern.
-> Speichern sie sich diese Exporteinstellung als Vorlage ab, um Sie später schneller wieder verwenden zu können.

3. Ein in WebUntis korrekt konfigurierter Import:
Als Zeichensatz ist UTF-8 zu wählen.
https://schulverwaltungsinfos.nrw.de/svws/forum/download/file.php?id=6319

Hinweise:
Wir benutzen die Interne ID-Nummer aus Schild / Schlüssel(extern) in WebUnits zur Schüleridentifikation. Das kann bei Ihnen anders sein.
Wir benutzen das Feld Faxnummer aus Schild als Mobiltelefonnummer
Importieren sie den Status aktiv, werden inaktive Schüler in WebUnits deaktiviert (nicht gelöscht)
Importieren sie das Entlassdatum, werden Schüler auch in WebUntis ab diesem Datum nicht mehr in dem Klassenbuch angezeigt, rückwirkend aber schon. Es gehen keine Daten verloren.
Die Daten Schulpflicht und Volljährig sind nur bei Nutzung des digitalen Klassenbuchs oder bei der Nutzung von WebUnits als digialer Klassenordner von Nutzen.
Testen Sie den Import unbedingt vorher in einer WebUnits Spielwiese! Ich übernehme keinerlei Haftung.
Sie erhalten unter folgenden Links die ausführbaren .exe Dateien,
die zu grundliegenden Python Skripte, aus dem die .exe Datei kompiliert wurden
und den Quellcode nochmal als .txt Dateien.
