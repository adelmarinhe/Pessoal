
public class Person {
	
	private String name;
	private String cpf;
	private int age;
	
	public Person(String name, String cpf, int age) {
		this.name = name;
		this.setCpf(cpf);
		this.setAge(age);
	}

	public String getName() {
		return name;
	}
	
	public void setName(String name) {
		this.name = name;
	}
	
	public int getAge() {
		return age;
	}
	
	private void setCpf(String cpf) {
		this.cpf = Integer.parseInt(cpf) + "";
	}

	public void setAge(int age) {
		if(age >= 0 && age <= 150) {
			this.age = age;
		}
	}
	
	public String getCpf() {
		return cpf;
	}
}
