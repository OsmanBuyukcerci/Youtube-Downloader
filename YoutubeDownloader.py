import ttkbootstrap as ttk
from pytube import YouTube
import os

def download_func():
    radio_value = var_radio.get()
    videos = text.get('1.0', 'end-1c')
    videos = videos.split('\n')
    
    for video in range(len(videos)):
        yt = YouTube(videos[video])
        if var_checkbutAudio.get() == True:
            stream = yt.streams.get_audio_only()
            stream.download(audioPATH)
        else:
            try:
                if radio_value == 2:
                    yt.streams.filter(res='360p').first().download(videoPATH)
                elif radio_value == 3:
                    yt.streams.filter(res='480p').first().download(videoPATH)
                elif radio_value == 4:
                    yt.streams.filter(res='720p').first().download(videoPATH)
                elif radio_value == 5:
                    yt.streams.filter(res='1080p').first().download(videoPATH)
                else:
                    yt.streams.get_highest_resolution().download(videoPATH)
            except:
                yt.streams.get_highest_resolution().download(videoPATH)
    completion_label.configure(text='Progress finished.')
    completion_label.grid(row=10, column=1, padx=10, pady=10, sticky='W')

def enable_video_set():
    if var_checkbutVideo.get() == True:
        audio_checkbut.config(state='disabled')
        radio360.config(state='enabled')
        radio480.config(state='enabled')
        radio720.config(state='enabled')
        radio1080.config(state='enabled')
        radioHighest.config(state='enabled')
    else:
        audio_checkbut.config(state='enabled')
        radio360.config(state='disabled')
        radio480.config(state='disabled')
        radio720.config(state='disabled')
        radio1080.config(state='disabled')
        radioHighest.config(state='disabled')

def audio_checkbut_func():
    if var_checkbutAudio.get() == True:
        video_checkbut.config(state='disabled')
    else:
        video_checkbut.config(state='enabled')

WIDHT = 1920
HEIGHT = 1080 
WIDHT = (WIDHT-700)/2
HEIGHT = (HEIGHT-400)/2

logo_file = "youtubeLogo.ico"
logo_path = os.path.abspath(logo_file)

audioPATH = os.getcwd() + '\\Audio'
videoPATH = os.getcwd() + '\\Video'

#window
window = ttk.Window(themename='darkly')
window.geometry('700x400+' + str(int(WIDHT)) + '+' + str(int(HEIGHT)))
window.title('Youtube Audio/Video Downloader')
window.resizable(False, False)
window.iconbitmap(logo_path)

#textbox
text = ttk.Text()
text.grid(row=0, column=0, pady=10, padx=10)

#settings frame
var_checkbutAudio = ttk.BooleanVar()
var_checkbutVideo = ttk.BooleanVar()
var_radio = ttk.IntVar()
frame = ttk.Frame()
frame.grid(row=0, column=1)
label = ttk.Label(
    master=frame,
    text='Settings',
    font='Arial, 24'
)
label.grid(row=0, column=1, sticky='w')

completion_label = ttk.Label(
    master=frame,
    text= None,
    font='Arial, 8'
)

audio_checkbut= ttk.Checkbutton(
    master=frame,
    text='Audio',
    state='False',
    variable=var_checkbutAudio,
    command=audio_checkbut_func
)
audio_checkbut.grid(row=1, column=1, pady=10 , padx=10, sticky='W')

video_checkbut= ttk.Checkbutton(
    master=frame,
    text='Video',
    state='False',
    variable=var_checkbutVideo,
    command=enable_video_set
)
video_checkbut.grid(row=2, column=1, pady=10 , padx=10, sticky='W')

radio360 = ttk.Radiobutton(
    master=frame,
    text='360p',
    value=2,
    variable=var_radio,
    state='disabled'
)
radio360.grid(row=3, column=1, pady=10, padx=10, sticky='W')

radio480 = ttk.Radiobutton(
    master=frame,
    text='480p',
    value=3,
    variable=var_radio,
    state='disabled'
)
radio480.grid(row=4, column=1, pady=10, padx=10, sticky='W')

radio720 = ttk.Radiobutton(
    master=frame,
    text='720p',
    value=4,
    variable=var_radio,
    state='disabled'
)
radio720.grid(row=5, column=1, pady=10, padx=10, sticky='W')

radio1080 = ttk.Radiobutton(
    master=frame,
    text='1080p',
    value=5,
    variable=var_radio,
    state='disabled'
)
radio1080.grid(row=6, column=1, pady=10, padx=10, sticky='W')

radioHighest = ttk.Radiobutton(
    master=frame,
    text='Highest Resolution Possible',
    value=6,
    variable=var_radio,
    state='disabled'
)
radioHighest.grid(row=7, column=1, pady=10, padx=10, sticky='W')

#button
download_but = ttk.Button(
    master=frame,
    text='Download',
    command=download_func
)
download_but.grid(row=9, column=1, pady=10, padx=10, sticky='W')

#run
window.mainloop()