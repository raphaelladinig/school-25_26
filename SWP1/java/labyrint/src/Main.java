import java.util.HashMap;
import java.util.Map;

public class Main {

    public static void main(String[] args) {
        // 1. HashMap erstellen und 10 Schüler mit Note speichern (Schlüssel: Name, Wert: Note)
        HashMap<String, Double> schuelerNoten = new HashMap<>();

        // Beispiel-Daten (10 Schüler)
        schuelerNoten.put("Anna", 1.5);
        schuelerNoten.put("Bernd", 3.0);
        schuelerNoten.put("Clara", 2.0);
        schuelerNoten.put("David", 4.5);
        schuelerNoten.put("Emil", 1.0);
        schuelerNoten.put("Franziska", 2.5);
        schuelerNoten.put("Gustav", 5.0);
        schuelerNoten.put("Hanna", 1.0);
        schuelerNoten.put("Ines", 3.5);
        schuelerNoten.put("Jonas", 2.0);

        // 2. Alle Schüler mit Note < 3.0 ausgeben
        System.out.println("--- Schüler mit Note < 3.0 ---");
        for (Map.Entry<String, Double> eintrag : schuelerNoten.entrySet()) {
            if (eintrag.getValue() < 3.0) {
                System.out.println(eintrag.getKey() + ": " + eintrag.getValue());
            }
        }

        // 3. Durchschnittsnote berechnen
        double summeNoten = 0.0;
        for (double note : schuelerNoten.values()) {
            summeNoten += note;
        }

        double anzahlSchueler = schuelerNoten.size();
        double durchschnitt = 0.0;

        if (anzahlSchueler > 0) {
            durchschnitt = summeNoten / anzahlSchueler;
        }

        // 4. Durchschnitt ausgeben
        System.out.println("\n--- Durchschnittsnote ---");
        System.out.printf("Die Durchschnittsnote beträgt: %.2f%n", durchschnitt);
    }
}