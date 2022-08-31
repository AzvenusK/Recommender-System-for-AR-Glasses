using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Blinking : MonoBehaviour
{
    public GameObject front;
    public GameObject left;
    public GameObject right;
    
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if (Time.time < 5.0f)
        {
            front.SetActive(true);
            StartCoroutine(BlinkGameObject(front, 2, 10));
        }
        else if (Time.time > 5.0f && Time.time < 7.0f)
        {
            front.SetActive(false);
            right.SetActive(true);
            StartCoroutine(BlinkGameObject(right, 2, 2));
        }
        else if (Time.time > 7.0f && Time.time < 18.0f)
        {
            right.SetActive(false);
            front.SetActive(true);
            StartCoroutine(BlinkGameObject(front, 2, 10));
        }
        else
            front.SetActive(false);
    }

    public IEnumerator BlinkGameObject(GameObject gameObject, int numBlinks, float seconds)
    {
        // In this method it is assumed that your game object has a SpriteRenderer component attached to it
        SpriteRenderer renderer = gameObject.GetComponent<SpriteRenderer>();
        // disable animation if any animation is attached to the game object
        //      Animator animator = gameObject.GetComponent<Animator>();
        //      animator.enabled = false; // stop animation for a while
        for (int i = 0; i < numBlinks; i++)
        {
            //toggle renderer
            renderer.enabled = !renderer.enabled;
            
            //
            yield return new WaitForSeconds(seconds);
        }
        //make sure renderer is enabled when we exit
        renderer.enabled = true;
        //    animator.enabled = true; // enable animation again, if it was disabled before
    }
}
