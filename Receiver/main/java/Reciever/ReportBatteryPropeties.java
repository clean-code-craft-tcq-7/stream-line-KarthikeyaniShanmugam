package Reciever;

public class ReportBatteryPropeties implements PrintProperty {

	public void printReport(BatteryProperties battery) {

		System.out.println("Maximum Temperature: " + battery.getMaxChargeRate());
		System.out.println("Minimum Temperature: " + battery.getMinChargeRate());
		System.out.println("Average Temperature: " + battery.getAverageChargeRate());
		System.out.println("Maximum state of charge: " + battery.getMaxSoc());
		System.out.println("Minimum state of charge: " + battery.getMinSoc());
		System.out.println("Average state of charge: " + battery.getAverageSoc());
	}
}