package generics.basics;

import java.util.*;

public class DataStructureWithGenericsTypeInference {

	public static void printIntegerList(List<Integer> list){
//		for (Object l : list) {
//			Integer i = (Integer)l;
//			System.out.println(i);
//		}
		for (Integer l : list) {
			System.out.println(l);
		}
	}

	public static void main(String[] args) {
		List<Integer> list = new ArrayList<>();
		list.add(new Integer(10));
		list.add(new Integer(20));
		printIntegerList(list);
//		list.add(new String("10"));
		printIntegerList(list);
	}

}
