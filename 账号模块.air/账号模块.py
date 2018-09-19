# -*- encoding=utf8 -*-
__author__ = "guhao"

from airtest.core.api import *

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco()

start_app("com.thinkhome.v3")
sleep(5)

#登录183684893627
poco("com.thinkhome.v3:id/et_account").set_text("18368493627")
poco("com.thinkhome.v3:id/et_password").set_text("123456")
poco("com.thinkhome.v3:id/btn_login").click()
poco(text="测试").click()
sleep(5)
poco(text="设置").click()
poco(text="账号管理").click()


# 拍照
poco("com.thinkhome.v3:id/image_layout").click()
poco(text="拍照").click()
poco("com.huawei.camera:id/shutter_button").click()#考虑用图像识别
poco("com.huawei.camera:id/btn_done").click()#考虑用图像识别
poco("com.android.gallery3d:id/head_select_right").click()
assert_exists(Template(r"tpl1533883870891.png", record_pos=(0.001, 0.528), resolution=(1080, 1920)), "拍照修改头像成功")

# 选择本地图片
poco("com.thinkhome.v3:id/image_layout").click()
poco(text="选择本地图片").click()
poco(text="最近").click()
poco("com.android.documentsui:id/grid").child("android.widget.FrameLayout")[0].child("android.widget.LinearLayout").child("com.android.documentsui:id/icon_mime").click()
poco("com.android.documentsui:id/icon_mime").click()
poco("com.android.gallery3d:id/head_select_right").click()
assert_exists(Template(r"tpl1533883908278.png", record_pos=(0.002, 0.532), resolution=(1080, 1920)), "本地图片修改头像成功")

# 取消修改
poco("com.thinkhome.v3:id/image_layout").click()
poco(text="取消").click()

# 修改姓名：为空
poco("com.thinkhome.v3:id/name").click()
poco("com.thinkhome.v3:id/name").set_text("")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
assert_exists(Template(r"tpl1533883588719.png", record_pos=(-0.001, 0.528), resolution=(1080, 1920)),"姓名为空验证通过")

# 修改姓名：包含<字符
poco("com.thinkhome.v3:id/name").set_text("<")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
message = poco("android:id/message").get_text()
assert_equal(message,"可能包含></等特殊字符，请修改重试。","姓名包含<验证通过")
poco("android:id/button3").click()

# 修改姓名：包含>字符
poco("com.thinkhome.v3:id/name").set_text(">")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
message = poco("android:id/message").get_text()
assert_equal(message,"可能包含></等特殊字符，请修改重试。","姓名包含<验证通过")
poco("android:id/button3").click()

# 修改姓名：包含&字符
poco("com.thinkhome.v3:id/name").set_text("&")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
message = poco("android:id/message").get_text()
assert_equal(message,"可能包含></等特殊字符，请修改重试。","姓名包含<验证通过")
poco("android:id/button3").click()

# 修改姓名：包含\字符
poco("com.thinkhome.v3:id/name").set_text("\\")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
message = poco("android:id/message").get_text()
assert_equal(message,"可能包含></等特殊字符，请修改重试。","姓名包含<验证通过")
poco("android:id/button3").click()

# 正确修改姓名
testName = "张三"
poco("com.thinkhome.v3:id/name").set_text(testName)
poco("com.thinkhome.v3:id/toolbar_right_text").click()
realName = poco("com.thinkhome.v3:id/name").child("android.widget.RelativeLayout").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
assert_equal(testName,realName,"修改姓名成功")

# 修改邮箱：为空
poco("com.thinkhome.v3:id/email").click()
poco("com.thinkhome.v3:id/name").set_text("")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
assert_exists(Template(r"tpl1533883588719.png", record_pos=(-0.001, 0.528), resolution=(1080, 1920)),"邮箱为空验证通过")

# 修改邮箱：格式不正确
poco("com.thinkhome.v3:id/name").set_text("111111")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
assert_exists(Template(r"tpl1533887453233.png", record_pos=(-0.005, 0.528), resolution=(1080, 1920)), "邮箱格式不正确验证通过")

# 正确修改邮箱
testEmail = "1234567@qq.com"
poco("com.thinkhome.v3:id/name").set_text(testEmail)
poco("com.thinkhome.v3:id/toolbar_right_text").click()
realEmail = poco("com.thinkhome.v3:id/email").child("android.widget.RelativeLayout").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
assert_equal(testEmail,realEmail,"修改邮箱成功")

# 修改密码：旧密码为空
poco("com.thinkhome.v3:id/change_password").click()
poco("com.thinkhome.v3:id/edit_pwd_new").set_text("123456")
poco("com.thinkhome.v3:id/edit_pwd_new_confirm").set_text("123456")
poco("com.thinkhome.v3:id/btn_modify").click()
message = poco("android:id/message").get_text()
assert_equal(message,"旧密码不能为空","旧密码为空验证通过")
poco("android:id/button3").click()

# 修改密码：新密码为空
poco("com.thinkhome.v3:id/edit_pwd_old").set_text("123456")
poco("com.thinkhome.v3:id/edit_pwd_new").set_text("")
poco("com.thinkhome.v3:id/edit_pwd_new_confirm").set_text("123456")
poco("com.thinkhome.v3:id/btn_modify").click()
message = poco("android:id/message").get_text()
assert_equal(message,"新密码不能为空","新密码为空验证通过")
poco("android:id/button3").click()

# 修改密码：确认密码为空
poco("com.thinkhome.v3:id/edit_pwd_old").set_text("123456")
poco("com.thinkhome.v3:id/edit_pwd_new").set_text("123456")
poco("com.thinkhome.v3:id/edit_pwd_new_confirm").set_text("")
poco("com.thinkhome.v3:id/btn_modify").click()
message = poco("android:id/message").get_text()
assert_equal(message,"确认密码不能为空","确认密码为空验证通过")
poco("android:id/button3").click()

# 修改密码：旧密码错误
poco("com.thinkhome.v3:id/edit_pwd_old").set_text("999999")
poco("com.thinkhome.v3:id/edit_pwd_new_confirm").set_text("123456")
poco("com.thinkhome.v3:id/btn_modify").click()
message = poco("android:id/message").get_text()
assert_equal(message,"旧密码输入错误","旧密码错误验证通过")
poco("android:id/button3").click()

# 修改密码：新密码长度小于6位
poco("com.thinkhome.v3:id/edit_pwd_old").set_text("123456")
poco("com.thinkhome.v3:id/edit_pwd_new").set_text("12345")
poco("com.thinkhome.v3:id/edit_pwd_new_confirm").set_text("12345")
poco("com.thinkhome.v3:id/btn_modify").click()
message = poco("android:id/message").get_text()
assert_equal(message,"密码长度不能少于6位","新密码长度小于6位验证通过")
poco("android:id/button3").click()

# 修改密码：新密码与确认密码不一致
poco("com.thinkhome.v3:id/edit_pwd_new").set_text("1234567")
poco("com.thinkhome.v3:id/edit_pwd_new_confirm").set_text("12345678")
poco("com.thinkhome.v3:id/btn_modify").click()
message = poco("android:id/message").get_text()
assert_equal(message,"两次新密码输入不一致","新密码与确认密码不一致验证通过")
poco("android:id/button3").click()

# 正确修改密码
poco("com.thinkhome.v3:id/edit_pwd_new").set_text("123456")
poco("com.thinkhome.v3:id/edit_pwd_new_confirm").set_text("123456")
poco("com.thinkhome.v3:id/btn_modify").click()
assert_exists(Template(r"tpl1533890116594.png", record_pos=(-0.003, 0.526), resolution=(1080, 1920)), "修改密码成功")

# # 意见反馈：为空
# poco("com.thinkhome.v3:id/feedback").click()
# poco("com.thinkhome.v3:id/feedback_send").click()
# message = poco("android:id/message").get_text()
# assert_equal(message,"反馈内容不能为空","意见反馈为空验证通过")
# poco("android:id/button3").click()
# 
# # 意见反馈成功
# poco("com.thinkhome.v3:id/feedback").set_text("test")
# poco("com.thinkhome.v3:id/feedback_send").click()
# assert_exists(Template(r"tpl1533890705033.png", record_pos=(-0.007, 0.527), resolution=(1080, 1920)), "意见反馈成功")

# 账号切换：添加账号、切换账号
poco("com.thinkhome.v3:id/toolbar_right_text").click()
poco("com.thinkhome.v3:id/add_text").click()
poco("com.thinkhome.v3:id/et_account").set_text("18606683597")
poco("com.thinkhome.v3:id/et_password").set_text("123456")
poco("com.thinkhome.v3:id/btn_login").click()
poco(text="我的家").click()
sleep(2)
poco(text="设置").click()
poco(text="账号管理").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
poco(text="18606683597").click()
poco(text="18368493627").click()
poco("com.thinkhome.v3:id/toolbar_btn_back").click()
poco("com.thinkhome.v3:id/toolbar_btn_back").click()
realAccount = poco("com.thinkhome.v3:id/account").child("android.widget.RelativeLayout").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
assert_equal("18606683597",realAccount,"切换账号返回验证通过")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
poco(text="18368493627").click()
poco(text="测试").click()
sleep(5)
poco(text="设置").click()
poco(text="账号管理").click()
realAccount = poco("com.thinkhome.v3:id/account").child("android.widget.RelativeLayout").child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
assert_equal("18368493627",realAccount,"切换账号成功")
