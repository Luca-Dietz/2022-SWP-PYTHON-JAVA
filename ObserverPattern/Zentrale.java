public class Zentrale extends Wetterstation {
    private Wetterdaten newestData;

    public void setNewestData(Wetterdaten wetterdaten) {
        this.newestData = wetterdaten;
        distributeInformation(newestData);
    }

    public Wetterdaten getNewestData() {
        return newestData;
    }
}