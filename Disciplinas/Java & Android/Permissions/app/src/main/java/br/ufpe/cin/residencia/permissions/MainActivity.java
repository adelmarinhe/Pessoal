package br.ufpe.cin.residencia.permissions;

import android.Manifest;
import android.content.pm.PackageManager;
import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;

import androidx.annotation.IdRes;
import androidx.annotation.NonNull;
import androidx.annotation.StringRes;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    private Button btn_location;
    private Button btn_camera;
    private Button btn_internet;
    private Button btn_contacts;
    private Button btn_storage;
    private TextView msg;

    private static final String[] CAMERA_PERMISSION = {
            Manifest.permission.CAMERA
    };

    private static final String[] ONCREATE_PERMISSIONS = {
            Manifest.permission.ACCESS_FINE_LOCATION,
            Manifest.permission.CAMERA,
            Manifest.permission.READ_CONTACTS
    };

    private static final int CAMERA_REQUEST = 42;
    private static final int LOCATION_REQUEST = 44;
    private static final int CONTACTS_REQUEST = 45;
    private static final int INTERNET_REQUEST = 46;
    private static final int STORAGE_REQUEST = 47;

    private static final int ONCREATE_REQUEST = 43;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btn_location = findViewById(R.id.btn_location);
        btn_camera = findViewById(R.id.btn_camera);
        btn_internet = findViewById(R.id.btn_internet);
        btn_contacts = findViewById(R.id.btn_contacts);
        btn_storage = findViewById(R.id.btn_storage);
        msg = findViewById(R.id.mensagem);

        btn_camera.setOnClickListener(
                v -> {
                    if (podeUsarCamera()) {
                        acessarRecurso(R.string.msg_camera);
                    }
                    else {
                        requestPermissions(CAMERA_PERMISSION, CAMERA_REQUEST);
                    }
                }
        );

        btn_location.setOnClickListener(
                v -> {
                    if (podeUsarLocation1() && podeUsarLocation2()) {
                        acessarRecurso(R.string.msg_contacts);
                    }
                    else {
                        sem_permissao();
                    }
                }
        );
        btn_storage.setOnClickListener(
                v -> {
                    if (podeUsarLocation1()) {
                        acessarRecurso(R.string.msg_location);
                    }
                    else {
                        sem_permissao();
                    }
                }
        );
        btn_contacts.setOnClickListener(
                v -> {
                    if (podeUsarContatos()) {
                        acessarRecurso(R.string.msg_contacts);
                    }
                    else {
                        sem_permissao();
                    }
                }
        );

        btn_internet.setOnClickListener(
                v -> {
                    if (podeUsarInternet()) {
                        acessarRecurso(R.string.msg_internet);
                    }
                    else {
                        sem_permissao();
                    }
                }
        );

        requestPermissions(ONCREATE_PERMISSIONS,ONCREATE_REQUEST);
    }

    @Override
    public void onRequestPermissionsResult(
            int requestCode,
            @NonNull String[] permissions,
            @NonNull int[] grantResults)
    {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        if (requestCode == CAMERA_REQUEST) {
            if (grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                acessarRecurso(R.string.msg_camera);
            }
            else {
                sem_permissao();
            }
        }
        if (requestCode == LOCATION_REQUEST) {
            if (grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                acessarRecurso(R.string.msg_location);
            }
            else {
                sem_permissao();
            }
        }
        if (requestCode == STORAGE_REQUEST) {
            if (grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                acessarRecurso(R.string.msg_armazenamento);
            }
            else {
                sem_permissao();
            }
        }
        if (requestCode == CONTACTS_REQUEST) {
            if (grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                acessarRecurso(R.string.msg_contacts);
            }
            else {
                sem_permissao();
            }
        }
        if (requestCode == INTERNET_REQUEST) {
            if (grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                acessarRecurso(R.string.msg_internet);
            }
            else {
                sem_permissao();
            }
        }
    }

    private boolean podeUsarLocation1() {
        return temPermissao(Manifest.permission.ACCESS_FINE_LOCATION);
    }
    private boolean podeUsarLocation2() {
        return temPermissao(Manifest.permission.ACCESS_COARSE_LOCATION);
    }
    private boolean podeUsarContatos() { return temPermissao(Manifest.permission.READ_CONTACTS); }
    private boolean podeUsarInternet() {
        return temPermissao(Manifest.permission.INTERNET);
    }
    private boolean podeUsarCamera() {
        return temPermissao(Manifest.permission.CAMERA);
    }
    private boolean podeUsarStorage() {
        return temPermissao(Manifest.permission.READ_EXTERNAL_STORAGE);

    }


    private boolean temPermissao(String perm) {
        return (
                checkSelfPermission(perm)
                        ==
                        PackageManager.PERMISSION_GRANTED
        );
    }

    private void sem_permissao() {
        msg.setText(R.string.msg_sem_permissao);
    }

    private void acessarRecurso(@StringRes int id) {
        msg.setText(id);
    }

}