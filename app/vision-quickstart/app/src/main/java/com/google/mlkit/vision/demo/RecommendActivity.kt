package com.google.mlkit.vision.demo

import android.content.Intent
import android.content.pm.PackageManager
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.TextView
import java.net.URL

class RecommendActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_recommend)
        val apiResponse = URL("https://recommend-ar.herokuapp.com").readText()
        var delimiter1 = " "
        var delimiter2 = "\""
        val recParts = apiResponse.split(delimiter1,delimiter2)
        findViewById<TextView>(R.id.rec1).text = recParts[3]
        findViewById<TextView>(R.id.rec1).setOnClickListener {
            val intent = Intent(this@RecommendActivity,LaunchNavActivity::class.java)
            startActivity(intent)
        }
        findViewById<TextView>(R.id.rec2).text = recParts[4]
        findViewById<TextView>(R.id.rec2).setOnClickListener {
            val intent = Intent(this@RecommendActivity,LaunchNavActivity::class.java)
            startActivity(intent)
        }
        findViewById<TextView>(R.id.rec3).text = recParts[5]
        findViewById<TextView>(R.id.rec3).setOnClickListener {
            val intent = Intent(this@RecommendActivity,LaunchNavActivity::class.java)
            startActivity(intent)
        }
    }
}