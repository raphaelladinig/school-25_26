5. Erkenntnisse

5.1 Eignung der Regressionsgeraden für die Prognose

Kurzfristig (bis 2030): Die lineare Regression eignet sich gut für kurzfristige Prognosen (z. B. 10–15 Jahre). Die Bevölkerungsentwicklung in stabilen Regionen wie Tirol verläuft oft sehr stetig, weshalb der lineare Trend für das Jahr 2030 eine plausible Schätzung liefert.

Langfristig (bis 2100): Für sehr lange Zeiträume ist die lineare Regression weniger geeignet.

Grund: Ein lineares Modell geht von einem unendlichen Wachstum mit gleicher absoluter Zahl pro Jahr aus (y=ax+b).

Realität: In der Realität gibt es Sättigungsgrenzen (Wohnraum, Ressourcen) oder demografische Wandel (Geburtenrückgang), die das Wachstum verlangsamen. Für 2100 würde das Modell vermutlich unrealistisch hohe Zahlen liefern. Ein logistisches Wachstumsmodell wäre hier oft besser.

5.2 Erkenntnisse aus dem Datenmaterial

Durch die Analyse der Koeffizienten (a und b) und der Grafiken lassen sich folgende Schlüsse ziehen:

Wachstumsgeschwindigkeit (Steigung a): Der Wert a (in model.params[1]) gibt exakt an, um wie viele Personen die Bevölkerung bzw. die Nächtigungen pro Jahr im Durchschnitt wachsen.

Beispiel: Ein hohes a bei Innsbruck-Land im Vergleich zu einem niedrigen a in einem Randbezirk (z. B. Reutte oder Lienz) bestätigt den Trend der Urbanisierung (Zuzug in Ballungsräume).

Stetigkeit des Trends (R2): Das Bestimmtheitsmaß R2 (im Code model.rsquared) zeigt, wie gleichmäßig die Entwicklung war.

Liegt R2 nahe bei 1 (z. B. > 0.9), verlief das Wachstum sehr konstant.

Ein niedrigeres R2 deutet auf Schwankungen hin (z. B. durch Wirtschaftskrisen, Pandemien oder touristische Einbrüche in bestimmten Jahren).

Regionale Unterschiede: Der grafische Vergleich der Bezirke zeigt deutlich, ob sich die Schere zwischen städtischen und ländlichen Regionen weiter öffnet (wenn die Geraden auseinanderlaufen) oder ob der Trend parallel verläuft
