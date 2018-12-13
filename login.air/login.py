# -*- encoding=utf8 -*-
__author__ = "guhao"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco()

auto_setup(__file__)

start_app("com.thinkhome.v3")
sleep(5)


def register(phonenum, password, verify):
    poco("com.thinkhome.v3:id/register_phonenum").set_text(phonenum)
    poco("com.thinkhome.v3:id/register_password").set_text(password)
    poco("com.thinkhome.v3:id/register_verify").set_text(verify)
    poco("com.thinkhome.v3:id/register_btn").click()


def forget_password(phonenum):
    poco("com.thinkhome.v3:id/et_find_password").set_text(phonenum)
    poco("com.thinkhome.v3:id/btn_get_password").click()


def reset_password(verify, new_password, confirm_password):
    poco("com.thinkhome.v3:id/et_verify_code").set_text(verify)
    poco("com.thinkhome.v3:id/et_new_password").set_text(new_password)
    poco("com.thinkhome.v3:id/et_confirm_password").set_text(confirm_password)
    poco("com.thinkhome.v3:id/btn_modify").click()


def login(account, password):
    poco("com.thinkhome.v3:id/et_account").set_text(account)
    poco("com.thinkhome.v3:id/et_password").set_text(password)
    poco("com.thinkhome.v3:id/btn_login").click()


def logout():
    poco("android:id/tabs").child("android.widget.RelativeLayout")[3].child("com.thinkhome.v3:id/tab_image").click()
    poco.scroll(direction='vertical', percent=0.3, duration=1.0)
    sleep(1)
    poco(text="账号管理").click()
    poco("com.thinkhome.v3:id/logout").click()
    poco("android:id/button1").click()
    while poco("com.thinkhome.v3:id/account_list").exists():
        poco("com.thinkhome.v3:id/account_list").child(
            "android.widget.RelativeLayout")[0].click()
        sleep(5)
        if poco("com.thinkhome.v3:id/house_list").exists():
            poco(
                "com.thinkhome.v3:id/house_list").child("android.widget.RelativeLayout")[0].click()
            sleep(10)
        logout()


# 初始化登录
try:
    if poco("com.thinkhome.v3:id/tv_currenthouse").exists():
        logout()
except BaseException:
    print("Error:初始化登录")

# 注册:号码为空
try:
    poco("com.thinkhome.v3:id/tv_welcome").click()
    poco("com.thinkhome.v3:id/tv_register").click()
    register("", "123456", "123456")
    message = poco("android:id/message").get_text()
    assert_equal(message, "手机号码不能为空", "注册:号码为空")
except BaseException:
    print("Error:注册号码为空")
finally:
    poco("android:id/button3").click()

# 注册:密码为空
try:
    register("18312345678", "", "123456")
    message = poco("android:id/message").get_text()
    assert_equal(message, "密码不能为空", "注册:密码为空")
except BaseException:
    print("Error:注册密码为空")
finally:
    poco("android:id/button3").click()

# 注册:确认密码为空
try:
    register("18312345678", "123456", "")
    message = poco("android:id/message").get_text()
    assert_equal(message, "确认密码不能为空", "注册:确认密码为空")
except BaseException:
    print("Error:注册确认密码为空")
finally:
    poco("android:id/button3").click()

# 注册:手机格式错误
try:
    register("1", "123456", "123456")
    message = poco("android:id/message").get_text()
    assert_equal(message, "手机格式不正确", "注册:手机格式不正确")
except BaseException:
    print("Error:注册手机格式错误")
finally:
    poco("android:id/button3").click()

# 注册:手机号已注册
try:
    register("18368493627", "123456", "123456")
    message = poco("android:id/message").get_text()
    assert_equal(message, "该账号已经被注册", "注册:手机号已注册")
except BaseException:
    print("Error:注册手机号已注册")
finally:
    poco("android:id/button3").click()

# 注册:密码小于6位
try:
    register("18312345678", "12345", "12345")
    message = poco("android:id/message").get_text()
    assert_equal(message, "密码长度不能少于6位", "注册:密码小于6位")
except BaseException:
    print("Error:#注册:密码小于6位")
finally:
    poco("android:id/button3").click()

# 注册:密码与确认密码不一致
try:
    register("18312345678", "123456", "1234567")
    message = poco("android:id/message").get_text()
    assert_equal(message, "两次密码不一致", "注册:密码与确认密码不一致")
except BaseException:
    print("Error:注册密码与确认密码不一致")
finally:
    poco("android:id/button3").click()

# 注册:验证码为空
try:
    register("18312345678", "123456", "123456")
    poco("com.thinkhome.v3:id/btn_confirm").click()
    message = poco("android:id/message").get_text()
    assert_equal(message, "验证码不能为空", "注册:验证码为空")
except BaseException:
    print("Error:注册验证码为空")
finally:
    poco("android:id/button3").click()

# 注册:验证码错误
try:
    poco("com.thinkhome.v3:id/et_verify").set_text("1")
    poco("com.thinkhome.v3:id/btn_confirm").click()
    message = poco("android:id/message").get_text()
    assert_equal(message, "验证码错误", "注册:验证码错误")
except BaseException:
    print("Error:注册验证码错误")
finally:
    poco("android:id/button3").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco("com.thinkhome.v3:id/tv_guest_login").click()

# 登录体验账号:号码为空
try:
    poco("com.thinkhome.v3:id/tv_countdown").click()
    message = poco("android:id/message").get_text()
    assert_equal(message, "手机号码不能为空", "登录体验账号:号码为空")
except BaseException:
    print("Error:登录体验账号号码为空")
finally:
    poco("android:id/button3").click()

# 登录体验账号:验证码错误
try:
    poco("com.thinkhome.v3:id/et_phone").set_text("18312345678")
    poco("com.thinkhome.v3:id/et_veryfy").set_text("1234")
    poco("com.thinkhome.v3:id/btn_login").click()
    message = poco("android:id/message").get_text()
    assert_equal(message, "验证码错误", "登录体验账号:验证码错误")
except BaseException:
    print("Error:登录体验账号验证码错误")
finally:
    poco("android:id/button3").click()
    keyevent("BACK")
    poco("com.thinkhome.v3:id/tv_forgot_password").click()

# 忘记密码:号码为空
try:
    forget_password("")
    message = poco("android:id/message").get_text()
    assert_equal(message, "手机号码不能为空", "忘记密码:号码为空")
except BaseException:
    print("Error:忘记密码号码为空")
finally:
    poco("android:id/button3").click()

# 忘记密码:账号格式错误
try:
    forget_password("183")
    message = poco("android:id/message").get_text()
    assert_equal(message, "手机格式不正确", "忘记密码:手机格式不正确")
except BaseException:
    print("Error:忘记密码账号格式错误")
finally:
    poco("android:id/button3").click()

'''
# 忘记密码:账号未注册
try:
    forget_password("18312345678")
    message = poco("android:id/message").get_text()
    assert_equal(message, "该账号尚未注册", "忘记密码:账号未注册")
except BaseException:
    print("Error:忘记密码账号未注册")
finally:
    poco("android:id/button3").click()
'''

# 忘记密码:验证码为空
try:
    forget_password("18368493627")
    reset_password("", "123456", "123456")
    message = poco("android:id/message").get_text()
    assert_equal(message, "验证码不能为空", "忘记密码:验证码为空")
except BaseException:
    print("Error:忘记密码验证码为空")
finally:
    poco("android:id/button3").click()

# 忘记密码:新密码为空
try:
    reset_password("1234", "", "123456")
    message = poco("android:id/message").get_text()
    assert_equal(message, "密码不能为空", "忘记密码:新密码为空")
except BaseException:
    print("Error:忘记密码新密码为空")
finally:
    poco("android:id/button3").click()

# 忘记密码:确认密码为空
try:
    reset_password("1234", "123456", "")
    message = poco("android:id/message").get_text()
    assert_equal(message, "确认密码不能为空", "忘记密码:确认密码为空")
except BaseException:
    print("Error:忘记密码确认密码为空")
finally:
    poco("android:id/button3").click()

# 忘记密码:验证码错误
try:
    reset_password("1234", "123456", "123456")
    message = poco("android:id/message").get_text()
    assert_equal(message, "验证码错误", "忘记密码:验证码错误")
except BaseException:
    print("Error:忘记密码验证码错误")
finally:
    poco("android:id/button3").click()

# 忘记密码:新密码小于6位
try:
    reset_password("1234", "123", "123")
    message = poco("android:id/message").get_text()
    assert_equal(message, "密码长度不能少于6位", "忘记密码:新密码小于6位")
except BaseException:
    print("Error:忘记密码新密码小于6位")
finally:
    poco("android:id/button3").click()

# 忘记密码:新密码与确认密码不一致
try:
    reset_password("1234", "123456", "1234567")
    message = poco("android:id/message").get_text()
    assert_equal(message, "两次密码不一致", "忘记密码:新密码与确认密码不一致")
except BaseException:
    print("Error:忘记密码新密码与确认密码不一致")
finally:
    poco("android:id/button3").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()
    poco("com.thinkhome.v3:id/toolbar_btn_back").click()

# 登录:账号为空
try:
    login("", "123456")
    message = poco("android:id/message").get_text()
    assert_equal(message, "账号不能为空", "登录:账号为空")
except BaseException:
    print("Error:登录账号为空")
finally:
    poco("android:id/button3").click()

# 登录:密码为空
try:
    login("18368493627", "")
    message = poco("android:id/message").get_text()
    assert_equal(message, "密码不能为空", "登录:密码为空")
except BaseException:
    print("Error:登录密码为空")
finally:
    poco("android:id/button3").click()

# 登录:账号格式不正确
try:
    login("183", "123456")
    message = poco("android:id/message").get_text()
    assert_equal(message, "手机格式不正确", "登录:手机格式不正确")
except BaseException:
    print("Error:登录账号格式不正确")
finally:
    poco("android:id/button3").click()

# 登录:账号未注册
try:
    login("18312345678", "123456")
    message = poco("android:id/message").get_text()
    assert_equal(message, "该账号尚未注册", "登录:账号未注册")
except BaseException:
    print("Error:登录账号未注册")
finally:
    poco("android:id/button3").click()

# 登录:账号或密码错误
try:
    login("18368493627", "1111112")
    message = poco("android:id/message").get_text()
    assert_equal(message, "身份验证失败，请检查用户名和密码是否填写正确", "登录：账号或密码错误")
except BaseException:
    print("Error:登录账号或密码错误")
finally:
    poco("android:id/button3").click()

# 登录:成功登录
try:
    login("18368493627", "123456")
    sleep(5)
    if poco("com.thinkhome.v3:id/house_list").exists():
        message1 = poco("com.thinkhome.v3:id/house_list").child("android.widget.RelativeLayout")[0].child("android.widget.LinearLayout").child("com.thinkhome.v3:id/name").get_text()
        poco("com.thinkhome.v3:id/house_list").child("android.widget.RelativeLayout")[0].click()
        sleep(10)
    else:
        message1 = poco("com.thinkhome.v3:id/tv_currenthouse").get_text()
    message2 = poco("com.thinkhome.v3:id/tv_currenthouse").get_text()
    assert_equal(message1, message2, "登录:成功登录")
except BaseException:
    print("Error:成功登录")

# 登录:退出登录
try:
    logout()
    if poco("com.thinkhome.v3:id/tv_welcome").exists:
        message = "已退出登录"
    else:
        message = "未退出登录"
    assert_equal(message, "已退出登录", "登录:退出登录")
except BaseException:
    print("Error:退出登录")
