package br.ufpe.cin.residencia.ui;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.SwitchCompat;

import android.os.Bundle;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.CompoundButton;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.RadioGroup;
import android.widget.SeekBar;
import android.widget.Switch;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //log é onde vai aparecer as mensagens geradas pelos listeners
        final TextView log = findViewById(R.id.log);
        final ImageView icone = findViewById(R.id.icon);
        final Button txtButton = findViewById(R.id.txtButton);
        final ImageButton botaoImagem = findViewById(R.id.imgButton);
        final SwitchCompat swytch = findViewById(R.id.swytch);
        final CheckBox checkBox = findViewById(R.id.checkbox);
        final RadioGroup radioGroup = findViewById(R.id.radioGroup);
        final SeekBar seekBar = findViewById(R.id.seekbar);

        txtButton.setOnClickListener(
                v -> log.setText(R.string.txtbutton_clicked)
        );
        botaoImagem.setOnClickListener(
                v -> log.setText(R.string.imgbutton_clicked)
        );
        icone.setOnClickListener(
                v -> log.setText(R.string.icon_clicked)
        );
        log.setOnClickListener(
                v -> log.setText(R.string.log_clicked)
        );

//        swytch.setOnCheckedChangeListener(
//                new CompoundButton.OnCheckedChangeListener() {
//                    @Override
//                    public void onCheckedChanged(CompoundButton compoundButton, boolean b) {
//                       if (b) {
//                           log.setText(R.string.switch_checked);
//                       }
//                       else {
//                           log.setText(R.string.switch_unchecked);
//                       }
//                    }
//                }
//        );

        swytch.setOnCheckedChangeListener(
                (compoundButton, b) -> {
                    if (b) {
                        log.setText(R.string.switch_checked);
                    }
                    else {
                        log.setText(R.string.switch_unchecked);
                    }
                }
        );

        checkBox.setOnCheckedChangeListener(
                (cButton, b) -> {
                    if (b) {
                        log.setText(R.string.checkbox_checked);
                    }
                    else {
                        log.setText(R.string.checkbox_unchecked);
                    }
                }
        );

        radioGroup.setOnClickListener(
                v -> log.setText(R.string.radiogroup_clicked)
        );

//        radioGroup.setOnCheckedChangeListener(
//                new RadioGroup.OnCheckedChangeListener() {
//                    @Override
//                    public void onCheckedChanged(RadioGroup radioGroup, int idSelected) {
//                        if (idSelected == R.id.radioButton1) {
//                            log.setText(R.string.radiobtn1_checked);
//                        }
//                        else if (idSelected == R.id.radioButton2) {
//                            log.setText(R.string.radiobtn2_checked);
//                        }
//                        else if (idSelected == R.id.radioButton3) {
//                            log.setText(R.string.radiobtn3_checked);
//                        }
//                    }
//                }
//        );

        radioGroup.setOnCheckedChangeListener(
                (radioGroup1, idSelected) -> {
                    if (idSelected == R.id.radioButton1) {
                        log.setText(R.string.radiobtn1_checked);
                    }
                    else if (idSelected == R.id.radioButton2) {
                        log.setText(R.string.radiobtn2_checked);
                    }
                    else if (idSelected == R.id.radioButton3) {
                        log.setText(R.string.radiobtn3_checked);
                    }
                }
        );

        seekBar.setOnSeekBarChangeListener(
                new SeekBar.OnSeekBarChangeListener() {
                    @Override
                    public void onProgressChanged(SeekBar seekBar, int valorAtual, boolean mudancaVeioDoUsuario) {
                        String msg = getString(R.string.seekbar_changed, valorAtual);
                        log.setText(msg);
                    }

                    @Override
                    public void onStartTrackingTouch(SeekBar seekBar) {
                        Toast.makeText(getApplicationContext(),"Iniciou tracking touch",Toast.LENGTH_SHORT).show();
                    }

                    @Override
                    public void onStopTrackingTouch(SeekBar seekBar) {
                        Toast.makeText(getApplicationContext(),"Parou tracking touch",Toast.LENGTH_SHORT).show();
                    }
                }
        );

    }
}