package br.ufpe.cin.motorola.banco.conta;

import br.ufpe.cin.motorola.banco.cliente.Cliente;
import br.ufpe.cin.motorola.banco.excecoes.SaldoInsuficienteException;

public class ContaImposto extends ContaAbstrata {
    public static final double TAXA = 0.10;
    public ContaImposto(String num, Cliente c) {
		super(num, c);
	}
	
	public ContaImposto(String num, double s, Cliente c) {
		super(num,s,c);
	}

	@Override
	public void debitar(double valor) throws SaldoInsuficienteException {
		double imposto = valor * TAXA;
		double valorDebitado = valor + imposto;
		if (valorDebitado <= getSaldo()) {
			setSaldo(getSaldo() - valorDebitado);
		} else {
			throw new SaldoInsuficienteException();
		}
	}

}