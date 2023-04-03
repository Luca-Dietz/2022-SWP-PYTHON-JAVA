import java.util.ArrayList;
import java.util.List;

public abstract class Wetterstation {
    private List<Observer> observerList = new ArrayList<Observer>();

    public void addObserver(Observer observer) {
        observerList.add(observer);
    }

    public void removeObserver(Observer observer) {
        observerList.remove(observer);
    }

    protected void distributeInformation(Wetterdaten wetterdaten) {
        for (Observer observer : observerList) {
            observer.getInformation(wetterdaten);
        }
    }

}
