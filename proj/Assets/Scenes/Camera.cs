using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Camera : MonoBehaviour
{
    public float lookSpeed = 1;
    float h = 0;
    float v = 0;
    public void Look() 
    {
        h += Mathf.Abs(Input.GetAxis("Mouse X") * lookSpeed);
        v += Mathf.Abs(Input.GetAxis("Mouse Y") * lookSpeed);
        transform.Rotate(-Vector3.right * (Input.GetAxis("Mouse Y") * lookSpeed));
        transform.Rotate(Vector3.up * (Input.GetAxis("Mouse X") * lookSpeed));
    }

    void OnApplicationFocus(bool hasFocus)
    {
        if (hasFocus)
        {
            Cursor.lockState = CursorLockMode.Locked;
        }
    }

    // Start is called before the first frame update
    void Start()
    {
        Cursor.lockState = CursorLockMode.Locked;
    }

    // Update is called once per frame
    void Update()
    {
        Look();

        if (Input.GetMouseButtonDown(0)) {
            RaycastHit hit;
            if (Physics.Raycast(transform.position, transform.forward, out hit, Mathf.Infinity, ~(1 <<  8))) {
                hit.collider.GetComponent<audio>().Hit(h, v);
                h = 0;
                v = 0;
            }
        }
        if (Input.GetKeyDown("9")) {
            lookSpeed -= 0.05f;
        }

        if (Input.GetKeyDown("0")) {
            lookSpeed += 0.05f;
        }

        if (Input.GetKey("escape")) {
            Application.Quit();
        }
    }
}