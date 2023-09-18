
public class PoolObjects {

	public static void main(String[] args) {
		String s1 = "Java";
		String s2 = "Java";
		String s3 = "Java";
		
//		System.out.println(s1 == s3);
//		System.out.println(s2 == s3);
//		System.out.println(s1 == s2);
		
//		System.out.println(s1.intern() == s2.intern());
//		System.out.println(s1.equals(s2));
//		System.out.println("String@"+System.identityHashCode(s1));
//		System.out.println("String@"+System.identityHashCode(s2));
//		System.out.println("String@"+System.identityHashCode(s3));
		
		Integer i = new Integer(12);
		Integer j = 12;
		int j2 = j;
		
//		System.out.println("Integer@"+System.identityHashCode(i));
//		System.out.println("Integer@"+System.identityHashCode(j));
		
		j = j2;
		
//		System.out.println("Integer@"+System.identityHashCode(j));
		
		
		String ss = new String( "Java");
		String ss2 = "Java";
		String ss3 = "Java";
		
//		ss += " is the best"; // new String
//		ss2 += " is the best";// new String
//		
		System.out.println(ss.intern() == ss2.intern());
		System.out.println(ss == ss2);

	}

}
