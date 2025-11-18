#set heading(numbering: "1.")
#set text(lang: "de")

#align(center + horizon)[
  #align(center)[
    #image("assets/logo.png", width: 80%)
  ]
  #v(1cm)
  #text(18pt)[
    *Laborbericht 3*
  ]
  #linebreak()
  #v(0.5em)
  #linebreak()
  *Autoren:* Steiner & Ladinig
  #linebreak()
  *Gruppe*: 1
  #linebreak()
  *Lehrer*: Wischounig Philipp
  #linebreak()
  *Durchführungsdatum*: 12.11.2025
]

#set page(numbering: "1")
#counter(page).update(1)

#outline()
#pagebreak()

= Sprungantwort

== Berechnung Zeitkonstanten $T_1$ und $T_2$

#align(center)[
  #image("assets/zeitkonstanten.png", width: 80%)
]

#figure(
  caption: [Sprungantwort Mess- & Rechenergebnisse],
)[
  #image("assets/sprungantwort.png")
]<sprungantwort>

In @sprungantwort ist die Sprungantwort anhand der berechneten Werte $T_1$ und $T_2$ zu sehen. Wir haben im Vergleich zur letzten Übung, uns für einen neuen Annäherungswert $K=12,2$ entschieden, weil wir diesen Wert als realistischer empfinden, da sich der Wert wahrscheinlich aufgrund von Änderung der Raumtemperatur ab ca. Minute 35 stark verändert und sich zuvor aber bereits eingependelt hat.

Außerdem mussten wir bei der Formel für die theoretische Sprungantwort: #box[$y(t)=K-K/(T_1-T_2)*[T_1*e^(-t/T_1)-T_2*e^(-t/T_2)]$] die Konstante t um 0,5 (aufgrund der Verzögerung am Anfang) verringern. Die Konstante K mussten wir nicht ändern da wir zuvor bereits mit diesem Wert gerechnet haben und nicht mit $K / 50$.

Aufgrund dessen ist unsere Sprungantwort aus den Messergebnissen genaugenommen keine Sprungantwort, da wir wie bereits erwähnt nicht bei 0 starten, sondern erst nach 30 Sekunden und unser K nicht das eigentliche K von $K / 50$ ist.

== Vergleich der Mess- & Rechenergebnisse

Es fällt auf, dass die Wendetangente wie erwartet für die beiden Graphen übereinstimmt und sich die theoretische Darstellung an K annähert. Gut gelungen und eigentlich auch so erwartet ist, dass die beiden Graphen, bis auf die starke Veränderung der Temperatur nach ca. 35 Minuten nahezu ident sind. Besonders in den ersten 10 Minuten liegen die Funktionen perfekt übereinander. Danach zeigt sich zunächst eine kurzfristige Verzögerung im Temperaturanstieg, gefolgt von einer leicht beschleunigten Erwärmung. Diese Abweichungen könnten durch äußere Störeinflüsse während der Messung verursacht worden sein.

= Zweipunktregelung

== Simulation in ANA

Die Regelstrecke wurde wie in @regelstrecke veranschaulicht in ANA aufgebaut.

#figure(
  caption: [Regelstrecke in ANA],
)[
  #image("assets/regelstrecke.png")
]<regelstrecke>

Es wurden zwei PT1 Glieder anstatt eines PT2 Glieds verwendet da ANA diese nicht unterstützt. In ANA kann man bei einem Zweipunktregler keinen Sprung zwischen 0 und 50 einstellen, deswegen wurde ein Addierer in Kombination mit einer Sprungantwort verwendet.

#pagebreak()

== Vergleich der Mess- & Simulationsergebnisse

In @ana sind die Messergebnisse von der vorherigen Einheit gegenüber den Simulationsergebnissen von ANA veranschaulicht.

#figure(
  caption: [Zweipunktregelung Mess- & Simulationsergebnisse],
)[
  #image("assets/ana.png")
]<ana>

Zu Beginn zeigen die gemessenen und die simulierten Werte eine hohe Übereinstimmung. Im weiteren Verlauf ist jedoch zu beobachten, dass der simulierte Abkühlvorgang deutlich rascher erfolgt, was zu einer mit jedem Zyklus zunehmenden Abweichung führt. Dies ist vermutlich darauf zurückzuführen, dass die Simulationsparameter aus einer Sprungantwort abgeleitet wurden, die zeitlich getrennt von der Zweipunktregelung erfasst wurde. Unterschiedliche Umgebungsbedingungen, wie etwa Raumtemperatur und Luftfeuchtigkeit, haben hierbei wahrscheinlich das Verhalten beeinflusst.

= Quellen

- Perplexity – wurde zur Rechtschreibüberprüfung verwendet
- Gemini – wurde zur Rechtschreibüberprüfung verwendet
