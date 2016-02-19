# Htwg Konstanz Thesis Template

Dies ist ein Template zum Schreiben der Bachelor/Masterarbeit an der Htwg Konstanz mit Markdown.

## Aufbau:

* __chapters:__  Enthält die Markdown-Dateien der eingentlichen Kapitel 
* __code:__ Code Beispiele
* __images:__ Ort für Bilder
* __resources:__ Deckblatt-Vorlage der HTWG im tex-Format
* __result:__ Ergebnis der Umwandlung von Pandoc

Die eigentlichen Kapitel werden als Markdown-Dateien geschrieben und mit dem Program__Pandoc__ zu einem PDF umgewandelt. Für Features die nicht von Markdown unterstützt werden, kann Latech-Code verwendet werden. Die vorhandenen Kapitel geben darüber Auskunft wie Code, Bilder, Fußnoten usw. im Dokument eingebaut werden.

## Einstellungen der Arbeit

Die Einstellungen der Arbeit (Author, Prüfer, usw. ) werden in der Datei ```settings.yaml``` vorgenommen.

__Quellen__ werden mit der Datei ```resources/thesis.bib``` gemanaged.

Der Style der Arbeit ist definiert durch die Datei ```resources/ba_template.tex```, dies ist das Standard Markdown zu PDF Template von Pandoc und wurde fürs schreiben der Thesis speziell angepasst.

## Wichtiges

* Jedes Markdowndokument mit einer leeren Zeile abschließen
* Kapitel die nicht als Chapter erkannt werden sollen müssen mit Latech definiert werden (siehe 998-thx.md)

## Known Bugs

* ```settings.yaml``` erlaubt keine deutschen Umlaute (ä ö ü ß), dies kann umgangen werden in dem man die jeweilige Einstellung per ```\renewcommand``` in ```resources\startthesis.tex``` überschreibt.
* Pandoc erlaubt es nicht Kapitel nach dem Quellenverzeichnis einzufügen, um dies zu bewerkstelligen muss jeglicher Anhang als Latech über den  ```--include-after-body``` Mechanismus angefügt werden. (Siehe https://github.com/jgm/pandoc/issues/771)

