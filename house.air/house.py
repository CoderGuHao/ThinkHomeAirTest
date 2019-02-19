# -*- encoding=utf8 -*-
# TAG = 6
__author__ = "lu201"

from airtest.core.api import *

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco()

# start_app('com.thinkhome.v3')
# sleep(5)

def accessToHouseSetting():
    poco("android:id/tabs").child("android.widget.RelativeLayout")[3].child("com.thinkhome.v3:id/tab_image").click()
    poco("com.thinkhome.v3:id/profile").click()

def editHouseName(name):
    poco("com.thinkhome.v3:id/name").set_text(name)
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    
def changeAccount(account,pwd):
    poco("android:id/tabs").child("android.widget.RelativeLayout")[3].child("com.thinkhome.v3:id/tab_image").click()
    poco.scroll(direction='vertical', percent=0.3, duration=1.0)
    poco(text="账号管理").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    poco("com.thinkhome.v3:id/toolbar_btn_setting").click()
    poco("com.thinkhome.v3:id/tv_welcome").click()
    poco("com.thinkhome.v3:id/et_account").set_text(account)
    poco("com.thinkhome.v3:id/et_password").set_text(pwd)
    poco("com.thinkhome.v3:id/btn_login").click()

def addHouse(name):
    poco("com.thinkhome.v3:id/house_name_edt").set_text(name)
    poco("com.thinkhome.v3:id/house_add_confirm_btn").click() 
    
def acceptInvite():
    #切换设备接受邀请
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    changeAccount("15558206037","123456")
    sleep(1)
    poco("com.thinkhome.v3:id/house_list").child("android.widget.RelativeLayout")[0].child("com.thinkhome.v3:id/image").click()
    sleep(2)
    if poco("android:id/parentPanel").exists:
        poco("android:id/button1").click()
        sleep(10)
    changeAccount("18158288412","4008002016")
    sleep(2)
    poco("com.thinkhome.v3:id/house_list").child("android.widget.RelativeLayout")[0].child("com.thinkhome.v3:id/image").click()
    sleep(10)
    # wait(Template(r"tpl1540570747227.png", record_pos=(0.0, -0.026), resolution=(1080, 1920)))
    # assert_exists(Template(r"tpl1540570747227.png", record_pos=(0.0, -0.026), resolution=(1080, 1920)), "接受邀请提示框验证")

    
#####################################################################################
#房屋名称修改：为空
try:
    accessToHouseSetting()
    poco(text="房屋名称").click()
    editHouseName("")
    snapshot(msg="房屋名称不能为空验证.")
except:
    print("Error: edit name failed!")
    
#房屋名称修改：为特殊字符&<>\'
try:
    editHouseName("&")
    resultScenario = poco("android:id/message").get_text()
    assert_equal(resultScenario, "数据包含特殊字符", "特殊字符&验证")
    poco("android:id/button3").click()
except:
    print("Error: edit name failed!")
    
try:
    editHouseName("<")
    resultScenario = poco("android:id/message").get_text()
    assert_equal(resultScenario, "数据包含特殊字符", "特殊字符<验证")
    poco("android:id/button3").click()
except:
    print("Error: edit name failed!")
    
try:
    editHouseName(">")
    resultScenario = poco("android:id/message").get_text()
    assert_equal(resultScenario, "数据包含特殊字符", "特殊字符>验证")
    poco("android:id/button3").click()
except:
    print("Error: edit name failed!")
    
try:
    editHouseName("\\")
    resultScenario = poco("android:id/message").get_text()
    assert_equal(resultScenario, "数据包含特殊字符", "特殊字符\验证")
    poco("android:id/button3").click()
except:
    print("Error: edit name failed!")

try:
    editHouseName("'")
    resultScenario = poco("android:id/message").get_text()
    assert_equal(resultScenario, "数据包含特殊字符", "特殊字符'验证")
    poco("android:id/button3").click()
except:
    print("Error: edit name failed!")

#房屋名称正确修改
try:
    editHouseName("名称修改")
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    realName = poco("com.thinkhome.v3:id/house_layout").child("com.thinkhome.v3:id/name").get_text()
    assert_equal(realName,"名称修改","房屋名称正确修改")
except:
    print("Error: edit name failed")
else:
    #房屋名称修改回旧值
    poco("com.thinkhome.v3:id/profile").click()
    poco(text="房屋名称").click()
    editHouseName("0正式")

#成员与权限
#成员邀请：访问通讯录
try:
    poco(text="成员与权限").click()
    sleep(2)
    poco("com.thinkhome.v3:id/toolbar_btn_setting").click()
    poco("com.thinkhome.v3:id/address_image").click()
    sleep(1)
    poco(text="自动化测试").click()
    resultScenario = poco("com.thinkhome.v3:id/user_account_edt").get_text()
    assert_equal(resultScenario, "15558206037", "访问通讯录验证")
except:
    print("Error!")
    
#邀请普通成员
try:
    poco("com.thinkhome.v3:id/user_account_edt").set_text("15558206037")
    poco("com.thinkhome.v3:id/initiate_invitation").click()
    sleep(1)
    message = poco("android:id/message").get_text()
    assert_equal(message,"邀请发送成功！","邀请普通成员")
except:
    print("Error!")
finally:
    poco("android:id/button3").click()
    
#切换账号接受邀请
try:
    acceptInvite()
    sleep(5)
    accessToHouseSetting()
    poco(text="成员与权限").click()
    sleep(2)
    poco(text="路飞").click()
    if poco("com.thinkhome.v3:id/upgrade_to_administrator").exists:
        result = "普通成员"
    else:
        result = "管理员"
    assert_equal(result,"普通成员","普通成员邀请并接受成功验证")
except:
    print("Change account to accept invite:Error!")    
    
#成员设置：升级为管理员
try:
    poco("com.thinkhome.v3:id/upgrade_to_administrator").click()
    poco("android:id/button1").click()
    poco(text="路飞").click()
    if poco("com.thinkhome.v3:id/remove_administrator_privileges").exists:
        result = "管理员"
    else:
        result = "普通成员"
    assert_equal(result,"管理员", "升级为管理员权限验证")
except:
    print("Update to admin: Error!")

#解除管理员权限
try:
    poco("com.thinkhome.v3:id/remove_administrator_privileges").click()
    poco("android:id/button1").click()
    poco(text="路飞").click()
    if poco("com.thinkhome.v3:id/upgrade_to_administrator").exists:
        result = "普通成员"
    else:
        result = "管理员"
    assert_equal(result,"普通成员","解除管理员权限验证")
except:
    print("Update to admin: Error!")
finally:
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    
#邀请成员：账号为自己
try:
    poco("com.thinkhome.v3:id/toolbar_btn_setting").click()
    poco("com.thinkhome.v3:id/user_account_edt").set_text("18158288412")
    poco("com.thinkhome.v3:id/initiate_invitation").click()
    resultScenario = poco("android:id/message").get_text()
    assert_equal(resultScenario, "输入的账号与当前账号相同，请更换一个账号", "邀请成员：账号为当前登录账号 验证")
except:
    print("Error!")
finally:
    poco("android:id/button3").click()
    
# 账号为已邀请
try:
    poco("com.thinkhome.v3:id/user_account_edt").set_text("15558206037")
    poco("com.thinkhome.v3:id/initiate_invitation").click()
    resultScenario = poco("android:id/message").get_text()
    assert_equal(resultScenario, "该用户已拥有权限或已邀请", "邀请成员：账号为已邀请 验证")
except:
    print("Error!")
finally:
    poco("android:id/button3").click()

# # 账号为空
# try:
#     poco("com.thinkhome.v3:id/user_account_edt").set_text("")
#     poco("com.thinkhome.v3:id/initiate_invitation").click()
#     resultScenario = poco("android:id/message").get_text()
#     assert_equal(resultScenario, "发起邀请", "邀请成员：账号为空验证")
# except:
#     print("Error!")
      
# #邀请成员：账号未注册
# try:
#     poco("com.thinkhome.v3:id/user_account_edt").set_text("13958310827")
#     poco("com.thinkhome.v3:id/initiate_invitation").click()
#     resultScenario = poco("android:id/message").get_text()
#     assert_equal(resultScenario, "该账号尚未注册", "邀请成员：账号尚未注册验证")
# except:
#     print("Error!")
# finally:
#     poco("android:id/button3").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    
#成员设置：房间权限设置
try:
    poco(text="路飞").click()
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
finally:
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
finally:
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
    poco("com.thinkhome.v3:id/remark").set_text("&")

    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    resultScenario = poco("android:id/message").get_text()
    assert_equal(resultScenario, "数据包含特殊字符", "成员设置：备注为特殊字符验证")
except:
    print("Error!")
finally:
    poco("android:id/button3").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()

#成员设置：删除
try:
    poco("com.thinkhome.v3:id/delete").click()
    poco("android:id/button1").click()
    sleep(2)
    resultScenario = poco(text="路飞").exists()
    assert_equal(resultScenario, False, "成员删除验证")
except:
    print("Member delete: Error!")
    
#邀请管理员
try:
    #邀请
    poco("com.thinkhome.v3:id/toolbar_btn_setting").click()
    poco("com.thinkhome.v3:id/user_account_edt").set_text("15558206037")
    poco(text="成员类型选择").click()
    poco(text="管理员").click()
    poco("android:id/button1").click()
    poco("com.thinkhome.v3:id/initiate_invitation").click()
    sleep(1)
    poco("android:id/button3").click()
    #切换账号接受邀请
    acceptInvite()
    sleep(5)
    accessToHouseSetting()
    poco(text="成员与权限").click()
    sleep(5)
    #验证
    poco(text="路飞").click()
    if poco("com.thinkhome.v3:id/remove_administrator_privilegeMinitouch").exists:
        resultScenario = "管理员"
    else:
        resultScenario = "普通成员"
    assert_equal(resultScenario, "管理员", "管理员邀请并接受成功验证")
except:
    print("Invite admin user: error!")
finally:
    poco("com.thinkhome.v3:id/delete").click()
    poco("android:id/button1").click()
    
#过户：账号为空
try:
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco(text="过户").click()
    poco("com.thinkhome.v3:id/btn_transfer_next").click()
    poco("com.thinkhome.v3:id/btn_transfer").click()
    resultScenario = poco("android:id/message").get_text()
    assert_equal(resultScenario, "接受方手机号不能为空", "过户账号为空验证")
except:
    print("Error!")
finally:
    poco("android:id/button3").click() 
    
#过户：账号格式错误
try:
    poco("com.thinkhome.v3:id/edit_transfer_account").set_text("12345678")
    poco("com.thinkhome.v3:id/btn_transfer").click()
    resultScenario = poco("android:id/message").get_text()
    assert_equal(resultScenario, "手机格式不正确", "过户账号格式错误验证")
except:
    print("Error!")
finally:
    poco("android:id/button3").click() 
        
#过户：验证码为空
try:
    poco("com.thinkhome.v3:id/edit_transfer_account").set_text("15558206037")
    poco("com.thinkhome.v3:id/btn_transfer").click()
    resultScenario = poco("android:id/message").get_text()
    assert_equal(resultScenario, "验证码不能为空", "过户：验证码为空验证")
except:
    print("Error!")
finally:
    poco("android:id/button3").click() 
    
#过户：验证码错误
try:
    poco("com.thinkhome.v3:id/edit_transfer_verify").set_text("1234")
    poco("com.thinkhome.v3:id/btn_transfer").click()
    resultScenario = poco("android:id/message").get_text()
    assert_equal(resultScenario, "验证码错误", "过户：输入错误验证码验证")
except:
    print("Error!")
finally:
    poco("android:id/button3").click() 
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    
#房屋添加：名称为空
try:
    poco("android:id/tabs").child("android.widget.RelativeLayout")[0].child("com.thinkhome.v3:id/tab_image").click()
    poco("com.thinkhome.v3:id/tv_currenthouse").click()
    poco("com.thinkhome.v3:id/toolbar_btn_setting").click()
    addHouse("")
    resultScenario = poco("android:id/message").get_text()
    assert_equal(resultScenario, "房屋名称不能为空", "添加房屋，名称为空验证")
except:
    print("Error!")
finally:
    poco("android:id/button3").click()

#房屋添加：名称包含特殊字符&\'<>
try:
    addHouse("&")
    resultScenario = poco("android:id/message").get_text()
    assert_equal(resultScenario, "数据包含特殊字符", "添加房屋，名称为特殊字符&验证") 
    poco("android:id/button3").click()
    sleep(2)
    
    addHouse("\\")
    resultScenario = poco("android:id/message").get_text()
    assert_equal(resultScenario, "数据包含特殊字符", "添加房屋，名称为特殊字符\验证") 
    poco("android:id/button3").click()
    sleep(2)
    
    addHouse("'")
    resultScenario = poco("android:id/message").get_text()
    assert_equal(resultScenario, "数据包含特殊字符", "添加房屋，名称为特殊字符'验证") 
    poco("android:id/button3").click()
    sleep(2)

    addHouse("<>")
    resultScenario = poco("android:id/message").get_text()
    assert_equal(resultScenario, "数据包含特殊字符", "添加房屋，名称为特殊字符<>验证") 
    poco("android:id/button3").click()
    sleep(2)
except:
    print("Error!")
    
#房屋添加：正确输入
try:
    addHouse("自动化测试房屋")
    sleep(10)
    poco("android:id/tabs").child("android.widget.RelativeLayout")[3].child("com.thinkhome.v3:id/tab_image").click()
    resultScenario = poco("com.thinkhome.v3:id/house_layout").child("com.thinkhome.v3:id/name").get_text()
    assert_equal(resultScenario, "自动化测试房屋", "新增房屋验证")
    sleep(2)
except:
    print("Error!")

#房屋切换
try:
    poco("android:id/tabs").child("android.widget.RelativeLayout")[0].child("com.thinkhome.v3:id/tab_image").click()
    poco("com.thinkhome.v3:id/tv_currenthouse").click()
    poco(text="0正式").click()
    sleep(10)
    resultScenario =  poco("com.thinkhome.v3:id/tv_currenthouse").get_text()
    assert_equal(resultScenario, "0正式", "房屋切换验证")
except:
    print("Error!")
    
#房屋删除
try:
    poco("com.thinkhome.v3:id/tv_currenthouse").click()
    deleteHouse = poco(text="自动化测试房屋").exists()
    #需要优化
    while not deleteHouse:
        poco.scroll(direction='vertical',percent=0.3,duration=1.0)
        sleep(1)
        deleteHouse = poco(text="自动化测试房屋").exists()
    poco(text="自动化测试房屋").click()
    sleep(8)
    poco("android:id/tabs").child("android.widget.RelativeLayout")[3].child("com.thinkhome.v3:id/tab_image").click()
    poco("com.thinkhome.v3:id/profile").click()
    poco("com.thinkhome.v3:id/delete").click()
    poco("android:id/button1").click()
    sleep(3)
    resultScenario = True
    for i in range(1,10):
        if  poco(text="自动化测试房屋").exists():
            resultScenario = False
            break
        else:
            poco.scroll(direction='vertical',percent=0.3,duration=1.0)
            sleep(2)
    assert_equal(resultScenario, False, "房屋删除成功")
    poco(text="0正式").click()
except:
    print("Delete house Error!")
