package generics.wildcards.extendsBoundary;

import java.util.ArrayList;
import java.util.List;

import util.*;

public class NoWildcardBoundary {

	public static void processElements(List<A> elements){
		for(A a : elements){
			System.out.println(a.getValue());
		}
	}

	public static void main(String[] args) {
		List<A> listA = new ArrayList<>();
		List<B> listB = new ArrayList<>();
		List<B2> listB2 = new ArrayList<>();
		List<C> listC = new ArrayList<>();
		List<String> listS = new ArrayList<>();

		//listA elements
		listA.add(new A(10));
		listA.add(new B(20));
		listA.add(new C(30));
		
		// listB elements
		listB.add(new B(20));
		listB.add(new B2(25));
		
		// listB2 elements
		listB2.add(new B2(26));
		listB2.add(new B2(28));
		
		// listC elements
		listC.add(new C(30));
		
		// listS elements
		listS.add("C#");
		listS.add("Java");
		listS.add("Android");

		// What if to print all kind of lists??
		processElements(listA);
//		processElements(listB);
//		processElements(listB2);
//		processElements(listC);
//		processElements(listS);
	}
}
