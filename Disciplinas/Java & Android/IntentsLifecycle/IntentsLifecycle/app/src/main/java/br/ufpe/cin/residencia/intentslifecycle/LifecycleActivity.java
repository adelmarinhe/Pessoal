package br.ufpe.cin.residencia.intentslifecycle;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import java.util.Random;

public class LifecycleActivity extends AppCompatActivity {

    int activityId;
    TextView lifecycleLog, identificadores, textoExibido;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_lifecycle);
        activityId = new Random().nextInt();

        identificadores = findViewById(R.id.identificadores);
        lifecycleLog = findViewById(R.id.lifecycle);
        textoExibido = findViewById(R.id.textoDigitado);
        EditText campoTexto = findViewById(R.id.campoTexto);
        Button botao = findViewById(R.id.botao);

        botao.setOnClickListener(
                v -> {
                    String oQueFoiDigitado = campoTexto.getText().toString();
                    textoExibido.setText(oQueFoiDigitado);
                }
        );

        identificadores.setText(getString(R.string.identificadoresInicial, activityId));

    }
}