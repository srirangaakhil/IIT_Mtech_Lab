import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.*;
import javax.swing.*; 
import java.io.File;
import java.nio.file.Files; 
import java.nio.file.Paths; 
import java.util.Arrays; 
import java.util.ArrayList; 
import java.util.LinkedHashMap; 
import java.util.List; 
import java.util.Map; 
import java.util.function.Function; 
import java.util.stream.Collectors; 
import java.util.Iterator;
  
public class q4{ 
static String path;
  
public static void main(String[] args) 
{ 
    JFrame frame = new JFrame("q4");  
    JButton sf = new JButton("Select File"); 
    JButton process = new JButton("process");
    JTextArea csv = new JTextArea();
    
  
    JPanel panel = new JPanel(new GridLayout(3, 2, 10, 10)); 
	
	sf.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent ae) {
        JFileChooser fileChooser = new JFileChooser();
        int returnValue = fileChooser.showOpenDialog(null);
        if (returnValue == JFileChooser.APPROVE_OPTION) {
          File selectedFile = fileChooser.getSelectedFile();
	path=selectedFile.getAbsolutePath();
	//System.out.println(path);
	//System.out.println(selectedFile.getName());
        }
      }
    });
	
        process.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String contents = csv.getText();
                //System.out.println("contents = " + contents);
		String[] values = contents.split(",");
		for (int i = 0; i < values.length; i++)
    		values[i] = values[i].trim();
		//System.out.println(Arrays.toString(values));
		tokenize(path,values);
            }
        });
  
    panel.add(sf);  
    panel.add(process);  
    panel.add(csv); 
  
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); 
    frame.setSize(600, 400); 
    frame.getContentPane().add(panel); 
    frame.setVisible(true); 
} 

 public static void tokenize(String path,String[] values){ 		
	String input = readFile(path);		
	List<String> list = new ArrayList<>(Arrays.asList(input.replaceAll("[^a-zA-Z0-9\\s+]", "").split("\\s+"))); 				
	String[] stopWords = values; 		
	list.removeAll(Arrays.asList(stopWords)); 		
	Map<String, Long> counted = list.stream().collect(Collectors.groupingBy(Function.identity(), Collectors.counting())); 		
	Map<String, Long> sortedByCount = counted.entrySet().stream().sorted((Map.Entry.<String, Long>comparingByValue().reversed())).collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue, (e1,e2) -> e1, LinkedHashMap::new));
	Object[] str = sortedByCount.keySet().toArray(); 
	Object[] val = sortedByCount.values().toArray();
	Object[][] c = new Object[str.length][2];
	for(int i = 0; i < str.length; i++){
	    c[i][0] = str[i];
	    c[i][1] = val[i];
	}
	JFrame f = new JFrame("q4"); 
	JPanel panel = new JPanel(new GridLayout(3, 2, 10, 10));    
    String column[]={"Words","Frequency"};         
    
	f = new JFrame(); 
	JTable j; 
        f.setTitle("JTable Example"); 

   
        String[] columnNames = { "Words", "Frequency"}; 
  
        j = new JTable(c, columnNames); 
        j.setBounds(30, 40, 200, 300); 
  
        JScrollPane sp = new JScrollPane(j); 
        f.add(sp); 
        f.setSize(500, 200); 
        f.setVisible(true); 
      
}
	
	
public static String readFile(String file){ 		
	try{ 			
	return new String(Files.readAllBytes(Paths.get(file))); 		
	} catch(Exception e){ 			
	e.printStackTrace(); 		} 		
	return ""; 	
}
} 