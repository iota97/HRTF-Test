import plotly.graph_objects as go
import scipy
import os

def plot(mono, stereo, hrtf, y_label):
    x = ['White noise']*int((len(mono)/3))+['Steps']*(int(len(mono)/3))+['Gunshots']*int((len(mono)/3))
    fig = go.Figure()
    fig.add_trace(go.Box(
        y=mono,
        x=x,
        name='Mono',
    ))
    fig.add_trace(go.Box(
        y=stereo,
        x=x,
        name='Stereo panning',
    ))
    fig.add_trace(go.Box(
        y=hrtf,
        x=x,
        name='SteamAudio HRTF',
    ))
    fig.update_layout(
        yaxis_title=y_label,
        boxmode='group'
    )
    fig.show()

mono_white_time = []
mono_shot_time = []
mono_step_time = []
stereo_white_time = []
stereo_shot_time = []
stereo_step_time = []
hrtf_white_time = []
hrtf_shot_time = []
hrtf_step_time = []
mono_white_horiz = []
mono_shot_horiz = []
mono_step_horiz = []
stereo_white_horiz = []
stereo_shot_horiz = []
stereo_step_horiz = []
hrtf_white_horiz = []
hrtf_shot_horiz = []
hrtf_step_horiz = []
mono_white_vert = []
mono_shot_vert = []
mono_step_vert = []
stereo_white_vert = []
stereo_shot_vert = []
stereo_step_vert = []
hrtf_white_vert = []
hrtf_shot_vert = []
hrtf_step_vert = []

def process_file(file_path):
    global mono_white_time
    global mono_shot_time
    global mono_step_time
    global stereo_white_time
    global stereo_shot_time
    global stereo_step_time
    global hrtf_white_time
    global hrtf_shot_time
    global hrtf_step_time
    global mono_white_horiz
    global mono_shot_horiz
    global mono_step_horiz
    global stereo_white_horiz
    global stereo_shot_horiz
    global stereo_step_horiz
    global hrtf_white_horiz
    global hrtf_shot_horiz
    global hrtf_step_horiz
    global mono_white_vert
    global mono_shot_vert
    global mono_step_vert
    global stereo_white_vert
    global stereo_shot_vert
    global stereo_step_vert
    global hrtf_white_vert
    global hrtf_shot_vert
    global hrtf_step_vert

    with open(file_path, 'r') as f:
        lines = f.readlines()

        mode = ''
        if (lines[1].strip() == 'Mode: Mono'):
            mode = 'mono'
        if (lines[1].strip() == 'Mode: Stereo'):
            mode = 'stereo'
        if (lines[1].strip() == 'Mode: Default'):
            mode = 'hrtf'

        for line in lines:
            if mode == 'mono' and line.startswith('White time (s): '): 
                mono_white_time += eval(line[len('White time (s): '):])
            if mode == 'mono' and line.startswith('Shot time (s): '): 
                mono_shot_time += eval(line[len('Shot time (s): '):])
            if mode == 'mono' and line.startswith('Step time (s): '): 
                mono_step_time += eval(line[len('Step time (s): '):])
            if mode == 'mono' and line.startswith('White horz (deg): '): 
                mono_white_horiz += eval(line[len('White horz (deg): '):])
            if mode == 'mono' and line.startswith('Shot horz (deg): '): 
                mono_shot_horiz += eval(line[len('Shot horz (deg): '):])
            if mode == 'mono' and line.startswith('Step horz (deg): '): 
                mono_step_horiz += eval(line[len('Step horz (deg): '):])
            if mode == 'mono' and line.startswith('White vert (deg): '): 
                mono_white_vert += eval(line[len('White vert (deg): '):])
            if mode == 'mono' and line.startswith('Shot vert (deg): '): 
                mono_shot_vert += eval(line[len('Shot vert (deg): '):])
            if mode == 'mono' and line.startswith('Step vert (deg): '): 
                mono_step_vert += eval(line[len('Step vert (deg): '):])
            if mode == 'stereo' and line.startswith('White time (s): '): 
                stereo_white_time += eval(line[len('White time (s): '):])
            if mode == 'stereo' and line.startswith('Shot time (s): '): 
                stereo_shot_time += eval(line[len('Shot time (s): '):])
            if mode == 'stereo' and line.startswith('Step time (s): '): 
                stereo_step_time += eval(line[len('Step time (s): '):])
            if mode == 'stereo' and line.startswith('White horz (deg): '): 
                stereo_white_horiz += eval(line[len('White horz (deg): '):])
            if mode == 'stereo' and line.startswith('Shot horz (deg): '): 
                stereo_shot_horiz += eval(line[len('Shot horz (deg): '):])
            if mode == 'stereo' and line.startswith('Step horz (deg): '): 
                stereo_step_horiz += eval(line[len('Step horz (deg): '):])
            if mode == 'stereo' and line.startswith('White vert (deg): '): 
                stereo_white_vert += eval(line[len('White vert (deg): '):])
            if mode == 'stereo' and line.startswith('Shot vert (deg): '): 
                stereo_shot_vert += eval(line[len('Shot vert (deg): '):])
            if mode == 'stereo' and line.startswith('Step vert (deg): '): 
                stereo_step_vert += eval(line[len('Step vert (deg): '):])
            if mode == 'hrtf' and line.startswith('White time (s): '): 
                hrtf_white_time += eval(line[len('White time (s): '):])
            if mode == 'hrtf' and line.startswith('Shot time (s): '): 
                hrtf_shot_time += eval(line[len('Shot time (s): '):])
            if mode == 'hrtf' and line.startswith('Step time (s): '): 
                hrtf_step_time += eval(line[len('Step time (s): '):])
            if mode == 'hrtf' and line.startswith('White horz (deg): '): 
                hrtf_white_horiz += eval(line[len('White horz (deg): '):])
            if mode == 'hrtf' and line.startswith('Shot horz (deg): '): 
                hrtf_shot_horiz += eval(line[len('Shot horz (deg): '):])
            if mode == 'hrtf' and line.startswith('Step horz (deg): '): 
                hrtf_step_horiz += eval(line[len('Step horz (deg): '):])
            if mode == 'hrtf' and line.startswith('White vert (deg): '): 
                hrtf_white_vert += eval(line[len('White vert (deg): '):])
            if mode == 'hrtf' and line.startswith('Shot vert (deg): '): 
                hrtf_shot_vert += eval(line[len('Shot vert (deg): '):])
            if mode == 'hrtf' and line.startswith('Step vert (deg): '): 
                hrtf_step_vert += eval(line[len('Step vert (deg): '):])

def parse_all():
    for file in os.listdir():
        if file.endswith(".txt"):
            process_file(file)

def plot_all():
    plot(mono_white_time+mono_step_time+mono_shot_time,
        stereo_white_time+stereo_step_time+stereo_shot_time,
        hrtf_white_time+hrtf_step_time+hrtf_shot_time,       
        "Time (s)")
    plot(mono_white_horiz+mono_step_horiz+mono_shot_horiz,
        stereo_white_horiz+stereo_step_horiz+stereo_shot_horiz,
        hrtf_white_horiz+hrtf_step_horiz+hrtf_shot_horiz,       
        "Horizontal movement (deg)")
    plot(mono_white_vert+mono_step_vert+mono_shot_vert,
        stereo_white_vert+stereo_step_vert+stereo_shot_vert,
        hrtf_white_vert+hrtf_step_vert+hrtf_shot_vert,       
        "Vertical movement (deg)")

def print_pval(a, b):
    p = scipy.stats.kstest(eval(a), eval(b)).pvalue
    print(a+" vs "+b+": "+"{:.2e}".format(p) + ("*" if p < 0.05 else ""))

def print_ks():
    print_pval("mono_white_time", "stereo_white_time")
    print_pval("mono_white_time", "hrtf_white_time")
    print_pval("stereo_white_time", "hrtf_white_time")
    print("---")
    print_pval("mono_step_time", "stereo_step_time")
    print_pval("mono_step_time", "hrtf_step_time")
    print_pval("stereo_step_time", "hrtf_step_time")
    print("---")
    print_pval("mono_shot_time", "stereo_shot_time")
    print_pval("mono_shot_time", "hrtf_shot_time")
    print_pval("stereo_shot_time", "hrtf_shot_time")
    print("---")
    print_pval("mono_white_time", "mono_step_time")
    print_pval("mono_white_time", "mono_shot_time")
    print_pval("mono_shot_time", "mono_step_time")
    print("---")
    print_pval("stereo_white_time", "stereo_step_time")
    print_pval("stereo_white_time", "stereo_shot_time")
    print_pval("stereo_shot_time", "stereo_step_time")
    print("---")
    print_pval("hrtf_white_time", "hrtf_step_time")
    print_pval("hrtf_white_time", "hrtf_shot_time")
    print_pval("hrtf_shot_time", "hrtf_step_time")
    print("---")
    print("---")
    print_pval("mono_white_horiz", "stereo_white_horiz")
    print_pval("mono_white_horiz", "hrtf_white_horiz")
    print_pval("stereo_white_horiz", "hrtf_white_horiz")
    print("---")
    print_pval("mono_step_horiz", "stereo_step_horiz")
    print_pval("mono_step_horiz", "hrtf_step_horiz")
    print_pval("stereo_step_horiz", "hrtf_step_horiz")
    print("---")
    print_pval("mono_shot_horiz", "stereo_shot_horiz")
    print_pval("mono_shot_horiz", "hrtf_shot_horiz")
    print_pval("stereo_shot_horiz", "hrtf_shot_horiz")
    print("---")
    print_pval("mono_white_horiz", "mono_step_horiz")
    print_pval("mono_white_horiz", "mono_shot_horiz")
    print_pval("mono_shot_horiz", "mono_step_horiz")
    print("---")
    print_pval("stereo_white_horiz", "stereo_step_horiz")
    print_pval("stereo_white_horiz", "stereo_shot_horiz")
    print_pval("stereo_shot_horiz", "stereo_step_horiz")
    print("---")
    print_pval("hrtf_white_horiz", "hrtf_step_horiz")
    print_pval("hrtf_white_horiz", "hrtf_shot_horiz")
    print_pval("hrtf_shot_horiz", "hrtf_step_horiz")
    print("---")
    print("---")
    print_pval("mono_white_vert", "stereo_white_vert")
    print_pval("mono_white_vert", "hrtf_white_vert")
    print_pval("stereo_white_vert", "hrtf_white_vert")
    print("---")
    print_pval("mono_step_vert", "stereo_step_vert")
    print_pval("mono_step_vert", "hrtf_step_vert")
    print_pval("stereo_step_vert", "hrtf_step_vert")
    print("---")
    print_pval("mono_shot_vert", "stereo_shot_vert")
    print_pval("mono_shot_vert", "hrtf_shot_vert")
    print_pval("stereo_shot_vert", "hrtf_shot_vert")
    print("---")
    print_pval("mono_white_vert", "mono_step_vert")
    print_pval("mono_white_vert", "mono_shot_vert")
    print_pval("mono_shot_vert", "mono_step_vert")
    print("---")
    print_pval("stereo_white_vert", "stereo_step_vert")
    print_pval("stereo_white_vert", "stereo_shot_vert")
    print_pval("stereo_shot_vert", "stereo_step_vert")
    print("---")
    print_pval("hrtf_white_vert", "hrtf_step_vert")
    print_pval("hrtf_white_vert", "hrtf_shot_vert")
    print_pval("hrtf_shot_vert", "hrtf_step_vert")

def plot_sep():
    fig = go.Figure()
    fig.add_trace(go.Box(name="Steam Audio HRTF", x=hrtf_white_time))
    fig.add_trace(go.Box(name="Stereo panning", x=stereo_white_time))
    fig.add_trace(go.Box(name="Mono", x=mono_white_time))
    fig.update_layout(xaxis=dict(title='Time (s)'), showlegend=False, title="White noise")
    fig.show()

    fig = go.Figure()
    fig.add_trace(go.Box(name="Steam Audio HRTF", x=hrtf_shot_time))
    fig.add_trace(go.Box(name="Stereo panning", x=stereo_shot_time))
    fig.add_trace(go.Box(name="Mono", x=mono_shot_time))
    fig.update_layout(xaxis=dict(title='Time (s)'), showlegend=False, title="Shots sound")
    fig.show()

    fig = go.Figure()
    fig.add_trace(go.Box(name="Steam Audio HRTF", x=hrtf_step_time))
    fig.add_trace(go.Box(name="Stereo panning", x=stereo_step_time))
    fig.add_trace(go.Box(name="Mono", x=mono_step_time))
    fig.update_layout(xaxis=dict(title='Time (s)'), showlegend=False, title="Steps sound")
    fig.show()

    fig = go.Figure()
    fig.add_trace(go.Box(name="Steam Audio HRTF", x=hrtf_white_horiz))
    fig.add_trace(go.Box(name="Stereo panning", x=stereo_white_horiz))
    fig.add_trace(go.Box(name="Mono", x=mono_white_horiz))
    fig.update_layout(xaxis=dict(title='Horizontal movement (deg)'), showlegend=False, title="White noise")
    fig.show()

    fig = go.Figure()
    fig.add_trace(go.Box(name="Steam Audio HRTF", x=hrtf_shot_horiz))
    fig.add_trace(go.Box(name="Stereo panning", x=stereo_shot_horiz))
    fig.add_trace(go.Box(name="Mono", x=mono_shot_horiz))
    fig.update_layout(xaxis=dict(title='Horizontal movement (deg)'), showlegend=False, title="Shots sound")
    fig.show()

    fig = go.Figure()
    fig.add_trace(go.Box(name="Steam Audio HRTF", x=hrtf_step_horiz))
    fig.add_trace(go.Box(name="Stereo panning", x=stereo_step_horiz))
    fig.add_trace(go.Box(name="Mono", x=mono_step_horiz))
    fig.update_layout(xaxis=dict(title='Horizontal movement (deg)'), showlegend=False, title="Steps sound")
    fig.show()

    fig = go.Figure()
    fig.add_trace(go.Box(name="Steam Audio HRTF", x=hrtf_white_vert))
    fig.add_trace(go.Box(name="Stereo panning", x=stereo_white_vert))
    fig.add_trace(go.Box(name="Mono", x=mono_white_vert))
    fig.update_layout(xaxis=dict(title='Vertical movement (deg)'), showlegend=False, title="White noise")
    fig.show()

    fig = go.Figure()
    fig.add_trace(go.Box(name="Steam Audio HRTF", x=hrtf_shot_vert))
    fig.add_trace(go.Box(name="Stereo panning", x=stereo_shot_vert))
    fig.add_trace(go.Box(name="Mono", x=mono_shot_vert))
    fig.update_layout(xaxis=dict(title='Vertical movement (deg)'), showlegend=False, title="Shots sound")
    fig.show()

    fig = go.Figure()
    fig.add_trace(go.Box(name="Steam Audio HRTF", x=hrtf_step_vert))
    fig.add_trace(go.Box(name="Stereo panning", x=stereo_step_vert))
    fig.add_trace(go.Box(name="Mono", x=mono_step_vert))
    fig.update_layout(xaxis=dict(title='Vertical movement (deg)'), showlegend=False, title="Steps sound")
    fig.show()

parse_all()
plot_all()
#plot_sep()
print_ks()
input()