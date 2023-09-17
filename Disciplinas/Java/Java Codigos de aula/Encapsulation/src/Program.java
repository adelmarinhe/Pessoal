
public class Program {

	public static void main(String[] args) {
//		Person p = new Person("Henrique Rebelo", "123456", 37);
//		
//		System.out.println(p.getName());
//		System.out.println(p.getCpf());
//		System.out.println(p.getAge());
		
		Conta c1 = new Conta("123");
		Conta c2 = new Conta("124");
		
		c1.setChequeEspecial(true);
		
		c1.creditar(100);
		c2.creditar(200);
		
		System.out.println(c1.toString());
		System.out.println(c2);
		System.out.println();
		
		c1.debitar(3000);
		c1.creditar(-200);
		
		c2.debitar(300);
		
		c1.saldo = -4000;
		
		System.out.println(c1.toString());
		System.out.println(c2);

	}

}
