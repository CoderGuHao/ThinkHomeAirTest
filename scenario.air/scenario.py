# -*- encoding=utf8 -*-
__author__ = "lu201"

from airtest.core.api import *
from poco.exceptions import PocoNoSuchNodeException


auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
#poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
poco = AndroidUiautomationPoco()

#open APP
start_app('com.thinkhome.v3')

#open scenario list
def gotoScenario():
    poco("android:id/tabs").child("android.widget.RelativeLayout")[0].child("com.thinkhome.v3:id/tab_image").click()
    poco(text="场景").click()

def doInputPassword():
    poco("com.thinkhome.v3:id/et_password").click()
    text("1234")
    
#Add new scenario
def addScenario(ScenarioName,addMode):
    poco("com.thinkhome.v3:id/toolbar_btn_setting").click()
    
    if addMode == 0:
        poco(text="新增场景").click()
    elif addMode == 1:
        poco(text="根据当前自动生成").click()
    else:
        poco(text="取消").click()
        
    poco("com.thinkhome.v3:id/tv_name_value").click()
    sleep(1)
    poco("com.thinkhome.v3:id/tv_name_value").set_text(ScenarioName)
    sleep(2)
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    sleep(5)
    try:
        if poco(text="密码").exists():
            doInputPassword()
    except:
        print("No passowrd find")        

def exitAddScenario():
    poco("android:id/button3").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    

def gotoSceneSetting(scenarioName):
    #gotoScenario()
    #Find the scenario need to delete
    isNameExists=poco(text=scenarioName).exists()
    while not isNameExists :
        isNameExists=poco(text=scenarioName).exists()
        poco.scroll(direction='vertical',percent=0.3,duration=1.0)
        #snapshot()
    poco(text=scenarioName).long_click()
    poco(text="更多设置").click()
    
def deleteNewScenario(scenarioName):
    gotoSceneSetting(scenarioName)
    poco("com.thinkhome.v3:id/btn_delete").click()
    poco("android:id/button1").click()
    if poco(text="密码").exists():
        doInputPassword()   
        
#进入场景设置        
def gotoSceneNameChange():
    poco("com.thinkhome.v3:id/tv_name").click()
    poco(text="回家").click()
    
#场景名称修改
def doNameChange(scenarioName):
    poco("com.thinkhome.v3:id/tv_name").click()
    poco("com.thinkhome.v3:id/tv_name").set_text(scenarioName)
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    
gotoScenario()

#新增场景：正确添加
try:
    addScenario("新增测试场景",0)
    print("*"*10)
    sleep(3)
    newScenarioResult = poco(text="新增测试场景").exists()
    print (newScenarioResult)
    while not newScenarioResult:
        poco.scroll(direction='vertical',percent=0.3,duration=1.0)
        newScenarioResult = poco(text="新增测试场景").exists()
        #snapshot() 
    resultScenario = poco(text="新增测试场景").get_text()
    assert_equal(resultScenario, "新增测试场景", "正确新增场景.")
except:
    print("Add scenario with correct value: Error!")
else:
    deleteNewScenario("新增测试场景")
    sleep(5)

#新增场景：名称为空
try:
    addScenario("",0) 
    resultScenario = poco(text="场景名称不能为空").get_text()
    assert_equal(resultScenario, "场景名称不能为空", "名称为空验证.")
    sleep(2)
    exitAddScenario()
except:
    print("Add scenario with empty value: Error!")
    
#新增场景: 名称包含特殊字符 '<>&\
try:
    addScenario("&",0)
    resultScenario = poco(text="数据包含特殊字符").get_text()
    assert_equal(resultScenario, "数据包含特殊字符", "特殊字符&验证.")
    exitAddScenario()
except:
    print("Add scenario with & value: Error!")

#Verify: <>
try:
    addScenario("<>",0)
    resultScenario = poco(text="数据包含特殊字符").get_text()
    assert_equal(resultScenario, "数据包含特殊字符", "特殊字符<>验证.")
    exitAddScenario()
except:
    print("Add scenario with <> value: Error!")

#Verify:'
try:
    addScenario("'",0)
    resultScenario = poco(text="数据包含特殊字符").get_text()
    assert_equal(resultScenario, "数据包含特殊字符", "特殊字符'验证.")
    exitAddScenario()
except:
    print("Add scenario with ' value: Error!")
    
#Verify:\
try:
    addScenario("\\",0)
    resultScenario = poco(text="数据包含特殊字符").get_text()
    assert_equal(resultScenario, "数据包含特殊字符", "特殊字符\验证.")
    exitAddScenario()
except:
    print("Add scenario with \ value: Error!")
    
#根据当前自动生成:名称为空
try:
    addScenario("",1)    
    resultScenario = poco(text="场景名称不能为空").get_text()
    assert_equal(resultScenario, "场景名称不能为空", "根据当前自动生成 名称为空验证.")
    sleep(2)
    exitAddScenario()
except:
    print("Generate scenario with empty name: Error!")

#根据当前自动生成:正确新增
try:
    addScenario("自动生成",1)
    isExitAutoGenerate=poco(text="自动生成").exists()
    while not isExitAutoGenerate:
        poco.scroll(direction='vertical',percent=0.3,duration=1.0)
        isExitAutoGenerate=poco(text="自动生成").exists()
        #snapshot()
    resultScenario = poco(text="自动生成").get_text()
    assert_equal(resultScenario, "自动生成", "根据当前自动生成：正确新增验证.") 
except:
    print("Generate scenario: Error!")

try:
    #场景删除
    deleteNewScenario("自动生成")
    sleep(5)
    resultScenario = poco(text="自动生成").exists()
    assert_equal(resultScenario, False, "场景删除验证.") 
except:
    print("Delete scenario: Error!")
    
#场景设置：修改类型
try:
    addScenario("新增测试场景",0)
    gotoSceneSetting("新增测试场景")
    gotoSceneNameChange()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    snapshot(msg="场景设置：修改类型验证.")
    sleep(2)
except:
    print("Change scenario type: Error!")

#场景设置：修改图标-拍照
try:
    gotoSceneNameChange()
    poco("com.thinkhome.v3:id/img_photo").click()
    sleep(10)
    poco(text="拍照").click()
    poco("com.huawei.camera:id/shutter_button").click()
    sleep(2)
    poco("com.huawei.camera:id/btn_done").click()
    poco("com.thinkhome.v3:id/btn_crop").click()
    snapshot(msg="修改图标：拍照.")
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
except:
    print("Edit scenario image by camera:Error!")
    
#场景设置：修改图标-从相册选择
try:
    gotoSceneNameChange()
    poco("com.thinkhome.v3:id/img_photo").click()
    poco(text="从相册选择").click()
    poco("com.android.documentsui:id/grid").child("android.widget.FrameLayout")[1].child("com.android.documentsui:id/icon_thumb").click()
    poco("com.android.documentsui:id/grid").child("android.widget.FrameLayout")[3].child("com.android.documentsui:id/icon_thumb").click()
    poco("com.thinkhome.v3:id/btn_crop").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    snapshot(msg="场景设置：修改图标，从相册选择 验证.")
except:
    print("Edit scenario image from album: Error!")
    
#场景设置：修改图标-使用默认图标
try:
    gotoSceneNameChange()
    poco("com.thinkhome.v3:id/img_icon").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    snapshot(msg="场景设置：修改图标-使用默认图标 验证.")
except:
    print("Edit scenario image with default: Error!")
    
#场景设置：修改名称，为空
try:
    gotoSceneNameChange()
    doNameChange("")
    resultScenario = poco(text="名称不能为空").get_text()
    assert_equal(resultScenario, "名称不能为空", "场景名称为空 验证.") 
    poco("android:id/button3").click()
except:
    print("Edit scenario name with empty value:Error!")
    
#场景设置：修改名称，特殊字符
try:
    doNameChange("&")
    resultScenario = poco(text="数据包含特殊字符").get_text()
    assert_equal(resultScenario, "数据包含特殊字符", "场景名称为特殊字符& 验证.") 
    poco("android:id/button3").click()
except:
    print("Edit scenario name with & value: Error!")
    
#'
try:
    doNameChange("'")
    resultScenario = poco(text="数据包含特殊字符").get_text()
    assert_equal(resultScenario, "数据包含特殊字符", "场景名称为特殊字符' 验证.") 
    poco("android:id/button3").click()
except:
    print("Edit scenario name with ' value:Error!")
    
#\
try:
    doNameChange("\\")
    resultScenario = poco(text="数据包含特殊字符").get_text()
    assert_equal(resultScenario, "数据包含特殊字符", "场景名称为特殊字符\ 验证.")
    poco("android:id/button3").click()
except:
    print("Edit scenario name with \ value:Error!")

#<>
try:
    doNameChange("<>")
    resultScenario = poco(text="数据包含特殊字符").get_text()
    assert_equal(resultScenario, "数据包含特殊字符", "场景名称为特殊字符<> 验证.")
    poco("android:id/button3").click()
except:
    print("Edit scenario name with <> value:Error!")

#场景设置：修改名称，正确输入
try:
    doNameChange("自动化修改")
    resultScenario = poco(text="自动化修改").get_text()
    assert_equal(resultScenario, "自动化修改", "场景设置：修改名称 正确输入 验证.")
except:
    print("Edit scenario name with correct value:Error!")

#添加定时
try:
    poco(text="定时").click()
    sleep(5)
    poco("com.thinkhome.v3:id/toolbar_btn_setting").click()
    poco("com.thinkhome.v3:id/open_checkbox").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    sleep(5)
    resultScenario = poco(text="至少选择一个时间").get_text()
    assert_equal(resultScenario, "至少选择一个时间", "定时：没有选择任何定时 验证.")
    sleep(2)
    poco("android:id/button3").click()
except:
    print("Add timer without chosen: Error!")
else:
    #定时：正确添加
    poco("com.thinkhome.v3:id/open_checkbox").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    resultScenario = poco(text="执行").get_text()
    assert_equal(resultScenario, "执行", "定时正确添加 验证.")
finally:
    print("Execute finally")

    
#修改定时：修改时间
try:
    poco("com.thinkhome.v3:id/tv_open").click()
    poco("com.thinkhome.v3:id/checkbox_monday").click()
    poco("com.thinkhome.v3:id/checkbox_tuesday").click()
    poco("com.thinkhome.v3:id/checkbox_wednesday").click()
    poco("com.thinkhome.v3:id/checkbox_thursday").click()
    poco("com.thinkhome.v3:id/checkbox_friday").click()
    poco("com.thinkhome.v3:id/open_time").click()
    poco("14").swipe([-0.2305, -0.0298])
    poco("5").swipe([-0.1184, 0.2558])

    poco("android:id/button1").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    resultScenario = poco(text="23:30").get_text()
    assert_equal(resultScenario, "23:30", "修改定时：修改时间 验证.")
    
except:
    print("Change timer: Error!")  
else:
    #定时：日期验证
    resultScenario = poco(text="工作日").get_text()
    assert_equal(resultScenario, "工作日", "日期 验证.")
finally:
    print("Execute finally")
        
#定时：选择普通定时或日出日落定时
try:
    poco("com.thinkhome.v3:id/tv_open").click()
    poco("com.thinkhome.v3:id/radio_on_sunsets").click()
    poco("com.thinkhome.v3:id/sunset_checkbox_on").click()
    poco("com.thinkhome.v3:id/checkbox_single").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    resultScenario = poco(text="16:57").get_text()
    assert_equal(resultScenario, "16:57", "日期 验证.")
    sleep(2)
except:
    print("Change sunsets or sunraise: Error!")

#定时停启用
try:
    poco("com.thinkhome.v3:id/switch_view").click()
    snapshot(msg="定时启用验证.")
    sleep(2)
except:
    print("Error!")
else:
    poco("com.thinkhome.v3:id/switch_view").click()
    snapshot(msg="定时停用验证.")

#删除定时
try:
    poco("com.thinkhome.v3:id/tv_open").long_click()
    poco(text="删除").click()
    sleep(2)
    resultScenario = poco(text="执行").exists()
    assert_equal(resultScenario, False, "删除定时 验证.")
except:
    print("Delete timer: Error!")

#设备组合，不选择设备添加
try:
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco(text="设备组合").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    sleep(2)
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    sleep(3)
    resultScenario = poco(text="您至少需要选择一个设备").get_text()
    assert_equal(resultScenario, "您至少需要选择一个设备", "设备组合，不选择设备添加.")
    sleep(2)

    poco("android:id/button1").click()
    sleep(2)

except:
    print("Error!")
else:
    #正确添加设备
    #poco(text="网页版App勿删").click()
    poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[1].child("com.thinkhome.v3:id/checkbox").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    sleep(2)
    resultScenario = poco(text="灯光").get_text()
    assert_equal(resultScenario, "灯光", "设备组合，正确添加验证.")
    
#设备组合：删除
try:
    poco("com.thinkhome.v3:id/listView").child("com.thinkhome.v3:id/item_layout")[0].child("com.thinkhome.v3:id/item").child("com.thinkhome.v3:id/ll_title").child("com.thinkhome.v3:id/tv_name").long_click()
    poco(text="删除").click()
    sleep(2)
    resultScenario = poco(text="灯光").exists()
    assert_equal(resultScenario, False, "设备组合，删除 验证.")
    sleep(2)
except:
    print("Error!")
finally:
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()

#联动组合：不选择联动添加
try:
    poco(text="联动组合").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    resultScenario = poco(text="您至少需要选择一个联动").get_text()
    assert_equal(resultScenario, "您至少需要选择一个联动", "联动组合：不选择联动添加 验证.")
    sleep(2)
    poco("android:id/button3").click()
except:
    print("Error!")
else:
    #正确添加
    addLinkageCombination = poco("com.thinkhome.v3:id/tv_device_text").get_text()
    poco("com.thinkhome.v3:id/xlistView").child("android.widget.RelativeLayout")[0].child("com.thinkhome.v3:id/tv_device_checked").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    resultScenario = poco("com.thinkhome.v3:id/tv_name").get_text()
    assert_equal(resultScenario, addLinkageCombination, "联动组合正确添加验证.")
    sleep(2)
    #修改联动动作
    poco("com.thinkhome.v3:id/tv_action").click()
    poco(text="启用").click()
    poco("android:id/button1").click()
    resultScenario = poco(text="启用").get_text()
    assert_equal(resultScenario, "启用", "联动组合：修改动作验证.")
    sleep(2)
    #联动组合：删除
    poco("com.thinkhome.v3:id/img_icon").long_click()
    poco(text="删除").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()

#分享：正确云子分享
try:
    poco(text="分享").click()
    poco("com.thinkhome.v3:id/name").click()
    poco("com.thinkhome.v3:id/tv_device").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    resultScenario = poco(text="1").get_text()
    assert_equal(resultScenario, "1", "云子正确分享.")
except:
    print("Error!")
else:
    #取消分享
    poco("com.thinkhome.v3:id/name").click()
    poco("com.thinkhome.v3:id/tv_device").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    resultScenario = poco(text="0").get_text()
    assert_equal(resultScenario, "0", "云子取消分享.")
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()

#开关绑定：
#查看说明
try:
    poco(text="开关绑定").click() 
    poco("com.thinkhome.v3:id/help").click()
    sleep(2)
    resultScenario = poco(text="开关绑定说明").get_text()
    assert_equal(resultScenario, "开关绑定说明", "开关绑定：查看说明.")
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
except:
    print("Error!")

#场景隐藏
try:
    poco(text="场景隐藏").click()
    poco(text="隐藏").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    resultScenario = poco(text="已隐藏").get_text()
    assert_equal(resultScenario, "已隐藏", "场景隐藏.")
except:
    print("Error!")
else:
    #场景取消隐藏
    poco(text="场景隐藏").click()
    poco(text="正常显示").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    resultScenario = poco(text="正常显示").get_text()
    assert_equal(resultScenario, "正常显示", "场景 正常显示.")
    
#日志
try:
    poco(text="日志").click()
    snapshot(msg="日志查看页面.")
except:
    print("Error!")  
finally:
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco("com.thinkhome.v3:id/btn_back").click()
    
 #本地场景：正确新增
try:
    poco("android:id/tabs").child("android.widget.RelativeLayout")[3].child("com.thinkhome.v3:id/tab_image").click()
    sleep(2)
    poco(text="设备管理").click()
    sleep(2)
    isExitAutoGenerate=poco(text="P8Pro").exists()
    while not isExitAutoGenerate:
        poco.scroll(direction='vertical',percent=0.3,duration=1.0)
        isExitAutoGenerate=poco(text="P8Pro").exists()
        
    poco(text="P8Pro").click()
    sleep(2)
    poco("com.thinkhome.v3:id/toolbar_btn_setting").click()
    sleep(2)
    poco(text="本地场景").click()
    sleep(2)
    poco("com.thinkhome.v3:id/toolbar_btn_setting").click()
    poco("com.thinkhome.v3:id/tv_name_value").click()
    poco("com.thinkhome.v3:id/tv_name_value").set_text("本地场景测试")
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    resultScenario = poco(text="本地场景测试").get_text()
    assert_equal(resultScenario, "本地场景测试", "本地场景 正确新增.")
except:
    print("Error!")    
    
#本地场景：修改类型和名称
try:
    poco("com.thinkhome.v3:id/tv_device").long_click()
    poco(text="更多设置").click()
    poco("com.thinkhome.v3:id/tv_name").click()
    poco("com.thinkhome.v3:id/listView").child("android.widget.RelativeLayout")[2].child("com.thinkhome.v3:id/tv_device_checked").click()
    poco("com.thinkhome.v3:id/tv_name").click()
    poco("com.thinkhome.v3:id/tv_name").set_text("本地场景修改")
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    sleep(2)
    snapshot(msg="本地场景类型修改图标 验证.")
    resultScenario = poco(text="本地场景修改").get_text()
    assert_equal(resultScenario, "本地场景修改", "本地场景名修改 验证.")
except:
    print("Error!")

#本地场景：设备组合
try:
    poco(text="设备组合").click()
    sleep(2)
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    addLinkageCombination = poco("com.thinkhome.v3:id/tv_device_text").get_text()
    poco("com.thinkhome.v3:id/listview").child("android.widget.RelativeLayout")[0].child("com.thinkhome.v3:id/tv_device_checked").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    sleep(2)
    resultScenario = poco("com.thinkhome.v3:id/tv_name").get_text()
    assert_equal(resultScenario, "灯光", "本地场景：设备组合 验证")
    sleep(3)
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
except:
    print("Error!")
    
#本地场景：固化
try:
    poco(text="本地场景固化").click()
    poco("com.thinkhome.v3:id/btn_add_local_scene").click()
    sleep(5)
    snapshot(msg="截图：本地场景固化验证.")
    poco("com.thinkhome.v3:id/btn_confirm").click()
    #重新进入页面验证是否固化成功
    poco(text="本地场景固化").click()
    resultScenario = poco(text="当前场景已固化").exists()
    assert_equal(resultScenario, "当前场景已固化", "本地场景删除验证.")
    #返回
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
except:
    print("Error!") 
    poco("android:id/button3").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()

 #本地场景：删除
try:
    poco("com.thinkhome.v3:id/btn_delete").click()
    poco("android:id/button1").click()
    resultScenario = poco(text="本地场景修改").exists()
    assert_equal(resultScenario, False, "本地场景删除验证.")
except:
    print("Error!")
finally:
    #回到首页
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco("android:id/tabs").child("android.widget.RelativeLayout")[0].child("com.thinkhome.v3:id/tab_image").click()

#场景控制：5秒内连续操作
try:
    poco(text="场景").click()
    poco(text="本地场景修改").click()
    poco("com.thinkhome.v3:id/switch_button").click()
    poco("com.thinkhome.v3:id/switch_button").click()
    resultScenario = poco(text="场景操作过于频繁，同一场景连续两次操作时间间隔至少为5s").get_text()
    assert_equal(resultScenario, "场景操作过于频繁，同一场景连续两次操作时间间隔至少为5s", "5秒内连续操作验证.")
    poco("android:id/button3").click()
    poco("com.thinkhome.v3:id/btn_back").click()
except:
    print("Error!")
    
#全部场景控制
try:
    #打开调光
    poco("android:id/tabs").child("android.widget.RelativeLayout")[2].child("com.thinkhome.v3:id/tab_image").click()
    poco(text="灯光").click()
    poco("com.thinkhome.v3:id/scroll").child("android.widget.RelativeLayout")[1].child("com.thinkhome.v3:id/tv_status").click()
    poco("com.thinkhome.v3:id/scroll").child("android.widget.RelativeLayout")[3].child("com.thinkhome.v3:id/tv_status").click()
    poco("com.thinkhome.v3:id/scroll").child("android.widget.RelativeLayout")[4].child("com.thinkhome.v3:id/tv_status").click()
    poco("com.thinkhome.v3:id/scroll").child("android.widget.RelativeLayout")[5].child("com.thinkhome.v3:id/tv_status").click()
    poco("com.thinkhome.v3:id/scroll").child("android.widget.RelativeLayout")[6].child("com.thinkhome.v3:id/tv_status").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco("android:id/tabs").child("android.widget.RelativeLayout")[0].child("com.thinkhome.v3:id/tab_image").click()
    #全部控制
    poco(text="全部调光").click()
    poco("com.thinkhome.v3:id/seek_bar").swipe([-0.0031, 0.6501])
    poco("com.thinkhome.v3:id/btn_back").click()
    
except:
    print("Error!")
else:
    poco("android:id/tabs").child("android.widget.RelativeLayout")[2].child("com.thinkhome.v3:id/tab_image").click()
    poco(text="灯光").click()
    snapshot(msg="场景控制验证.")
        












