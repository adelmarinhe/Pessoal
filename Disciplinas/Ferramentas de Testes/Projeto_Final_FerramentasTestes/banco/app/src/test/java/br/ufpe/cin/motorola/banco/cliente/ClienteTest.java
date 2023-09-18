package br.ufpe.cin.motorola.banco.cliente;

import br.ufpe.cin.motorola.banco.conta.RepositorioContasMap;
import br.ufpe.cin.motorola.banco.excecoes.ClienteInexistenteException;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class ClienteTest {
    RepositorioClientesMap RCMap;
    Cliente cliente;


     @BeforeEach
      void setUp(){
        cliente = new Cliente("000","aaa", TipoCliente.CLASS);
         RCMap = new RepositorioClientesMap();
      }

    @Test
    public void getCpf() {
        assertFalse(cliente.getCpf().isEmpty());
    }

    @Test
    public void atualizarMap () {
         assertDoesNotThrow(
                 ()->{
                     RCMap.inserir(cliente);
                     Cliente cliente2 = RCMap.procurar("000");
                     assertEquals("aaa", cliente2.getNome());
                     cliente2.setNome("xyz");
                     RCMap.atualizar(cliente2);
                     Cliente clienteNovo = RCMap.procurar("000");
                     assertEquals("xyz", clienteNovo.getNome());
                                      });



    }

    @Test
    public void atualizarCliNullMap () {

        assertThrows(ClienteInexistenteException.class, ()->{
            RCMap.atualizar(cliente);
        });

    }

    @Test
    public void removerMap () throws ClienteInexistenteException {
        RCMap.inserir(cliente);
        Cliente cliente2 = RCMap.procurar("000");
        assertEquals("aaa", cliente2.getNome());
        RCMap.remover("000");

        assertThrows(ClienteInexistenteException.class, ()->{
            RCMap.procurar("000");
        });

    }

    @Test
    public void removerCliNullMap () {

        assertThrows(ClienteInexistenteException.class, ()->{
            RCMap.remover("000");
        });

    }


    @Test
    public void getNome() {
        assertFalse(cliente.getNome().isEmpty());
    }

    @Test
    void getTipo() {
        assertEquals(TipoCliente.CLASS, cliente.getTipo());
    }

    @Test
    void setCpf() {
        assertTrue(cliente.setCpf("555"));

    }

    @Test
    void setNome() {
        assertTrue(cliente.setNome("gle"));

    }

    @Test
    void setTipo() {
        assertTrue(cliente.setTipo(TipoCliente.VIP));
    }
}