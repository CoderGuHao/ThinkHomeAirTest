# -*- encoding=utf8 -*-
# TAG = 2
__author__ = "guhao"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco()

auto_setup(__file__)

# start_app("com.thinkhome.v3")
# sleep(5)


def login(account, password):
    poco("com.thinkhome.v3:id/et_account").set_text(account)
    poco("com.thinkhome.v3:id/et_password").set_text(password)
    poco("com.thinkhome.v3:id/btn_login").click()


def modify_name(name):
    poco("com.thinkhome.v3:id/name").set_text(name)
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco("com.thinkhome.v3:id/et_password").exists():
        doInputPassword()


def modify_email(email):
    poco("com.thinkhome.v3:id/name").set_text(email)
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco("com.thinkhome.v3:id/et_password").exists():
        doInputPassword()


def modify_password(old_password, new_password, confirm_password):
    poco("com.thinkhome.v3:id/edit_pwd_old").set_text(old_password)
    poco("com.thinkhome.v3:id/edit_pwd_new").set_text(new_password)
    poco("com.thinkhome.v3:id/edit_pwd_new_confirm").set_text(confirm_password)
    poco("com.thinkhome.v3:id/btn_modify").click()
    if poco("com.thinkhome.v3:id/et_password").exists():
        doInputPassword()
    
    
def change_account(account, password):
    poco("android:id/tabs").child("android.widget.RelativeLayout")[3].child("com.thinkhome.v3:id/tab_image").click()
    poco.scroll(direction='vertical', percent=0.3, duration=1.0)
    poco(text="账号管理").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    poco("com.thinkhome.v3:id/toolbar_btn_setting").click()
    poco("com.thinkhome.v3:id/tv_welcome").click()
    login(account, password)
    
def change_house(house_name):
    poco("com.thinkhome.v3:id/btn_search").click()
    poco("com.thinkhome.v3:id/edt_search").set_text(house_name)
    poco("com.thinkhome.v3:id/rv_result").click()


# 登录并进入账号管理
try:
    poco("com.thinkhome.v3:id/tv_welcome").click()
    login("18368493627", "123456")
    sleep(5)
    if poco("com.thinkhome.v3:id/house_list").exists():
        poco("com.thinkhome.v3:id/house_list").child("android.widget.RelativeLayout")[0].click()
        sleep(10)
    poco(text="设置").click()
    poco.scroll(direction='vertical', percent=0.3, duration=1.0)
    poco(text="账号管理").click()
except BaseException:
    print("Error:登录并进入账号管理")

'''
# 拍照
poco("com.thinkhome.v3:id/image_layout").click()
poco(text="拍照").click()
poco("com.huawei.camera:id/shutter_button").click()#考虑用图像识别
poco("com.huawei.camera:id/btn_done").click()#考虑用图像识别
poco("com.android.gallery3d:id/head_select_right").click()
try:
    assert_exists(Template(r"tpl1533883870891.png", record_pos=(0.001, 0.528), resolution=(1080, 1920)), "拍照修改头像成功")
except:
    print("error")
else:
    print("pass")

# 选择本地图片
poco("com.thinkhome.v3:id/image_layout").click()
poco(text="选择本地图片").click()
poco(text="最近").click()
poco("com.android.documentsui:id/grid").child("android.widget.FrameLayout")[0].child("android.widget.LinearLayout").child("com.android.documentsui:id/icon_mime").click()
poco("com.android.documentsui:id/icon_mime").click()
poco("com.android.gallery3d:id/head_select_right").click()
try:
    assert_exists(Template(r"tpl1533883908278.png", record_pos=(0.002, 0.532), resolution=(1080, 1920)), "本地图片修改头像成功")
except:
    print("error")
else:
    print("pass")

# 取消修改
poco("com.thinkhome.v3:id/image_layout").click()
poco(text="取消").click()
'''
# 修改姓名：为空
try:
    poco(text="姓名").click()
    modify_name("")
    assert_exists(Template(r"tpl1533883588719.png", record_pos=(-0.001, 0.528), resolution=(1080, 1920)), "修改姓名：为空")
except BaseException:
    print("Error:修改姓名为空")

# 修改姓名：包含<字符
try:
    modify_name("<")
    message = poco("android:id/message").get_text()
    assert_equal(message, "数据包含特殊字符", "修改姓名：包含<字符")
except BaseException:
    print("Error:修改姓名包含<字符")
finally:
    poco("android:id/button3").click()

# 修改姓名：包含>字符
try:
    modify_name(">")
    message = poco("android:id/message").get_text()
    assert_equal(message, "数据包含特殊字符", "修改姓名：包含>字符")
except BaseException:
    print("Error:修改姓名包含>字符")
finally:
    poco("android:id/button3").click()

# 修改姓名：包含&字符
try:
    modify_name("&")
    message = poco("android:id/message").get_text()
    assert_equal(message, "数据包含特殊字符", "修改姓名：包含&字符")
except BaseException:
    print("Error:修改姓名包含&字符")
finally:
    poco("android:id/button3").click()

# 修改姓名：包含\字符
try:
    modify_name("\\")
    message = poco("android:id/message").get_text()
    assert_equal(message, "数据包含特殊字符", r"修改姓名：包含\字符")
except BaseException:
    print(r"Error:修改姓名包含\字符")
finally:
    poco("android:id/button3").click()

# 正确修改姓名
try:
    testName = '张三'
    modify_name(testName)
    realName = poco("com.thinkhome.v3:id/name").child("android.widget.RelativeLayout").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
    assert_equal(testName, realName, "正确修改姓名")
except BaseException:
    print("Error:正确修改姓名")
finally:
    poco("com.thinkhome.v3:id/name").click()
    modify_name("顾豪")
    poco(text="邮箱").click()

# 修改邮箱：为空
try:
    modify_email("")
    assert_exists(Template(r"tpl1533883588719.png", record_pos=(-0.001, 0.528), resolution=(1080, 1920)), "修改邮箱：为空")
except BaseException:
    print("Error:修改邮箱为空")

# 修改邮箱：格式不正确
try:
    modify_email("1")
    assert_exists(Template(r"tpl1533887453233.png", record_pos=(-0.005, 0.528), resolution=(1080, 1920)), "修改邮箱：格式不正确")
except BaseException:
    print("Error:修改邮箱格式不正确")

# 正确修改邮箱
try:
    testEmail = "1234567@qq.com"
    modify_email(testEmail)
    realEmail = poco("com.thinkhome.v3:id/email").child("android.widget.RelativeLayout").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
    assert_equal(testEmail, realEmail, "正确修改邮箱")
except BaseException:
    print("Error:正确修改邮箱")
finally:
    poco("com.thinkhome.v3:id/email").click()
    modify_email("814659370@qq.com")
    poco(text="修改密码").click()

# 修改密码：旧密码为空
try:
    modify_password("", "123456", "123456")
    message = poco("android:id/message").get_text()
    assert_equal(message, "旧密码不能为空", "修改密码：旧密码为空")
except BaseException:
    print("Error:修改密码旧密码为空")
finally:
    poco("android:id/button3").click()

# 修改密码：新密码为空
try:
    modify_password("123456", "", "123456")
    message = poco("android:id/message").get_text()
    assert_equal(message, "新密码不能为空", "修改密码：新密码为空")
except BaseException:
    print("Error:修改密码新密码为空")
finally:
    poco("android:id/button3").click()

# 修改密码：确认密码为空
try:
    modify_password("123456", "123456", "")
    message = poco("android:id/message").get_text()
    assert_equal(message, "确认密码不能为空", "修改密码：确认密码为空")
except BaseException:
    print("Error:修改密码：确认密码为空")
finally:
    poco("android:id/button3").click()

# 修改密码：旧密码错误
try:
    modify_password("999999", "123456", "123456")
    message = poco("android:id/message").get_text()
    assert_equal(message, "旧密码输入错误", "修改密码：旧密码错误")
except BaseException:
    print("Error:修改密码旧密码错误")
finally:
    poco("android:id/button3").click()

# 修改密码：新密码长度小于6位
try:
    modify_password("123456", "12345", "12345")
    message = poco("android:id/message").get_text()
    assert_equal(message, "密码长度不能少于6位", "修改密码：新密码长度小于6位")
except BaseException:
    print("Error:修改密码新密码长度小于6位")
finally:
    poco("android:id/button3").click()

# 修改密码：新密码与确认密码不一致
try:
    modify_password("123456", "123456", "1234567")
    message = poco("android:id/message").get_text()
    assert_equal(message, "两次新密码输入不一致", "修改密码：新密码与确认密码不一致")
except BaseException:
    print("Error:修改密码新密码与确认密码不一致")
finally:
    poco("android:id/button3").click()

# 正确修改密码
try:
    modify_password("123456", "123456", "123456")
    assert_exists(Template(r"tpl1533890116594.png", record_pos=(-0.003, 0.526), resolution=(1080, 1920)), "正确修改密码")
except BaseException:
    print("Error:正确修改密码")
finally:
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    change_account("18158288412", "4008002016")
    sleep(5)
    change_house("0正式")

'''
# 账号切换：添加账号、切换账号
poco("com.thinkhome.v3:id/toolbar_right_text").click()
poco("com.thinkhome.v3:id/toolbar_btn_setting").click()
poco("com.thinkhome.v3:id/tv_welcome").click()
poco("com.thinkhome.v3:id/et_account").set_text("18158288412")
poco("com.thinkhome.v3:id/et_password").set_text("0123456")
poco("com.thinkhome.v3:id/btn_login").click()
poco(
    "com.thinkhome.v3:id/house_list").child("android.widget.RelativeLayout")[0].click()
sleep(2)
poco(text="设置").click()
poco(text="账号管理").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
poco(text="18158288412").click()
poco(text="18368493627").click()
poco("com.thinkhome.v3:id/toolbar_btn_back").click()
poco("com.thinkhome.v3:id/toolbar_btn_back").click()
realAccount = poco("com.thinkhome.v3:id/account").child("android.widget.RelativeLayout").child(
    "android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
try:
    assert_equal("18158288412", realAccount, "切换账号返回验证通过")
except BaseException:
    print("error")
else:
    print("pass")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
poco(text="18368493627").click()
sleep(3)
poco(
    "com.thinkhome.v3:id/house_list").child("android.widget.RelativeLayout")[0].click()
sleep(5)
poco(text="设置").click()
poco(text="账号管理").click()
realAccount = poco("com.thinkhome.v3:id/account").child("android.widget.RelativeLayout").child(
    "android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
try:
    assert_equal("18368493627", realAccount, "切换账号成功")
except BaseException:
    print("error")
else:
    print("pass")

poco("com.thinkhome.v3:id/logout").click()
poco("android:id/button1").click()
poco(text="18158288412").click()
poco("com.thinkhome.v3:id/house_list").child("android.widget.RelativeLayout")[0].click()
'''
