// Class 1: Simulating a Network Module
class NetworkModule {
    public void connect() {
        Logger.getInstance().log("NetworkModule: Attempting connection...");
        // Simulate work
        Logger.getInstance().log("NetworkModule: Connection established.");
    }
}

// Class 2: Simulating User Input
class UserInput {
    public void inputData(String data) {
        Logger.getInstance().log("UserInput: Received data - " + data);
    }
}

public class Main {
    public static void main(String[] args) {
        // Instantiate the different components
        NetworkModule net = new NetworkModule();
        UserInput user = new UserInput();

        // Perform actions
        net.connect();
        user.inputData("Login_User_123");

        // Even if we call it directly here, it uses the exact same instance
        Logger.getInstance().log("Main: System shutdown sequence.");
    }
}