package generics.basics;

import java.util.*;

public class DataStructureNoGenerics {

	// JDK 1.4
	public static void printIntegerList(List list){
		for (Object l : list) {
//			Integer i = (Integer)l;
//			System.out.println(i);
			
//			codigo de correcao
			if(l instanceof Integer) {
				Integer i = (Integer)l;
				System.out.println(i);
			}
			else if(l instanceof String){
				String s = (String)l;
				System.out.println(s);
			}
			else if(l instanceof Double) {
				Double d = (Double)l;
				System.out.println(d);
			}
			else if(l instanceof Float) {
				Float f = (Float)l;
				System.out.println(f);
			}
		}
	}

	public static void main(String[] args) {
		List list = new ArrayList();
		List list2 = new Vector();
		list.add(new Integer(10));
		list.add(new Integer(20));
		list.add(30); // autoboxing
		printIntegerList(list);
		
		list.add(new String("Java"));
		list.add(new String("C#"));
		System.out.println();
		printIntegerList(list);
		System.out.println();
////		
		list.add(new Double(20.5));
		printIntegerList(list);
		System.out.println();
////		
		list.add(new Float(10.5));
		printIntegerList(list);
//		
//		list.add(true);
	}
}
