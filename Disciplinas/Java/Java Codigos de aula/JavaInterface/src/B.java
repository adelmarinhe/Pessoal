
public class B extends A{
	
	private int z = 12;
	
	public void m() {
		System.out.println("B.m()");
	}

//	@Override
//	public String toString() {
//		return "B [z=" + z + ", x=" + x + ", y=" + y + "]";
//	}

	@Override
	public String toString() {
		return "B [z=" + z + ", toString()=" + super.toString() + "]";
	}
	
	public void h() {
		System.out.println("B.h()");
	}
	
	public void h2() {
		System.out.println("B.h2()");
	}
	
	

}
