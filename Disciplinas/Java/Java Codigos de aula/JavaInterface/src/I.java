
public interface I extends SuperI{
	
	int x = 10;
	
	public void p();
	
	default public void h() {
		System.out.println("I.h()");
	}
	

}
