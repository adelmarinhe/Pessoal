package br.ufpe.cin.motorola.banco.fachada;

import java.lang.reflect.Field;

import br.ufpe.cin.motorola.banco.cliente.Cliente;
import br.ufpe.cin.motorola.banco.cliente.RepositorioClientesMap;
import br.ufpe.cin.motorola.banco.cliente.TipoCliente;
import br.ufpe.cin.motorola.banco.conta.Conta;
import br.ufpe.cin.motorola.banco.conta.ContaAbstrata;
import br.ufpe.cin.motorola.banco.excecoes.ClienteInexistenteException;
import br.ufpe.cin.motorola.banco.excecoes.ContaExistenteException;
import br.ufpe.cin.motorola.banco.excecoes.ContaInexistenteException;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class FachadaTest {

    Fachada fachada;

    @BeforeEach
    void setUp() {
        fachada = Fachada.obterInstancia();
    }

    @AfterEach
    void tearDown() {
        try {
            Field instance = Fachada.class.getDeclaredField("instancia");
            instance.setAccessible(true);
            instance.set(null, null);
            fachada = null;
        } catch (NoSuchFieldException e) {
            e.printStackTrace();
        } catch (IllegalAccessException e) {
            e.printStackTrace();
        }
    }

    @Test
    void atualizar() {
        try {
            Cliente cliente = new Cliente("1111", "abc", TipoCliente.CLASS);
            fachada.cadastrar(cliente);
            Cliente cliente2 = fachada.procurarCliente("1111");
            assertEquals("abc", cliente2.getNome());
            cliente2.setNome("xyz");
            fachada.atualizar(cliente2);
            Cliente clienteNovo = fachada.procurarCliente("1111");
            assertEquals("xyz", clienteNovo.getNome());

        }catch(Exception e){
            System.out.println("Erro! " + e.getMessage());
            assert false;
        }
    }

    @Test
    void procurarCliente() {
        try {
            Cliente cliente = new Cliente("1111", "abc", TipoCliente.CLASS);
            fachada.cadastrar(cliente);
            Cliente cliente2 = fachada.procurarCliente("1111");
            assertEquals("1111", cliente2.getCpf());

        }catch(Exception e){
            System.out.println("Erro! " + e.getMessage());
            assert false;
        }
    }

    @Test
    void cadastrar() {
        try {
            Cliente cliente = new Cliente("1111", "abc", TipoCliente.CLASS);
            fachada.cadastrar(cliente);
            assert true;

        }catch(Exception e){
            System.out.println("Erro! " + e.getMessage());
            assert false;
        }

    }

    @Test
    void descadastrarCliente() {
        try {
            Cliente cliente = new Cliente("1111", "abc", TipoCliente.CLASS);
            fachada.cadastrar(cliente);
            Cliente cliente2 = fachada.procurarCliente("1111");
            assertEquals("abc", cliente2.getNome());
            fachada.descadastrarCliente("1111");
            assertThrows(ClienteInexistenteException.class,()->{
                fachada.procurarCliente("1111");
            });


        }catch(Exception e){
            System.out.println("Erro! " + e.getMessage());
            assert false;
        }
    }

    @Test
    void testAtualizar() {
        try {
            Cliente cliente = new Cliente("1111", "abc",TipoCliente.CLASS);
            fachada.cadastrar(cliente);
            Conta conta = new Conta("0000",cliente);
            fachada.cadastrar(conta);
            ContaAbstrata conta2 = fachada.procurarConta("0000");
            assertEquals("abc", conta2.getCliente().getNome());
            conta2.getCliente().setNome("abc e d");
            fachada.atualizar(conta2);
            ContaAbstrata contaNova = fachada.procurarConta("0000");
            assertEquals("abc e d", contaNova.getCliente().getNome());



        }catch(Exception e){
            System.out.println("Erro! " + e.getMessage());
            assert false;
        }
    }

    @Test
    void procurarConta() {
        try {
            Cliente cliente = new Cliente("1111", "abc",TipoCliente.CLASS);
            fachada.cadastrar(cliente);
            Conta conta = new Conta("0000",cliente);
            fachada.cadastrar(conta);
            ContaAbstrata conta2 = fachada.procurarConta("0000");
            assertEquals("abc", conta2.getCliente().getNome());

        }catch(Exception e){
            System.out.println("Erro! " + e.getMessage());
            assert false;
        }
    }

    @Test
    void testCadastrar() {
        try {
            Cliente cliente = new Cliente("1111", "abc",TipoCliente.CLASS);
            fachada.cadastrar(cliente);
            Conta conta = new Conta("0000",cliente);
            fachada.cadastrar(conta);
            ContaAbstrata conta2 = fachada.procurarConta("0000");
            assertEquals("abc", conta2.getCliente().getNome());


        }catch(Exception e){
            System.out.println("Erro! " + e.getMessage());
            assert false;
        }
    }

    @Test
    void descadastrarConta() {
        try {
            Cliente cliente = new Cliente("1111", "abc",TipoCliente.CLASS);
            fachada.cadastrar(cliente);
            Conta conta = new Conta("0000",cliente);
            fachada.cadastrar(conta);
            ContaAbstrata conta2 = fachada.procurarConta("0000");
            assertEquals("abc", conta2.getCliente().getNome());
            fachada.descadastrarConta("0000");
            assertThrows(ContaInexistenteException.class,() ->{
                fachada.procurarConta("0000");
            });



        }catch(Exception e){
            System.out.println("Erro! " + e.getMessage());
            assert false;
        }
    }

    @Test
    void creditar() {
        try {
            Cliente cliente = new Cliente("1111", "abc",TipoCliente.CLASS);
            fachada.cadastrar(cliente);
            Conta conta = new Conta("0000",cliente);
            fachada.cadastrar(conta);
            ContaAbstrata conta2 = fachada.procurarConta("0000");
            assertEquals(0, conta2.getSaldo());
            fachada.creditar("0000", 5000);
            ContaAbstrata contaNova = fachada.procurarConta("0000");
            assertEquals(5000, contaNova.getSaldo());


        }catch(Exception e){
            System.out.println("Erro! " + e.getMessage());
            assert false;
        }
    }

    @Test
    void debitar() {
        try {
            Cliente cliente = new Cliente("1111", "abc",TipoCliente.CLASS);
            fachada.cadastrar(cliente);
            Conta conta = new Conta("0000",2000,cliente);
            fachada.cadastrar(conta);
            ContaAbstrata conta2 = fachada.procurarConta("0000");
            assertEquals(2000, conta2.getSaldo());
            fachada.debitar("0000", 500);
            ContaAbstrata contaNova = fachada.procurarConta("0000");
            assertEquals(1500, contaNova.getSaldo());


        }catch(Exception e){
            System.out.println("Erro! " + e.getMessage());
            assert false;
        }
    }

    @Test
    void transferir() {
        try {
            Cliente cliente = new Cliente("1111", "abc",TipoCliente.CLASS);
            fachada.cadastrar(cliente);
            Conta conta = new Conta("0000",5000,cliente);
            fachada.cadastrar(conta);

            Cliente cliente2 = new Cliente("2222", "xyz",TipoCliente.CLASS);
            fachada.cadastrar(cliente2);
            Conta conta2 = new Conta("9999",2000,cliente2);
            fachada.cadastrar(conta2);

            fachada.transferir("0000","9999",1000);
            ContaAbstrata contaTransferida = fachada.procurarConta("0000");
            assertEquals(4000, contaTransferida.getSaldo());

            ContaAbstrata contaRecebida = fachada.procurarConta("9999");
            assertEquals(3000, contaRecebida.getSaldo());


        }catch(Exception e){
            System.out.println("Erro! " + e.getMessage());
            assert false;
        }
    }







}