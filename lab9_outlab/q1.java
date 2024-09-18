import java.io.IOException;
import java.io.File; 
import java.io.FileInputStream;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors; 
import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.pdmodel.PDPage;
import org.apache.pdfbox.pdmodel.PDPageContentStream;
import org.apache.pdfbox.pdmodel.font.PDType1Font;
import org.apache.pdfbox.text.PDFTextStripper;
import org.apache.poi.openxml4j.opc.OPCPackage;
import org.apache.poi.xwpf.usermodel.XWPFDocument;
import org.apache.poi.xwpf.extractor.XWPFWordExtractor;
import org.apache.poi.hwpf.HWPFDocument;
import org.apache.poi.hwpf.extractor.WordExtractor;

public class q1{
	public static void main(String args[]) {
		try {
			PDDocument document = new PDDocument();    
	    	
	    	// args[0] takes filename as input
	    	addText(document, processText(args[0]));

			document.save("./doc.pdf");
		    document.close();

		} catch(IOException e) {
			e.printStackTrace();
		}
	}

	public static void addText (PDDocument document, Map<String, Long> map) {
		int ENTRIES_PER_PAGE = 46, count = 0;
		try {
			PDPage page = new PDPage();
			PDPageContentStream contentStream = new PDPageContentStream(document, page);
			contentStream.beginText();
	    	contentStream.setFont(PDType1Font.TIMES_ROMAN, 16 );
	  		//Setting the leading
	    	contentStream.setLeading(14.5f);
	  		//Setting the position for the line
			contentStream.newLineAtOffset(25, 725);
			for (Map.Entry<String, Long> entry : map.entrySet()){
				contentStream.showText(entry.getKey() + "    " + entry.getValue());
	            contentStream.newLine();

	            // To have limited number of entries per page
	            if (++count % ENTRIES_PER_PAGE == 0){
	            	//Ending the content stream
			      	contentStream.endText();
			      	contentStream.close();
			    	document.addPage(page);

			    	page = new PDPage();
			    	contentStream = new PDPageContentStream(document, page);
					contentStream.beginText();
			    	contentStream.setFont(PDType1Font.TIMES_ROMAN, 16 );
			  		//Setting the leading
			    	contentStream.setLeading(14.5f);
			  		//Setting the position for the line
					contentStream.newLineAtOffset(25, 725);
	            }
			}
			//Ending the content stream
	      	contentStream.endText();
	      	contentStream.close();
			if (count % ENTRIES_PER_PAGE != 0){
		    	document.addPage(page);
			}
	    } catch(IOException e) {
	    	e.printStackTrace();
	    } 
	}

	public static Map<String, Long> processText (String file) {
		String input = readFile(file); 
		List<String> list = new ArrayList<>(Arrays.asList(input.replaceAll("[^a-zA-Z0-9\\s+]", "").split("\\s+")));
		
		String[] stopWords = {"and", "the", "is", "in", "at", "of", "his", "her", "him"};
		list.removeAll(Arrays.asList(stopWords));

		Map<String, Long> counted = list.stream()
										.collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));
		Map<String, Long> sortedByCount = counted.entrySet()
                						.stream()
                						.sorted((Map.Entry.<String, Long>comparingByValue().reversed()))
                						.collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue, (e1, e2) -> e1, LinkedHashMap::new));
		return sortedByCount;
	}

	public static String readFile(String file){
		String result = "";
		
		try{
			String extension = file.substring(file.lastIndexOf(".") + 1);
			if (extension.equals("txt")){
				
				result = new String(Files.readAllBytes(Paths.get(file)));

			} else if (extension.equals("docx")) {
				
				FileInputStream fis = new FileInputStream(file);
				XWPFDocument xdoc = new XWPFDocument(OPCPackage.open(fis));
				XWPFWordExtractor extractor = new XWPFWordExtractor(xdoc);
				result = extractor.getText();
				fis.close();

			} else if (extension.equals("doc")) {
				
				FileInputStream fis = new FileInputStream(file);
	            HWPFDocument doc = new HWPFDocument(fis);
	            WordExtractor extractor = new WordExtractor(doc);
	            result = extractor.getText();
	            fis.close();

			} else if (extension.equals("pdf")) {
				
				PDDocument doc = PDDocument.load(new File(file));
				result = new PDFTextStripper().getText(doc);
				doc.close();

			}
		} catch (Exception e) {
			e.printStackTrace();
		}

		return result;
	}

}