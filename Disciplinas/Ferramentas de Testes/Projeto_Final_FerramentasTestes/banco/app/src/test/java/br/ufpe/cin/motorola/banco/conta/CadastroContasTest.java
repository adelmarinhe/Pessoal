package br.ufpe.cin.motorola.banco.conta;

import br.ufpe.cin.motorola.banco.cliente.Cliente;
import br.ufpe.cin.motorola.banco.cliente.TipoCliente;
import br.ufpe.cin.motorola.banco.excecoes.ContaExistenteException;
import br.ufpe.cin.motorola.banco.excecoes.ContaInexistenteException;
import br.ufpe.cin.motorola.banco.excecoes.SaldoInsuficienteException;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class CadastroContasTest {

    CadastroContas cArray;
    ContaAbstrata conta;
    ContaAbstrata contaBonificada;
    ContaAbstrata contaImposto;
    Poupanca poupanca;
    CadastroContas cMaps;

    Cliente cliente;
    Cliente cliente2;
    Cliente cliente3;
    Cliente cliente4;

    @BeforeEach
    void setUp() {
        cArray = new CadastroContas(new RepositorioContasArray());
        cMaps = new CadastroContas(new RepositorioContasMap());
        cliente = new Cliente("000", "Comum", TipoCliente.CLASS);
        cliente2 = new Cliente("111", "Rico", TipoCliente.VIP);
        cliente3 = new Cliente("222", "Ray", TipoCliente.ESPECIAL);
        cliente4 = new Cliente("333", "Ze", TipoCliente.CLASS);
        conta = new Conta("999", cliente);
        conta.setSaldo(10000);
        contaBonificada = new ContaBonificada("111", cliente2);
        contaBonificada = new ContaBonificada("111", 2000.50, cliente2);
        contaImposto = new ContaImposto("222", cliente3);
        contaImposto = new ContaImposto("222", 5000.80, cliente3);
        poupanca = new Poupanca("333", cliente4);
        poupanca = new Poupanca("333", 3000.20, cliente4);
    }

    @Test
    void cadastrarArray() {
        try {
            cArray.cadastrar(conta);
            assertNotEquals(null, cArray.procurar(conta.getNumero()));
            cArray.cadastrar(contaBonificada);
            assertNotEquals(null, cArray.procurar(contaBonificada.getNumero()));
            cArray.cadastrar(contaImposto);
            assertNotEquals(null, cArray.procurar(contaImposto.getNumero()));

        } catch (ContaExistenteException e) {
            e.printStackTrace();
        } catch (ContaInexistenteException e) {
            e.printStackTrace();
        }
        Exception ex = assertThrows(ContaExistenteException.class, () -> {
            cArray.cadastrar(conta);
        });
        assertEquals("Conta ja existe!", ex.getMessage());
    }

    @Test
    void cadastrarMaps() throws ContaExistenteException, ContaInexistenteException {
        cMaps.cadastrar(conta);
        assertNotEquals(null, conta);
        cMaps.cadastrar(contaBonificada);
        assertNotEquals(null, contaBonificada);
        cMaps.cadastrar(contaImposto);
        assertNotEquals(null, contaImposto);
    }

    @Test
    void creditarArray() throws ContaInexistenteException, ContaExistenteException {
        cArray.cadastrar(conta);
        cArray.cadastrar(contaBonificada);
        cArray.cadastrar(contaImposto);

        double valorAtual = conta.getSaldo();
        double credit = 500.0;
        cArray.creditar(conta.getNumero(), credit);
        conta = cArray.procurar(conta.getNumero());
        assertEquals(valorAtual + credit, conta.getSaldo());

        valorAtual = contaImposto.getSaldo();
        credit = 50.0;
        cArray.creditar(contaImposto.getNumero(), credit);
        contaImposto = cArray.procurar(contaImposto.getNumero());
        assertEquals(valorAtual + credit, contaImposto.getSaldo());

        valorAtual = contaBonificada.getSaldo();
        credit = 250.0;
        cArray.creditar(contaBonificada.getNumero(), credit);
        contaBonificada = cArray.procurar(contaBonificada.getNumero());
        assertEquals(valorAtual + credit, contaBonificada.getSaldo());

    }

    @Test
    void debitarArray() throws ContaInexistenteException, ContaExistenteException, SaldoInsuficienteException {
        cArray.cadastrar(conta);
        cArray.cadastrar(contaBonificada);
        cArray.cadastrar(contaImposto);

        double valorAtual = conta.getSaldo();
        double deb = 50.0;
        cArray.debitar(conta.getNumero(), deb);
        conta = cArray.procurar(conta.getNumero());
        assertEquals(valorAtual - deb, conta.getSaldo());
        Exception ex = assertThrows(SaldoInsuficienteException.class, () -> {
            cArray.debitar(conta.getNumero(), 20000.0);
        });
        assertEquals("Saldo insuficiente!", ex.getMessage());

        valorAtual = contaImposto.getSaldo();
        deb = 100.0;
        cArray.debitar(contaImposto.getNumero(), deb);
        contaImposto = cArray.procurar(contaImposto.getNumero());
        assertEquals(valorAtual - (deb + deb * ContaImposto.TAXA), contaImposto.getSaldo());
        ex = assertThrows(SaldoInsuficienteException.class, () -> {
            cArray.debitar(contaImposto.getNumero(), 9000.0);
        });
        assertEquals("Saldo insuficiente!", ex.getMessage());

        valorAtual = contaBonificada.getSaldo();
        deb = 200.0;
        cArray.debitar(contaBonificada.getNumero(), deb);
        contaBonificada = cArray.procurar(contaBonificada.getNumero());
        assertEquals(valorAtual - deb, contaBonificada.getSaldo());
    }

    @Test
    void transferirArray() throws ContaExistenteException, SaldoInsuficienteException, ContaInexistenteException {
        cArray.cadastrar(conta);
        cArray.cadastrar(contaBonificada);
        cArray.cadastrar(contaImposto);

        double valorAtualConta = conta.getSaldo();
        double valorAtualImposto = contaImposto.getSaldo();
        double transferencia = 1000.0;
        cArray.transferir(conta.getNumero(), contaImposto.getNumero(), transferencia);
        conta = cArray.procurar(conta.getNumero());
        contaImposto = cArray.procurar(contaImposto.getNumero());
        assertEquals(valorAtualConta - transferencia, conta.getSaldo());
        assertEquals(valorAtualImposto + transferencia, contaImposto.getSaldo());

        valorAtualImposto = contaImposto.getSaldo();
        double valorAtualBonificada = contaBonificada.getSaldo();
        transferencia = 1000.0;
        cArray.transferir(contaImposto.getNumero(), contaBonificada.getNumero(), transferencia);
        contaImposto = cArray.procurar(contaImposto.getNumero());
        contaBonificada = cArray.procurar(contaBonificada.getNumero());
        assertEquals(valorAtualImposto - (transferencia + transferencia * ContaImposto.TAXA),
                contaImposto.getSaldo());
        assertEquals(valorAtualBonificada + transferencia,
                contaBonificada.getSaldo());

        valorAtualBonificada = contaBonificada.getSaldo();
        valorAtualConta = conta.getSaldo();
        transferencia = 1000.0;
        cArray.transferir(contaBonificada.getNumero(), conta.getNumero(), transferencia);
        contaBonificada = cArray.procurar(contaBonificada.getNumero());
        conta = cArray.procurar(conta.getNumero());
        assertEquals(valorAtualBonificada - transferencia, contaBonificada.getSaldo());
        assertEquals(valorAtualConta + transferencia, conta.getSaldo());
    }

    @Test
    void atualizarArray() throws ContaInexistenteException, ContaExistenteException {
        cArray.cadastrar(conta);
        cArray.cadastrar(contaBonificada);
        cArray.cadastrar(contaImposto);

        conta.setCliente(cliente2);
        cArray.atualizar(conta);
        conta = cArray.procurar(conta.getNumero());
        assertEquals(cliente2.getCpf(), conta.getCliente().getCpf());

        contaImposto.setCliente(cliente3);
        cArray.atualizar(contaImposto);
        contaImposto = cArray.procurar(contaImposto.getNumero());
        assertEquals(cliente3.getCpf(), contaImposto.getCliente().getCpf());

        contaBonificada.setCliente(cliente);
        cArray.atualizar(contaBonificada);
        contaBonificada = cArray.procurar(contaBonificada.getNumero());
        assertEquals(cliente.getCpf(), contaBonificada.getCliente().getCpf());

        Exception ex = assertThrows(ContaInexistenteException.class, () -> {
            cArray.atualizar(new Conta("333", cliente4));
        });
        assertEquals("Conta Inexistente!", ex.getMessage());
    }

    @Test
    void atualizarMaps() throws ContaExistenteException, ContaInexistenteException {
        cMaps.cadastrar(conta);
        cMaps.cadastrar(contaBonificada);
        cMaps.cadastrar(contaImposto);

        conta.setCliente(cliente2);
        assertEquals(cliente2.getCpf(), conta.getCliente().getCpf());

        contaImposto.setCliente(cliente4);
        assertEquals(cliente4.getCpf(), contaImposto.getCliente().getCpf());

        contaBonificada.setCliente(cliente);
        assertEquals(cliente.getCpf(), contaBonificada.getCliente().getCpf());

        Exception ex = assertThrows(ContaInexistenteException.class, () -> {
            cMaps.atualizar(new Conta("333", cliente4));
        });
        assertEquals("Conta Inexistente!", ex.getMessage());

    }

    @Test
    void procurarArray() throws ContaExistenteException, ContaInexistenteException {
        cArray.cadastrar(conta);
        cArray.cadastrar(contaBonificada);
        cArray.cadastrar(contaImposto);

        assertNotEquals(null, cArray.procurar(conta.getNumero()));
        assertNotEquals(null, cArray.procurar(contaImposto.getNumero()));
        assertNotEquals(null, cArray.procurar(contaBonificada.getNumero()));

        Exception ex = assertThrows(ContaInexistenteException.class, () -> {
            cArray.procurar("5555");
        });
        assertEquals("Conta Inexistente!", ex.getMessage());
    }

    @Test
    void procurarMaps() throws ContaExistenteException, ContaInexistenteException {
        cMaps.cadastrar(conta);
        cMaps.cadastrar(contaBonificada);
        cMaps.cadastrar(contaImposto);

        assertEquals("999", conta.getNumero());
        assertEquals("111", contaBonificada.getNumero());
        assertEquals("222", contaImposto.getNumero());

        Exception ex = assertThrows(ContaInexistenteException.class, () -> {
            cMaps.procurar("85887");
        });
        assertEquals("Conta Inexistente!", ex.getMessage());

            }

    @Test
    void removerArray() throws ContaExistenteException {
        cArray.cadastrar(conta);

        try {
            cArray.remover("999");
        } catch (ContaInexistenteException cie) {
            assert false;
        }

        Exception ex = assertThrows(ContaInexistenteException.class, () -> {
            cArray.remover("2222");
        });
        assertEquals("Conta Inexistente!", ex.getMessage());
    }

    @Test
    void removerMaps() throws ContaExistenteException, ContaInexistenteException {
        cMaps.cadastrar(conta);

        Exception ex = assertThrows(ContaInexistenteException.class, () -> {
            cMaps.procurar("2222");
        });
        assertEquals("Conta Inexistente!", ex.getMessage());

        ex = assertThrows(ContaInexistenteException.class, () -> {
            cMaps.remover("2222");
        });
        assertEquals("Conta Inexistente!", ex.getMessage());
    }

    @Test
    void renderJurosPoupanca() {
        double saldoAtual = poupanca.getSaldo();
        poupanca.renderJuros(0.05);
        assertTrue(saldoAtual < poupanca.getSaldo());
    }

    @Test
    void renderJurosBonificada() {
        double saldoAtual = contaBonificada.getSaldo();
        contaBonificada.creditar(1000);
        assertTrue(((ContaBonificada) contaBonificada).getBonus() > 0);
        ((ContaBonificada)contaBonificada).renderBonus();
        assertTrue(saldoAtual < poupanca.getSaldo());
    }
}