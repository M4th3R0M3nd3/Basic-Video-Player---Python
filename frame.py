from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from moviepy.editor import VideoFileClip
from pytube import YouTube
import pygame
import subprocess
import threading

# Inicializar o pygame para reproduzir o áudio
pygame.mixer.init()

def play_online_video(entry_url):
    url = entry_url.get()  # Obtém a URL do campo de entrada
    try:
        # Baixa o vídeo do YouTube
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension="mp4").first()
        stream.download(output_path="videos", filename="video.mp4")

        # Converte o áudio do vídeo para um formato compatível com o pygame
        video_clip = VideoFileClip("videos/video.mp4")
        audio_clip = video_clip.audio
        audio_clip.write_audiofile("videos/audio.mp3")

        # Reproduz o áudio
        pygame.mixer.music.load("videos/audio.mp3")
        pygame.mixer.music.play()

        # Reproduz o vídeo
        video_clip.preview()

    except Exception as e:
        messagebox.showerror("Erro", str(e))

def criar_janela_logado():
    janela_logado = Tk()
    janela_logado.title('Área Logado')

    # Adicione widgets à nova janela
    ttk.Label(janela_logado, text="Bem-vindo à área logada!").pack()

    # Campo para inserir a URL
    ttk.Label(janela_logado, text="Insira a URL do vídeo:").pack()
    entry_url = ttk.Entry(janela_logado)
    entry_url.pack()

    # Botão para reproduzir um vídeo online
    ttk.Button(janela_logado, text="Reproduzir Vídeo Online", command=lambda: threading.Thread(target=play_online_video, args=(entry_url,)).start()).pack()

    janela_logado.mainloop()

if __name__ == '__main__':
    criar_janela_logado()
