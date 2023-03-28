class SWDrucker implements Drucker {
    public void print(String msg) {
        System.out.println("Nachricht " + msg + " wird in SchwarzWeiß gedruckt!");
    }
}