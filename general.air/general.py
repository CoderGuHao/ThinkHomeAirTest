# -*- encoding=utf8 -*-
__author__ = "lu201"

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *

auto_setup(__file__)

poco = AndroidUiautomationPoco()

# 开启app
# start_app('com.thinkhome.v3')
# sleep(10)


def login():
    # poco("com.thinkhome.v3:id/btn").click()
    poco("com.thinkhome.v3:id/tv_welcome").click()
    poco("com.thinkhome.v3:id/et_account").click()
    poco("com.thinkhome.v3:id/et_account").set_text("18158288412")
    poco("com.thinkhome.v3:id/et_password").click()
    poco("com.thinkhome.v3:id/et_password").set_text("0123456")
    poco("com.thinkhome.v3:id/btn_login").click()
    poco(text="0正式").click()
    sleep(5)


def changeAccount():
    poco("android:id/tabs").child("android.widget.RelativeLayout")[
        3].child("com.thinkhome.v3:id/tab_image").click()
    poco(text="账号管理").click()
    poco(text="切换账号").click()
    poco("com.thinkhome.v3:id/toolbar_btn_setting").click()


def systemPwd(pwd):
    poco(text="系统密码").click()
    poco("com.thinkhome.v3:id/et_password").click()
    poco("com.thinkhome.v3:id/et_password").set_text(pwd)


# 进入设置
poco("android:id/tabs").child("android.widget.RelativeLayout")[
    3].child("com.thinkhome.v3:id/tab_image").click()

# 震动反馈停启用
try:
    poco(text="通用").click()
    snapshot(msg="震动反馈设置前.")
    poco("com.thinkhome.v3:id/item_vibration_feedback").child(
        "android.widget.RelativeLayout").child("com.thinkhome.v3:id/switch_view").click()
    snapshot(msg="震动反馈设置后.")
except BaseException:
    print("Error!")

# 音效反馈停启用
try:
    poco(text="通用").click()
    snapshot(msg="音效反馈设置前.")
    poco("com.thinkhome.v3:id/item_audio_feedback").child(
        "android.widget.RelativeLayout").child("com.thinkhome.v3:id/switch_view").click()
    snapshot(msg="音效反馈设置后.")
except BaseException:
    print("Error!")

# 语音控制停启用
try:
    poco(text="通用").click()
    snapshot(msg="语音控制设置前.")
    poco("com.thinkhome.v3:id/item_voice_control").child(
        "android.widget.RelativeLayout").child("com.thinkhome.v3:id/switch_view").click()
    snapshot(msg="语音控制设置后.")
except BaseException:
    print("Error!")


# 首页：开启首页设置
try:
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco("android:id/tabs").child("android.widget.RelativeLayout")[
        0].child("com.thinkhome.v3:id/tab_image").click()
    poco("com.thinkhome.v3:id/img_setting").click()
    sleep(2)
    poco(text="设为开启首页").click()
    changeAccount()
    sleep(3)
    login()
    snapshot(msg="首页：设为开启首页功能 验证.")
except BaseException:
    print("Error!")

# 房间头部：开启首页设置
try:
    poco("android:id/tabs").child("android.widget.RelativeLayout")[
        1].child("com.thinkhome.v3:id/tab_image").click()
    poco("com.thinkhome.v3:id/toolbar_tv_name").click()
    poco(text="设为开启首页").click()
    changeAccount()
    sleep(3)
    login()
    sleep(2)
    resultScenario = poco("android:id/tabs").child("android.widget.RelativeLayout")[
        1].child("com.thinkhome.v3:id/tab_text").get_text()
    assert_equal(resultScenario, "房间", "房间头部：开启首页设置 验证")
except BaseException:
    print("Error:房间头部开启首页设置")

# 房间:设备tab页设为开启首页
try:
    poco("android:id/tabs").child("android.widget.RelativeLayout")[
        1].child("com.thinkhome.v3:id/tab_image").click()
    poco(text="网页版App勿删").click()
    poco("com.thinkhome.v3:id/img_setting").click()
    poco(text="设为开启首页").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    changeAccount()
    sleep(3)
    login()
    sleep(2)
    resultScenario = poco("com.thinkhome.v3:id/title_text").get_text()
    assert_equal(resultScenario, "一层网页版App勿删", "房间设备tab设为开启首页 验证")
except BaseException:
    print("Error:房间设备tab页设为开启首页")

# 通用：开启首页设置
try:
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco("android:id/tabs").child("android.widget.RelativeLayout")[
        3].child("com.thinkhome.v3:id/tab_image").click()
    poco(text="通用").click()
    poco(text="开启首页设置").click()
    poco(text="一层").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    changeAccount()
    sleep(3)
    login()
    sleep(2)
    resultScenario = poco("com.thinkhome.v3:id/title_text").get_text()
    assert_equal(resultScenario, "一层", "通用：开启首页 验证")
except BaseException:
    print("Error:通用开启首页设置")
else:
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco("android:id/tabs").child("android.widget.RelativeLayout")[
        3].child("com.thinkhome.v3:id/tab_image").click()
    poco(text="通用").click()
    poco(text="开启首页设置").click()
    sleep(2)
    poco(text="全部设备列表").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
finally:
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()

# 设备自动更新停启用
try:
    poco("android:id/tabs").child("android.widget.RelativeLayout")[
        3].child("com.thinkhome.v3:id/tab_image").click()
    poco(text="通用").click()
    poco(text="设备自动更新").click()
    snapshot(msg="设备自动更新 设置前.")
    poco("com.thinkhome.v3:id/switch_view").click()
    snapshot(msg="设备自动更新 设置后.")
except BaseException:
    print("Error:设备自动更新停启用")

# 设备自动更新：正确时间设置
try:
    snapshot(msg="设备自动更新，时间设置前.")
    sleep(2)
    poco(text="开始时间").click()
    sleep(2)
    poco(text="02:00").click()
    poco("android:id/button1").click()
    sleep(2)
    poco(text="结束时间").click()
    sleep(2)
    poco(text="04:00").click()
    poco("android:id/button1").click()
    snapshot(msg="设备自动更新，时间设置后.(02:00-04:00)")
except BaseException:
    print("Error:设备自动更新正确时间设置")

# 设备自动更新：错误时间设置
try:
    snapshot(msg="设备自动更新，时间设置前.")
    sleep(2)
    poco(text="开始时间").click()
    sleep(2)
    poco(text="03:00").click()
    poco("android:id/button1").click()
    sleep(2)
    poco(text="结束时间").click()
    sleep(2)
    poco(text="03:00").click()
    poco("android:id/button1").click()
    resultScenario = poco("android:id/message").get_text()
    assert_equal(resultScenario, "开始时间必须小于结束时间", "设备自动更新，错误时间验证")
    poco("android:id/button3").click()
except BaseException:
    print("Error:设备自动更新错误时间设置")
else:
    # 改回原值
    sleep(2)
    poco(text="开始时间").click()
    sleep(2)
    poco(text="02:00").click()
    poco(text="01:00").click()
    sleep(2)
    poco("android:id/button1").click()
    poco(text="结束时间").click()
    sleep(2)
    poco(text="05:00").click()
    poco("android:id/button1").click()

# 关于：检查更新
# try:
#     poco("android:id/tabs").child("android.widget.RelativeLayout")[3].child("com.thinkhome.v3:id/tab_image").click()
#     poco(text="通用").click()
#     poco(text="关于").click()
#     newUpdate = poco(text="检测到最新版本！").exists()
#     if newUpdate:
#         poco("com.thinkhome.v3:id/tv_updateprompt").click()
#         poco("android:id/button3").click()
# except:
#     print("检查更新：Error！")
# finally:
#     poco("com.thinkhome.v3:id/toolbar_btn_back").click()
#     poco("com.thinkhome.v3:id/toolbar_btn_back").click()

# 关于智轩
try:
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco(text="通用").click()
    poco(text="关于").click()
    poco(text="关于智轩").click()
    snapshot(msg="关于智轩 跳转验证.")
except BaseException:
    print("Error:关于智轩")
finally:
    start_app('com.thinkhome.v3')
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()

# 关于：商务合作：成功案例
try:
    poco(text="通用").click()
    poco(text="关于").click()
    poco(text="商务合作").click()
    poco(text="成功案例").click()
    sleep(10)
    snapshot(msg="成功案例跳转验证.")
except BaseException:
    print("Error:成功案例")
finally:
    start_app('com.thinkhome.v3')

# 关于：商务合作：渠道合作
try:
    poco(text="渠道合作").click()
    sleep(10)
    snapshot(msg="渠道合作跳转验证.")
except BaseException:
    print("Error:渠道合作")
finally:
    start_app('com.thinkhome.v3')

# 关于：商务合作：房产合作
try:
    poco(text="房产合作").click()
    sleep(10)
    snapshot(msg="房产合作跳转验证.")
except BaseException:
    print("Error:房产合作")
finally:
    start_app('com.thinkhome.v3')
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()

# 关于：软件协议
try:
    poco(text="软件协议和隐私政策").click()
    poco(text="软件协议").click()
    resultScenario = poco("com.thinkhome.v3:id/toolbar_tv_name").get_text()
    assert_equal(resultScenario, "软件协议", "软件协议跳转验证")
except BaseException:
    print("Error:软件协议")
finally:
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()

# 关于：隐私政策
try:
    poco(text="隐私政策").click()
    resultScenario = poco("com.thinkhome.v3:id/toolbar_tv_name").get_text()
    assert_equal(resultScenario, "隐私政策", "隐私政策跳转验证")
except BaseException:
    print("Error:隐私政策")
finally:
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()

# 系统密码停启用
try:
    systemPwd("1234")
    sleep(2)
    snapshot(msg="系统密码设置前")
    poco("com.thinkhome.v3:id/switch_view").click()
    sleep(2)
    snapshot(msg="系统密码设置后")
except BaseException:
    print("Error:系统密码停启用")
finally:
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()

# 系统密码修改密码:正确输入
try:
    poco("android:id/tabs").child("android.widget.RelativeLayout")[
        3].child("com.thinkhome.v3:id/tab_image").click()
    systemPwd("1234")
    poco("com.thinkhome.v3:id/left_text").click()
    poco("com.thinkhome.v3:id/et_old_password").click()
    poco("com.thinkhome.v3:id/et_old_password").set_text("1234")
    poco("com.thinkhome.v3:id/et_new_password").click()
    poco("com.thinkhome.v3:id/et_new_password").set_text("5678")
    poco("com.thinkhome.v3:id/et_confirm_password").click()
    poco("com.thinkhome.v3:id/et_confirm_password").set_text("5678")
    poco("android:id/button1").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    systemPwd("5678")
    snapshot(msg="系统密码修改成功验证.")
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
except BaseException:
    print("Error:系统密码修改密码正确输入")

# 系统密码修改密码:旧密码错误
try:
    poco("android:id/tabs").child("android.widget.RelativeLayout")[
        3].child("com.thinkhome.v3:id/tab_image").click()
    systemPwd("5678")
    poco("com.thinkhome.v3:id/left_text").click()
    poco("com.thinkhome.v3:id/et_old_password").click()
    poco("com.thinkhome.v3:id/et_old_password").set_text("1234")
    poco("com.thinkhome.v3:id/et_new_password").click()
    poco("com.thinkhome.v3:id/et_new_password").set_text("5678")
    poco("com.thinkhome.v3:id/et_confirm_password").click()
    poco("com.thinkhome.v3:id/et_confirm_password").set_text("5678")
    poco("android:id/button1").click()
    resultScenario = poco("com.thinkhome.v3:id/wrong_password_hint").get_text()
    print(resultScenario)
    assert_equal(resultScenario, "原密码错误", "原密码错误验证")
except BaseException:
    print("Error:系统密码修改密码旧密码错误")

# 系统密码修改密码:新密码与确认密码不一致
try:
    poco("com.thinkhome.v3:id/et_old_password").click()
    poco("com.thinkhome.v3:id/et_old_password").set_text("5678")
    poco("com.thinkhome.v3:id/et_new_password").click()
    poco("com.thinkhome.v3:id/et_new_password").set_text("5678")
    poco("com.thinkhome.v3:id/et_confirm_password").click()
    poco("com.thinkhome.v3:id/et_confirm_password").set_text("1234")
    poco("android:id/button1").click()
    resultScenario = poco("com.thinkhome.v3:id/wrong_password_hint").get_text()
    assert_equal(resultScenario, "确认密码与新密码不一致", "新密码与确认密码不一致验证")
    poco("android:id/button2").click()

except BaseException:
    print("Error:系统密码修改密码新密码与确认密码不一致")

# 改回原系统密码
try:
    poco("com.thinkhome.v3:id/left_text").click()
    poco("com.thinkhome.v3:id/et_old_password").click()
    poco("com.thinkhome.v3:id/et_old_password").set_text("5678")
    poco("com.thinkhome.v3:id/et_new_password").click()
    poco("com.thinkhome.v3:id/et_new_password").set_text("1234")
    poco("com.thinkhome.v3:id/et_confirm_password").click()
    poco("com.thinkhome.v3:id/et_confirm_password").set_text("1234")
    poco("android:id/button1").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
except BaseException:
    print("Error:改回原系统密码")

# 系统密码：开启APP 设置
try:
    poco("android:id/tabs").child("android.widget.RelativeLayout")[
        3].child("com.thinkhome.v3:id/tab_image").click()
    systemPwd("1234")
    sleep(2)
    snapshot(msg="设置前")
    poco("com.thinkhome.v3:id/pwd_app").child("android.widget.RelativeLayout").child(
        "com.thinkhome.v3:id/switch_view").click()
    poco("com.thinkhome.v3:id/pwd_system").child(
        "android.widget.RelativeLayout").child("com.thinkhome.v3:id/switch_view").click()
    poco("com.thinkhome.v3:id/pwd_single_item").child(
        "android.widget.RelativeLayout").child("com.thinkhome.v3:id/switch_view").click()
    poco("com.thinkhome.v3:id/device_list").child("android.widget.LinearLayout")[1].child(
        "android.widget.RelativeLayout").child("com.thinkhome.v3:id/switch_view").click()
    sleep(2)
    snapshot(msg="设置后")
except BaseException:
    print("Error:系统密码开启APP 设置")
else:
    poco("com.thinkhome.v3:id/pwd_app").child("android.widget.RelativeLayout").child(
        "com.thinkhome.v3:id/switch_view").click()
    poco("com.thinkhome.v3:id/pwd_system").child(
        "android.widget.RelativeLayout").child("com.thinkhome.v3:id/switch_view").click()
    poco("com.thinkhome.v3:id/pwd_single_item").child(
        "android.widget.RelativeLayout").child("com.thinkhome.v3:id/switch_view").click()
    snapshot(msg="设置后")
    poco("com.thinkhome.v3:id/pwd_all").child("android.widget.RelativeLayout").child(
        "com.thinkhome.v3:id/switch_view").click()

# 系统密码-忘记密码：验证码为空
try:
    poco("android:id/tabs").child("android.widget.RelativeLayout")[
        3].child("com.thinkhome.v3:id/tab_image").click()
    poco(text="系统密码").click()
    poco("com.thinkhome.v3:id/forget_password").click()
    poco("com.thinkhome.v3:id/btn_modify").click()
    resultScenario = poco("android:id/message").get_text()
    assert_equal(resultScenario, "验证码不能为空", "忘记密码，验证码为空")
    poco("android:id/button3").click()

    # 验证码错误
    poco("com.thinkhome.v3:id/et_verify_code").click()
    poco("com.thinkhome.v3:id/et_verify_code").set_text("123456")
    poco("com.thinkhome.v3:id/et_new_password").click()
    poco("com.thinkhome.v3:id/et_new_password").set_text("1234")
    poco("com.thinkhome.v3:id/et_confirm_password").click()
    poco("com.thinkhome.v3:id/et_confirm_password").set_text("1234")
    poco("com.thinkhome.v3:id/btn_modify").click()
    resultScenario = poco("android:id/message").get_text()
    assert_equal(resultScenario, "验证码错误", "忘记密码，验证码错误 验证")
    poco("android:id/button3").click()

    # 俩次密码不一致
    poco("com.thinkhome.v3:id/et_verify_code").click()
    poco("com.thinkhome.v3:id/et_verify_code").set_text("076807")
    poco("com.thinkhome.v3:id/et_new_password").click()
    poco("com.thinkhome.v3:id/et_new_password").set_text("1234")
    poco("com.thinkhome.v3:id/et_confirm_password").click()
    poco("com.thinkhome.v3:id/et_confirm_password").set_text("1111")
    poco("com.thinkhome.v3:id/btn_modify").click()
    resultScenario = poco("android:id/message").get_text()
    assert_equal(resultScenario, "两次密码不一致", "忘记密码，俩次密码不一致 验证")
    poco("android:id/button3").click()
except BaseException:
    print("Error:忘记密码验证码为空")
else:
    # 退出忘记密码界面
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()

# 普通背景：从图库选择
try:
    poco("android:id/tabs").child("android.widget.RelativeLayout")[
        0].child("com.thinkhome.v3:id/tab_image").click()
    poco("com.thinkhome.v3:id/img_setting").click()
    poco(text="背景设置").click()
    poco(text="从图库选择").click()
    sleep(5)
    poco("com.thinkhome.v3:id/recycler_view").child("android.widget.LinearLayout")[0].child(
        "com.thinkhome.v3:id/grid_view").child("android.widget.LinearLayout")[2].child("com.thinkhome.v3:id/image_view").click()
    poco("com.thinkhome.v3:id/btn_confirm").click()
    sleep(3)
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    snapshot(msg="普通背景，从图库选择 验证.")
except BaseException:
    print("Error:普通背景从图库选择")

# #普通背景：从相册选择
# try:
#     poco("com.thinkhome.v3:id/img_setting").click()
#     poco(text="背景设置").click()
#     poco(text="从相册选择").click()
#     sleep(5)
#     poco("com.android.documentsui:id/grid").child("android.widget.FrameLayout")[1].child("android.widget.LinearLayout").child("com.android.documentsui:id/icon_mime").click()
#     poco("com.android.documentsui:id/grid").child("android.widget.FrameLayout")[1].child("android.widget.LinearLayout").child("com.android.documentsui:id/icon_mime").click()
#     poco("com.android.gallery3d:id/head_select_right").click()
#     snapshot(msg="普通背景，从相册选择 验证.")
# except:
#     print("Background: Error!")

# 普通背景：恢复默认背景
try:
    poco("com.thinkhome.v3:id/img_setting").click()
    poco(text="背景设置").click()
    poco(text="恢复默认照片").click()
    poco("android:id/button1").click()
    sleep(2)
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    snapshot(msg="普通背景，恢复默认 验证.")
    sleep(2)
except BaseException:
    print("Error:普通背景恢复默认背景")

# 动态背景：模板
try:
    poco("com.thinkhome.v3:id/img_setting").click()
    poco(text="背景设置").click()
    poco(text="动态背景").click()
    poco(text="模版").click()
    sleep(2)
    poco("com.thinkhome.v3:id/recycler_view").child("android.widget.LinearLayout")[2].child("android.widget.RelativeLayout").child(
        "com.thinkhome.v3:id/grid_view").child("android.widget.LinearLayout").child("com.thinkhome.v3:id/image_view").click()
    sleep(1)
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    # poco(text="测试1").click()
    poco("com.thinkhome.v3:id/list_view").child("android.widget.RelativeLayout")[3].child(
        "android.widget.LinearLayout")[0].child("com.thinkhome.v3:id/tv_device_name").click()
    sleep(1)
    poco(text="1").click()
    poco("android:id/button1").click()
    poco("com.thinkhome.v3:id/list_view").child("android.widget.RelativeLayout")[1].child(
        "android.widget.LinearLayout")[0].child("com.thinkhome.v3:id/tv_device_name").click()
    sleep(1)
    poco(text="2").click()
    poco("android:id/button1").click()
    poco("com.thinkhome.v3:id/list_view").child("android.widget.RelativeLayout")[2].child(
        "android.widget.LinearLayout")[0].child("com.thinkhome.v3:id/tv_device_name").click()
    sleep(1)
    poco(text="2").click()
    poco(text="3").click()
    poco("android:id/button1").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    sleep(1)
    poco("android:id/button1").click()
    sleep(10)
    poco("android:id/button3").click()
    sleep(2)
    snapshot(msg="动态背景：根据模板 验证.")
    sleep(2)
except BaseException:
    print("Error:动态背景模板")

# 动态背景：下载
try:
    poco(text="下载").click()
    poco("android:id/button1").click()
    sleep(5)
    resultScenario = poco("android:id/message").get_text()
    assert_equal(resultScenario, "下载成功！", "动态背景：下载 验证")
    sleep(2)
    poco("android:id/button3").click()
except BaseException:
    print("Error:动态背景下载")

# 动态背景：包含设备
try:
    poco(text="包含设备").click()
    snapshot(msg="包含设备验证.")
except BaseException:
    print("Error:动态背景包含设备")
else:
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()

# 动态背景：单张修改
try:
    poco(text="单张修改").click()
    poco("com.thinkhome.v3:id/grid_view").child("android.widget.RelativeLayout")[
        0].child("com.thinkhome.v3:id/image").click()
    poco("com.thinkhome.v3:id/toolbar_btn_setting").click()
    poco(text="从相册选择").click()
    poco("com.android.documentsui:id/grid").child("android.widget.FrameLayout")[
        1].child("com.android.documentsui:id/icon_thumb").click()
    poco("com.android.documentsui:id/grid").child("android.widget.FrameLayout")[
        1].child("com.android.documentsui:id/icon_thumb").click()
    poco("com.android.gallery3d:id/head_select_right").click()
    poco("com.thinkhome.v3:id/toolbar_btn_setting").click()
    poco(text="确定上传").click()
    snapshot(msg="动态背景单张修改验证.")
    sleep(2)
    poco("android:id/button3").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
except BaseException:
    print("Error:动态背景单张修改")

# 动态背景：清除
try:
    poco("com.thinkhome.v3:id/img_setting").click()
    poco(text="背景设置").click()
    poco(text="动态背景").click()
    poco(text="清除").click()
    poco("android:id/button1").click()
    resultScenario = poco("android:id/message").get_text()
    assert_equal(resultScenario, "清除成功！", "动态背景清除 验证")
    poco("android:id/button3").click()

except BaseException:
    print("Error:动态背景清除")
else:
    poco(text="普通背景").click()
    poco(text="恢复默认照片").click()
    poco("android:id/button1").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
