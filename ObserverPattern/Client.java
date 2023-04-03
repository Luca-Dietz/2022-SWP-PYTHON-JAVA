public class Client {
    public static void main(String[] args) {
        Zentrale zentrale = new Zentrale();
        Observer observer1 = new Observer1();
        Observer observer2 = new Observer2();
        zentrale.addObserver(observer1);
        zentrale.addObserver(observer2);

        zentrale.setNewestData(new Wetterdaten(20.6, 30));
        zentrale.removeObserver(observer2);
        zentrale.setNewestData(new Wetterdaten(30, 40));
    }
}
