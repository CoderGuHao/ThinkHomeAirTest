# -*- encoding=utf8 -*-
__author__ = "lu201"

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *

auto_setup(__file__)

#poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
poco = AndroidUiautomationPoco()

# open APP
# start_app('com.thinkhome.v3')
# sleep(5)

# open scenario list


def gotoScenario():
    poco("android:id/tabs").child("android.widget.RelativeLayout")[
        0].child("com.thinkhome.v3:id/tab_image").click()
    poco(text="场景").click()


def doInputPassword():
    poco("com.thinkhome.v3:id/et_password").set_text("1234")

# Add new scenario


def addScenario(ScenarioName, addMode):
    poco("com.thinkhome.v3:id/toolbar_btn_setting").click()

    if addMode == 0:
        poco(text="新增场景").click()
    elif addMode == 1:
        poco(text="根据当前自动生成").click()
    else:
        poco(text="取消").click()

    poco("com.thinkhome.v3:id/tv_name_value").set_text(ScenarioName)
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    sleep(5)
    try:
        if poco("com.thinkhome.v3:id/et_password").exists():
            doInputPassword()
    except BaseException:
        print("No passowrd find")


def exitAddScenario():
    poco("android:id/button3").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()


def gotoSceneSetting(scenarioName):
    # gotoScenario()
    # Find the scenario need to delete
    isNameExists = poco(text=scenarioName).exists()
    while not isNameExists:
        isNameExists = poco(text=scenarioName).exists()
        poco.scroll(direction='vertical', percent=0.3, duration=1.0)
        # snapshot()
    poco(text=scenarioName).long_click()
    poco(text="更多设置").click()


def deleteNewScenario(scenarioName):
    gotoSceneSetting(scenarioName)
    poco("com.thinkhome.v3:id/btn_delete").click()
    poco("android:id/button1").click()
    if poco("com.thinkhome.v3:id/et_password").exists():
        doInputPassword()

# 进入场景设置


def gotoSceneNameChange():
    poco("com.thinkhome.v3:id/tv_name").click()
    poco(text="回家").click()

# 场景名称修改


def doNameChange(scenarioName):
    poco("com.thinkhome.v3:id/tv_name").click()
    poco("com.thinkhome.v3:id/tv_name").set_text(scenarioName)
    poco("com.thinkhome.v3:id/toolbar_right_text").click()


# 新增场景：正确添加
try:
    gotoScenario()
    addScenario("新增测试场景", 0)
    sleep(3)
    newScenarioResult = poco(text="新增测试场景").exists()
    # print (newScenarioResult)
    while not newScenarioResult:
        poco.scroll(direction='vertical', percent=0.3, duration=1.0)
        newScenarioResult = poco(text="新增测试场景").exists()
        # snapshot()
    # resultScenario = poco(text="新增测试场景").get_text()
    assert_equal(newScenarioResult, True, "正确新增场景.")
except BaseException:
    print("Error:新增场景正确添加")
finally:
    if newScenarioResult:
        deleteNewScenario("新增测试场景")
        sleep(5)

# 新增场景：名称为空
try:
    addScenario("", 0)
    resultScenario = poco("android:id/message").get_text()
    assert_equal(resultScenario, "场景名称不能为空", "名称为空验证.")
except BaseException:
    print("Error:新增场景名称为空")
finally:
    exitAddScenario()

# 新增场景: 名称包含特殊字符 '<>&\
try:
    addScenario("&", 0)
    resultScenario = poco("android:id/message").get_text()
    assert_equal(resultScenario, "数据包含特殊字符", "特殊字符&验证.")
except BaseException:
    print("Error:新增场景名称包含特殊字符&")
finally:
    exitAddScenario()

# Verify: <>
try:
    addScenario("<>", 0)
    resultScenario = poco("android:id/message").get_text()
    assert_equal(resultScenario, "数据包含特殊字符", "特殊字符<>验证.")
except BaseException:
    print("Error:新增场景名称包含特殊字符<>")
finally:
    exitAddScenario()

# Verify:'
try:
    addScenario("'", 0)
    resultScenario = poco("android:id/message").get_text()
    assert_equal(resultScenario, "数据包含特殊字符", "特殊字符'验证.")
except BaseException:
    print("Error:新增场景名称包含特殊字符'")
finally:
    exitAddScenario()

# Verify:\
try:
    addScenario("\\", 0)
    resultScenario = poco("android:id/message").get_text()
    assert_equal(resultScenario, "数据包含特殊字符", r"特殊字符\验证.")
except BaseException:
    print("Error: 新增场景名称包含特殊字符\\")
finally:
    exitAddScenario()

# 根据当前自动生成:名称为空
try:
    addScenario("", 1)
    resultScenario = poco("android:id/message").get_text()
    assert_equal(resultScenario, "场景名称不能为空", "根据当前自动生成 名称为空验证.")
except BaseException:
    print("Error:根据当前自动生成名称为空")
finally:
    exitAddScenario()

# 根据当前自动生成:正确新增
try:
    addScenario("自动生成", 1)
    isExitAutoGenerate = poco(text="自动生成").exists()
    while not isExitAutoGenerate:
        poco.scroll(direction='vertical', percent=0.3, duration=1.0)
        isExitAutoGenerate = poco(text="自动生成").exists()
        # snapshot()
    # resultScenario = poco(text="自动生成").get_text()
    assert_equal(isExitAutoGenerate, True, "根据当前自动生成：正确新增验证.")
except BaseException:
    print("Error:根据当前自动生成正确新增")

try:
    # 场景删除
    if resultScenario:
        deleteNewScenario("自动生成")
        sleep(5)
    resultScenario = poco(text="自动生成").exists()
    assert_equal(resultScenario, False, "场景删除验证.")
except BaseException:
    print("Error:场景删除")

# 场景设置：修改类型
try:
    addScenario("新增测试场景", 0)
    gotoSceneSetting("新增测试场景")
    gotoSceneNameChange()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco("com.thinkhome.v3:id/et_password").exists():
        doInputPassword()
    snapshot(msg="场景设置：修改类型验证.")
    sleep(2)
except BaseException:
    print("Error:场景设置修改类型")

# 场景设置：修改图标-拍照
try:
    gotoSceneNameChange()
    poco("com.thinkhome.v3:id/img_photo").click()
    poco(text="拍照").click()
    poco("com.huawei.camera:id/shutter_button").click()
    sleep(2)
    poco("com.huawei.camera:id/btn_done").click()
    poco("com.thinkhome.v3:id/btn_crop").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco("com.thinkhome.v3:id/et_password").exists():
        doInputPassword()
    snapshot(msg="修改图标：拍照.")
except BaseException:
    print("Error:场景设置修改图标-拍照")

# 场景设置：修改图标-从相册选择
try:
    gotoSceneNameChange()
    poco("com.thinkhome.v3:id/img_photo").click()
    poco(text="从相册选择").click()
    poco("com.android.documentsui:id/grid").child("android.widget.FrameLayout")[
        1].child("com.android.documentsui:id/icon_thumb").click()
    poco("com.android.documentsui:id/grid").child("android.widget.FrameLayout")[
        3].child("com.android.documentsui:id/icon_thumb").click()
    poco("com.thinkhome.v3:id/btn_crop").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco("com.thinkhome.v3:id/et_password").exists():
        doInputPassword()
    snapshot(msg="场景设置：修改图标，从相册选择 验证.")
except BaseException:
    print("Error:场景设置修改图标-从相册选择")

# 场景设置：修改图标-使用默认图标
try:
    gotoSceneNameChange()
    poco("com.thinkhome.v3:id/img_icon").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco("com.thinkhome.v3:id/et_password").exists():
        doInputPassword()
    snapshot(msg="场景设置：修改图标-使用默认图标 验证.")
except BaseException:
    print("Error:场景设置修改图标-使用默认图标")

# 场景设置：修改名称，为空
try:
    gotoSceneNameChange()
    doNameChange("")
    resultScenario = poco("android:id/message").get_text()
    assert_equal(resultScenario, "名称不能为空", "场景名称为空 验证.")
except BaseException:
    print("Error:场景设置修改名称为空")
finally:
    poco("android:id/button3").click()

# 场景设置：修改名称，特殊字符
try:
    doNameChange("&")
    resultScenario = poco("android:id/message").get_text()
    assert_equal(resultScenario, "数据包含特殊字符", "场景名称为特殊字符& 验证.")
except BaseException:
    print("Error:场景设置修改名称特殊字符&")
finally:
    poco("android:id/button3").click()

# '
try:
    doNameChange("'")
    resultScenario = poco("android:id/message").get_text()
    assert_equal(resultScenario, "数据包含特殊字符", "场景名称为特殊字符' 验证.")
except BaseException:
    print("Error:场景设置修改名称特殊字符'")
finally:
    poco("android:id/button3").click()

# \
try:
    doNameChange("\\")
    resultScenario = poco("android:id/message").get_text()
    assert_equal(resultScenario, "数据包含特殊字符", r"场景名称为特殊字符\ 验证.")
except BaseException:
    print("Error: 场景设置修改名称特殊字符\\")
finally:
    poco("android:id/button3").click()

# <>
try:
    doNameChange("<>")
    resultScenario = poco("android:id/message").get_text()
    assert_equal(resultScenario, "数据包含特殊字符", "场景名称为特殊字符<> 验证.")
except BaseException:
    print("Error:场景设置修改名称特殊字符<>")
finally:
    poco("android:id/button3").click()

# 场景设置：修改名称，正确输入
try:
    doNameChange("自动化修改")
    resultScenario = poco("com.thinkhome.v3:id/tv_name").get_text()
    assert_equal(resultScenario, "自动化修改", "场景设置：修改名称 正确输入 验证.")
except BaseException:
    print("Error:场景设置修改名称正确输入")

# 添加定时
try:
    poco(text="定时").click()
    sleep(2)
    poco("com.thinkhome.v3:id/toolbar_btn_setting").click()
    poco("com.thinkhome.v3:id/open_checkbox").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    resultScenario = poco("android:id/message").get_text()
    assert_equal(resultScenario, "至少选择一个时间", "定时：没有选择任何定时 验证.")
except BaseException:
    print("Error:添加定时")
finally:
    # 定时：正确添加
    poco("android:id/button3").click()
    poco("com.thinkhome.v3:id/open_checkbox").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco("com.thinkhome.v3:id/ll_timing_empty").exists():
        resultScenario = False
    else:
        resultScenario = True
    assert_equal(resultScenario, True, "定时：没有选择任何定时 验证.")

# 修改定时：修改时间
try:
    poco("com.thinkhome.v3:id/tv_open").click()
    poco("com.thinkhome.v3:id/checkbox_monday").click()
    poco("com.thinkhome.v3:id/checkbox_tuesday").click()
    poco("com.thinkhome.v3:id/checkbox_wednesday").click()
    poco("com.thinkhome.v3:id/checkbox_thursday").click()
    poco("com.thinkhome.v3:id/checkbox_friday").click()
    poco("com.thinkhome.v3:id/open_time").click()
    poco("23").click()
    poco("30").click()
    poco("android:id/button1").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco("com.thinkhome.v3:id/et_password").exists():
        doInputPassword()
    sleep(2)
    resultScenario = poco("com.thinkhome.v3:id/tv_open_time").get_text()
    assert_equal(resultScenario, "23:30", "修改定时：修改时间 验证.")
except BaseException:
    print("Error:修改定时修改时间")

try:
    # 定时：日期验证
    resultScenario = poco("com.thinkhome.v3:id/tv_frequency").get_text()
    assert_equal(resultScenario, "工作日", "日期 验证.")
except BaseException:
    print("Error:修改定时日期")

# 定时：选择普通定时或日出日落定时
try:
    poco("com.thinkhome.v3:id/tv_open").click()
    poco("com.thinkhome.v3:id/radio_on_sunsets").click()
    poco("com.thinkhome.v3:id/sunset_checkbox_on").click()
    poco("com.thinkhome.v3:id/checkbox_single").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco("com.thinkhome.v3:id/et_password").exists():
        doInputPassword()
    sleep(2)
    if poco("com.thinkhome.v3:id/img_sunrise").exists():
        resultScenario = True
    else:
        resultScenario = False
    assert_equal(resultScenario, True, "日出日落 验证.")
except BaseException:
    print("Error:定时选择普通定时或日出日落定时")

# 定时停启用
try:
    poco("com.thinkhome.v3:id/switch_view").click()
    if poco("com.thinkhome.v3:id/et_password").exists():
        doInputPassword()
    snapshot(msg="定时启用验证.")
    sleep(2)
except BaseException:
    print("Error:定时启用")

try:
    poco("com.thinkhome.v3:id/switch_view").click()
    if poco("com.thinkhome.v3:id/et_password").exists():
        doInputPassword()
    snapshot(msg="定时停用验证.")
except BaseException:
    print("Error:定时停用")

# 删除定时
try:
    poco("com.thinkhome.v3:id/tv_open").long_click()
    poco(text="删除").click()
    sleep(2)
    if poco("com.thinkhome.v3:id/ll_timing_empty").exists():
        resultScenario = True
    else:
        resultScenario = False
    assert_equal(resultScenario, True, "删除定时 验证.")
except BaseException:
    print("Error:删除定时")

# 设备组合，不选择设备添加
try:
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco(text="设备组合").click()
    sleep(3)
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    sleep(5)
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco("com.thinkhome.v3:id/et_password").exists():
        doInputPassword()
    resultScenario = poco("android:id/message").get_text()
    assert_equal(resultScenario, "您至少需要选择一个设备", "设备组合，不选择设备添加.")
except BaseException:
    print("Error:设备组合，不选择设备添加")
finally:
    poco("android:id/button1").click()

try:
    # 正确添加设备
    poco("com.thinkhome.v3:id/expand_listview").child(
        "android.widget.RelativeLayout")[1].child("com.thinkhome.v3:id/checkbox").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco("com.thinkhome.v3:id/et_password").exists():
        doInputPassword()
    sleep(5)
    if poco("com.thinkhome.v3:id/listView").exists():
        resultScenario = True
    else:
        resultScenario = False
    assert_equal(resultScenario, True, "设备组合，正确添加验证.")
except BaseException:
    print("Error:正确添加设备")

# 设备组合：删除
try:
    while poco("com.thinkhome.v3:id/listView").exists():
        poco("com.thinkhome.v3:id/listView").child(
            "com.thinkhome.v3:id/item_layout")[0].long_click()
        poco(text="删除").click()
        if poco("com.thinkhome.v3:id/et_password").exists():
            doInputPassword()
        sleep(2)
    if poco("com.thinkhome.v3:id/listView").exists():
        resultScenario = False
    else:
        resultScenario = True
    print(resultScenario)
    assert_equal(resultScenario, True, "设备组合，删除 验证.")
except BaseException:
    print("Error:设备组合：删除")
finally:
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()

# 联动组合：不选择联动添加
try:
    poco(text="联动组合").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    sleep(5)
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco("com.thinkhome.v3:id/et_password").exists():
        doInputPassword()
    resultScenario = poco("android:id/message").get_text()
    assert_equal(resultScenario, "您至少需要选择一个联动", "联动组合：不选择联动添加 验证.")
except BaseException:
    print("Error:联动组合：不选择联动添加")
finally:
    poco("android:id/button3").click()

try:
    # 正确添加
    addLinkageCombination = poco("com.thinkhome.v3:id/xlistView").child("android.widget.RelativeLayout")[0].child(
        "com.thinkhome.v3:id/item_add_device_lv").child("com.thinkhome.v3:id/tv_device_text").get_text()
    poco("com.thinkhome.v3:id/xlistView").child("android.widget.RelativeLayout")[
        0].child("com.thinkhome.v3:id/tv_device_checked").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco("com.thinkhome.v3:id/et_password").exists():
        doInputPassword()
    sleep(5)
    resultScenario = poco("com.thinkhome.v3:id/tv_name").get_text()
    assert_equal(resultScenario, addLinkageCombination, "联动组合正确添加验证.")
except BaseException:
    print("Error:联动组合：正确添加")

try:
    # 修改联动动作
    poco("com.thinkhome.v3:id/tv_action").click()
    poco(text="启用").click()
    poco("android:id/button1").click()
    if poco("com.thinkhome.v3:id/et_password").exists():
        doInputPassword()
    resultScenario = poco("com.thinkhome.v3:id/tv_action").get_text()
    assert_equal(resultScenario, "启用", "联动组合：修改动作验证.")
except BaseException:
    print("Error:联动组合：修改动作验证")
finally:
    # 联动组合：删除
    poco("com.thinkhome.v3:id/img_icon").long_click()
    poco(text="删除").click()
    if poco("com.thinkhome.v3:id/et_password").exists():
        doInputPassword()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()

# 分享：正确云子分享
try:
    poco(text="分享").click()
    poco(text="Beacon").click()
    poco("com.thinkhome.v3:id/tv_device").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    sleep(2)
    resultScenario = poco("com.thinkhome.v3:id/value").get_text()
    assert_equal(resultScenario, "1", "云子正确分享.")
except BaseException:
    print("Error:分享：正确云子分享")

try:
    # 取消分享
    poco(text="Beacon").click()
    poco("com.thinkhome.v3:id/tv_device").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    sleep(2)
    resultScenario = poco("com.thinkhome.v3:id/value").get_text()
    assert_equal(resultScenario, "0", "云子取消分享.")
except BaseException:
    print("Error:分享：云子取消分享")
finally:
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()

# 开关绑定：
# 查看说明
try:
    poco(text="开关绑定").click()
    poco("com.thinkhome.v3:id/help").click()
    sleep(2)
    resultScenario = poco("com.thinkhome.v3:id/toolbar_tv_name").get_text()
    assert_equal(resultScenario, "开关绑定说明", "开关绑定：查看说明.")
except BaseException:
    print("Error:查看开关绑定说明")
finally:
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()

# 场景隐藏
try:
    poco(text="场景隐藏").click()
    poco(text="隐藏").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco("com.thinkhome.v3:id/et_password").exists():
        doInputPassword()
    resultScenario = poco("com.thinkhome.v3:id/setting_hide_pattern").child(
        "android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
    assert_equal(resultScenario, "已隐藏", "场景隐藏.")
except BaseException:
    print("Error:场景隐藏")

try:
    # 场景取消隐藏
    poco(text="场景隐藏").click()
    poco(text="正常显示").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco("com.thinkhome.v3:id/et_password").exists():
        doInputPassword()
    resultScenario = poco("com.thinkhome.v3:id/setting_hide_pattern").child(
        "android.widget.RelativeLayout").child("com.thinkhome.v3:id/value").get_text()
    assert_equal(resultScenario, "正常显示", "场景 正常显示.")
except BaseException:
    print("Error:场景取消隐藏")

# 日志
try:
    poco(text="日志").click()
    snapshot(msg="日志查看页面.")
except BaseException:
    print("Error:查看日志")
finally:
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco("com.thinkhome.v3:id/btn_delete").click()
    poco("android:id/button1").click()
    if poco("com.thinkhome.v3:id/et_password").exists():
        doInputPassword()

# 本地场景：正确新增
try:
    poco("android:id/tabs").child("android.widget.RelativeLayout")[
        3].child("com.thinkhome.v3:id/tab_image").click()
    poco(text="设备管理").click()
    sleep(2)
    isExitAutoGenerate = poco(text="ThinkID:97231665").exists()
    while not isExitAutoGenerate:
        poco.scroll(direction='vertical', percent=0.3, duration=1.0)
        isExitAutoGenerate = poco(text="ThinkID:97231665").exists()

    poco(text="ThinkID:97231665").click()
    sleep(2)
    poco("com.thinkhome.v3:id/toolbar_btn_setting").click()
    poco(text="本地场景").click()
    sleep(2)
    poco("com.thinkhome.v3:id/toolbar_btn_setting").click()
    poco("com.thinkhome.v3:id/tv_name_value").set_text("本地场景测试")
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco("com.thinkhome.v3:id/et_password").exists():
        doInputPassword()
    resultScenario = poco("com.thinkhome.v3:id/tv_device").get_text()
    assert_equal(resultScenario, "本地场景测试", "本地场景 正确新增.")
except BaseException:
    print("Error:本地场景新增")

# 本地场景：修改类型和名称
try:
    poco("com.thinkhome.v3:id/tv_device").long_click()
    poco(text="更多设置").click()
    poco("com.thinkhome.v3:id/tv_name").click()
    poco("com.thinkhome.v3:id/listView").child("android.widget.RelativeLayout")[
        2].child("com.thinkhome.v3:id/tv_device_checked").click()
    poco("com.thinkhome.v3:id/tv_name").set_text("本地场景修改")
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco("com.thinkhome.v3:id/et_password").exists():
        doInputPassword()
    sleep(2)
    snapshot(msg="本地场景类型修改图标 验证.")
    resultScenario = poco("com.thinkhome.v3:id/tv_name").get_text()
    assert_equal(resultScenario, "本地场景修改", "本地场景名修改 验证.")
except BaseException:
    print("Error:本地场景修改类型和名称")

# 本地场景：设备组合
try:
    poco(text="设备组合").click()
    sleep(5)
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    sleep(5)
    addLinkageCombination = poco(
        "com.thinkhome.v3:id/tv_device_text").get_text()
    poco("com.thinkhome.v3:id/listview").child("android.widget.RelativeLayout")[
        0].child("com.thinkhome.v3:id/tv_device_checked").click()
    poco("com.thinkhome.v3:id/toolbar_right_text").click()
    if poco("com.thinkhome.v3:id/et_password").exists():
        doInputPassword()
    sleep(2)
    resultScenario = poco("com.thinkhome.v3:id/tv_name").get_text()
    assert_equal(resultScenario, addLinkageCombination, "本地场景：设备组合 验证")
except BaseException:
    print("Error:本地场景添加设备组合")
finally:
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()

# 复制场景
try:
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco("com.thinkhome.v3:id/tv_device").long_click()
    poco(text="复制场景").click()
    poco("android:id/button1").click()
except BaseException:
    print("Error:本地场景复制")

# #本地场景：固化
# try:
#     poco(text="本地场景固化").click()
#     poco("com.thinkhome.v3:id/btn_add_local_scene").click()
#     sleep(5)
#     snapshot(msg="截图：本地场景固化验证.")
#     poco("com.thinkhome.v3:id/btn_confirm").click()
#     #重新进入页面验证是否固化成功
#     poco(text="本地场景固化").click()
#     resultScenario = poco(text="当前场景已固化").exists()
#     assert_equal(resultScenario, "当前场景已固化", "本地场景删除验证.")
#     #返回
#     poco("com.thinkhome.v3:id/toolbar_btn_back").click()
# except:
#     print("Error!")
#     poco("android:id/button3").click()
#     poco("com.thinkhome.v3:id/toolbar_btn_back").click()

# 本地场景：删除
try:
    deleteNewScenario("本地场景修改")
    resultScenario = poco(text="本地场景修改").exists()
    assert_equal(resultScenario, False, "本地场景删除验证.")
except BaseException:
    print("Error:删除本地场景")
finally:
    # 回到首页
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco("android:id/tabs").child("android.widget.RelativeLayout")[
        0].child("com.thinkhome.v3:id/tab_image").click()

# 场景控制：5秒内连续操作
try:
    poco(text="场景").click()
    poco(text="本地场景修改").click()
    poco("com.thinkhome.v3:id/switch_button").click()
    poco("com.thinkhome.v3:id/switch_button").click()
    resultScenario = poco("android:id/message").get_text()
    assert_equal(resultScenario, "场景操作过于频繁，同一场景连续两次操作时间间隔至少为5s", "5秒内连续操作验证.")
except BaseException:
    print("Error:场景控制5秒内连续操作")
finally:
    poco("android:id/button3").click()
    poco("com.thinkhome.v3:id/btn_back").click()

# 删除复制场景
try:
    deleteNewScenario("本地场景修改")
except BaseException:
    print("Error:删除复制场景")

# 全部调光控制
try:
    poco(text="全部调光").click()
    poco("com.thinkhome.v3:id/seek_bar").swipe([-0.0179, -0.6308])
    poco("com.thinkhome.v3:id/btn_back").click()
    poco("android:id/tabs").child("android.widget.RelativeLayout")[
        2].child("com.thinkhome.v3:id/tab_image").click()
    poco(text="灯光").click()
    state = poco("com.thinkhome.v3:id/scroll").child("android.widget.RelativeLayout")[
        0].child("com.thinkhome.v3:id/tv_status").get_text()
    assert_equal(state, "100%", "全部调光场景：100%")
except BaseException:
    print("Error:全部场景控制打开调光100%")
finally:
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco("android:id/tabs").child("android.widget.RelativeLayout")[
        0].child("com.thinkhome.v3:id/tab_image").click()


try:
    poco(text="全部调光").click()
    poco("com.thinkhome.v3:id/seek_bar").swipe([0.0, 0.6248])
    poco("com.thinkhome.v3:id/btn_back").click()
    poco("android:id/tabs").child("android.widget.RelativeLayout")[
        2].child("com.thinkhome.v3:id/tab_image").click()
    poco(text="灯光").click()
    state = poco("com.thinkhome.v3:id/scroll").child("android.widget.RelativeLayout")[
        0].child("com.thinkhome.v3:id/tv_status").get_text()
    assert_equal(state, "0%", "全部调光场景：0%")
except BaseException:
    print("Error:全部调光控制0%")
finally:
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco("android:id/tabs").child("android.widget.RelativeLayout")[
        0].child("com.thinkhome.v3:id/tab_image").click()
