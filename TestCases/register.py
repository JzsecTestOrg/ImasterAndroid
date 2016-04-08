# -*- coding: UTF-8 -*-
__author__ = 'xuwen'

import traceback, time
from Elements.cappElements import firstElements, mineElements, loginElements, registerElements
from CommonMethods import globalData, generateLog, Data, verCode, userStatus, dataBase, findToast, screenShot

def register_smoking(self, i):
    if(userStatus.isRegisterSuccess(Data.getNumber('register', 'register', 'phoneText', i))):
      dataBase.delete_cuser(Data.getNumber('register', 'register', 'phoneText', i))
    firstElements.personcenterButton(self).click()
    globalData.LOG += generateLog.format_log("点击进入个人中心")
    mineElements.loginentranceButton(self).click()
    globalData.LOG += generateLog.format_log("点击进入登录页面")
    loginElements.registerLink(self).click()
    globalData.LOG += generateLog.format_log("登录页面点击‘快速注册’")
    if(registerElements.registerPage(self)):
        globalData.LOG += generateLog.format_log("快速注册页面正确显示")
    #注册页面手机号验证
    try:
        registerElements.phoneText(self).clear()
        registerElements.phoneText(self).send_keys(Data.getNumber('register', 'register', 'phoneText', i))
        globalData.LOG += generateLog.format_log("输入注册手机号: " + Data.getNumber('register', 'register', 'phoneText', i))
    except Exception, e:
        globalData.LOG += generateLog.format_log("注册页面手机号输入框错误\n" + traceback.format_exc())

    #注册页面发送验证码验证
    try:
        registerElements.vercodeButton(self).click()
        globalData.LOG += generateLog.format_log("验证码发送中...")
        # if(findToast.find_toast(self, Data.getMessage('register', 'register', 'phoneText', i))):
        #     globalData.LOG += generateLog.format_log('提示正确：' + Data.getMessage('register', 'register', 'phoneText', i))
        # else:
        #     globalData.LOG += generateLog.format_log('提示错误')
        if(registerElements.vercodeButton(self).get_attribute('text') != '发送验证码'):
            globalData.LOG += generateLog.format_log('验证码发送过程发送验证码按钮文案显示正确')
        else:
            globalData.LOG += generateLog.format_log('验证码发送过程发送验证码按钮文案显示错误:' + registerElements.vercodeButton(self).get_attribute('text'))
        time.sleep(60)
        globalData.LOG += generateLog.format_log('等待60s')
        if(registerElements.vercodeButton(self).get_attribute('text') == '发送验证码'):
            globalData.LOG += generateLog.format_log('验证码发送完成60s后发送验证码按钮文案显示正确：发送验证码')
        else:
            globalData.LOG += generateLog.format_log('验证码发送完成60s后发送验证码按钮文案显示错误：' + registerElements.vercodeButton(self).get_attribute('text'))
        verCode.clear_vercode(Data.getNumber('register', 'register', 'phoneText', i))
        globalData.LOG += generateLog.format_log('清除redis验证码缓存')
        registerElements.vercodeButton(self).click()
        globalData.LOG += generateLog.format_log("验证码发送中...")
    except Exception, e:
        globalData.LOG += generateLog.format_log("按钮发送验证码识别错误\n" + traceback.format_exc())
    for i in range(0, 21):
        if(verCode.registersendVercode(Data.getNumber('register', 'register', 'phoneText', i)) != '0'):
            time.sleep(5)
        else:
            globalData.LOG += generateLog.format_log("验证码发送成功")
            break
    code = verCode.registerVercode(Data.getNumber('register', 'register', 'phoneText', i))
    try:
        registerElements.vercodeText(self).send_keys(code)
        globalData.LOG += generateLog.format_log("输入验证码: " + code)
    except Exception, e:
        globalData.LOG += generateLog.format_log("注册页面验证码输入框错误\n" + traceback.format_exc())


    try:
        registerElements.plainpasswordText(self).send_keys(Data.getValue('register', 'register', 'passwordText', 1))
        globalData.LOG += generateLog.format_log("输入注册密码: " + Data.getValue('register', 'register', 'passwordText', 1))
        if(registerElements.cipherpasswordText(self) != None):
            globalData.LOG += generateLog.format_log('密码显示正确：暗文')
        else:
            globalData.LOG += generateLog.format_log('密码显示错误：明文')
        registerElements.eyecloseButton(self).click()
        globalData.LOG += generateLog.format_log("切换密码为明文")
        if(registerElements.plainpasswordText(self) != None):
            globalData.LOG += generateLog.format_log('密码显示正确：明文')
        else:
            globalData.LOG += generateLog.format_log('密码显示错误：暗文')
        registerElements.eyeopenButton(self).click()
        globalData.LOG += generateLog.format_log("切换密码为暗文")
        if(registerElements.cipherpasswordText(self) != None):
            globalData.LOG += generateLog.format_log('密码显示正确：暗文')
        else:
            globalData.LOG += generateLog.format_log('密码显示错误：明文')
    except Exception, e:
        globalData.LOG += generateLog.format_log("注册页面密码错误\n" + traceback.format_exc())

    #注册昵称验证
    try:
        registerElements.nicknameText(self).send_keys(unicode(Data.getValue('register', 'register', 'nicknameText', 1), 'utf-8'))
        globalData.LOG += generateLog.format_log("输入昵称: " + Data.getValue('register', 'register', 'nicknameText', 1))
    except Exception, e:
        globalData.LOG += generateLog.format_log("注册页面昵称输入框错误\n" + traceback.format_exc())


    #阅读投资大师用户注册协议验证
    try:
        if(registerElements.protocolCheckbox(self).get_attribute('checked')):
            globalData.LOG += generateLog.format_log('《投资大师用户注册协议》默认勾选')
        else:
            globalData.LOG += generateLog.format_log('《投资大师用户注册协议》默认未勾选错误')
        registerElements.protocolCheckbox(self).click()
        globalData.LOG += generateLog.format_log("不勾选《投资大师用户注册协议》")
        registerElements.registerButton(self).click()
        globalData.LOG += generateLog.format_log("点击立即注册")
        # if(findToast.find_toast(self, Data.getMessage('register', 'register', 'registerButton', 1))):
        #     globalData.LOG += generateLog.format_log('提示正确：' + Data.getMessage('register', 'register', 'registerButton', 1))
        # else:
        #     globalData.LOG += generateLog.format_log('提示错误')
        registerElements.protocolCheckbox(self).click()
        globalData.LOG += generateLog.format_log("勾选《投资大师用户注册协议》")
        if(registerElements.protocolCheckbox(self).get_attribute('checked')):
            globalData.LOG += generateLog.format_log('《投资大师用户注册协议》已勾选')
        else:
            globalData.LOG += generateLog.format_log('《投资大师用户注册协议》未勾选错误')
        registerElements.protocolLink(self).click()
        globalData.LOG += generateLog.format_log('点击《投资大师用户注册协议》')
        if(registerElements.protocolPage(self)):
            globalData.LOG += generateLog.format_log('《投资大师用户注册协议》页面显示正确')
        else:
            globalData.LOG += generateLog.format_log('《投资大师用户注册协议》页面显示错误')
        if(registerElements.protocolText(self)):
            globalData.LOG += generateLog.format_log('《投资大师用户注册协议》内容显示正确')
        else:
            globalData.LOG += generateLog.format_log('《投资大师用户注册协议》内容显示错误')
    except Exception, e:
        globalData.LOG += generateLog.format_log("阅读《投资大师用户注册协议》错误\n" + traceback.format_exc())

    #注册页面注册按钮验证
    try:
        registerElements.registerButton(self).click()
        globalData.LOG += generateLog.format_log("点击注册按钮")
    except Exception, e:
        globalData.LOG += generateLog.format_log("注册页面注册按钮错误\n" + traceback.format_exc())

    #验证注册成功
    try:
        if(registerElements.registefinishPage(self)):
            globalData.LOG += generateLog.format_log('注册成功页面正确显示')
        else:
            globalData.LOG += generateLog.format_log('注册成功页面显示错误')
    except:
        globalData.LOG += generateLog.format_log('注册失败')

def register(self, i):
    #构造前置条件：注册过的手机号，未注册过的手机号
    if(Data.getPrecondition('register', i) == '注册过的手机号'):
        if(userStatus.isRegisterSuccess(Data.getTestdata('register', i, 2)) == False):
            dataBase.insert_cuser(Data.getTestdata('register', i, 2))
    else:
        if(userStatus.isRegisterSuccess(Data.getTestdata('register', i, 2)) == True):
            dataBase.delete_cuser(Data.getTestdata('register', i, 2))
    verCode.clear_vercode(Data.getTestdata('register', i, 2))
    #进入注册页面
    firstElements.personcenterButton(self).click()
    globalData.LOG += generateLog.format_log("点击进入个人中心")
    mineElements.loginentranceButton(self).click()
    globalData.LOG += generateLog.format_log("点击进入登录页面")
    loginElements.registerLink(self).click()
    globalData.LOG += generateLog.format_log("登录页面点击‘快速注册’")
    if(registerElements.registerPage(self)):
        globalData.LOG += generateLog.format_log("快速注册页面正确显示")
    #处理注册手机号逻辑
    registerElements.phoneText(self).clear()
    registerElements.phoneText(self).send_keys(Data.getTestdata('register', i, 2))
    #处理验证码逻辑
    if(Data.getTestdata('register', i, 3) == 'None'):
        registerElements.vercodeButton(self).click()
        globalData.LOG += generateLog.format_log('点击发送验证码')
        screenShot.get_screenshot(self, i)
        globalData.LOG += generateLog.format_log('不对验证码进行校验')
    elif(Data.getTestdata('register', i, 3) == 'Y'):
        registerElements.vercodeButton(self).click()
        globalData.LOG += generateLog.format_log("验证码发送中...")
        # for j in range(0, 50):
        #     if(verCode.registersendVercode(Data.getTestdata('register', i, 2)) != '0'):
        #         time.sleep(3)
        #     else:
        #         globalData.LOG += generateLog.format_log('验证码发送成功！')
        time.sleep(10)
        globalData.LOG += generateLog.format_log('验证码发送成功！')
        code = verCode.registerVercode(Data.getTestdata('register', i, 2))
        registerElements.vercodeText(self).send_keys(code)
        globalData.LOG += generateLog.format_log("输入验证码: " + code)
    elif(Data.getTestdata('register', i, 13) == '6位错误的验证码'):
        registerElements.vercodeButton(self).click()
        globalData.LOG += generateLog.format_log("验证码发送中...")
        # for i in range(0, 30):
        #     if(verCode.registersendVercode(Data.getTestdata('register', i, 2)) != '0'):
        #         time.sleep(3)
        #     else:
        #         globalData.LOG += generateLog.format_log('验证码发送成功！')
        time.sleep(10)
        globalData.LOG += generateLog.format_log('验证码发送成功！')
        code = '111111'
        registerElements.vercodeText(self).send_keys(code)
        globalData.LOG += generateLog.format_log("输入错误验证码: " + code)
    elif(Data.getTestdata('register', i, 13) == '6位过期的验证码'):
        registerElements.vercodeButton(self).click()
        globalData.LOG += generateLog.format_log("验证码发送中...")
        # for i in range(0, 30):
        #     if(verCode.registersendVercode(Data.getTestdata('register', i, 2)) != '0'):
        #         time.sleep(3)
        #     else:
        #         globalData.LOG += generateLog.format_log('验证码发送成功！')
        time.sleep(10)
        globalData.LOG += generateLog.format_log('验证码发送成功！')
        code = verCode.registerVercode(Data.getTestdata('register', i, 2))
        verCode.expireregisterVercode(Data.getTestdata('register', i, 2))
        registerElements.vercodeText(self).send_keys(code)
        globalData.LOG += generateLog.format_log("输入验证码: " + code)
    elif(Data.getTestdata('register', i, 13) == '使用过的验证码'):
        registerElements.phoneText(self).clear()
        registerElements.phoneText(self).send_keys(Data.getTestdata('register', 10, 2))
        globalData.LOG += generateLog.format_log('输入手机号：' + Data.getTestdata('register', 10, 2))
        registerElements.vercodeButton(self).click()
        globalData.LOG += generateLog.format_log("验证码发送中...")
        # for i in range(0, 30):
        #     if(verCode.registersendVercode(Data.getTestdata('register', 10, 2)) != '0'):
        #         time.sleep(3)
        #     else:
        #         globalData.LOG += generateLog.format_log('验证码发送成功！')
        time.sleep(10)
        globalData.LOG += generateLog.format_log('验证码发送成功！')
        code = verCode.registerVercode(Data.getTestdata('register', 10, 2))
        registerElements.vercodeText(self).send_keys(code)
        globalData.LOG += generateLog.format_log("输入验证码: " + code)
        registerElements.passwordText(self).send_keys(Data.getTestdata('register', 10, 4))
        globalData.LOG += generateLog.format_log('输入密码：' + Data.getTestdata('register', 10, 4))
        registerElements.nicknameText(self).send_keys(Data.getTestdata('register', 10, 6))
        globalData.LOG += generateLog.format_log('输入昵称：' + Data.getTestdata('register', 10, 6))
        registerElements.registerButton(self).click()
        globalData.LOG += generateLog.format_log('点击‘立即注册’')
        if(registerElements.registefinishPage(self)):
            globalData.LOG += generateLog.format_log('注册成功页面正确显示')
            registerElements.backButton(self).click()
            globalData.LOG += generateLog.format_log('点击返回按钮')
            mineElements.loginentranceButton(self).click()
            mineElements.logoutButton(self).click()
            globalData.LOG += generateLog.format_log('点击退出登录')
            mineElements.backButton(self).click()
            globalData.LOG += generateLog.format_log('返回到首页')
        dataBase.delete_cuser(Data.getTestdata('register', i, 2))
        verCode.expireregisterVercode(Data.getTestdata('register', i, 2))
        firstElements.personcenterButton(self).click()
        globalData.LOG += generateLog.format_log('点击首页个人中心入口')
        mineElements.loginentranceButton(self).click()
        globalData.LOG += generateLog.format_log('点击进入登录页面')
        loginElements.registerLink(self).click()
        globalData.LOG += generateLog.format_log('登录页面点击快速注册')
        registerElements.phoneText(self).clear()
        registerElements.phoneText(self).send_keys(Data.getTestdata('register', i, 2))
        globalData.LOG += generateLog.format_log('输入手机号：' + Data.getTestdata('register', i, 2))
        registerElements.vercodeText(self).send_keys(code)
        globalData.LOG += generateLog.format_log('输入已经用过的验证码：' + code)
    elif(Data.getTestdata('register', i, 13) == '超过60s重新触发发送验证码'):
        registerElements.vercodeButton(self).click()
        globalData.LOG += generateLog.format_log("验证码发送中...")
        if(registerElements.vercodeButton(self).get_attribute('text') != '发送验证码'):
            globalData.LOG += generateLog.format_log('验证码发送过程发送验证码按钮文案显示正确')
        else:
            globalData.LOG += generateLog.format_log('验证码发送过程发送验证码按钮文案显示错误:' + registerElements.vercodeButton(self).get_attribute('text'))
        time.sleep(60)
        globalData.LOG += generateLog.format_log('等待60s')
        if(registerElements.vercodeButton(self).get_attribute('text') == '发送验证码'):
            globalData.LOG += generateLog.format_log('验证码发送完成60s后发送验证码按钮文案显示正确：发送验证码')
        else:
            globalData.LOG += generateLog.format_log('验证码发送完成60s后发送验证码按钮文案显示错误：' + registerElements.vercodeButton(self).get_attribute('text'))
        verCode.clear_vercode(Data.getNumber('register', 'register', 'phoneText', i))
        globalData.LOG += generateLog.format_log('清除redis验证码缓存')
        registerElements.vercodeButton(self).click()
        globalData.LOG += generateLog.format_log("验证码发送中...")
        # for i in range(0, 30):
        #     if(verCode.registersendVercode(Data.getTestdata('register', i, 2)) != '0'):
        #         time.sleep(3)
        #     elif(len(verCode.registerVercode(Data.getTestdata('register', i, 2))) == 6):
        #         globalData.LOG += generateLog.format_log('验证码发送成功！')
        time.sleep(10)
        globalData.LOG += generateLog.format_log('验证码发送成功！')
    else:
        registerElements.vercodeText(self).send_keys(Data.getTestdata('register', i, 3))
        globalData.LOG += generateLog.format_log("输入验证码: " + Data.getTestdata('register', i, 3))

    #处理注册密码逻辑
    if(Data.getTestdata('register', i, 4) == 'None'):
        globalData.LOG += generateLog.format_log('不对密码进行校验')
    else:
        registerElements.passwordText(self).send_keys(Data.getTestdata('register', i, 4))
        globalData.LOG += generateLog.format_log('输入密码：' + Data.getTestdata('register', i, 4))

    #处理密码明暗文逻辑
    if(Data.getTestdata('register', i, 5) == 'None'):
        globalData.LOG += generateLog.format_log('不对密码明暗文进行校验')
    elif(Data.getTestdata('register', i, 5) == 'Y'):
        if(registerElements.cipherpasswordText(self) != None):
            globalData.LOG += generateLog.format_log('密码显示正确：暗文')
        else:
            globalData.LOG += generateLog.format_log('密码显示错误：明文')
        registerElements.eyeopenButton(self).click()
        globalData.LOG += generateLog.format_log("切换密码为明文")
        if(registerElements.plainpasswordText(self) != None):
            globalData.LOG += generateLog.format_log('密码显示正确：明文')
        else:
            globalData.LOG += generateLog.format_log('密码显示错误：暗文')
        registerElements.eyeopenButton(self).click()
        globalData.LOG += generateLog.format_log("切换密码为暗文")
        if(registerElements.cipherpasswordText(self) != None):
            globalData.LOG += generateLog.format_log('密码显示正确：暗文')
        else:
            globalData.LOG += generateLog.format_log('密码显示错误：明文')

    #处理昵称逻辑
    if(Data.getTestdata('register', i, 6) == 'None'):
        globalData.LOG += generateLog.format_log('不对昵称进行校验')
    else:
        registerElements.nicknameText(self).send_keys(Data.getTestdata('register', i, 6))
        globalData.LOG += generateLog.format_log("输入昵称: " + Data.getTestdata('register', i, 6))

    #处理投资大师注册协议勾选逻辑
    if(Data.getTestdata('register', i, 7) == 'None'):
        globalData.LOG += generateLog.format_log('不对投资大师注册协议勾选进行校验')
    elif(Data.getTestdata('register', i, 7) == 'Y'):
        if(registerElements.protocolCheckbox(self).get_attribute('checked')):
            globalData.LOG += generateLog.format_log('《投资大师用户注册协议》默认勾选')
        else:
            globalData.LOG += generateLog.format_log('《投资大师用户注册协议》默认未勾选错误')
        registerElements.protocolCheckbox(self).click()
        globalData.LOG += generateLog.format_log("不勾选《投资大师用户注册协议》")
        registerElements.protocolCheckbox(self).click()
        globalData.LOG += generateLog.format_log("勾选《投资大师用户注册协议》")
        if(registerElements.protocolCheckbox(self).get_attribute('checked')):
            globalData.LOG += generateLog.format_log('《投资大师用户注册协议》已勾选')
        else:
            globalData.LOG += generateLog.format_log('《投资大师用户注册协议》未勾选错误')
    else:
        if(registerElements.protocolCheckbox(self).get_attribute('checked')):
            globalData.LOG += generateLog.format_log('《投资大师用户注册协议》默认勾选')
        else:
            globalData.LOG += generateLog.format_log('《投资大师用户注册协议》默认未勾选错误')
        registerElements.protocolCheckbox(self).click()
        globalData.LOG += generateLog.format_log("不勾选《投资大师用户注册协议》")
        registerElements.protocolCheckbox(self).click()


    #处理投资大师注册协议内容逻辑
    if(Data.getTestdata('register', i, 8) == 'None'):
        globalData.LOG += generateLog.format_log('不对投资大师注册协议内容校验')
    elif(Data.getTestdata('register', i, 8) == 'Y'):
        registerElements.protocolLink(self).click()
        globalData.LOG += generateLog.format_log('点击《投资大师用户注册协议》')
        if(registerElements.protocolPage(self)):
            globalData.LOG += generateLog.format_log('《投资大师用户注册协议》页面显示正确')
        else:
            globalData.LOG += generateLog.format_log('《投资大师用户注册协议》页面显示错误')
        if(registerElements.protocolText(self)):
            globalData.LOG += generateLog.format_log('《投资大师用户注册协议》内容显示正确')
        else:
            globalData.LOG += generateLog.format_log('《投资大师用户注册协议》内容显示错误')
        registerElements.backButton(self).click()
        globalData.LOG += generateLog.format_log('返回注册页面')

    #处理点击注册按钮逻辑
    if(Data.getTestdata('register', i, 9) == 'None'):
        globalData.LOG += generateLog.format_log('不对点击注册进行校验')
        registerElements.backButton(self).click()
        globalData.LOG += generateLog.format_log('注册页面点击返回按钮')
        loginElements.backButton(self).click()
        globalData.LOG += generateLog.format_log('登录页面点击返回按钮')
        mineElements.backButton(self).click()
        globalData.LOG += generateLog.format_log('个人中心点击返回按钮')
    elif(Data.getTestdata('register', i, 9) == 'Y'):
        registerElements.registerButton(self).click()
        globalData.LOG += generateLog.format_log("点击注册按钮")
        if(Data.getTestdata('register', i, 11) == '1'):
            # if(findToast.find_toast(self, Data.getTestdata('register', i, 12))):
            #     globalData.LOG += generateLog.format_log('Toast提示正确：' + Data.getTestdata('register', i, 12))
            # else:
            #     globalData.LOG += generateLog.format_log('Toast提示错误')
            screenShot.get_screenshot(self, i)
            registerElements.backButton(self).click()
            globalData.LOG += generateLog.format_log('注册页面点击返回按钮')
            loginElements.backButton(self).click()
            globalData.LOG += generateLog.format_log('登录页面点击返回按钮')
            mineElements.backButton(self).click()
            globalData.LOG += generateLog.format_log('个人中心点击返回按钮')


    #处理注册成功校验逻辑
    if(Data.getTestdata('register', i, 10) == 'Y'):
        try:
            if(registerElements.registefinishPage(self)):
                globalData.LOG += generateLog.format_log('注册成功页面正确显示')
                registerElements.backButton(self).click()
                globalData.LOG += generateLog.format_log('点击返回按钮')
                mineElements.loginentranceButton(self).click()
                mineElements.logoutButton(self).click()
                globalData.LOG += generateLog.format_log('点击退出登录')
                mineElements.backButton(self).click()
                globalData.LOG += generateLog.format_log('返回到首页')
            else:
                globalData.LOG += generateLog.format_log('注册成功页面显示错误')
        except:
            globalData.LOG += generateLog.format_log('注册失败')
    elif(Data.getTestdata('register', i, 10) == 'None'):
        globalData.LOG += generateLog.format_log('不对注册成功逻辑进行校验')