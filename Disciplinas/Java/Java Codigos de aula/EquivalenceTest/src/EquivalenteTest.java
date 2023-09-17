import java.util.ArrayList;
import java.util.Arrays;

public class EquivalenteTest {
	
	public static String replace(String s, char target, char replacement) {
		char sCharArray [] = s.toCharArray();

		for (int i = 0; i < sCharArray.length; i++) {
			if (sCharArray[i] == target) {
				sCharArray[i] = replacement;
			}
		}

		String sfinal = Arrays.toString(sCharArray);
		
//		System.out.println(sCharArray.toString());
		
		

//		for (int i = 0; i < sCharArray.length; i++) {
//			sfinal = sfinal + sCharArray[i];
//		}

		return sfinal;
	}
	
	public static boolean containsAll(ArrayList<String> list1, ArrayList<String> list2) {
		// list1.containsAll(list2)
		
		
		
		return false;
	}

	public static void main(String[] args) {
		System.out.println(EquivalenteTest.replace("Java", 'a', '*'));
		
		ArrayList<String> list1 = new ArrayList<>(); 
		ArrayList<String> list2 = new ArrayList<>();
		String result = EquivalenteTest.replace("Java", 'a', '*');
		
		String s = "Java";
		
		s = s.replace("b","*");
		
//		System.out.println(s);
		
		
		list1.add(s);
		list1.add("C");
		list1.add("Python");
		
		list2.add("C#");
		list2.add(s);
				
//		System.out.println(list1 == list2);
//		System.out.println(list1.equals(list2));
		
//		System.out.println(s.contains("av"));
//		System.out.println(list1.contains("Java"));
//		System.out.println(list2.contains(s));
//		
//		System.out.println(list1.containsAll(list2));

	}

}
