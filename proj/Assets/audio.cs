using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class audio : MonoBehaviour
{
    public int PER_TYPE_COUNT = 30;

    AudioSource src;
    public AudioClip whiteSrc;
    public AudioClip shotSrc;
    public AudioClip stepSrc;

    float spawn;
    float lastT = 0;
    string bigData = "";
    int hit;
    List<int> type = new List<int>();
    List<float> whiteT = new List<float>();
    List<float> shotT = new List<float>();
    List<float> stepT = new List<float>();
    List<float> whiteH = new List<float>();
    List<float> shotH = new List<float>();
    List<float> stepH = new List<float>();
    List<float> whiteV = new List<float>();
    List<float> shotV = new List<float>();
    List<float> stepV = new List<float>();

    void Shuffle<T>(List<T> ts) {
        var count = ts.Count;
        var last = count - 1;
        for (var i = 0; i < last; ++i)
        {
            var r = UnityEngine.Random.Range(i, count);
            var tmp = ts[i];
            ts[i] = ts[r];
            ts[r] = tmp;
        }
    }

    void Reset() {    
        transform.position = GameObject.Find("Main Camera").GetComponent<Camera>().transform.forward * 10.0f;
        spawn = -1.0f;
        whiteT = new List<float>();
        shotT = new List<float>();
        stepT = new List<float>();
        whiteH = new List<float>();
        shotH = new List<float>();
        stepH = new List<float>();
        whiteV = new List<float>();
        shotV = new List<float>();
        stepV = new List<float>();
        White();
        hit = 0;
        bigData = "";
        Shuffle(type);
    }

    void HRTF_Default() {
        Reset();
        src.spatialize = true;
        src.spatialBlend = 1.0f;
        GameObject.Find("Steam Audio Manager").GetComponent<SteamAudio.SteamAudioManager>().currentHRTF = 0;
        GameObject.Find("text").GetComponent<TMPro.TextMeshProUGUI>().text = "Default";
    }

    void HRTF_Custom() {
        Reset();
        src.spatialize = true;
        src.spatialBlend = 1.0f;
        GameObject.Find("Steam Audio Manager").GetComponent<SteamAudio.SteamAudioManager>().currentHRTF = 1;
        GameObject.Find("text").GetComponent<TMPro.TextMeshProUGUI>().text = "Custom";
    }

    void Mono() {
        Reset();
        src.spatialize = false;
        src.spatialBlend = 0.0f;
        GameObject.Find("text").GetComponent<TMPro.TextMeshProUGUI>().text = "Mono";
    }

    void StereoPan() {
        Reset();
        src.spatialize = false;
        src.spatialBlend = 1.0f;
        GameObject.Find("text").GetComponent<TMPro.TextMeshProUGUI>().text = "Stereo";
        transform.position = GameObject.Find("Main Camera").GetComponent<Camera>().transform.forward * 10.0f;
    }

    void Start() {
        for (int i = 0; i < PER_TYPE_COUNT; i++) {
            type.Add(0);
        }
        for (int i = 0; i < PER_TYPE_COUNT; i++) {
            type.Add(1);
        }
        for (int i = 0; i < PER_TYPE_COUNT; i++) {
            type.Add(2);
        }

        src = GetComponent<AudioSource>();
        Mono();
        White();
        transform.position = new Vector3(0, 0, 10.0f);
    }

    void RandomPosition() {
        float azimut = Random.Range(-180, 180);
        float elevation = Random.Range(-180, 180);
        Vector3 vector = new Vector3(1, 0, 0);
        vector = Quaternion.AngleAxis(azimut, Vector3.up) * vector;
        vector = Quaternion.AngleAxis(elevation, Vector3.right) * vector;
        transform.position = vector * 10.0f;
        bigData += Time.time.ToString("F2") + ": "+vector.ToString()+": "+type[hit]+"\n";
    }

    void RandomType() {
        if (type[hit] == 0) {
            White();
        } else if (type[hit] == 1) {
            Shot();
        } else {
            Step();
        }
    }

    public void Hit(float h, float v) {
        if (GameObject.Find("text").GetComponent<TMPro.TextMeshProUGUI>().text == "Saved!") {
            return;
        }
        if (spawn >= 0) {
            if (type[hit] == 0) {
                whiteT.Add(Time.time - spawn);
                whiteH.Add(h);
                whiteV.Add(v);
            } else if (type[hit] == 1) {
                shotT.Add(Time.time - spawn);
                shotH.Add(h);
                shotV.Add(v);
            } else {
                stepT.Add(Time.time - spawn);
                stepH.Add(h);
                stepV.Add(v);
            }
            bigData += Time.time.ToString("F2") + ": "+GameObject.Find("Main Camera").GetComponent<Camera>().transform.forward.ToString()+"\n";
            hit++;
            if (PER_TYPE_COUNT*3 == hit) {
                save();
                return;
            }
        }
        RandomPosition();
        RandomType();
        spawn = Time.time;
    }

    void White() {
        src.clip = whiteSrc;
        src.volume = 1.0f;
        src.Play();
    }

    void Shot() {
        src.clip = shotSrc;
        src.volume = 0.045f;
        src.Play();
    }

    void Step() {
        src.clip = stepSrc;
        src.volume = 0.9f;
        src.Play();
    }

    string ListAsString(List<float> l) {
        string s = "";
        if (l.Count > 0) {
            for (int i = 0; i < l.Count-1; i++) {
                s = s + l[i] + ", ";
            }
            s = s + l[l.Count-1];
        }
        return s;
    }

    string getVal(string time) {
        string s = "";
        s = s + time + "\n";
        s = s + "Mode: " + GameObject.Find("text").GetComponent<TMPro.TextMeshProUGUI>().text + "\n";
        s = s + "White time (s): [" + ListAsString(whiteT) + "]\n";
        s = s + "Shot time (s): [" + ListAsString(shotT) + "]\n";
        s = s + "Step time (s): [" + ListAsString(stepT) + "]\n";

        s = s + "White horz (deg): [" + ListAsString(whiteH) + "]\n";
        s = s + "Shot horz (deg): [" + ListAsString(shotH) + "]\n";
        s = s + "Step horz (deg): [" + ListAsString(stepH) + "]\n";

        s = s + "White vert (deg): [" + ListAsString(whiteV) + "]\n";
        s = s + "Shot vert (deg): [" + ListAsString(shotV) + "]\n";
        s = s + "Step vert (deg): [" + ListAsString(stepV) + "]";
        return s;
    }

    void save() {
        string t = System.DateTime.Now.ToString();
        string path = t.Replace("/", "_").Replace(":", "_")+".txt";

        System.IO.File.WriteAllText(path, getVal(t));

        string big = "\n\nTime in sec: camera forward versor\nTime in sec: target versor: sound type (0 = White, 1 = Shot, 2 = Step)\nSTART\n"+bigData+"END";
        System.IO.File.AppendAllText(path, big);

        GameObject.Find("text").GetComponent<TMPro.TextMeshProUGUI>().text = "Saved!";

        transform.position = new Vector3(10000000.0f, 1000000.0f, 100000000.0f);
        src.Stop();
    }

    void Update() {
        if (Input.GetKeyDown("1")) {
            Mono();
        }
        if (Input.GetKeyDown("2")) {
            StereoPan();
        }
        if (Input.GetKeyDown("3")) {
            HRTF_Default();
        }
        if (Input.GetKeyDown("4")) {
            HRTF_Custom();
        }
        if (spawn >= 0 && GameObject.Find("text").GetComponent<TMPro.TextMeshProUGUI>().text != "Saved!" && Time.time > lastT + 0.1) { 
            lastT = Time.time;
            bigData += Time.time.ToString("F2") + ": "+GameObject.Find("Main Camera").GetComponent<Camera>().transform.forward.ToString()+"\n";
        }
    }
}
