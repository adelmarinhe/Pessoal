package generics.wildcards.extendsBoundary;

import java.util.ArrayList;
import java.util.List;

import util.*;

public class ExtendsWildcardBoundary {

	//	List<? extends A> means a List of objects that are instances of the class A, 
	//	or subclasses of A (e.g. B and C).
	//	You can now call the processElements() method with either a List<A>, List<B> or List<C>. 
	public static void processElements(List<? extends A> elements){
		for(A a : elements){
			System.out.println(a.getValue());
		}
	}
	
	public static void processElementsString(List<String> elements){
		for(String s : elements){
			System.out.println(s);
		}
	}

	public static void main(String[] args) {
//		List<Object> listObj = new ArrayList<>();
//		List<I> listI = new ArrayList<>();
		List<A> listA = new ArrayList<>();
		List<B> listB = new ArrayList<>();
		List<B2> listB2 = new ArrayList<>();
		List<C> listC = new ArrayList<>();
		List<D> listD = new ArrayList<>();
		List<E> listE = new ArrayList<>();
		List<String> listS = new ArrayList<>();        
		
		//listI elements
//		listI.add(new A(10));
//		listI.add(new B(20));
//		listI.add(new C(30));

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
		listS.add("p2");
		listS.add("Java");
		listS.add("Android");

		//listD elements
		listD.add(new D(10));
		listD.add(new D(20));
		listD.add(new D(30));
		
		//listE elements
		listE.add(new E(10));
		listE.add(new E(20));
		listE.add(new E(30));

		// What if to print all kind of lists??
		processElements(listA);
		processElements(listB);
		processElements(listB2);
		processElements(listC);
		processElements(listD);
		processElements(listE);
		processElementsString(listS);
	}
}
