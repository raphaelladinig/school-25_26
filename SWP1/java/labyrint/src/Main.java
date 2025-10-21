import java.util.*;

public class Main {
    static class Patient {
        private final String name;
        private final int priority;
        private final long arrivalOrder;

        public Patient(String name, int priority, long arrivalOrder) {
            if (priority < 1 || priority > 5) {
                throw new IllegalArgumentException("Priorität muss zwischen 1 und 5 liegen.");
            }
            this.name = name;
            this.priority = priority;
            this.arrivalOrder = arrivalOrder;
        }

        public String getName() { return name; }
        public int getPriority() { return priority; }
        public long getArrivalOrder() { return arrivalOrder; }

        @Override
        public String toString() {
            return name + " (Prio " + priority + ", #" + arrivalOrder + ")";
        }
    }
    public static void main(String[] args) {
        Comparator<Patient> patientOrder = Comparator
                .comparingInt(Patient::getPriority)
                .thenComparingLong(Patient::getArrivalOrder);

        PriorityQueue<Patient> triageQueue = new PriorityQueue<>(patientOrder);

        long seq = 0;

        triageQueue.offer(new Patient("Anna",   3, seq++));
        triageQueue.offer(new Patient("Boris",  1, seq++));
        triageQueue.offer(new Patient("Cem",    5, seq++));
        triageQueue.offer(new Patient("Daria",  2, seq++));
        triageQueue.offer(new Patient("Elif",   1, seq++));
        triageQueue.offer(new Patient("Felix",  2, seq++));
        triageQueue.offer(new Patient("Gina",   3, seq++));

        System.out.println("Behandlungsreihenfolge:");
        while (!triageQueue.isEmpty()) {
            Patient next = triageQueue.poll();
            System.out.println("  -> " + next);
        }
    }
}