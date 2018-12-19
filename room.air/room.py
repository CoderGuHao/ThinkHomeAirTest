# -*- encoding=utf8 -*-
# TAG = 3
__author__ = "guhao"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco()

auto_setup(__file__)

# start_app("com.thinkhome.v3")
# sleep(5.0)


def add_room(name):
    poco("com.thinkhome.v3:id/tv_name_value").set_text(name)
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco("com.thinkhome.v3:id/et_password").exists():
        doInputPassword()


def doInputPassword():
    poco("com.thinkhome.v3:id/et_password").set_text("1234")


def modify_room_name(name):
    poco("com.thinkhome.v3:id/tv_name").set_text(name)
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco("com.thinkhome.v3:id/et_password").exists():
        doInputPassword()


def add_room_share(name):
    poco("com.thinkhome.v3:id/share_name_edt").set_text(name)
    poco("com.thinkhome.v3:id/qr_code_is_generated").click()
    if poco("com.thinkhome.v3:id/et_password").exists():
        doInputPassword()


def modify_room_share(name):
    poco("com.thinkhome.v3:id/share_name_edt").set_text(name)
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco("com.thinkhome.v3:id/et_password").exists():
        doInputPassword()


def room_mark(tag):
    poco("com.thinkhome.v3:id/setting_bookmark").click()
    if tag == 1:  # 未标星
        poco(
            "com.thinkhome.v3:id/list_view").child("android.widget.RelativeLayout")[0].click()
    elif tag == 0:  # 已标星
        poco(
            "com.thinkhome.v3:id/list_view").child("android.widget.RelativeLayout")[1].click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco("com.thinkhome.v3:id/et_password").exists():
        doInputPassword()


def room_setting(name):
    isNameExists = poco(text=name).exists()
    while not isNameExists:
        isNameExists = poco(text=name).exists()
        poco.scroll(direction='vertical', percent=0.3, duration=1.0)
    poco(text=name).long_click()
    poco(text="更多设置").click()
    if poco("com.thinkhome.v3:id/et_password").exists():
        doInputPassword()


# 添加房间：房间名称为空
try:
    poco("android:id/tabs").child("android.widget.RelativeLayout")[1].click()
    poco("com.thinkhome.v3:id/toolbar_btn_setting").click()
    add_room("")
    message = poco("android:id/message").get_text()
    assert_equal(message, "房间名称不能为空", "添加房间：房间名称为空")
except BaseException:
    print("Error:添加房间名称为空")
finally:
    poco("android:id/button3").click()

# 添加房间：名称包含<符号
try:
    add_room("<")
    message = poco("android:id/message").get_text()
    assert_equal(message, "数据包含特殊字符", "添加房间：名称包含<符号")
except BaseException:
    print("Error:添加房间名称包含<符号")
finally:
    poco("android:id/button3").click()

# 添加房间：名称包含>符号
try:
    add_room(">")
    message = poco("android:id/message").get_text()
    assert_equal(message, "数据包含特殊字符", "添加房间：名称包含>符号")
except BaseException:
    print("Error:添加房间名称包含>符号")
finally:
    poco("android:id/button3").click()

# 添加房间：名称包含\符号
try:
    add_room("\\")
    message = poco("android:id/message").get_text()
    assert_equal(message, "数据包含特殊字符", r"添加房间：名称包含\符号")
except BaseException:
    print(r"Error:添加房间名称包含\符号")
finally:
    poco("android:id/button3").click()

# 添加房间：名称包含&符号
try:
    add_room("&")
    message = poco("android:id/message").get_text()
    assert_equal(message, "数据包含特殊字符", "房添加房间：名称包含&符号")
except BaseException:
    print("Error:添加房间名称包含&符号")
finally:
    poco("android:id/button3").click()

'''
#添加房间：名称包含'符号
try:
    add_room("'")
    message=poco("android:id/message").get_text()
    assert_equal(message, "数据包含特殊字符", "房间名称包含'符号验证通过")
except:
    print("Error:添加房间名称包含'符号")
finally:
    poco("android:id/button3").click()

#添加房间：名称包含"符号
try:
    add_room(""")
    message=poco("android:id/message").get_text()
    assert_equal(message, "数据包含特殊字符", "房间名称包含"符号验证通过")
except:
    print("Error:添加房间名称包含"符号")
finally:
    poco("android:id/button3").click()
'''

# 添加房间：正确输入
try:
    add_room("w测试卧室")
    result = False
    for i in range(1, 10):
        if poco(text="w测试卧室").exists():
            result = True
            break
        else:
            poco("android.widget.ListView").swipe("up")
    assert_equal(result, True, "添加房间：正确输入")
except BaseException:
    print("Error:添加房间正确输入")
finally:
    room_setting("w测试卧室")

'''
#修改房间图标：拍照
try:
    poco("com.thinkhome.v3:id/icon_layout").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    poco("com.thinkhome.v3:id/img_photo").click()
    poco(text="拍照").click()
    poco("com.huawei.camera:id/shutter_button").click()
    poco("com.huawei.camera:id/btn_done").click()
    poco("com.thinkhome.v3:id/btn_crop").click()
except:
    pass

#修改房间图标：本地图片
poco("com.thinkhome.v3:id/img_photo").click()
poco(text="从相册选择").click()
poco(text="最近").click()
poco("com.android.documentsui:id/grid").child("android.widget.FrameLayout")[0].child("android.widget.LinearLayout").child("com.android.documentsui:id/icon_mime").click()
poco("com.thinkhome.v3:id/btn_crop").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()

#修改房间图标：默认
poco("com.thinkhome.v3:id/icon_layout").click()
poco(text="客厅").click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()
if poco(text="密码").exists():
    poco("com.thinkhome.v3:id/et_password").set_text("1234")
poco("com.thinkhome.v3:id/icon_layout").click()
if poco("com.thinkhome.v3:id/listView").child("android.widget.RelativeLayout")[2].child("android.widget.LinearLayout").child("com.thinkhome.v3:id/tv_room").poco(checked="True").exists:
    message = "客厅"
try:
    assert_equal(message,"客厅","修改房间图标：默认，验证通过")
except:
    print("error")
else:
    print("ok")
finally:
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
'''

# 修改房间名称：为空
try:
    poco("com.thinkhome.v3:id/icon_layout").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    modify_room_name("")
    message = poco("android:id/message").get_text()
    assert_equal(message, "名称不能为空", "修改房间名称：为空")
except BaseException:
    print("Error:修改房间名称为空")
finally:
    poco("android:id/button3").click()

# 修改房间名称：包含<字符
try:
    modify_room_name("<")
    message = poco("android:id/message").get_text()
    assert_equal(message, "数据包含特殊字符", "修改房间名称：包含<字符")
except BaseException:
    print("Error:修改房间名称包含<字符")
finally:
    poco("android:id/button3").click()

# 修改房间名称：包含>字符
try:
    modify_room_name(">")
    message = poco("android:id/message").get_text()
    assert_equal(message, "数据包含特殊字符", "修改房间名称：包含>字符")
except BaseException:
    print("Error:修改房间名称包含>字符")
finally:
    poco("android:id/button3").click()

# 修改房间名称：包含\字符
try:
    modify_room_name("\\")
    message = poco("android:id/message").get_text()
    assert_equal(message, "数据包含特殊字符", r"修改房间名称：包含\字符")
except BaseException:
    print(r"Error：修改房间名称包含\字符")
finally:
    poco("android:id/button3").click()

# 修改房间名称：包含&字符
try:
    modify_room_name("&")
    message = poco("android:id/message").get_text()
    assert_equal(message, "数据包含特殊字符", "修改房间名称：包含&字符")
except BaseException:
    print("Error：修改房间名称包含&字符")
finally:
    poco("android:id/button3").click()

'''
#修改房间名称：包含'字符
try:
    modify_room_name("'")
    message=poco("android:id/message").get_text()
    assert_equal(message, "数据包含特殊字符", "修改房间名称：包含'字符")
except:
    print("Error：修改房间名称包含'字符")
finally:
    poco("android:id/button3").click()

#修改房间名称：包含"字符
try:
    modify_room_name(""")
    message=poco("android:id/message").get_text()
    assert_equal(message, "数据包含特殊字符", "修改房间名称：包含"字符")
except:
    print("Error：修改房间名称包含"字符")
finally:
    poco("android:id/button3").click()
'''

# 修改房间名称：正确输入
try:
    modify_room_name("w测试客厅")
    message = poco("com.thinkhome.v3:id/tv_name").get_text()
    assert_equal(message, "w测试客厅", "修改房间名称：正确输入")
except BaseException:
    print("Error：修改房间名称正确输入")
finally:
    poco("com.thinkhome.v3:id/setting_floor").click()

# 修改楼层
try:
    while poco("android:id/numberpicker_input").get_text() != "2F":
        poco("android.widget.NumberPicker").swipe("up")
    poco("android:id/button1").click()
    message = poco("com.thinkhome.v3:id/setting_floor").child(
        "android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
    assert_equal(message, "二层", "修改楼层")
except BaseException:
    print("Error:修改楼层")
finally:
    poco("com.thinkhome.v3:id/setting_share").click()
    poco("com.thinkhome.v3:id/btn_add_new_share_ms").click()

# 新增房间分享：名称为空
try:
    add_room_share("")
    message = poco("android:id/message").get_text()
    assert_equal(message, "分享名称不能为空", "新增房间分享：名称为空")
except BaseException:
    print("Error：新增房间分享名称为空")
finally:
    poco("android:id/button3").click()

# 新增房间分享：正确输入
try:
    add_room_share("w测试分享")
    # 保存二维码图片
    poco("com.thinkhome.v3:id/save_qr_code_image").click()
    message = poco("android:id/message").get_text()
    assert_equal(message, "图片已保存至系统相册", "保存二维码图片")
    poco("android:id/button3").click()
    poco("com.thinkhome.v3:id/back_button").click()
    result = False
    if poco(text="w测试分享").exists:
        result = True
    assert_equal(result, True, "新增房间分享：正确输入")
except BaseException:
    print("Error:新增房间分享正确输入")
finally:
    poco("com.thinkhome.v3:id/btn_add_new_share_ms").click()


# 新增房间分享：当前时间已有分享
try:
    add_room_share("w测试分享2")
    message = poco("android:id/message").get_text()
    assert_equal(message, "当前选择时间已有分享，请重新设置时间！", "新增房间分享：当前时间已有分享")
except BaseException:
    print("Error：新增房间分享当前时间已有分享")
finally:
    poco("android:id/button3").click()

# 新增房间分享：截止时间早于开始时间
try:
    poco("com.thinkhome.v3:id/start_time_iteam").click()
    poco("com.thinkhome.v3:id/year").swipe("up")
    poco("com.thinkhome.v3:id/year").swipe("up")
    poco("com.thinkhome.v3:id/tv_ensure").click()
    poco("com.thinkhome.v3:id/qr_code_is_generated").click()
    message = poco("android:id/message").get_text()
    assert_equal(message, "开始时间不能晚于截止时间", "新增房间分享：开始时间晚于截止时间")
except BaseException:
    print("Error：新增房间分享分享开始时间晚于截止时间")
finally:
    poco("android:id/button3").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()

# 新增房间分享：截止时间早于当前时间
try:
    poco("com.thinkhome.v3:id/btn_add_new_share_ms").click()
    poco("com.thinkhome.v3:id/share_name_edt").set_text("w测试分享2")
    poco("com.thinkhome.v3:id/start_time_iteam").click()
    poco("com.thinkhome.v3:id/year").swipe("down")
    poco("com.thinkhome.v3:id/year").swipe("down")
    poco("com.thinkhome.v3:id/tv_ensure").click()
    poco("com.thinkhome.v3:id/end_time_iteam").click()
    poco("com.thinkhome.v3:id/year").swipe("down")
    poco("com.thinkhome.v3:id/year").swipe("down")
    poco("com.thinkhome.v3:id/tv_ensure").click()
    poco("com.thinkhome.v3:id/qr_code_is_generated").click()
    message = poco("android:id/message").get_text()
    assert_equal(message, "截止时间不能早于当前时间", "新增房间分享:截止时间早于当前时间")
except BaseException:
    print("Error:新增房间分享截止时间早于当前时间")
finally:
    poco("android:id/button3").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()

# 删除房间：还存在分享
try:
    poco("com.thinkhome.v3:id/btn_delete").click()
    if poco("com.thinkhome.v3:id/et_password").exists():
        doInputPassword()
    message = poco("android:id/message").get_text()
    assert_equal(message, "房间分享未结束，禁止删除！", "删除房间：还存在分享")
except BaseException:
    print("Error:删除房间还存在分享")
finally:
    poco("android:id/button3").click()

# 修改房间分享：名称为空
try:
    poco(text="房间分享").click()
    poco(text="w测试分享").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    modify_room_share("")
    message = poco("android:id/message").get_text()
    assert_equal(message, "分享名称不能为空", "修改房间分享名称：为空")
except BaseException:
    print("Error：修改房间分享名称为空")
finally:
    poco("android:id/button3").click()

# 修改房间分享：名称正确输入
try:
    modify_room_share("w测试分享修改")
    result = False
    if poco(text="w测试分享修改").exists():
        result = True
    assert_equal(result, True, "修改房间分享名称：正确输入")
except BaseException:
    print("Error：修改房间分享名称正确输入")

# 修改房间分享：截止时间早于开始时间
try:
    poco(text="w测试分享修改").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    poco("com.thinkhome.v3:id/start_time_iteam").click()
    poco("com.thinkhome.v3:id/year").swipe("up")
    poco("com.thinkhome.v3:id/year").swipe("up")
    poco("com.thinkhome.v3:id/tv_ensure").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    message = poco("android:id/message").get_text()
    assert_equal(message, "开始时间不能晚于截止时间", "修改房间分享：截止时间早于开始时间")
except BaseException:
    print("Error：修改房间分享截止时间早于开始时间")
finally:
    poco("android:id/button3").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()

# 修改房间分享：截止时间早于当前时间
try:
    poco(text="w测试分享修改").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    poco("com.thinkhome.v3:id/start_time_iteam").click()
    poco("com.thinkhome.v3:id/year").swipe("down")
    poco("com.thinkhome.v3:id/year").swipe("down")
    poco("com.thinkhome.v3:id/tv_ensure").click()
    poco("com.thinkhome.v3:id/end_time_iteam").click()
    poco("com.thinkhome.v3:id/year").swipe("down")
    poco("com.thinkhome.v3:id/year").swipe("down")
    poco("com.thinkhome.v3:id/tv_ensure").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    message = poco("android:id/message").get_text()
    assert_equal(message, "截止时间不能早于当前时间", "修改房间分享:截止时间早于当前时间")
except BaseException:
    print("Error:修改房间分享截止时间早于当前时间")
finally:
    poco("android:id/button3").click()

# 修改房间分享：取消分享
try:
    poco("com.thinkhome.v3:id/cancel_the_share_btn").click()
    poco("android:id/button1").click()
    result = False
    if not poco(text="w测试分享修改").exists():
        result = True
    assert_equal(result, True, "修改房间分享：取消分享")
except BaseException:
    print("Error:修改房间分享取消分享")
finally:
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()

# 标星
try:
    room_mark(1)
    result = poco("com.thinkhome.v3:id/setting_bookmark").child(
        "android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
    assert_equal(result, "已标星", "标星")
except BaseException:
    print("Error:标星")

# 取消标星
try:
    room_mark(0)
    result = poco("com.thinkhome.v3:id/setting_bookmark").child(
        "android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
    assert_equal(result, "未标星", "取消标星")
except BaseException:
    print("Error:取消标星")

# 删除房间
try:
    poco("com.thinkhome.v3:id/btn_delete").click()
    if poco("com.thinkhome.v3:id/et_password").exists():
        doInputPassword()
    poco("android:id/button1").click()
    result = True
    for i in range(1, 10):
        if poco(text="w测试客厅").exists():
            result = False
            break
        else:
            poco.scroll(direction='vertical', percent=0.3, duration=1.0)
    assert_equal(result, True, "删除房间")
except BaseException:
    print("Error:删除房间")

# #楼层控制：灯光全开
# poco(text="1F").long_click()
# poco(text="灯光全开").click()
# #楼层控制：灯光全关
# poco(text="1F").long_click()
# poco(text="灯光全关").click()
# #楼层控制：设备全关
# poco(text="1F").long_click()
# poco(text="设备全关").click()
# #房间控制：灯光全开
# poco(text="客厅").long_click()
# poco(text="灯光全开").click()
# #房间控制：灯光全关
# poco(text="客厅").long_click()
# poco(text="灯光全关").click()
# #房间控制：设备全关
# poco(text="客厅").long_click()
# poco(text="设备全关").click()

'''
#户型图功能：停用
poco("android:id/tabs").child("android.widget.RelativeLayout")[3].click()
poco(text="通用").click()
poco(text="户型图").click()
poco("com.thinkhome.v3:id/switch_view").click()
poco("com.thinkhome.v3:id/toolbar_btn_back").click()
poco("com.thinkhome.v3:id/toolbar_btn_back").click()
poco("android:id/tabs").child("android.widget.RelativeLayout")[1].click()
if not poco("com.thinkhome.v3:id/clickable_image_view").exists():
    message="无户型图"
else:
    message="有户型图"
try:
    assert_equal(message, "无户型图", "户型图停用验证通过")
except:
    print("Error")
else:
    print("Ok")

#户型图：启用
poco("android:id/tabs").child("android.widget.RelativeLayout")[3].click()
poco(text="通用").click()
poco(text="户型图").click()
poco("com.thinkhome.v3:id/switch_view").click()
poco("com.thinkhome.v3:id/toolbar_btn_back").click()
poco("com.thinkhome.v3:id/toolbar_btn_back").click()
poco("android:id/tabs").child("android.widget.RelativeLayout")[1].click()
if not poco("com.thinkhome.v3:id/clickable_image_view").exists():
    message="无户型图"
else:
    message="有户型图"
try:
    assert_equal(message, "有户型图", "户型图启用验证通过")
except:
    print("Error")
else:
    print("Ok")

#添加楼层户型图：楼层下没有房间
poco("android:id/tabs").child("android.widget.RelativeLayout")[3].click()
poco(text="通用").click()
poco(text="户型图").click()
poco(text="四层").click()
try:
    message=poco("android:id/message").get_text()
    assert_equal(message, "该楼层没有房间，不可以添加户型图，请先为此楼层添加房间。", "添加楼层户型图：楼层下没有房间，验证通过")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco("android:id/button3").click()

#添加楼层户型图：从相册选择
poco(text="未设楼层").click()
if poco(text="更换底图").exists():
    poco("com.thinkhome.v3:id/tv_change").click()
else:
    poco("com.thinkhome.v3:id/add_img").click()
poco(text="从相册选择").click()
poco("android:id/list").child("android.widget.LinearLayout")[0].click()
poco("com.android.documentsui:id/grid").child("android.widget.FrameLayout")[0].click()
poco("com.android.gallery3d:id/head_select_right").click()

#添加楼层户型图：从图库选择
poco("com.thinkhome.v3:id/tv_change").click()
poco(text="从图库选择").click()
poco("com.thinkhome.v3:id/recycler_view").child("android.widget.LinearLayout")[0].child("android.widget.RelativeLayout").child("com.thinkhome.v3:id/grid_view").child("android.widget.LinearLayout")[0].click()
poco("com.thinkhome.v3:id/toolbar_right_text").click()

# #户型图房间设置：正确设置
# poco("com.thinkhome.v3:id/list_view").child("android.widget.RelativeLayout")[0].click()
# touch((0.5,0.3),1)#点击户型图报错
# poco("com.thinkhome.v3:id/toolbar_right_text").click()
# poco(text="未设楼层").click()
# try:
#     message=poco("com.thinkhome.v3:id/list_view").child("android.widget.RelativeLayout")[0].child("com.thinkhome.v3:id/detail_layout").child("com.thinkhome.v3:id/tv_count").get_text()
#     assert_equal(message, "已设置", "户型图房间设置验证通过")
# except:
#     print("Error")
# else:
#     print("Ok")
# finally:
#     poco("com.thinkhome.v3:id/toolbar_btn_back").click()
#
# #户型图房间设置：删除设置
# poco("com.thinkhome.v3:id/list_view").child("android.widget.RelativeLayout")[0].long_click()
# poco(text="删除").click()

#楼层户型图功能：停用
poco("com.thinkhome.v3:id/toolbar_btn_back").click()
poco(text="未设楼层").long_click()
poco(text="停用").click()
try:
    message=poco(boundsInParent="[0.5583333333333333, 0.03125]").get_text()
    assert_equal(message, "停用", "楼层户型图停用验证通过")
except:
    print("Error")
else:
    print("Ok")

#楼层户型图功能：启用
poco(text="未设楼层").long_click()
poco(text="启用").click()
try:
    message=poco(boundsInParent="[0.5583333333333333, 0.03125]").get_text()
    assert_equal(message, "启用", "楼层户型图启用验证通过")
except:
    print("Error")
else:
    print("Ok")

#楼层户型图功能：删除
poco(text="未设楼层").long_click()
poco(text="删除").click()
try:
    message=poco(boundsInParent="[0.5583333333333333, 0.03125]").get_text()
    assert_equal(message, "未设置", "楼层户型图删除验证通过")
except:
    print("Error")
else:
    print("Ok")

poco("com.thinkhome.v3:id/toolbar_btn_back").click()
poco("com.thinkhome.v3:id/toolbar_btn_back").click()
poco("android:id/tabs").child("android.widget.RelativeLayout")[1].click()

#户型图操作：长按
poco("com.thinkhome.v3:id/clickable_image_view").long_click()
try:
    message=poco("android:id/alertTitle").get_text()
    assert_equal(message, "1F", "户型图长按验证通过")
except:
    print("Error")
else:
    print("Ok")
finally:
    poco(text="取消").click()

# # 户型图操作：双击
# poco("com.thinkhome.v3:id/clickable_image_view").double_click()
# try:
#     message=poco("com.thinkhome.v3:id/title_text").get_text()
#     assert_equal(message, "一层", "户型图双击验证通过")
# except:
#     print("Error")
# else:
#     print("Ok")
# finally:
#     poco("com.thinkhome.v3:id/toolbar_btn_back").click()
#
# #户型图操作：单击设置区域
# poco("com.thinkhome.v3:id/clickable_image_view").click()
# try:
#     message=poco("com.thinkhome.v3:id/title_text").get_text()
#     assert_equal(message, "一层餐厅", "户型图单击设置区域验证通过")
# except:
#     print("Error")
# else:
#     print("Ok")
# finally:
#     poco("com.thinkhome.v3:id/toolbar_btn_back").click()
'''
