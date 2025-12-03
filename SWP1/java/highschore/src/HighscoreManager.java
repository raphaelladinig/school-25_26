public class HighscoreManager {

    // 1. Static variable to hold the single instance of the class
    private static HighscoreManager instance;

    // Variable to manage the score state
    private int score;

    // 2. Private constructor: This prevents other classes from using 'new HighscoreManager()'
    private HighscoreManager() {
        this.score = 0;
        System.out.println("HighscoreManager initialized.");
    }

    // 3. Public static method to access the single instance
    public static HighscoreManager getInstance() {
        if (instance == null) {
            // If the instance doesn't exist yet, create it.
            instance = new HighscoreManager();
        }
        // Return the existing instance
        return instance;
    }

    // 4. Method to add points
    public void addPoints(int p) {
        this.score += p;
        System.out.println(p + " points added. Current Score: " + this.score);
    }

    // 5. Method to read the score
    public int getScore() {
        return this.score;
    }
}