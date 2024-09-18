import java.util.Scanner;
import java.util.Random; 
import java.lang.Math;

public class q2 {
	
	public double mean(int arr[]) {
		int arrlen = arr.length;
		double sum = 0;
		for(int i = 0; i < arrlen; i++) {
        	sum = sum + arr[i];
        }
        return sum/arrlen; 
	} 

	public double standard_deviation(int arr[], double mean) {
		int arrlen = arr.length;
		double sum = 0;
		for(int i = 0; i < arrlen; i++) {
        	sum = sum + Math.pow((arr[i] - mean), 2);
        }
        return Math.sqrt(sum/arrlen); 
	}

    public static void main(String[] args) {
    	Scanner in = new Scanner(System.in);
    	int n = in.nextInt();
    	int i;
    	int arr[] = new int[n];
    	Random rand = new Random();
    	double mean = 0, sd = 0;
    	q2 obj = new q2();

        for(i = 0; i < n; i++) {
        	arr[i] = rand.nextInt();
        	//System.out.println(arr[i]);
        }

        mean = obj.mean(arr);
        sd = obj.standard_deviation(arr, mean);
        System.out.println(mean);
        System.out.println(sd);
    }
}
