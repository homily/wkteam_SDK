import httpx
from pprint import pp
import time
class wxgj():
    
    def __init__(self,account,password):
        self.Account= account
        self.Password= password
        self.Host = 'http://xingshenapi.com'
        self.Authorization=None
        self.wcId=''
        self.wId=''
        self._sign_request()
    
    def _post(self,path,params):
        if(self.Authorization==None):
            headers=None
        else:
            headers={'Authorization':self.Authorization}
        return(httpx.post(path,headers=headers,json = params).json())

    def _sign_request(self):#登录微控平台(第一步)
        url = self.Host + '/member/login'
        payload = {'account':self.Account,'password':self.Password}
        sign=self._post(url,payload)
        if(sign['code']=='1000'):
            self.Authorization=sign['data']['Authorization']
        else:
            pp(sign)

    def iPadLogin(self):#获取微信二维码（第二步）
        url = self.Host + '/iPadLogin'
        payload = {'wcId':self.wcId,'type':2}
        iPadLoginInfo=self._post(url,payload)
        if(iPadLoginInfo['code']=='1000'):
            qrCodeUrl=iPadLoginInfo['data']['qrCodeUrl']
            self.wId=iPadLoginInfo['data']['wId']
            png=httpx.get(qrCodeUrl)
            from PIL import Image
            im = Image.open(png)
            im.show()
        else:
            pp(iPadLoginInfo)


    def secondLogin(self):#二次登录
        url = self.Host +'/secondLogin'
        payload = {'wcId':self.wcId,'type':2}
        iPadLoginInfo=self._post(url,payload)
        pp(iPadLoginInfo)

    def getIpadLoginInfo(self):#执行微信登录（第三步）
        url = self.Host +'/getIPadLoginInfo'
        payload = {'wId':self.wId}
        iPadLoginInfo=self._post(url,payload)
        pp(iPadLoginInfo)

    def getAllContace(self):#获取联系人列表(群、好友)
        url = self.Host + '/getAllContact'
        payload = {'wId':self.wId}
        AllContaceInfo=self._post(url,payload)
        #pp(AllContaceInfo)
        
        if(len(friend:=AllContaceInfo['data']['friend'])>0):
            for x in range(len(friend)):
                print(friend[x]['nickName'],friend[x]['userName'])
                
        if(len(group:=AllContaceInfo['data']['group'])>0): 
            for x in range(len(group)):
                print(group[x]['nickName'],group[x]['userName'])
        else:
            print('Group 0')

    def logout(self):# 登出
        url = self.Host + '/logout'
        payload = {'wId':self.wId}
        logoutInfo=self._post(url,payload)
        pp(logoutInfo)

    #====================================================================
    def setHttpCallbackUrl(self,httpUrl):#设置消息接收地址
        url = self.Host + '/setHttpCallbackUrl'
        payload = {'httpUrl':httpUrl}
        httpInfo=self._post(url,payload)
        pp(httpInfo)


    def cancelHttpCallbackUrl(self):#取消消息接收
        url = self.Host + '/cancelHttpCallbackUrl'
        payload =None
        httpInfo=self._post(url,payload)
        pp(httpInfo)


    #====================================================================
    def sendText(self,wcId,content,at=None):#发送文本消息
        url = self.Host + '/sendText'
        payload = {'wId':self.wId,'wcId':wcId,'content':content}
        print(payload)
        contentInfo=self._post(url,payload)
        pp(contentInfo)


    def sendImage(self,wcId,picUrl):#发送图片消息
        url = self.Host + '/sendImage'
        payload = {'wld':self.wId,'wcld':wcId,'content':picUrl}
        contentInfo=self._post(url,payload)
        pp(contentInfo)


    def sendVideo(self,wcId,videoUrl,thumbPath):#发送视频消息
        url = self.Host + '/sendVideo'
        payload = {'wld':self.wId,'wcld':wcId,'content':videoUrl,'thumbPath':thumbPath}#视频封面url链接，可自定义（也可自己服务器获取视频首帧）http://xxx.jpg
        contentInfo=self._post(url,payload)
        pp(contentInfo)

    def sendVoice(self,wcId,content,length):#发送语音
        url = self.Host + '/sendVoice'
        payload = {'wld':self.wId,'wcld':wcId,'content':content,'length':length}#silk格式https://xxx.silk
        contentInfo=self._post(url,payload)
        pp(contentInfo)

    def sendVoice(self,wcId,content,length):#发送语音
        url = self.Host + '/sendVoice'
        payload = {'wld':self.wId,'wcld':wcId,'content':content,'length':length}#silk格式https://xxx.silk
        contentInfo=self._post(url,payload)
        pp(contentInfo)

    #====================================================================
    def getCircle(self):#获取朋友圈
        url = self.Host +'/getCircle'
        payload = {'wId':self.wId,'statusId':0}
        Circle=self._post(url,payload)
        pp(Circle)

        
a=wxgj('135xxxxxxx','123456')
#a.iPadLogin()

