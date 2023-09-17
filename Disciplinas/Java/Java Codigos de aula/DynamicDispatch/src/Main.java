
public class Main {
	
	public static A factory() {
		return new C();
	}
	
	public static void manipulaHierarquia(A a) {
		a.m();
		if(a instanceof C) {
			((C)a).o();
		}
	}

	public static void main(String[] args) {
		A a = new A();
		B b = new B();
		C c = new C();
		System.out.println(c);
		a.m();
		b.m();
		c.m();
		System.out.println();
		
		A a2 = factory();
		
		manipulaHierarquia(new A());
//		manipulaHierarquia(new C());

	}

}
