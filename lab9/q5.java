import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors; 

public class q5{
	public static void main(String[] args){
		String input = readFile(args[0]); 
		List<String> list = new ArrayList<>(Arrays.asList(input.replaceAll("[^a-zA-Z0-9\\s+]", "").split("\\s+")));
		
		String[] stopWords = {"and", "the", "is", "in", "at", "of", "his", "her", "him"};
		list.removeAll(Arrays.asList(stopWords));

		Map<String, Long> counted = list.stream()
										.collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));
		Map<String, Long> sortedByCount = counted.entrySet()
                						.stream()
                						.sorted((Map.Entry.<String, Long>comparingByValue().reversed()))
                						.collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue, (e1, e2) -> e1, LinkedHashMap::new));
		sortedByCount.forEach((word, count) -> {
            System.out.println(word + "\t" + count);
        });
	}

	public static String readFile(String file){
		try{
			return new String(Files.readAllBytes(Paths.get(file)));
		} catch(Exception e){
			e.printStackTrace();
		}
		return "";
	}
}