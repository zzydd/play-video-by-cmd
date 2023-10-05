print('')
print('程序正在初始化，请稍等...')
import os
import sys
import cv2
import time
import base64
import win32ui
import win32api
import win32con
import TestPage
import pyautogui
import datetime
from PIL import Image

#模拟F11全屏
win32api.keybd_event(122, 0, 0, 0)#按下按键
win32api.keybd_event(122, 0, win32con.KEYEVENTF_KEYUP, 0)#施放按键
time.sleep(0.1)

#获取屏幕尺寸
screenWidth, screenHeight = pyautogui.size()

#基础布局
os.system('title 基于命令提示符的播放器v1.0')
os.system('color 1f')
MainPath = os.path.realpath(sys.argv[0])
MainName = os.path.basename(MainPath)
MainDir = os.path.dirname(MainPath)
RunCommand = ('RUN')
FileType = ('NotReady')
StopCode = ('')

#获取时间
year=(str(datetime.datetime.now().year))
mounth=(str(datetime.datetime.now().month))
date=(str(datetime.datetime.now().day))
hour=(str(datetime.datetime.now().hour))
minute=(str(datetime.datetime.now().minute))
second=(str(datetime.datetime.now().second))
TimeCut = (year+mounth+date+hour+minute+second)


#创建数据文件夹
try:
    os.makedirs(MainDir+'/设置数据')
except:
    pass

with open (MainDir+'/设置数据/计算公式.txt','w') as file:
    file.write('播放速度公式：刷新速度 = (1/(帧率*播放倍率))+(播放微调/100)，取5位。单位秒\n')
    file.write('1080P画面压缩公式：宽/10     高/10/2\n')
    file.write('4K   画面压缩公式：宽/20*2   高/40*2\n')
    file.write('8K   画面压缩公式：宽/40*2   高/40\n')


#【读取数据】

try:
    #灰度字符
    with open (MainDir+'/设置数据/灰度字符.txt','r') as file:
        CharListData = file.read()
    CharList = list(CharListData)
except:
    with open (MainDir+'/设置数据/灰度字符.txt','w') as file:
        file.write("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
    CharList = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

try:
    #播放倍率
    with open (MainDir+'/设置数据/播放倍率.ini','r') as file:
        PlayTimes = file.read()
    PlayTimes = float(PlayTimes)
except:
    with open (MainDir+'/设置数据/播放倍率.ini','w') as file:
        file.write('1')
    PlayTimes = float(1)

try:
    #速度微调
    with open (MainDir+'/设置数据/播放微调.ini','r') as file:
        PlayMove = file.read()
    PlayMove = float(PlayMove)
except:
    with open (MainDir+'/设置数据/播放微调.ini','w') as file:
        file.write('0')
    PlayMove = float(0)

try:
    #播放模式
    with open (MainDir+'/设置数据/播放模式.ini','r') as file:
        PlayMode = file.read()
except:
    with open (MainDir+'/设置数据/播放模式.ini','w') as file:
        file.write('0')
    PlayMode = ('0')

try:
    #界面颜色
    with open (MainDir+'/设置数据/界面颜色.txt','r') as file:
        MainColor = file.read()
except:
    with open (MainDir+'/设置数据/界面颜色.txt','w') as file:
        file.write('color f')
    MainColor = ('color f')



#【开始页】
    
os.system('cls')
print('''
【程序信息】

 名称：基于命令提示符的视频播放器
 作者：豆豆ZZYDD
 

【基本说明】

 这个播放器会将你选择的视频以类似于字符画的形式展现在在CMD界面
 但是不同的设备效果和速度可能不同，您可以根据以下步骤进行微调。
 注：调整为实时生效，如有必要您现在就可以调整并作用于本次运行。

 1：设置文件位置
    设置文件的位置是在程序相同目录下的 "设置数据" 文件夹中。

 2：设置播放倍率
    如果您感觉播放有明显偏慢，您可以打开"播放倍率.ini"
    该键值仅支持输入数字

 3：设置播放微调
    如果您感觉播放有轻微偏差，您可以打开"播放微调.ini"
    该键值调整幅度很小，同时仅支持输入数字

 4：调整灰度字符
    如果您想用其他字符替代当前字符，您可以打开"灰度字符.txt"
    该键共70个字符串，不可以增加减少，不可以换行。

 5：修改界面颜色
    如果您想修改播放界面颜色，您可以打开"界面颜色.txt"
    语法与cmd命令相同，你可以使用color命令来修改颜色


【关于闪烁】

 部分设备播放会有快速的闪烁，这是因为字符渲染速度跟不上画面刷新速度。
 与硬件配置、显示器刷新率、系统流畅度 等因素有关。且暂无完美解决方案。
 不过你仍可尝试以下方法：

 1：以管理员权限运行
    以管理员权限运行部分情况下可以完美解决该问题，但播放速度可能会变慢。

 2：调整播放速度
    你可以尝试条慢播放速度，这有几率完美解决该问题，但不是100%。

 3：关闭杀毒软件
    杀毒软件会检查程序所有操作导致渲染变慢。关闭杀软有几率缓解该问题。

 4：调整播放模式
    禁用清屏100%解决该问题，但可能会有多余画面，并且可能伴随轻微抖动。
    如果需要禁用清屏功能，请将设置文件 "播放模式.ini" 中的键值改为 1。


【更多建议】

 1：视频分辨率建议小于1080P
 2：视频帧率建议小于30fps
 3：程序支持8K，但效果不佳
 4：已默认全屏，可按F11退出

    ''')

wait = input(' 按回车选择文件→')
os.system('cls')

#【读取数据-2】

try:
    #灰度字符
    with open (MainDir+'/设置数据/灰度字符.txt','r') as file:
        CharListData = file.read()
    CharList = list(CharListData)
except:
    CharList = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

try:
    #播放倍率
    with open (MainDir+'/设置数据/播放倍率.ini','r') as file:
        PlayTimes = file.read()
    PlayTimes = float(PlayTimes)
except:
    PlayTimes = float(1)

try:
    #速度微调
    with open (MainDir+'/设置数据/播放微调.ini','r') as file:
        PlayMove = file.read()
    PlayMove = float(PlayMove)
except:
    PlayMove = float(0)

try:
    #播放模式
    with open (MainDir+'/设置数据/播放模式.ini','r') as file:
        PlayMode = file.read()
except:
    PlayMode = ('0')

try:
    #界面颜色
    with open (MainDir+'/设置数据/界面颜色.txt','r') as file:
        MainColor = file.read()
except:
    MainColor = ('color f')




#【选择文件】  
lpszFilter = "视频文件 |*.mp4;*.mov;*.mkv;*.avi|" \
             "图像文件 |*.jpg;*.png;*.bmp|" \
             "所有文件 |*.*|" \
             "豆豆ZZYDD|*.zzydd|"
dlg = win32ui.CreateFileDialog(True,"mp4", None, 0x04 | 0x02, lpszFilter)
dlg.SetOFNInitialDir(MainDir)
dlg.DoModal()
VideoFile = dlg.GetPathName()
VideoFileName = os.path.basename(VideoFile)
VideoFilePath = os.path.dirname(VideoFile)
suffix=os.path.splitext(VideoFile)[1]

#界面优化
MouseX, MouseY = pyautogui.position() #获取当前鼠标位置
pyautogui.leftClick((screenWidth-20), (screenHeight-20))#点击界面
pyautogui.moveTo(MouseX, MouseY) #移动鼠标至原先位置



#判断文件种类
if suffix in ['.mp4','.mov','.mkv','.avi']:
    FileType = ('Video')
elif suffix in ['.jpg','.png','.bmp',]:
    FileType = ('Image')
elif suffix =='':
    FileType = ('None')
    RunCommand=('STOP')
    StopCode = (StopCode+'\n 01：未选择文件，运行个蛋')
else:
    FileType = ('Unknow')
    

#验证文件格式
if suffix not in ['.mp4','.mov','.mkv','.avi','.jpg','.png','.bmp',]:
    RunCommand=('STOP')
    StopCode = (StopCode+'\n 01：不受支持的文件格式')

#显示反馈
if FileType == 'Video':
    print('''
【操作提示】

 下一步将显示一张测试图片\n 打开后请用 "Ctrl+滚轮" 调整界面大小至合适位置
     
    ''')
    wait = input(' 按回车显示测试页→')
    os.system('cls')
    os.system(MainColor)

elif FileType == 'Image':
    print('''
【操作提示】

 你选择了图像文件，已启用字符画模式
 生成的内容将会以文本文件的进行保存
 当前界面可用 "Ctrl+滚轮" 对预览图像进行缩放

 该模式还在开发中，属于隐藏内测模式，部分功能可能还不完善
     
    ''')
    wait = input(' 按回生成字符画→')
    os.system('cls')
    os.system(MainColor)



#【字符画】

def CharPaint(IMG, W, H):

    #映射灰度
    def get_char(r,g,b,alpha=256):
        if alpha==0:#透明度
            return ' '  
        length=len(CharList)
        gray=int(0.2126*r+0.7152*g+0.0722*b)#计算灰度
        unit=(256.0+1)/length
        return CharList[int(gray/unit)]#映射色块

    #处理照片
    W = int(W)
    H = int(H)
    IMG = IMG.resize((W,H),Image.NEAREST)

    #生成文本
    text=""
    for i in range(H):  
        for j in range(W):  
            text+=get_char(*IMG.getpixel((j,i)))  
        text+='\n'

    #输出文本
    if PlayMode=='0':
        sys.stdout.write('\033[2J\033[1;1H')
        time.sleep(BreakTime)
        sys.stdout.flush()
        sys.stdout.write(text)
        sys.stdout.flush()
        
    elif PlayMode=='1':
        print('')
        print(text)
        print('')

    #图像模式
    if FileType=='Image':
        try:
            os.makedirs(MainDir+'/字符画')
        except:
            pass
        with open(MainDir+'/字符画/'+VideoFileName+'-'+TimeCut+'.txt','w') as file:  
            file.write(text)
        
    



#【视频处理】

#打开视频
cap = cv2.VideoCapture(VideoFile)

#获取尺寸
VideoW = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  
VideoH = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
VideoF = int(cap.get(cv2.CAP_PROP_FPS))

if VideoF==0:
    RunCommand=('STOP')
    StopCode = (StopCode+'\n 02：帧率获取失败，请检测文件是否损坏')
    

#判断分辨率
if VideoW*VideoH <= 2073600:
    Res = '1080P'
elif VideoW*VideoH > 2073600 and VideoW*VideoH <= 8294400:
    Res = '4K'
elif VideoW*VideoH > 8294400 and VideoW*VideoH <= 33177600:
    Res = '8K'
elif VideoW*VideoH > 33177600:
    Res = '16K'
    RunCommand=('STOP')
    StopCode = (StopCode+'\n 03：分辨率过高，暂不支持>8K的视频')

    
#压缩质量
ResSet='1'
if Res == '1080P':
    #低
    INPUTW = VideoW/10
    INPUTH = VideoH/10/2

if Res == '4K':
    #低
    INPUTW = VideoW/20*2
    INPUTH = VideoH/20

if Res == '8K':
    #低
    INPUTW = VideoW/40*2
    INPUTH = VideoH/40


#渲染间隔
try:
    BreakTime = (1/(VideoF*PlayTimes))+(PlayMove/100)
    BreakTime = round(BreakTime,5)
except:
    RunCommand=('STOP')
    StopCode = (StopCode+'\n 04：渲染间隔计算异常')

'''
BadApple 1080P: BreakTime = (1/(VideoF*1.315))+(0/100)
'''



#【显示测试】

if RunCommand=='RUN' and FileType =='Video':
    #释放图片
    TestPageData = TestPage.Icon
    TestPageIMG = TestPageData().ig
    with open(MainDir+'/TestPage.png', 'wb') as file:
        file.write(base64.b64decode(TestPageIMG))

    #打开图片
    TestIMG = Image.open(MainDir+'/TestPage.png')
    CharPaint(TestIMG, INPUTW, INPUTH)
    print('')

    #删除缓存
    wait=input(' 调整完毕后按回车正式运行→')
    os.system('cls')
    os.remove(MainDir+'/TestPage.png')

else:
    pass




#【视频帧处理】

while RunCommand=='RUN':
    #读取帧  
    ret, frame = cap.read()  

    #渲染帧
    if ret:
        #格式转换
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #BGR转RGB  
        img = Image.fromarray(frame)#numpy数组转PIL图像

        #生成字符
        CharPaint(img, INPUTW, INPUTH)

    #结束判断
    elif not ret:break  
  
#释放对象  
cap.release()

#清除屏幕
if FileType =='Video':
    os.system('cls')
elif FileType =='Image':
    print('\n\n')
    print('生成的内容存储在程序目录下 "字符画" 文件夹中')
    print('')
    wait==input('回车继续→')
    os.system('cls')


if RunCommand=='RUN':
    
    #界面优化
    MouseX, MouseY = pyautogui.position() #获取当前鼠标位置
    pyautogui.leftClick((screenWidth-20), (screenHeight-20))#点击界面
    pyautogui.moveTo(MouseX, MouseY) #移动鼠标至原先位置

    #模拟F11退出全屏
    win32api.keybd_event(122, 0, 0, 0)#按下按键
    win32api.keybd_event(122, 0, win32con.KEYEVENTF_KEYUP, 0)#施放按键
    time.sleep(0.1)
    
    #显示信息
    os.system('color 1f')
    print('\n【播放完成】\n')
    print('')
    print(' 程序作者：豆豆ZZYDD')
    url = ("https://space.bilibili.com/543085311")
    print(' 个人主页：', url)
    print('')
    wait = input(' 按回车键关闭程序→')
    time.sleep(0.1)


elif RunCommand=='STOP':
      
    #界面优化
    MouseX, MouseY = pyautogui.position() #获取当前鼠标位置
    pyautogui.leftClick((screenWidth-20), (screenHeight-20))#点击界面
    pyautogui.moveTo(MouseX, MouseY) #移动鼠标至原先位置

    #模拟F11退出全屏
    win32api.keybd_event(122, 0, 0, 0)#按下按键
    win32api.keybd_event(122, 0, win32con.KEYEVENTF_KEYUP, 0)#施放按键
    time.sleep(0.1)


    #显示信息
    os.system('color c')
    print('\n【播放失败】\n')
    print('【错误提示】'+StopCode)
    print('')
    print(' 程序作者：豆豆ZZYDD')
    url = ("https://space.bilibili.com/543085311")
    print(' 个人主页：', url)
    print('')
    wait = input(' 按回车键关闭程序→')
    time.sleep(0.1)















