package br.ufpe.cin.motorola.banco.fachada;

import java.lang.reflect.Field;

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
    }

    @Test
    void procurarCliente() {
    }

    @Test
    void cadastrar() {
    }

    @Test
    void descadastrarCliente() {
    }

    @Test
    void testAtualizar() {
    }

    @Test
    void procurarConta() {
    }

    @Test
    void testCadastrar() {
    }

    @Test
    void descadastrarConta() {
    }

    @Test
    void creditar() {
    }

    @Test
    void debitar() {
    }

    @Test
    void transferir() {
    }
}