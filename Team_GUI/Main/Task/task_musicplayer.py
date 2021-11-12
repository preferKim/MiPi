import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtGui import *
from pygame import mixer

class musicPlayerWindow(QDialog):
    def __init__(self, parent): # 부모 윈도우(메모장)가 있기 때문에 parent 적어주기
        super(musicPlayerWindow, self).__init__(parent)
        uic.loadUi("Task/task_musicplayer.ui", self)
        
        # 윈도우 타이틀, 사이즈 설정
        #self.setGeometry(500, 500, 600, 400)  # x, y, w, h : 창 크기 조절
        self.setWindowTitle("Music") # 윈도우 타이틀 설정     
        self.show()
        self.songList_index = 0
        ### 기능연결 ###
        # 앨범 이미지, 노래 타이틀
        self.label_ALBUM.setPixmap(self.loadImageFromFile("image_source/img_album_sample.png", 200))
        
        # Play, Stop
        self.btn_play.clicked.connect(self.playSongFunction)
        self.btn_stop.clicked.connect(self.stopSongFunction)
        self.btn_next.clicked.connect(self.playNextSong)
        self.btn_prev.clicked.connect(self.playPrevSong)
        
        # Back: Close Window
        self.btn_back.clicked.connect(self.backToMainWindow)

    # 이미지 로드
    def loadImageFromFile(self, source_url, width_size): # source_url의 이미지로 qPixmap 객체생성 후, 해당 객체 리턴
        self.qPixmapFileVar = QPixmap()  # qPixmap 객체 생성
        self.qPixmapFileVar.load(source_url)  # 이미지 로드
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(width_size)  # 크기 조절
        return self.qPixmapFileVar
    
    def musicList(self):
        songList = []
        songList.append("./audio_source/Alex Cohen - Good Old Times.mp3")
        songList.append("./audio_source/Sound Creator - Christmas Postcard.mp3")
        songList.append("./audio_source/BDKSonic - Riverside Walk Dreamy Romantic Emotional Piano.mp3")
        return songList

    def playSongFunction(self):
        ### 노래재생 소스코드 실행 ###
        print("play song...")
        mixer.init()
        song_list = self.musicList()
        if(self.songList_index>len(song_list)-1):
            self.songList_index-=1
        elif(self.songList_index<0):
            self.songList_index+=1
        mixer.music.load(song_list[self.songList_index])
        mixer.music.play()
        print(f"song is now playing...{self.songList_index+1}")
        
    def stopSongFunction(self):
        ### 노래중지 소스코드 실행 ###
        print("stop song...")
        mixer.music.fadeout(1000)
    
    def playNextSong(self):
        ### 다음곡 실행 소스코드 ###
        print("play next song...")        
        self.songList_index+=1
        self.playSongFunction()
    
    def playPrevSong(self, a):
        ### 이전곡 실행 소스코드 ### 
        print("play prev song...")
        self.songList_index-=1
        self.playSongFunction()
    
    # 현재 dialog 창 종료
    def backToMainWindow(self):
        self.close()
        print("close dialog...")
