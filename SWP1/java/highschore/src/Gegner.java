public class Gegner {
    public void besiege() {
        System.out.println("Enemy defeated!");
        // Access the global HighscoreManager and add points
        HighscoreManager.getInstance().addPoints(50);
    }
}