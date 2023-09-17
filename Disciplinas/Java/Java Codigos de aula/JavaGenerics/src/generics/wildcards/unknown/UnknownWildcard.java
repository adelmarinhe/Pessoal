package generics.wildcards.unknown;

import java.util.ArrayList;
import java.util.List;

import util.*;

public class UnknownWildcard {
	
	public void m(List<?> s) {}

//	List<?> means a list typed to an unknown type. 
//	This could be a List<A>, a List<B>, a List<String> etc.
	public static void processElements(List<?> elements){
		for(Object o : elements){
			if(o instanceof A) {
				System.out.println(((A)o).getValue());
			}
			else if (o instanceof String) {
				System.out.println(((String)o).toString());
			}
			else if (o instanceof Integer) {
				System.out.println(((Integer)o).toString());
			}
			else if (o instanceof Double) {
				System.out.println(((Double)o).toString());
			}
		}
	}

	public static void main(String[] args) {
		List<A> listA = new ArrayList<>();
		List<B> listB = new ArrayList<>();
		List<String> listS = new ArrayList<>();
		List<Integer> listInt = new ArrayList<>();
		List<Double> listDouble = new ArrayList<>();
		
		//listA elements
		listA.add(new A(10));
		listA.add(new B(20));
		listA.add(new C(30));
		// listB elements
		listB.add(new B(20));
		listB.add(new B2(25));
		// listS elements
		listS.add("p2");
		listS.add("Java");
		listS.add("Android");
		
		listInt.add(2000);
		listDouble.add(10.5);
		
		// What if to print all kind of lists??
		processElements(listA);
		System.out.println();
		processElements(listB);
		System.out.println();
		processElements(listS);		
		
		System.out.println();
		processElements(listInt);		
		
		System.out.println();
		processElements(listDouble);		
	}
}
