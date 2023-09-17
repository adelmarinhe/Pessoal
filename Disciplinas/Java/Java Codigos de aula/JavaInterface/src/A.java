
public class A {
	
	private int x = 20;
	private int y = 30;
	
	public void m() {
		System.out.println("A.m()");
	}

	@Override
	public String toString() {
		return "A [x=" + x + ", y=" + y + "]";
	}
	
}
