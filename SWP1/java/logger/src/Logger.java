import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class Logger {
    // 1. Static variable to hold the single instance
    private static Logger instance;

    // 2. Private constructor: No one else can instantiate this class
    private Logger() {
        // Optional: Log that the logger has been started
        System.out.println("--- System Logger Initialized ---");
    }

    // 3. Public static method to get the instance
    public static Logger getInstance() {
        if (instance == null) {
            instance = new Logger();
        }
        return instance;
    }

    // 4. The log method with timestamp
    public void log(String msg) {
        // Create a timestamp
        String timestamp = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));

        // Print to console
        System.out.println("[" + timestamp + "] LOG: " + msg);
    }
}
