import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.Reader;
import java.net.HttpURLConnection;
import java.net.URL; 
import java.net.URLEncoder;
import java.util.Scanner;

public class q3 {
	public static void main(String args[]) {
		Scanner inp = new Scanner(System.in);
		String input = inp.nextLine();
		String getURL = "https://www.cse.iitb.ac.in/~diptesh/get_hash.php?input=" + input;
		String postURL = "https://www.cse.iitb.ac.in/~diptesh/post_hash.php";
		try {
			//// GET
			URL url = new URL(getURL);
     		HttpURLConnection con = (HttpURLConnection) url.openConnection();
     		// optional default is GET
     		con.setRequestMethod("GET");
     		//add request header
     		con.setRequestProperty("User-Agent", "Mozilla/5.0");
     		int responseCode = con.getResponseCode();
     		BufferedReader in = new BufferedReader(
        		new InputStreamReader(con.getInputStream()));
     		String inputLine;
     		StringBuffer response = new StringBuffer();
     		while ((inputLine = in.readLine()) != null) {
        		response.append(inputLine);
     		}
     		in.close();
     		//print in String
     		System.out.println(response.toString());



     		//// POST
     		url = new URL(postURL);
     		StringBuilder postData = new StringBuilder();
     		postData.append(URLEncoder.encode("input", "UTF-8"));
     		postData.append('=');
     		postData.append(URLEncoder.encode(input, "UTF-8"));
     		byte[] postDataBytes = postData.toString().getBytes("UTF-8");
     		HttpURLConnection conn = (HttpURLConnection)url.openConnection();
	    	conn.setRequestMethod("POST");
	    	conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
	    	conn.setRequestProperty("Content-Length", String.valueOf(postDataBytes.length));
	    	conn.setDoOutput(true);
	    	conn.getOutputStream().write(postDataBytes);
	    	Reader inx = new BufferedReader(new InputStreamReader(conn.getInputStream(), "UTF-8"));
	    	StringBuilder sb = new StringBuilder();
	    	for (int c; (c = inx.read()) >= 0;)
	        	sb.append((char)c);
	    	String responsePost = sb.toString();
	    	System.out.println(responsePost);
		}
		catch(Exception e) {
			e.printStackTrace();
		}
		
	}
}