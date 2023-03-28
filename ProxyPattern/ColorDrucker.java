public class ColorDrucker implements Drucker {
    public void print(String msg) {
        System.out.println("Nachricht " + msg + " wird in Farbe gedruckt!");
    }
}
