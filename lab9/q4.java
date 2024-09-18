import java.time.format.DateTimeFormatter;
import java.time.LocalDateTime;    
import java.util.Timer;
import java.util.TimerTask;

class PrintTime implements Runnable{
	public void run(){
		new Timer().schedule(new TimerTask(){
			public void run(){
				System.out.println(LocalDateTime.now().format(DateTimeFormatter.ofPattern("HH:mm:ss")));
			}
		}, 0, 1000);
	}
}

class q4{
	public static void main(String args[]){
		new Thread(new PrintTime()).start();
	}
}