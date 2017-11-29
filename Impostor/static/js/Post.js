//记录已经输入的数据到cookie
function record(){
    if (document.getElementById("checkbox").checked)
    {
        var first_item = document.getElementById("name").value;
        document.cookie = "name" +"=" + first_item;
        var second_item = document.getElementById("sex").value;
        document.cookie = first_item + "=" + second_item;
        var third_item = document.getElementById("appearance").value;
        document.cookie = second_item + "=" + third_item;
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
      document.getElementById("sex").value = cookies[i].substring(items_left.length + 1);
      var items_left = cookies[i].substring(items_left.length + 1) + "=";
      break;
    }
  }
  for (var i = 0; i < cookies.length; i++)
  {
    if (cookies[i].indexOf(items_left) == 1)
      {
        document.getElementById("appearance").value = cookies[i].substring(items_left.length + 1);
        break;
      }

  }
}

// 监听函数
function checkCookie(){
    var input = document.getElementById("name").value;
    // document.getElementById("test").innerHTML = document.cookie;
    fill_in_auto(input);

}

$('#submit').click(function(){
    var input_name = $('#username').val();
    var passwords = $('#keywords').val();
    $.ajax({
        url: "/login/", data: {'username': input_name, 'keywords': passwords}, type: 'POST',
        //success: function (arg) {
          //  $('#feedback').html("<p>"+"登陆失败"+"</p>")
        //}
    })

})
