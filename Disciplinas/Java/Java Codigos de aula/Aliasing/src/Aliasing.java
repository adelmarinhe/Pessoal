import java.util.ArrayList;

public class Aliasing {

	static int inc(int y) { // y = x;
		y += 1;
		return y;
	}
	
	
	static void manipulaSB(StringBuffer sb2) { //  sb2 = sb
//		sb2 = new StringBuffer();
		sb2.append("/Python");
		sb2 = null;
//		sb2.append("/Python");
	}
	
	public static void main(String[] args) {
//		StringBuffer sb = new StringBuffer("");
//		StringBuffer sb2 = sb;
//		
//		sb.append("Java");
//		sb2.append("/C#");
//		manipulaSB(sb);
//		System.out.println(sb);
//		
//		int x = 10;
//		x = inc(x);
//		System.out.println(x);
//		
		ArrayList<String> list1 = new ArrayList<>();
		ArrayList list2 = new ArrayList<>();
//		list1.add("Java");
//		list1.add("C#");
//		
//		System.out.println(list1);
		
		String s1 = new String("Java");
		String s2 = "Java";
		String s3 = "Java";
		
//		System.out.println(s1.intern() == s2);
//		System.out.println(s1.intern() == s3);
//		System.out.println(s2 == s3);
		
//		StringBuffer sb = new StringBuffer();
//		for (int i = 0; i < 99; i++) {
//			sb.append("--"+i);
//			s1 += "--"+i;
//			System.out.println(System.identityHashCode(sb));
////			System.out.println(s1);
//			
//		}
		
		int x = 10;
		Integer y = x;
		System.out.println(System.identityHashCode(y));
		y++;
		System.out.println(System.identityHashCode(y));
	
		
	}

}
