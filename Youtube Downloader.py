from pytube import YouTube
the_url=input("請輸入想下載的影片:")
yt=YouTube(url=the_url)#想下載的影片
print("影片:",yt.title)#影片標題
file_type=input("請輸入想下載的格式 mp3 or mp4:")
if (file_type == 'mp3'):
    spec=yt.streams.filter(adaptive=True,type=("audio"))
    print(spec)
    qua=input("請輸入想下載的音樂音質:")
    spec=yt.streams.filter(adaptive=True,abr=(qua))
    print(spec)
    itag=input("請輸入想下載的音樂itag:")
    try:
        stream=yt.streams.get_by_itag(itag)
        stream.download(output_path=("D:\MyFold\Python Project\python-"))
        print('完成')
    except Exception:
        print("無符合格式") 
elif file_type=='mp4':
    spec=yt.streams.filter(adaptive=True,file_extension=("mp4"))
    print(spec)
    resol=input("請輸入想下載的影片畫質(只支援到720p):")
    spec=yt.streams.filter(adaptive=True,res=(resol),file_extension=("mp4"))
    
    try:
        stream=yt.streams.get_by_resolution(resol)
        stream.download(output_path=("D:\MyFold\Python Project\python-"))
        print('完成')
    except Exception:
        print("無符合格式")       
else:
    print("輸入不正確")
# print(yt.streams.filter(adaptive=True,res=("1080p"),file_extension=("mp4")))#可支援格式 filter表示篩選 pytube只支援到720p
stream=yt.streams.get_by_resolution("720p")
stream.download(output_path=("D:\MyFold\Python Project\python-"))