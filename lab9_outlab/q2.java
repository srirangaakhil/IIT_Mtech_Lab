import java.util.Arrays;
import java.util.concurrent.TimeUnit;
import java.util.stream.IntStream;
import java.util.Random;

public class q2 {
	
	private static final int ARR_LENGTH = 30000;

	public static void main(String args[]) {
		int x[] = createRandomIntArray();
		int y[] = createRandomIntArray();

		executeUsingThreads(x, y);

		executeSerially(x, y);
	}

	public static void executeUsingThreads(int[] x, int[] y){
		Add add = new Add(x, y);
		Multiply multiply = new Multiply(x, y);

		Thread adder = new Thread(add);
		Thread multiplier = new Thread(multiply);
		

		long startTime = System.nanoTime();
		adder.start();
		multiplier.start();
		// Wait for threads to complete execution
		try {
			adder.join();
			multiplier.join();
		} catch(Exception e) {
			e.printStackTrace();
		}

		long endTime = System.nanoTime();
		long timeElapsed = endTime - startTime;
		
		System.out.println("Execution time using Threads:\t" + timeElapsed / 1000000.0 + " ms");
	}

	public static void executeSerially(int[] x, int[] y){
		int[] result1 = new int[ARR_LENGTH];
		int[] result2 = new int[ARR_LENGTH];
		
		long startTime = System.nanoTime();
		
		for(int i = 0; i < ARR_LENGTH; i++){
			result1[i] = x[i] + y[i];
		}
		
		for(int i = 0; i < ARR_LENGTH; i++){
			result2[i] = x[i] * y[i];
		}

		long endTime = System.nanoTime();
		long timeElapsed = endTime - startTime;

		System.out.println("Execution time without Threads:\t" + timeElapsed / 1000000.0 + " ms");
	}

	// Generate arrays of ARR_LENGTH with random integers in [0, 100]
	public static int[] createRandomIntArray() {
		Random rand = new Random();
		return IntStream.range(0, ARR_LENGTH).map(i -> rand.nextInt(101)).toArray();
	}
}

class Add implements Runnable {
	private int x[], y[], result[];

	public Add (int x[], int y[]){
		this.x = x;
		this.y = y;
		this.result = new int[x.length];
	}

	public void run() {
		for (int i = 0; i < x.length; i++)
			result[i] = x[i] + y[i];
	}

	public int[] getResult() {
		return result;
	}
}

class Multiply implements Runnable {
	private int x[], y[], result[];

	public Multiply (int x[], int y[]) {
		this.x = x;
		this.y = y;
		this.result = new int[x.length];
	}

	public void run() {
		for (int i = 0; i < x.length; i++) 
			result[i] = x[i] * y[i];
	}

	public int[] getResult() {
		return result;
	}
}

/*
For ARRAY_LENGTH = 1000 or 1K
Unthreaded implementation is always faster.
example:
Execution time using Threads:	0.120143 ms
Execution time without Threads:	0.045236 ms

For ARRAY_LENGTH = 2000 or 2K
Ocassionally threaded implementation is faster. But most of the times unthreaded implementations is still faster.
example 1:
Execution time using Threads:	0.070445 ms
Execution time without Threads:	0.083763 ms
example 2:
Execution time using Threads:	0.091853 ms
Execution time without Threads:	0.072859 ms

For ARRAY_LENGTH = 20000 or 20K
Both perform similarly most of the time. They both beat each other in different runs but unthreaded implementation 
still performs better. 
example:
Execution time using Threads:	0.809525 ms
Execution time without Threads:	0.778273 ms

For ARRAY_LENGTH = 30000 or 30K
Threaded implementations is (almost) 	always faster.
example:
Execution time using Threads:	0.897238 ms
Execution time without Threads:	1.015335 ms

Observation:
For larger values of ARRAY_LENGTH the threaded implementation is faster. But when ARRAY_LENGTH is small, the 
unthreaded or serial implementation performs better (in terms of time). This is because for small arrays the 
overheads are more than the performance gained, therefore unthreaded implementations perform better.

On viewing the bytecode, "javap -v <class-name>.class" one can see that there is no compile time optimization 
in "executeSerially" function which merges the two "for" loops.

But one can easily find out that JIT compiler performs some run time optimizations. A comprehensive list of JIT 
optimizations can be found here for IBM SDK
(https://www.ibm.com/support/knowledgecenter/en/SSYKE2_8.0.0/com.ibm.java.vm.80.doc/docs/jit_optimize.html).
More can be found here 
(https://www.beyondjava.net/a-close-look-at-javas-jit-dont-waste-your-time-on-local-optimizations).

Once loops optimizations they are no longer executed one after the other. But these loops are rather merged and 
unrolled. When ARRAY_LENGTH is large, the threads beat the unthreaded implementation, this is beacuse these these 
threads can execute concurrently and the benfits of concurreny outweigh the overheads of thread management.
*/