public class Muenze {
    public void einsammeln() {
        System.out.println("Coin collected!");
        // Access the global HighscoreManager and add points
        HighscoreManager.getInstance().addPoints(10);
    }
}