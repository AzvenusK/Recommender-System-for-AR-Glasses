package com.google.mlkit.vision.demo;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.pm.ResolveInfo;
import android.os.Bundle;
import android.widget.Toast;

import java.util.List;


public class LaunchNavActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_launch_nav);
        Intent mainIntent = new Intent(Intent.ACTION_MAIN, null);
        mainIntent.addCategory(Intent.CATEGORY_LAUNCHER);
        List<ResolveInfo> pkgAppsList = getPackageManager().queryIntentActivities( mainIntent, 0);
        //Intent launchIntent = getPackageManager().getLaunchIntentForPackage("com.google.android.youtube");
        if (mainIntent != null) {
            startActivity(mainIntent);
        } else {
            Toast.makeText(LaunchNavActivity.this, "There is no package available in android", Toast.LENGTH_LONG).show();
        }
    }
}