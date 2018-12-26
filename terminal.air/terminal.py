# -*- encoding=utf8 -*-
# TAG = 4
__author__ = "guhao"

import random
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco()

auto_setup(__file__)

# start_app("com.thinkhome.v3")
# sleep(5)


def doInputPassword():
    poco("com.thinkhome.v3:id/et_password").set_text("1234")


def go_terminal():
    poco("android:id/tabs").child("android.widget.RelativeLayout")[
        3].child("com.thinkhome.v3:id/tab_image").click()
    poco(text="设备管理").click()


def add_terminal_by_id(num):
    poco("com.thinkhome.v3:id/manually_enter_id").set_text(num)
    poco("com.thinkhome.v3:id/btn_ok").click()


def go_terminal_setting(name):
    for i in range(1, 10):
        if poco(text=name).exists():
            poco(text=name).long_click()
            poco(text="更多设置").click()
            break
        else:
            poco.scroll(direction='vertical', percent=0.3, duration=1.0)
            sleep(2)


def delete_terminal():
    poco("com.thinkhome.v3:id/btn_delete").click()
    poco("android:id/button1").click()
    if poco("com.thinkhome.v3:id/et_password").exists():
        doInputPassword()


def edit_terminal_name(name):
    poco("com.thinkhome.v3:id/tv_name").set_text(name)
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco("com.thinkhome.v3:id/et_password").exists():
        doInputPassword()


def edit_terminal_location(info):
    poco("com.thinkhome.v3:id/feedback").set_text(info)
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco("com.thinkhome.v3:id/et_password").exists():
        doInputPassword()


# 手动输入：为空
try:
    go_terminal()
    poco("com.thinkhome.v3:id/toolbar_btn_setting").click()
    poco("com.thinkhome.v3:id/toolbar_btn_setting").click()
    poco(text="手动输入").click()
    add_terminal_by_id("")
    assert_exists(Template(r"tpl1536719197979.png", record_pos=(-0.003, 0.529), resolution=(1080, 1920)), "手动输入：为空")
except BaseException:
    print("Error:手动输入为空")

# 手动输入：ID格式不正确
try:
    add_terminal_by_id("1")
    assert_exists(Template(r"tpl1536719983748.png", record_pos=(-0.001, 0.527), resolution=(1080, 1920)), "手动输入：ID格式不正确")
except BaseException:
    print("Error:手动输入ID格式不正确")

# 手动输入：ID不存在
try:
    add_terminal_by_id("12345678")
    message = poco("android:id/message").get_text()
    assert_equal(message, "控制器不存在", "手动输入：ID不存在")
except BaseException:
    print("Error:手动输入ID不存在")
finally:
    poco("android:id/button3").click()

# 手动输入：已被该账号添加
# 硬件掉线的情况下无法正常执行
try:
    add_terminal_by_id("77670215")
    poco("com.thinkhome.v3:id/btn_active").click()
    poco("com.thinkhome.v3:id/btn_active").click()
    message = poco("android:id/message").get_text()
    assert_equal(message, "控制器已被该帐号添加", "手动输入：已被该账号添加")
except BaseException:
    print("Error:手动输入已被该账号添加 ")
finally:
    poco("android:id/button3").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()

# 手动输入：已被其他账号添加
try:
    add_terminal_by_id("97557754")
    message = poco("android:id/message").get_text()
    assert_equal(message, "控制器已被其他帐号添加", "手动输入：已被其他账号添加")
except BaseException:
    print("Error:手动输入已被其他账号添加")
finally:
    poco("android:id/button3").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()

# 控制器删除：主机下还有从机挂载
try:
    go_terminal_setting("ThinkID:77670215")
    delete_terminal()
    sleep(2)
    message = poco("android:id/message").get_text()
    assert_equal(message, "请先删除该控制器下挂载的从机", "控制器删除：主机下还有从机挂载")
except BaseException:
    print("Error:控制器删除主机下还有从机挂载")
finally:
    poco("android:id/button3").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()

'''
# 控制器删除：删除成功
try:
    go_terminal_setting("ThinkID:33049825")
    delete_terminal()
    if poco(text="ThinkID:33049825").exists():
        message = "删除失败"
    else:
        message = "删除成功"
    assert_equal(message, "删除成功", "控制器删除：删除成功")
except BaseException:
    print("Error:控制器删除删除成功")
'''

# 修改名称：为空
try:
    go_terminal_setting("ThinkID:77670215")
    poco("com.thinkhome.v3:id/icon_layout").click()
    edit_terminal_name("")
    message = poco("android:id/message").get_text()
    assert_equal(message, "名称不能为空", "修改名称：为空")
except BaseException:
    print("Error:修改名称为空")
finally:
    poco("android:id/button3").click()

# 修改名称：包含<字符
try:
    edit_terminal_name("<")
    message = poco("android:id/message").get_text()
    assert_equal(message, "数据包含特殊字符", "修改名称：包含<字符")
except BaseException:
    print("Error:修改名称包含<字符")
finally:
    poco("android:id/button3").click()

# 修改名称：包含>字符
try:
    edit_terminal_name("<")
    message = poco("android:id/message").get_text()
    assert_equal(message, "数据包含特殊字符", "修改名称：包含>字符")
except BaseException:
    print("Error:修改名称包含>字符")
finally:
    poco("android:id/button3").click()

# 修改名称：包含&字符
try:
    edit_terminal_name("&")
    message = poco("android:id/message").get_text()
    assert_equal(message, "数据包含特殊字符", "修改名称：包含&字符")
except BaseException:
    print("Error:修改名称包含&字符")
finally:
    poco("android:id/button3").click()

# 修改名称：包含\字符
try:
    edit_terminal_name("\\")
    message = poco("android:id/message").get_text()
    assert_equal(message, "数据包含特殊字符", "修改名称：包含\字符")
except BaseException:
    print(r"Error:修改名称包含\字符")
finally:
    poco("android:id/button3").click()

'''
# 修改名称：包含＇字符
try:
    edit_terminal_name("＇")
    message = poco("android:id/message").get_text()
    assert_equal(message,"数据包含特殊字符","修改名称：包含＇字符")
except:
    print("Error:修改名称包含＇字符")
finally:
    poco("android:id/button3").click()
'''

# 修改名称：正确输入
try:
    edit_terminal_name("测试")
    message = poco("com.thinkhome.v3:id/tv_name").get_text()
    assert_equal(message, "测试", "修改名称：正确输入")
except BaseException:
    print("Error:修改名称正确输入")
finally:
    poco("com.thinkhome.v3:id/icon_layout").click()
    edit_terminal_name("P9S")

'''
# 位置：拍照
poco(text="位置").click()
poco("com.thinkhome.v3:id/iv").click()
poco(text="拍照").click()
poco("com.huawei.camera:id/shutter_button").click()#考虑用图像识别
poco("com.huawei.camera:id/btn_done").click()#考虑用图像识别
poco("com.android.gallery3d:id/head_select_right").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()

# 位置：从相册选择
poco(text="位置").click()
poco("com.thinkhome.v3:id/iv").click()
poco(text="从相册选择").click()
poco(text="最近").click()
poco("com.android.documentsui:id/icon_mime").click()
poco("com.android.gallery3d:id/head_select_right").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()


# 位置：删除
poco(text="位置").click()
poco("com.thinkhome.v3:id/iv").click()
poco(text="删除").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
'''

# 位置：添加描述
try:
    poco(text="位置").click()
    edit_terminal_location("测试")
    poco(text="位置").click()
    message = poco("com.thinkhome.v3:id/feedback").get_text()
    assert_equal(message, "测试", "位置：添加描述")
except BaseException:
    print("Error:位置添加描述")
finally:
    edit_terminal_location("")
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()



'''
# 功能停启用：停用
poco(text="功能停启用").click()
poco(text="A门锁1").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()

# 功能停启用：启用
poco(text="功能停启用").click()
poco(text="A门锁1").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
poco("com.thinkhome.v3:id/toolbar_btn_back").click()

# 反馈数据选项设置:恢复默认
try:
    go_terminal_setting("ThinkID:82758873")
    poco(text="指示灯方案").click()
    poco(text="反馈数据选项").click()
    poco(text="反馈数据选项").click()
    poco("com.thinkhome.v3:id/btn_restore").click()
    poco(text="保存").click()
poco(text="二氧化碳").click()
poco(text="TVOC").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()

# 反馈数据选项：恢复默认
poco(text="反馈数据选项").click()
poco("com.thinkhome.v3:id/btn_restore").click()
poco(text="保存").click()

# 夜间显示：设置
poco(text="夜间显示").click()
poco(text="昏暗不显示").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
poco("com.thinkhome.v3:id/toolbar_btn_back").click()
poco("com.thinkhome.v3:id/toolbar_btn_back").click()
poco("com.thinkhome.v3:id/toolbar_btn_back").click()
poco(text="设备管理").click()

# 替换：为空
poco("com.thinkhome.v3:id/expand_listview").child("com.thinkhome.v3:id/detail_layout")[0].child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/expand_img").click()
poco(text="ThinkID:94170840").long_click()
poco(text="更多设置").click()
poco(text="替换").click()
# poco("com.thinkhome.v3:id/edit_text_view").set_text("")
# poco("com.thinkhome.v3:id/toolbar_right_text").click()
# message = poco("com.thinkhome.v3:id/tv_name").get_text()
# try:
#     assert_equal(message,"内容不能为空","替换：为空")
# except:
#     print("Error")
# else:
#     print("Ok")
# finally:
#     poco("android:id/button3").click()

# 替换：控制器不存在
poco("com.thinkhome.v3:id/edit_text_view").set_text("111")
poco("com.thinkhome.v3:id/toolbar_right_text").click()
message = poco("com.thinkhome.v3:id/message").get_text()
try:
    assert_equal(message,"控制器不存在","替换：控制器不存在")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco("android:id/button3").click()
'''
