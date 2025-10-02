= Übung 02: Erste Auswertung mit Matplotlib und NumPy

=== 2.

Anzahl der Einträge pro Monat:
#table(
  columns: 2,
  align: (center, center),
  [MONTH], [Einträge],
  [1], [153],
  [2], [153],
  [3], [153],
  [4], [153],
  [5], [154],
  [6], [154],
  [7], [154],
  [8], [154],
  [9], [153],
  [10], [153],
  [11], [153],
  [12], [153],
)

Ältestes Jahr im Datensatz: 1872
Aktuellstes Jahr im Datensatz: 2025

Statistiken für wichtige Variablen:
Variable 'T': Min = -9.7, Max = 24.3
Variable 'NUMFROST': Min = 0, Max = 31
Variable 'NUMSUMMER': Min = 0, Max = 30

Anzahl der fehlenden Werte (NaN) pro wichtiger Variable:
Variable 'T': 0 NaN-Werte
Variable 'NUMFROST': 0 NaN-Werte
Variable 'NUMSUMMER': 0 NaN-Werte

=== 2.1

#image("./out/temperaturunterschiede_boxplot.png")

=== 2.2

#image("./out/durchschnittstemperatur_juli.png")

#image("./out/hitzetage.png")

#image("./out/frosttage.png")

#image("./out/windtage.png")

=== 2.3

#image("./out/boxplot_vergleich_perioden.png")

=== 2.4

Top 5 Jahre mit den meisten Frosttagen:
1. Jahr 1875 mit 119 Frosttagen
2. Jahr 1887 mit 112 Frosttagen
3. Jahr 1924 mit 111 Frosttagen
4. Jahr 1888 mit 111 Frosttagen
5. Jahr 1889 mit 111 Frosttagen
