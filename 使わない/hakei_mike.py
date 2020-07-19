# coding: UTF-8
import wave
import pyaudio
from numpy import *
from scipy import fft, zeros, arange
from PyQt4 import QtGui
import pyqtgraph as pg

def printWaveInfo(wf):
    print("チャンネル数: " + str(wf.getnchannels()))
    print("サンプル幅: " + str(wf.getsampwidth()))
    print("サンプリング周波数: " + str(wf.getframerate()))
    print("フレーム数: " + str(wf.getnframes()))
    print("パラメータ: " + str(wf.getparams()))
    print("長さ（秒）: " + str(float(wf.getnframes()) / wf.getframerate()))

class ButtonBox(QtGui.QWidget) :
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent = parent)

if __name__=="__main__":

    wf = wave.open("test.wav", "rb")
    printWaveInfo(wf)
    buffer = wf.readframes(wf.getnframes())
    print(len(buffer))
    data = frombuffer(buffer, dtype="int16")
    wf = wave.open("test.wav", "rb")
    p = pyaudio.PyAudio()
    stream = p.open(
        format = p.get_format_from_width(wf.getsampwidth()) ,
        channels = wf.getnchannels () ,
        rate = wf.getframerate () ,
        output = True
    )

    app = QtGui.QApplication([])
    app.quitOnLastWindowClosed()

    w = QtGui.QWidget()     #top level wodgit
    w.resize(850, 700)
    layout = QtGui.QGridLayout()
    w.setLayout(layout)
    w.setWindowTitle("Spectrum Analyzer")

    pw = pg.PlotWidget()
    pw2 = pg.PlotWidget()
    pw.getPlotItem()
    pw.setYRange(-12000, 12000)
    pw.setXRange(0, 440)
    pw2.getPlotItem()
    pw2.setYRange(0,6000)
    pw2.setXRange(0, 1024, padding = 0)
    fs = wf.getframerate()

    #グラフ描画設定
    pw2Axis = pw2.getAxis("bottom")
    pw2Axis.setLabel("Frequency [Hz]")
    pw2Axis.setScale(fs / 1024)
    hz_interval = 500
    newXAxis = (arange(int(fs / 2 / hz_interval)) + 1) * hz_interval
    oriXAxis = newXAxis / (fs / 2. / (1024 + 1))
    pw2Axis.setTicks([zip(oriXAxis, newXAxis)])

    layout.addWidget(pw, 0, 1)
    layout.addWidget(pw2, 1, 1)
    w.show()

    num = wf.getnframes()
    x = arange(0, num, 2)
    chunk = wf.getframerate() / 12
    d = wf.readframes(chunk)
    data2 = data[::2]
    signal_scale = 1. / 500
    signal = zeros(chunk, dtype = float)

    for i in range(0, num, chunk) :
        pw.plot(x[0:chunk], data2[i: i + chunk], clear = True)     #波形
        signal = data2[i: i+chunk]   #フーリエ変換
        fftspec = fft(signal)
        pw2.plot(abs(fftspec[0: chunk / 2] * signal_scale), clear = True)  #スペクトル
        stream.write(d)
        QtGui.QApplication.processEvents()
        d = wf.readframes(chunk)

    app.exec_()

