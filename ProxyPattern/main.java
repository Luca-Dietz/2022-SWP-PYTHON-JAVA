public class main {
    public static void main(String[] args) {
        Drucker d = new ProxyDrucker();
    
        d.print("Hilfe");
    
        ((ProxyDrucker) d).switchToColor();
        d.print("Hilfe aber in Farbe");
    
        ((ProxyDrucker) d).switchToBlackAndWhite();
        d.print("Hilfe");
    }
}
