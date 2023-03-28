public class ProxyDrucker implements Drucker{
    private Drucker drucker;

    public ProxyDrucker() {
        drucker = new SWDrucker();
    }

    public void switchToColor() {
        drucker = new ColorDrucker();
    }

    public void switchToBlackAndWhite() {
        drucker = new SWDrucker();
    }

    public void print(String msg) {
        drucker.print(msg);
    }
}
