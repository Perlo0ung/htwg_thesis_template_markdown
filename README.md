# Htwg Konstanz Thesis Template

Dies ist ein Template zum Schreiben der Bachelor/Masterarbeit an der Htwg Konstanz mit dem Markdown Syntax.

## Benötigte Software:

* __Pandoc__
* __MikTex__
* (Python)

## Aufbau:

* __chapters:__  Enthält die Markdown-Dateien der eingentlichen Kapitel 
* __code:__ Code Beispiele
* __images:__ Ort für Bilder
* __resources:__ Deckblatt-Vorlage der HTWG im tex-Format
* __result:__ Ergebnis der Umwandlung von Pandoc

Die eigentlichen Kapitel werden als Markdown-Dateien geschrieben und mit dem Program __Pandoc__ zu einem PDF umgewandelt. Für Features die nicht von Markdown unterstützt werden, kann Latech-Code verwendet werden. Die vorhandenen Kapitel geben darüber Auskunft wie Code, Bilder, Fußnoten usw. im Dokument eingebaut werden.

## Einstellungen der Arbeit

Die Einstellungen der Arbeit (Author, Prüfer, usw. ) werden in der Datei ```settings.yaml``` vorgenommen.

__Quellen__ werden mit der Datei ```resources/thesis.bib``` gemanaged.

Der Style der Arbeit ist definiert durch die Datei ```resources/ba_template.tex```, dies ist das Standard Markdown zu PDF Template von Pandoc und wurde fürs schreiben der Thesis speziell angepasst.


## Dokument erstellen

Entweder:

* Script nutzen ```python build.py```

oder:

* Kommandozeile
```
pandoc -p 
      -f markdown 
      --csl=resources/ieee.csl 
      --chapters 
      --number-sections 
      --include-before-body=resources/startthesis.tex 
      --include-after-body=resources/appendix.tex 
      --template=resources/ba_template.tex 
      -o result.pdf 
      --bibliography resources/thesis.bib 
      settings.yaml 100-chapter1.md 200-chapter2.md 300-chapter3.md 998-thx.md 999-literatur.md
````


## Wichtiges

* Jedes Markdowndokument mit einer leeren Zeile abschließen
* Kapitel die nicht als Chapter erkannt werden sollen müssen mit Latech definiert werden (siehe 998-thx.md)
* Das Quellenverzeichnis wird automatisch am Ende angefügt, dafür muss ein Markdown Dokument vorhanden sein (999-literatur.md)
* Bildergrößen lassen sich nur über Latex Imageinput Kommandos definieren, sollte man den Markdown Syntax verwenden muss das Bild bereits auf die richtige Größe skaliert sein.

## Known Bugs

* Pandoc erlaubt es nicht Kapitel nach dem Quellenverzeichnis einzufügen, um dies zu bewerkstelligen muss jeglicher Anhang als Latech über den  ```--include-after-body``` Mechanismus angefügt werden. (Siehe https://github.com/jgm/pandoc/issues/771)


