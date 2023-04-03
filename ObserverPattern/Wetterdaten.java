public class Wetterdaten {
    private final double temperature;
    private final double humidity;

    public Wetterdaten(double temperature, double humidity) {
        this.temperature = temperature;
        this.humidity = humidity;
    }

    public double getTemperature() {
        return temperature;
    }

    public double getHumidity() {
        return humidity;
    }

}
