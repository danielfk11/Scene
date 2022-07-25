# CRIAR EXECUTAVEL PARA TRANSFORMAR EM ARQUIVO/SITE PARA DOWNLOAD. V1.0.0
from pytube import YouTube                                              
import time

file = ""                                       #pasta onde salvar os videos baixados
file_logs = ""                                  #pasta para criar o arquivo de logs(apagavel)           
url = input(str("Digite a url que deseja baixar: "))

try:
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream_audio = yt.streams.get_audio_only()
    type_video = input("Deseja baixar mp3 ou mp4? ")
except:
    print("Link invalido..")

if type_video == "mp3":
    stream_audio.download(output_path=file)

if type_video == "mp4":
    stream.download(output_path=file)

text = "\n{} Media -> {}, Name -> {}({})".format(url, type_video, yt.title, yt.author)  #DELETE CASO NAO QUEIRA LOGS
                                                                                        #DELETE CASO NAO QUEIRA LOGS
try:                                                                                    #DELETE CASO NAO QUEIRA LOGS
    with open(file_logs, "a") as log:                                                   #DELETE CASO NAO QUEIRA LOGS
        log.write(text)                                                                 #DELETE CASO NAO QUEIRA LOGS
except:                                                                                 #DELETE CASO NAO QUEIRA LOGS
    print("[ERROR] Tipo de link invalido, nao foi possivel salvar nas logs.")           #DELETE CASO NAO QUEIRA LOGS

print("Fazendo download...")
time.sleep(5)
print("Download feito com sucesso!")
print("Title     ->",yt.title)
print("Thumbnail ->",yt.thumbnail_url)
print("Author    ->",yt.author)
print("Views     ->",yt.views)
print("Data      ->",yt.publish_date)
print("Media     ->", type_video)
print("URL       ->",url)

inp = input("[ENTER] para fechar ")
