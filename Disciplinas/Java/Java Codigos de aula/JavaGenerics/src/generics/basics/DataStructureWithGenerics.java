package generics.basics;

import java.util.*;

public class DataStructureWithGenerics {

	public static void printIntegerList(List<Integer> list){
		for (Integer l : list) {
			System.out.println(l);
		}
	}
	
	public static void printStringList(List<String> list){
		for (String l : list) {
			System.out.println(l);
		}
	}

	public static void main(String[] args) {
		List<Integer> list = new ArrayList<Integer>();
		list.add(10);
		list.add(20);
		list.add(new Integer("30"));
		printIntegerList(list);
		
		List<String> list2 = new ArrayList<String>();
		list2.add(new String("P2"));
		list2.add(new String("Java"));
		list2.add(new String("Android"));
		printStringList(list2);		
	}
}
