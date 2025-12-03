public class Main {
    public static void main(String[] args) {
        // Create the game objects
        Gegner enemy = new Gegner();
        Muenze coin = new Muenze();

        // Simulate game events
        enemy.besiege();      // Should add 50 points
        coin.einsammeln();    // Should add 10 points
        enemy.besiege();      // Should add another 50 points

        System.out.println("--------------------------");

        // Output the final score
        // We can access the score from anywhere using getInstance()
        int finalScore = HighscoreManager.getInstance().getScore();
        System.out.println("Final Score: " + finalScore);

        // Verification: Even if we try to call getInstance again, it is the SAME object
        // So the score is preserved.
    }
}