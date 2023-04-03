public class Observer2 implements Observer {

    @Override
    public void getInformation(Wetterdaten wetterdaten) {
        System.out.println("Observer1 bekommt folgende Daten zugesendet: " + wetterdaten.getTemperature() + "°C / "
                + wetterdaten.getHumidity() + "%");
    }

}
