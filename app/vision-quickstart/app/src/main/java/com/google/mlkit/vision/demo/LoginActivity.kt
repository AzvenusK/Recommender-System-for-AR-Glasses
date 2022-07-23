package com.google.mlkit.vision.demo

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.text.TextUtils
import android.view.View.BaseSavedState
import android.widget.TextView
import android.widget.Toast
import com.google.firebase.auth.AuthResult
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.auth.FirebaseUser
import com.google.mlkit.vision.demo.java.ChooserActivity
import kotlinx.android.synthetic.main.activity_login.*
import kotlinx.android.synthetic.main.activity_register.*

class LoginActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)

        tv_register.setOnClickListener{
            startActivity(Intent(this@LoginActivity,RegisterActivity::class.java))
        }

        btn_login.setOnClickListener{
            when{
                TextUtils.isEmpty(et_register_email.text.toString().trim{ it <= ' '}) -> {
                    Toast.makeText(
                        this@LoginActivity,
                        "Please Enter your Email Address.",
                        Toast.LENGTH_SHORT
                    ).show()
                }

                TextUtils.isEmpty(et_register_password.text.toString().trim { it <= ' '}) -> {
                    Toast.makeText(
                        this@LoginActivity,
                        "Please Enter your Password.",
                        Toast.LENGTH_SHORT
                    ).show()
                }
                else -> {
                    val email: String = et_register_email.text.toString().trim { it <= ' ' }
                    val password: String = et_register_password.text.toString().trim { it <= ' ' }

                    // Create an instance and create a register a user with email and password.
                    FirebaseAuth.getInstance().signInWithEmailAndPassword(email, password)
                        .addOnCompleteListener {  login_task ->
                    if (login_task.isSuccessful) {
                        Toast.makeText(
                            this@LoginActivity,
                            "You have logged in successfully",
                            Toast.LENGTH_SHORT
                        ).show()

                        /**
                         * The user has successfully signed-in now successfully so we just send him to the main screen.
                         */
                        val intent = Intent(this@LoginActivity, ChooserActivity::class.java)
                        intent.flags = Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TASK
                        intent.putExtra(
                            "user id",
                            FirebaseAuth.getInstance().currentUser!!.uid
                        )
                        intent.putExtra("email id", email)
                        startActivity(intent)
                        finish()
                    }
                    else {
                        // If the registration is not successful then show error message.
                        Toast.makeText(
                            this@LoginActivity,
                            login_task.exception!!.message.toString(),
                            Toast.LENGTH_SHORT
                        ).show()
                    }
                }
            }
        }
    }

}