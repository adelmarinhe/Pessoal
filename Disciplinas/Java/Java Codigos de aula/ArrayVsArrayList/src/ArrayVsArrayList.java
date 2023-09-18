import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;

public class ArrayVsArrayList {
	
	public static void ArrayCriteria() {
		// size: Fixed
		// data type: Primitive
		// generics: No
		int [] myIntArray = new int [10]; // fixed size of 10 during declaration!
		int [] myIntArray2 = {1,2,3,4,5,6,7,8,9,10}; // initialized but still has fixed size of 10 
		// during declaration with initialization

		// size: Fixed
		// data type: Object
		// generics: No
		String [] names = new String[10];

		// iteration: for loop
		System.out.print("[");
		for (int i = 0; i < myIntArray2.length; i++) {
			if(i != 0) {
				System.out.print(",");
			}
			System.out.print(myIntArray2[i]);
		}
		System.out.println("]");
		
		// iteration: for each
		int index = 0;
		System.out.print("[");
		for (String name : names) {
			if(index != 0) {
				System.out.print(",");
			}
			System.out.print(name);
			index++;
		}
		System.out.println("]");

		// Get size: through field .length
		System.out.println("myIntArray size = "+myIntArray.length);
		System.out.println("names size = "+names.length);

		// Add element: Operator =
		names[5] = "Henrique Rebelo";
		System.out.println(Arrays.toString(names));

		// Multidimensional: Yes
		int [][] points = new int [2][6];
		int [][] points2 = {
				{0,0}, {1,1}, {2,2},
				{3,3}, {4,4}, {5,5},
		};
		for (int[] a : points2) { 
			for (int i : a) { 
				System.out.print(i + "\t"); 
			} 
			System.out.println("\n"); 
		}


		System.out.println(Arrays.deepToString(points2));

		String[][] names2 = { {"John", "Smith"}, {"Javin", "Paul"}, {"James", "Gosling"}, };
		System.out.println(Arrays.deepToString(names2));
//		JOptionPane.showMessageDialog(null, "myArray contains:" + names);
	}

	public static void ArrayListCriteria() {
		// size: Flexible
		// data type: Only Object
		// generics: Yes
		ArrayList<String> myStringList = new ArrayList<>(); // it grows dynamically! no fixed size!
		ArrayList<Integer> myIntegerList = new ArrayList<>(); // it grows dynamically! no fixed size!

		// size: Flexible
		// data type: Only Object
		// generics: Yes [but without generics below...]
		ArrayList myHeterogeneousList = new ArrayList();

		// Get size: through method size()
		System.out.println("******************** Sizes********************");
		System.out.println("myStringList size = "+myStringList.size());
		System.out.println("myHeterogeneousList size = "+myHeterogeneousList.size());

		// Add element: method add()
		System.out.println();
		System.out.println("---> adding elements: method add()");
		System.out.println();
		myStringList.add("P2");
		myStringList.add("P3");
		myHeterogeneousList.add("IP");
		myHeterogeneousList.add("Compiladores");
		myHeterogeneousList.add("Semicondutores");
//		myStringList.add(100);

		System.out.println("******************** Sizes********************");
		System.out.println("myStringList size = "+myStringList.size());
		System.out.println("myHeterogeneousList size = "+myHeterogeneousList.size());

		// iteration: Iterator, for loop, and foreach
		System.out.println("******************** Iterator********************");
		for (Iterator<String> iterator = myStringList.iterator(); iterator.hasNext();) {
			String element =  iterator.next();
			System.out.println("element = "+element);
		}
		System.out.println("******************** for loop********************");
		for (int i = 0; i < myStringList.size(); i++) {
			String element = myStringList.get(i);
			System.out.println("element = "+element);
		}
		System.out.println("******************** for each********************");
		for (String element : myStringList) {
			System.out.println("element = "+element);
		}
		System.out.println();
		System.out.println("*************************************************");
		System.out.println("****************without generics****************");
		System.out.println("************************************************");
		System.out.println();
		// iteration without generic type
		System.out.println("******************** Iterator********************");
		for (Iterator iterator = myHeterogeneousList.iterator(); iterator.hasNext();) {
			String element =  (String) iterator.next();
			System.out.println("element = "+element);
		}
		System.out.println("******************** for loop********************");
		for (int i = 0; i < myHeterogeneousList.size(); i++) {
			String element = (String) myHeterogeneousList.get(i);
			System.out.println("element = "+element);
		}
		System.out.println("******************** for each********************");
		for (Object element : myHeterogeneousList) {
			System.out.println("element = "+(String)element);
		}

		// Multidimensional: No!
		
		System.out.println("-->"+ myStringList.toString());
		System.out.println("-->"+ myIntegerList.toString());
		System.out.println("-->"+ myHeterogeneousList.toString());
	}

	public static void main(String[] args) {
		// Array criteria
		ArrayVsArrayList.ArrayCriteria();
		
		// ArrayList criteria
		ArrayVsArrayList.ArrayListCriteria();
	}
}
