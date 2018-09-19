# -*- encoding=utf8 -*-
__author__ = "guhao"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco()

auto_setup(__file__)

start_app("com.thinkhome.v3")
sleep(5)

#注册:号码为空
poco("com.thinkhome.v3:id/tv_register").click()
poco("com.thinkhome.v3:id/register_password").set_text("123456")
poco("com.thinkhome.v3:id/register_verify").set_text("123456")
poco("com.thinkhome.v3:id/register_btn").click()
message = poco("android:id/message").get_text()
try:
    assert_equal(message,"手机号码不能为空","注册:号码为空")
except:
    print("error")
else:
    print("ok")
finally:
    poco("android:id/button3").click()

#注册:密码为空
poco("com.thinkhome.v3:id/register_phonenum").set_text("18312345678")
poco("com.thinkhome.v3:id/register_password").set_text("")
poco("com.thinkhome.v3:id/register_verify").set_text("123456")
poco("com.thinkhome.v3:id/register_btn").click()
message = poco("android:id/message").get_text()
try:
    assert_equal(message,"密码不能为空","注册:密码为空")
except:
    print("error")
else:
    print("ok")
finally:
    poco("android:id/button3").click()

#注册:确认密码为空
poco("com.thinkhome.v3:id/register_phonenum").set_text("18312345678")
poco("com.thinkhome.v3:id/register_password").set_text("123456")
poco("com.thinkhome.v3:id/register_verify").set_text("")
poco("com.thinkhome.v3:id/register_btn").click()
message = poco("android:id/message").get_text()
try:
    assert_equal(message,"确认密码不能为空","注册:确认密码为空")
except:
    print("error")
else:
    print("ok")
finally:
    poco("android:id/button3").click()


#注册:手机格式错误
poco("com.thinkhome.v3:id/register_phonenum").set_text("1")
poco("com.thinkhome.v3:id/register_password").set_text("123456")
poco("com.thinkhome.v3:id/register_verify").set_text("123456")
poco("com.thinkhome.v3:id/register_btn").click()
message = poco("android:id/message").get_text()
try:
    assert_equal(message,"手机号码格式不匹配","注册:手机号码格式不匹配")
except:
    print("error")
else:
    print("ok")
finally:
    poco("android:id/button3").click()

#注册:手机号已注册
poco("com.thinkhome.v3:id/register_phonenum").set_text("18368493627")
poco("com.thinkhome.v3:id/register_password").set_text("123456")
poco("com.thinkhome.v3:id/register_verify").set_text("123456")
poco("com.thinkhome.v3:id/register_btn").click()
message = poco("android:id/message").get_text()
try:
    assert_equal(message,"该账号已经被注册","注册:手机号已注册")
except:
    print("error")
else:
    print("ok")
finally:
    poco("android:id/button3").click()

#注册:密码小于6位
poco("com.thinkhome.v3:id/register_phonenum").set_text("18312345678")
poco("com.thinkhome.v3:id/register_password").set_text("12345")
poco("com.thinkhome.v3:id/register_verify").set_text("12345")
poco("com.thinkhome.v3:id/register_btn").click()
message = poco("android:id/message").get_text()
try:
    assert_equal(message,"密码长度不能少于6位","注册:密码小于6位")
except:
    print("error")
else:
    print("ok")
finally:
    poco("android:id/button3").click()

#注册:密码与确认密码不一致
poco("com.thinkhome.v3:id/register_phonenum").set_text("18312345678")
poco("com.thinkhome.v3:id/register_password").set_text("123456")
poco("com.thinkhome.v3:id/register_verify").set_text("1234567")
poco("com.thinkhome.v3:id/register_btn").click()
message = poco("android:id/message").get_text()
try:
    assert_equal(message,"两次密码不一致","注册:密码与确认密码不一致")
except:
    print("error")
else:
    print("ok")
finally:
    poco("android:id/button3").click()

#注册:验证码为空
poco("com.thinkhome.v3:id/register_phonenum").set_text("18312345678")
poco("com.thinkhome.v3:id/register_password").set_text("123456")
poco("com.thinkhome.v3:id/register_verify").set_text("123456")
poco("com.thinkhome.v3:id/register_btn").click()
poco("com.thinkhome.v3:id/btn_confirm").click()
message = poco("android:id/message").get_text()
try:
    assert_equal(message,"验证码不能为空","注册:验证码为空")
except:
    print("error")
else:
    print("ok")
finally:
    poco("android:id/button3").click()

#注册:验证码错误
poco("com.thinkhome.v3:id/et_verify").set_text("1")
poco("com.thinkhome.v3:id/btn_confirm").click()
message = poco("android:id/message").get_text()
try:
    assert_equal(message,"验证码错误","注册:验证码错误")
except:
    print("error")
else:
    print("ok")
finally:
    poco("android:id/button3").click()

# #登录体验账号:号码为空 9.18移除该用例
# poco("com.thinkhome.v3:id/et_phone").set_text("")
# poco("com.thinkhome.v3:id/et_veryfy").set_text("1234")
# poco("com.thinkhome.v3:id/btn_login").click()
# message = poco("android:id/message").get_text()
# assert_equal(message,"手机号码不能为空","登录体验账号:号码为空")
# poco("android:id/button3").click()

# #登录体验账号:验证码为空
# poco("com.thinkhome.v3:id/et_phone").set_text("18368493627")
# poco("com.thinkhome.v3:id/et_veryfy").set_text("")
# poco("com.thinkhome.v3:id/btn_login").click()
# message = poco("android:id/message").get_text()
# try:
#     assert_equal(message,"验证码不能为空","登录体验账号:验证码为空")
# except:
#     print("error")
# else:
#     print("ok")
# finally:
#     poco("android:id/button3").click()

#登录体验账号:验证码错误
poco("com.thinkhome.v3:id/toolbar_btn_back").click()
poco("com.thinkhome.v3:id/toolbar_btn_back").click()
poco("com.thinkhome.v3:id/tv_guest_login").click()
poco("com.thinkhome.v3:id/et_phone").set_text("18312345678")
poco("com.thinkhome.v3:id/tv_countdown").click()
poco("com.thinkhome.v3:id/et_veryfy").set_text("1")
poco("com.thinkhome.v3:id/btn_login").click()
message = poco("android:id/message").get_text()
try:
    assert_equal(message,"验证码错误","登录体验账号:验证码错误")
except:
    print("error")
else:
    print("ok")
finally:
    poco("android:id/button3").click()

keyevent("BACK")
# swipe((50,550),None,[0.6012, 0.0166])   #滑动返回无效，待改

#忘记密码:号码为空
poco("com.thinkhome.v3:id/tv_forgot_password").click()
poco("com.thinkhome.v3:id/btn_get_password").click()
message = poco("android:id/message").get_text()
try:
    assert_equal(message,"手机号码不能为空","忘记密码:号码为空")
except:
    print("error")
else:
    print("ok")
finally:
    poco("android:id/button3").click()

#忘记密码:账号格式错误
poco("com.thinkhome.v3:id/et_find_password").set_text("1")
poco("com.thinkhome.v3:id/btn_get_password").click()
message = poco("android:id/message").get_text()
try:
    assert_equal(message,"手机号码格式不匹配","忘记密码:账号格式错误")
except:
    print("error")
else:
    print("ok")
finally:
    poco("android:id/button3").click()

#忘记密码:账号未注册
poco("com.thinkhome.v3:id/et_find_password").set_text("18312345678")
poco("com.thinkhome.v3:id/btn_get_password").click()
message = poco("android:id/message").get_text()
try:
    assert_equal(message,"该账号尚未注册","忘记密码:账号未注册")
except:
    print("error")
else:
    print("ok")
finally:
    poco("android:id/button3").click()
    
#忘记密码:验证码为空
poco("com.thinkhome.v3:id/tv_forgot_password").click()
poco("com.thinkhome.v3:id/et_find_password").set_text("18368493627")
poco("com.thinkhome.v3:id/btn_get_password").click()
poco("com.thinkhome.v3:id/et_new_password").set_text("123456")
poco("com.thinkhome.v3:id/et_confirm_password").set_text("123456")
poco("com.thinkhome.v3:id/btn_modify").click()
message = poco("android:id/message").get_text()
try:
    assert_equal(message,"验证码不能为空","忘记密码:验证码为空")
except:
    print("error")
else:
    print("ok")
finally:
    poco("android:id/button3").click()

#忘记密码:新密码为空
poco("com.thinkhome.v3:id/et_verify_code").set_text("1234")
poco("com.thinkhome.v3:id/et_new_password").set_text("")
poco("com.thinkhome.v3:id/et_confirm_password").set_text("123456")
poco("com.thinkhome.v3:id/btn_modify").click()
message = poco("android:id/message").get_text()
try:
    assert_equal(message,"密码不能为空","忘记密码:新密码为空")
except:
    print("error")
else:
    print("ok")
finally:
    poco("android:id/button3").click()

#忘记密码:确认密码为空
poco("com.thinkhome.v3:id/et_verify_code").set_text("1234")
poco("com.thinkhome.v3:id/et_new_password").set_text("123456")
poco("com.thinkhome.v3:id/et_confirm_password").set_text("")
poco("com.thinkhome.v3:id/btn_modify").click()
message = poco("android:id/message").get_text()
try:
    assert_equal(message,"确认密码不能为空","忘记密码:确认密码为空")
except:
    print("error")
else:
    print("ok")
finally:
    poco("android:id/button3").click()

#忘记密码:验证码错误
poco("com.thinkhome.v3:id/et_verify_code").set_text("1")
poco("com.thinkhome.v3:id/et_new_password").set_text("123456")
poco("com.thinkhome.v3:id/et_confirm_password").set_text("123456")
poco("com.thinkhome.v3:id/btn_modify").click()
message = poco("android:id/message").get_text()
try:
    assert_equal(message,"验证码错误","忘记密码:验证码错误")
except:
    print("error")
else:
    print("ok")
finally:
    poco("android:id/button3").click()

#忘记密码:新密码小于6位
poco("com.thinkhome.v3:id/et_verify_code").set_text("1234")
poco("com.thinkhome.v3:id/et_new_password").set_text("12345")
poco("com.thinkhome.v3:id/et_confirm_password").set_text("12345")
poco("com.thinkhome.v3:id/btn_modify").click()
message = poco("android:id/message").get_text()
try:
    assert_equal(message,"密码长度不能少于6位","忘记密码:新密码小于6位")
except:
    print("error")
else:
    print("ok")
finally:
    poco("android:id/button3").click()

#忘记密码:新密码与确认密码不一致
poco("com.thinkhome.v3:id/et_verify_code").set_text("1234")
poco("com.thinkhome.v3:id/et_new_password").set_text("123456")
poco("com.thinkhome.v3:id/et_confirm_password").set_text("1234567")
poco("com.thinkhome.v3:id/btn_modify").click()
message = poco("android:id/message").get_text()
try:
    assert_equal(message,"两次密码不一致","忘记密码:新密码与确认密码不一致")
except:
    print("error")
else:
    print("ok")
finally:
    poco("android:id/button3").click()

poco("com.thinkhome.v3:id/toolbar_btn_back").click()
poco("com.thinkhome.v3:id/toolbar_btn_back").click()

#登录:账号为空
poco("com.thinkhome.v3:id/et_password").set_text("123456")
poco("com.thinkhome.v3:id/btn_login").click()
message = poco("android:id/message").get_text()
try:
    assert_equal(message,"账号不能为空","登录:账号为空")
except:
    print("error")
else:
    print("ok")
finally:
    poco("android:id/button3").click()

#登录:密码为空
poco("com.thinkhome.v3:id/et_account").set_text("18368493627")
poco("com.thinkhome.v3:id/et_password").set_text("")
poco("com.thinkhome.v3:id/btn_login").click()
message = poco("android:id/message").get_text()
try:
    assert_equal(message,"密码不能为空","登录:密码为空")
except:
    print("error")
else:
    print("ok")
finally:
    poco("android:id/button3").click()

#登录:账号格式不正确
poco("com.thinkhome.v3:id/et_account").set_text("1")
poco("com.thinkhome.v3:id/et_password").set_text("123456")
poco("com.thinkhome.v3:id/btn_login").click()
message = poco("android:id/message").get_text()
try:
    assert_equal(message,"手机号码格式不匹配","登录:账号格式不正确")
except:
    print("error")
else:
    print("ok")
finally:
    poco("android:id/button3").click()

#登录:账号未注册
poco("com.thinkhome.v3:id/et_account").set_text("18312345678")
poco("com.thinkhome.v3:id/et_password").set_text("123456")
poco("com.thinkhome.v3:id/btn_login").click()
message = poco("android:id/message").get_text()
try:
    assert_equal(message,"该账号尚未注册","登录:账号未注册")
except:
    print("error")
else:
    print("ok")
finally:
    poco("android:id/button3").click()

#登录:账号或密码错误
poco("com.thinkhome.v3:id/et_account").set_text("18368493627")
poco("com.thinkhome.v3:id/et_password").set_text("098765")
poco("com.thinkhome.v3:id/btn_login").click()
message = poco("android:id/message").get_text()
try:
    assert_equal(message,"身份验证失败，请检查用户名和密码是否填写正确","账号或密码错误")
except:
    print("error")
else:
    print("ok")
finally:
    poco("android:id/button3").click()

#登录:成功登录
poco("com.thinkhome.v3:id/et_account").set_text("18368493627")
poco("com.thinkhome.v3:id/et_password").set_text("123456")
poco("com.thinkhome.v3:id/btn_login").click()
poco(text="10").click()
sleep(2)
message = poco("com.thinkhome.v3:id/tv_currenthouse").get_text()
try:
    assert_equal(message,"10","登录:成功登录")
except:
    print("error")
else:
    print("ok")

#登录:退出登录
poco(text="设置").click()
poco(text="账号管理").click()
poco("com.thinkhome.v3:id/logout").click()
poco("android:id/button1").click()
if poco("com.thinkhome.v3:id/btn_login").exists:
    message = "已退出登录"
try:
    assert_equal(message,"已退出登录","登录:退出登录")
except:
    print("error")
else:
    print("ok")