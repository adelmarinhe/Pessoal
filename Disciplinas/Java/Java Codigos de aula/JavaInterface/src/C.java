
public class C extends B implements I, I2{

	private int w = 10;

	public void m() {
		System.out.println("C.m()");
	}

	public void o() {
		System.out.println("C.o()");
	}

	//	@Override
	//	public String toString() {
	//		return "C [w=" + w + ", z=" + z + ", x=" + x + ", y=" + y + "]";
	//	}

	@Override
	public String toString() {
		return "C [w=" + w + ", toString()=" + super.toString() + "]";
	}

	@Override
	public void p() {
		System.out.println("C.p()");
	}

	@Override
	public void q() {
		System.out.println("C.q()");
	}
	
//	public void h() {
//		I2.super.h();
//	}

}
