# -*- encoding=utf8 -*-
__author__ = "lu201"

from airtest.core.api import *

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco()

#start app
start_app('com.thinkhome.v3')

def accessToHouseSetting():
    poco("android:id/tabs").child("android.widget.RelativeLayout")[3].child("com.thinkhome.v3:id/tab_image").click()
    sleep(2)
    poco("com.thinkhome.v3:id/profile").click()

def editHouseName(name):
    poco("com.thinkhome.v3:id/name").click()
    poco("com.thinkhome.v3:id/name").set_text(name)
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    
def changeAccount(account,pwd):
    poco("android:id/tabs").child("android.widget.RelativeLayout")[3].child("com.thinkhome.v3:id/tab_image").click()
    poco(text="账号管理").click()
    sleep(1)
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    sleep(1)
    poco("com.thinkhome.v3:id/toolbar_btn_setting").click()
    sleep(1)
    poco("com.thinkhome.v3:id/tv_welcome").click()
    sleep(1)
    poco("com.thinkhome.v3:id/et_account").click()
    poco("com.thinkhome.v3:id/et_account").set_text(account)
    poco("com.thinkhome.v3:id/et_password").click()
    poco("com.thinkhome.v3:id/et_password").set_text(pwd)
    sleep(1)
    poco("com.thinkhome.v3:id/btn_login").click()

def addHouse(name):
    poco("com.thinkhome.v3:id/house_name_edt").click()
    poco("com.thinkhome.v3:id/house_name_edt").set_text(name)
    poco("com.thinkhome.v3:id/house_add_confirm_btn").click() 
    
def acceptInvite():
    #切换设备接受邀请
    #set_current("android://127.0.0.1:7555?cap_method=javacap&touch_method=adb")
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    changeAccount("15558206037","123456")
    sleep(2)
    poco("com.thinkhome.v3:id/house_list").child("android.widget.RelativeLayout")[0].child("com.thinkhome.v3:id/image").click()
    sleep(2)
    wait(Template(r"tpl1540570747227.png", record_pos=(0.0, -0.026), resolution=(1080, 1920)))
    assert_exists(Template(r"tpl1540570747227.png", record_pos=(0.0, -0.026), resolution=(1080, 1920)), "接受邀请提示框验证")

    poco("android:id/button1").click()
    sleep(5)
    changeAccount("18158288412","0123456")
    sleep(1)
    poco("com.thinkhome.v3:id/house_list").child("android.widget.RelativeLayout")[0].child("com.thinkhome.v3:id/image").click()
    sleep(2)

    
#####################################################################################
#房屋名称修改：为空
try:
    accessToHouseSetting()
    poco(text="0正式").click()
    sleep(1)
    editHouseName("")
    snapshot(msg="房屋名称不能为空验证.")
    sleep(2)
except:
    print("Error: edit name failed!")
    
#房屋名称修改：为特殊字符&<>\'
try:
    sleep(1)
    editHouseName("&")
    resultScenario = poco(text="数据包含特殊字符").get_text()
    assert_equal(resultScenario, "数据包含特殊字符", "特殊字符&验证")
    poco("android:id/button3").click()
except:
    print("Error: edit name failed!")
    
try:
    sleep(1)
    editHouseName("<>")
    resultScenario = poco(text="数据包含特殊字符").get_text()
    assert_equal(resultScenario, "数据包含特殊字符", "特殊字符<>验证")
    poco("android:id/button3").click()
except:
    print("Error: edit name failed!")
    
try:
    sleep(1)
    editHouseName("\\")
    resultScenario = poco(text="数据包含特殊字符").get_text()
    assert_equal(resultScenario, "数据包含特殊字符", "特殊字符\验证")
    poco("android:id/button3").click()
except:
    print("Error: edit name failed!")

try:
    sleep(1)
    editHouseName("'")
    resultScenario = poco(text="数据包含特殊字符").get_text()
    assert_equal(resultScenario, "数据包含特殊字符", "特殊字符'验证")
    poco("android:id/button3").click()
except:
    print("Error: edit name failed!")

#房屋名称正确修改
try:
    sleep(1)
    editHouseName("名称修改")
    sleep(5)
except:
    print("Error: edit name failed")
else:
    #房屋名称修改回旧值
    poco(text="名称修改").click()
    sleep(1)
    editHouseName("0正式")

#成员与权限
#成员邀请：访问通讯录
try:
    poco(text="成员与权限").click()
    sleep(2)
    poco("com.thinkhome.v3:id/toolbar_btn_setting").click()
    sleep(2)
    poco("com.thinkhome.v3:id/address_image").click()
    sleep(2)
    poco(text="自动化测试").click()
    resultScenario = poco(text="15558206037").get_text()
    assert_equal(resultScenario, "15558206037", "访问通讯录验证")
    sleep(2)
except:
    print("Error!")
    
#邀请普通成员
try:
    poco("com.thinkhome.v3:id/user_account_edt").set_text("15558206037")
    sleep(2)
    poco("com.thinkhome.v3:id/initiate_invitation").click()
    #resultScenario = poco(text="邀请发送成功").get_text()
    #sleep(1)
    #print("check value")
    #print(resultScenario)
    #assert_equal(resultScenario, "邀请发送成功", "邀请成功")
    sleep(3)
    poco("android:id/button3").click()
except:
    print("Error!")
    
#切换设备接受邀请
try:
    acceptInvite()
    accessToHouseSetting()
    poco(text="成员与权限").click()
    sleep(2)
    resultScenario = poco(text="普通成员").get_text()
    print(resultScenario)
    assert_equal(resultScenario, "普通成员", "普通成员邀请并接受成功验证")
    sleep(1)
except:
    print("Change account to accept invite:Error!")    
    
#成员设置：升级为管理员
try:
    poco("com.thinkhome.v3:id/value").click()
    sleep(2)
    poco("com.thinkhome.v3:id/upgrade_to_administrator").click()
    sleep(2)
    poco("android:id/button1").click()
    resultScenario = poco(text="管理员").get_text()
    assert_equal(resultScenario, "管理员", "升级为管理员权限验证")
    sleep(2)
except:
    print("Update to admin: Error!")
else:
    #解除管理员权限
    poco("com.thinkhome.v3:id/value").click()
    poco("com.thinkhome.v3:id/remove_administrator_privileges").click()
    poco("android:id/button1").click()
    resultScenario = poco(text="普通成员").get_text()
    assert_equal(resultScenario, "普通成员", "解除管理员权限验证")
    
#邀请成员：账号为自己
try:
    poco("com.thinkhome.v3:id/toolbar_btn_setting").click()
    poco("com.thinkhome.v3:id/user_account_edt").click()
    poco("com.thinkhome.v3:id/user_account_edt").set_text("18158288412")
    sleep(2)
    poco("com.thinkhome.v3:id/initiate_invitation").click()
    resultScenario = poco(text="输入的账号与当前账号相同，请更换一个账号").get_text()
    assert_equal(resultScenario, "输入的账号与当前账号相同，请更换一个账号", "邀请成员：账号为当前登录账号 验证")
    sleep(2)
    poco("android:id/button3").click()
except:
    print("Error!")
    
# 账号为已邀请
try:
    poco("com.thinkhome.v3:id/user_account_edt").click()
    poco("com.thinkhome.v3:id/user_account_edt").set_text("15558206037")
    sleep(2)
    poco("com.thinkhome.v3:id/initiate_invitation").click()
    resultScenario = poco(text="该用户已拥有权限或已邀请").get_text()
    assert_equal(resultScenario, "该用户已拥有权限或已邀请", "邀请成员：账号为已邀请 验证")
    sleep(2)
    poco("android:id/button3").click()
except:
    print("Error!")

# 账号为空
try:
    poco("com.thinkhome.v3:id/user_account_edt").click()
    poco("com.thinkhome.v3:id/user_account_edt").set_text("")
    sleep(2)
    poco("com.thinkhome.v3:id/initiate_invitation").click()
    resultScenario = poco(text="发起邀请").get_text()
    assert_equal(resultScenario, "发起邀请", "邀请成员：账号为空验证")
    sleep(2)
except:
    print("Error!")
    
    
#邀请成员：账号未注册
try:
    poco("com.thinkhome.v3:id/user_account_edt").click()
    poco("com.thinkhome.v3:id/user_account_edt").set_text("13958310827")
    sleep(2)
    poco("com.thinkhome.v3:id/initiate_invitation").click()
    sleep(1)
    resultScenario = poco(text="该账号尚未注册").get_text()
    assert_equal(resultScenario, "该账号尚未注册", "邀请成员：账号尚未注册验证")
    sleep(2)
    poco("android:id/button3").click()
    sleep(2)
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
except:
    print("Error!")
    
#成员设置：房间权限设置
try:
    poco("com.thinkhome.v3:id/value").click()
    poco(text="房间权限").click()
    sleep(2)
    poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[2].child("android.widget.LinearLayout")[1].child("com.thinkhome.v3:id/checkbox").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    sleep(3)
    poco(text="房间权限").click()
    snapshot(msg="房间权限设置验证.")
    sleep(2)
except:
    print("Error!")
else:
    #改回原值
    poco("com.thinkhome.v3:id/expand_listview").child("android.widget.RelativeLayout")[2].child("android.widget.LinearLayout")[1].child("com.thinkhome.v3:id/checkbox").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    
#成员设置：设备权限

try:
    poco(text="设备权限").click()
    poco("com.thinkhome.v3:id/listView").child("android.widget.RelativeLayout")[0].child("com.thinkhome.v3:id/tv_device_checked").click()
    poco("com.thinkhome.v3:id/listView").child("android.widget.RelativeLayout")[1].child("com.thinkhome.v3:id/tv_device_checked").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    sleep(3)
    poco(text="设备权限").click()
    snapshot(msg="邀请成员：设备权限验证")
    sleep(2)
except:
    print("Error!")
else:
    #改回原值
    poco("com.thinkhome.v3:id/listView").child("android.widget.RelativeLayout")[0].child("com.thinkhome.v3:id/tv_device_checked").click()
    poco("com.thinkhome.v3:id/listView").child("android.widget.RelativeLayout")[1].child("com.thinkhome.v3:id/tv_device_checked").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()

#成员设置:备注为空
try:
    poco(text="备注").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    snapshot(msg="成员设置：备注为空验证.")
except:
    print("Error!")

#成员设置：备注包含特殊字符
try:
    poco("com.thinkhome.v3:id/remark").click()
    poco("com.thinkhome.v3:id/remark").set_text("&")

    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    resultScenario = poco(text="数据包含特殊字符").get_text()
    assert_equal(resultScenario, "数据包含特殊字符", "成员设置：备注为特殊字符验证")
    sleep(2)
    poco("android:id/button3").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
except:
    print("Error!")

#成员设置：删除
try:
    poco("com.thinkhome.v3:id/delete").click()
    poco("android:id/button1").click()
    sleep(2)
    resultScenario = poco(text="路飞").exists()
    assert_equal(resultScenario, False, "成员删除验证")
    sleep(2)
    #返回成员设置
    #poco("com.thinkhome.v3:id/toolbar_btn_back").click()
except:
    print("Member delete: Error!")
    
#邀请管理员
try:
    #邀请
    poco("com.thinkhome.v3:id/toolbar_btn_setting").click()
    poco("com.thinkhome.v3:id/user_account_edt").click()
    poco("com.thinkhome.v3:id/user_account_edt").set_text("15558206037")
    poco(text="普通成员").click()
    poco(text="管理员").click()
    poco("android:id/button1").click()
    poco("com.thinkhome.v3:id/initiate_invitation").click()
    sleep(1)
    poco("android:id/button3").click()
    #切换账号接受邀请
    acceptInvite()
    accessToHouseSetting()
    poco(text="成员与权限").click()
    sleep(2)
    #验证
    resultScenario = poco(text="管理员").get_text()
    assert_equal(resultScenario, "管理员", "管理员邀请并接受成功验证")
except:
    print("Invite admin user: error!")
finally:
    if poco(text="路飞").exists():
        poco("com.thinkhome.v3:id/value").click()
        poco("com.thinkhome.v3:id/delete").click()
        poco("android:id/button1").click()
    
#过户：账号为空
try:
    poco(text="过户").click()
    poco("com.thinkhome.v3:id/btn_transfer_next").click()
    poco("com.thinkhome.v3:id/btn_transfer").click()
    resultScenario = poco(text="接受方手机号不能为空").get_text()
    assert_equal(resultScenario, "接受方手机号不能为空", "过户账号为空验证")
    poco("android:id/button3").click()  
    sleep(2)
except:
    print("Error!")
    
#过户：账号格式错误
try:
    poco("com.thinkhome.v3:id/edit_transfer_account").click()
    poco("com.thinkhome.v3:id/edit_transfer_account").set_text("12345678")
    poco("com.thinkhome.v3:id/btn_transfer").click()
    resultScenario = poco(text="手机格式不正确").get_text()
    assert_equal(resultScenario, "手机格式不正确", "过户账号格式错误验证")
    poco("android:id/button3").click()
    sleep(2)
except:
    print("Error!")
        
#过户：验证码为空
try:
    poco("com.thinkhome.v3:id/edit_transfer_account").click()
    poco("com.thinkhome.v3:id/edit_transfer_account").set_text("15558206037")
    poco("com.thinkhome.v3:id/btn_transfer").click()
    resultScenario = poco(text="验证码不能为空").get_text()
    assert_equal(resultScenario, "验证码不能为空", "过户：验证码为空验证")
    poco("android:id/button3").click()
    sleep(2)
except:
    print("Error!")

#过户：验证码错误
try:
    poco("com.thinkhome.v3:id/edit_transfer_account").click()
    poco("com.thinkhome.v3:id/edit_transfer_account").set_text("15558206037")
    poco("com.thinkhome.v3:id/edit_transfer_verify").click()
    poco("com.thinkhome.v3:id/edit_transfer_verify").set_text("1234")
    poco("com.thinkhome.v3:id/btn_transfer").click()
    resultScenario = poco(text="验证码错误").get_text()
    assert_equal(resultScenario, "验证码错误", "过户：输入错误验证码验证")
    sleep(2)
    poco("android:id/button3").click()
except:
    print("Error!")
finally:
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()

#房屋添加：名称为空
try:
    poco("android:id/tabs").child("android.widget.RelativeLayout")[0].child("com.thinkhome.v3:id/tab_image").click()
    poco("com.thinkhome.v3:id/tv_currenthouse").click()
    poco("com.thinkhome.v3:id/toolbar_btn_setting").click()
    addHouse("")
    resultScenario = poco(text="房屋名称不能为空").get_text()
    assert_equal(resultScenario, "房屋名称不能为空", "添加房屋，名称为空验证")
    poco("android:id/button3").click()
except:
    print("Error!")

#房屋添加：名称包含特殊字符&\'<>
try:
    addHouse("&")
    resultScenario = poco(text="数据包含特殊字符").get_text()
    assert_equal(resultScenario, "数据包含特殊字符", "添加房屋，名称为特殊字符&验证") 
    poco("android:id/button3").click()
    sleep(2)
    
    addHouse("\\")
    resultScenario = poco(text="数据包含特殊字符").get_text()
    assert_equal(resultScenario, "数据包含特殊字符", "添加房屋，名称为特殊字符\验证") 
    poco("android:id/button3").click()
    sleep(2)
    
    addHouse("'")
    resultScenario = poco(text="数据包含特殊字符").get_text()
    assert_equal(resultScenario, "数据包含特殊字符", "添加房屋，名称为特殊字符'验证") 
    poco("android:id/button3").click()
    sleep(2)

    addHouse("<>")
    resultScenario = poco(text="数据包含特殊字符").get_text()
    assert_equal(resultScenario, "数据包含特殊字符", "添加房屋，名称为特殊字符<>验证") 
    poco("android:id/button3").click()
    sleep(2)

except:
    print("Error!")
    
#房屋添加：正确输入
try:
    addHouse("自动化测试房屋")
    sleep(2)
    resultScenario = poco(text="自动化测试房屋").get_text()
    assert_equal(resultScenario, "自动化测试房屋", "新增房屋验证")
    sleep(2)
except:
    print("Error!")

#房屋切换
try:
    poco("com.thinkhome.v3:id/tv_currenthouse").click()
    poco(text="0正式").click()
    sleep(8)
    resultScenario =  poco("com.thinkhome.v3:id/tv_currenthouse").get_text()
    assert_equal(resultScenario, "0正式", "房屋切换验证")
except:
    print("Error!")
    
#房屋删除
try:
    poco("com.thinkhome.v3:id/tv_currenthouse").click()
    deleteHouse = poco(text="自动化测试房屋").exists()
    print (deleteHouse)
    while not deleteHouse:
        poco.scroll(direction='vertical',percent=0.3,duration=1.0)
        deleteHouse = poco(text="自动化测试房屋").exists()
    sleep(2)
    poco(text="自动化测试房屋").click()
    sleep(8)
    poco("android:id/tabs").child("android.widget.RelativeLayout")[3].child("com.thinkhome.v3:id/tab_image").click()
    sleep(2)
    poco(text="自动化测试房屋").click()
    sleep(1)
    poco("com.thinkhome.v3:id/delete").click()
    poco("android:id/button1").click()
    sleep(3)
    resultScenario = poco(text="自动化测试房屋").exists()
    assert_equal(resultScenario, False, "房屋删除成功")
    poco(text="0正式").click()
except:
    print("Delete house: Error!")





    
    
    
    
    
    
    
    
    
    
    