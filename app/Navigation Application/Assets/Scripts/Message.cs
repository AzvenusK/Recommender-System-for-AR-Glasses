using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Message : MonoBehaviour
{
    public GameObject messageObject;
    
    // Start is called before the first frame update
    void Start()
    {
        Invoke("activate", 18.0f);
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    void activate()
    {
        messageObject.SetActive(true);
        //Debug.Log("Time Up!");
    }
}
