$(document).ready(function() {
  $.urlParam = function(name) {
	var results = new RegExp('[\?&]' + name + '=([^&#]*)').exec(window.location.href);
	return results[1] || 0;
  };

  var isLogin = false;
  $('#login-button').click(function() {
    var username = $('#username').val();
    var password = $('#password').val();

    if (username === '' || !username) {
      $('#username').addClass('is-danger');
      $('#username-help').text('请输入用户名！');
      $('#username-help').removeClass('hidden');
    } else if (password === '' || !password) {
      $('#password').addClass('is-danger');
      $('#password-help').text('请输入密码！');
      $('#password-help').removeClass('hidden');
    } else if (!isLogin) {
      isLogin = true;
      var csrftoken = $("[name=csrfmiddlewaretoken]").val();
      $.ajax({
        type: "POST",
        headers: { "X-CSRFToken": csrftoken },
        url: '/accounts/ajax_login/',
        data: {
          'username': username,
          'password': password
        },
        success: function (data) {
          if (data.is_success) {
            var nextUrls = new RegExp('[\?&]next=([^&#]*)').exec(window.location.href);
            window.location.href = nextUrls ? (nextUrls[1] || '/') : '/';
          } else if (data.invalid_username) {
            isLogin = false;
            $('#username').addClass('is-danger');
            $('#password').removeClass('is-danger');
            $('#password-help').addClass('hidden');
            $('#username-help').text('该用户不存在！');
            $('#username-help').removeClass('hidden');
          } else if (data.invalid_password) {
            isLogin = false;
            $('#password').addClass('is-danger');
            $('#username').removeClass('is-danger');
            $('#username-help').addClass('hidden');
            $('#password-help').text('密码错误！');
            $('#password-help').removeClass('hidden');
          }
        },
        error: function(response, error) {
          isLogin = false;
          console.log(error);
        }
      });
    }
  });

  $('#username').change(function() {
    $('#username').removeClass('is-danger');
    $('#username-help').addClass('hidden');
  });

  $('#password').change(function() {
    $('#password').removeClass('is-danger');
    $('#password-help').addClass('hidden');
  });
});
