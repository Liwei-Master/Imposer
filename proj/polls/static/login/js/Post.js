
// 记录已经输入的数据到cookie






var _handle='';//储存电话是否填写正确

		$(function(){

			$(".signup-form input").on("focus",function(){

				$(this).parent().addClass("border");

			});

			$(".signup-form input").on("blur",function(){

				$(this).parent().removeClass("border");

			})

			//注册方式切换

			$(".signup-select").on("click",function(){

				var _text=$(this).text();

				var $_input=$(this).prev();

				$_input.val('');

				if(_text=="手机注册"){

					$(".signup-tel").fadeIn(200);

					$(".signup-email").fadeOut(180);

					$(this).text("邮箱注册");

					$_input.attr("placeholder","手机号码");

					$_input.attr("onblur","verify.verifyMobile(this)");

					$(this).parents(".form-group").find(".error-notic").text("手机号码格式不正确")



				}

				if(_text=="邮箱注册"){

					$(".signup-tel").fadeOut(180);

					$(".signup-email").fadeIn(200);

					$(this).text("手机注册");

					$_input.attr("placeholder","邮箱");

					$_input.attr("onblur","verify.verifyEmail(this)");

					$(this).parents(".form-group").find(".error-notic").text("邮箱格式不正确")

				}

			});

			//步骤切换

			var _boxCon=$(".box-con");

			$(".move-login").on("click",function(){

				$(_boxCon).css({

					'marginLeft':0

				})

			});

			$(".move-signup").on("click",function(){

				$(_boxCon).css({

					'marginLeft':-280

				})

			});

			$(".move-other").on("click",function(){

				$(_boxCon).css({

					'marginLeft':-560

				})

			});

			$(".reset").on("click",function(){

				$(_boxCon).css({

					'marginLeft':-560

				})

			});

			$("body").on("click",".move-addinf",function(){

				$(_boxCon).css({

					'marginLeft':-1120

				})

			});



			//获取短信验证码

			var messageVerify=function (){

				$(".get-message").on("click",function(){

					if(_handle){

						$("#message-inf").fadeIn(100)

						$(this).html('<a href="javascript:;">下一步</a><img class="loading" src="images/loading.gif">').addClass("move-addinf");

					}

				});

			}();

		});



		//表单验证

		function showNotic(_this){

			$(_this).parents(".form-group").find(".error-notic").fadeIn(100);

            $(_this).focus();

		}//错误提示显示

		function hideNotic(_this){

			$(_this).parents(".form-group").find(".error-notic").fadeOut(100);

		}//错误提示隐藏

		var verify={

			verifyEmail:function(_this){

				var validateReg = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;

				var _value=$(_this).val();

            	if(!validateReg.test(_value)){

            		showNotic(_this)

            	}else{

            		hideNotic(_this)

            	}

			},//验证邮箱

			verifyMobile:function(_this){

				var validateReg = /^((\+?86)|(\(\+86\)))?1\d{10}$/;

				var _value=$(_this).val();

            	if(!validateReg.test(_value)){

            		showNotic(_this);

            		_handle=false;

            	}else{

            		hideNotic(_this);

            		_handle=true;

            	}

            	return _handle

			},//验证手机号码

			PasswordLenght:function(_this){

				var _length=$(_this).val().length;

				if(_length<6){

					showNotic(_this)

				}else{

            		hideNotic(_this)

            	}

			},//验证设置密码长度

			Name:function(_this){

				var _length=$(_this).val().length;

				if(_length < 1){

					showNotic(_this)

				}else{

            		hideNotic(_this)

            	}

			},//验证设置密码长度

			VerifyCount:function(_this){

				var _count="123456";

				var _value=$(_this).val();

				console.log(_value)

				if(_value!=_count){

					showNotic(_this)

				}else{

					hideNotic(_this)

				}

			}//验证验证码

		}


//登陆非空验证
$(document).ready(function(){
	$("#login").click(function(){
		var login = $('#email').val();
		var pwd = $('#password').val();
		if(login==''){
			alert("请填写邮箱")
		}else if(pwd==''){
			alert("请填写密码")
		}
     	else{
	    	alert("登陆成功")
		}
	})
});

// cookie
//记录已经输入的数据到cookie
function record(){
    if (document.getElementById("checkbox").checked)
    {
        var first_item = document.getElementById("email").value;
        document.cookie = "name" +"=" + first_item;
        var second_item = document.getElementById("password").value;
        document.cookie = first_item + "=" + second_item;

    }

}

//从cookie中取出对应的数据
function fill_in_auto(first_row_item){
  var cookies = document.cookie.split(';');
  var items_left = first_row_item + "=";

  for (var i = 0; i < cookies.length; i++)
  {
    if (cookies[i].indexOf(items_left) == 1)
    {
      document.getElementById("password").value = cookies[i].substring(items_left.length + 1);
      var items_left = cookies[i].substring(items_left.length + 1) + "=";
      break;
    }
  }

}

// 监听函数
function checkCookie(){
    var input = document.getElementById("email").value;
    // document.getElementById("test").innerHTML = document.cookie;
    fill_in_auto(input);

}


