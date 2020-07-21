$(document).ready(function() {
  $('#change-password').click(function() {
    $('#change-password-modal').addClass('is-active');
  });

  function closeModal() {
    $('#change-password-modal').removeClass('is-active');
    $('#password').val('');
    $('#password').removeClass('is-danger');
    $('#password-help').addClass('hidden');
    $('#password-repeat').val('');
    $('#password-repeat').removeClass('is-danger');
    $('#password-repeat-help').addClass('hidden');
  }

  $('#cancel-change-password').click(function() {
    closeModal();
  });

  var isSubmit = false;
  $('#submit').click(function() {
    var password = $('#password').val();
    var passwordRepeat = $('#password-repeat').val();

    if (password === '' || !password) {
      $('#password').addClass('is-danger');
      $('#password-help').text('请输入新密码！');
      $('#password-help').removeClass('hidden');
    } else if (passwordRepeat === '' || !passwordRepeat) {
      $('#password-repeat').addClass('is-danger');
      $('#password-repeat-help').text('请再次输入新密码！');
      $('#password-repeat-help').removeClass('hidden');
    } else if (password != passwordRepeat) {
      $('#password-repeat').addClass('is-danger');
      $('#password-repeat-help').text('两次输入密码不同！');
      $('#password-repeat-help').removeClass('hidden');
    } else if (!isSubmit) {
      isSubmit = true;
      var csrftoken = $("[name=csrfmiddlewaretoken]").val();
      $.ajax({
        type: "POST",
        headers: { "X-CSRFToken": csrftoken },
        url: '/accounts/change_password/',
        data: {
          'password': password
        },
        success: function (data) {
          if (data.is_success) {
            bulmaToast.toast({
              message: "修改成功！",
              type: "is-success",
              position: "top-center"
            });
            closeModal();
          } else {
            bulmaToast.toast({
              message: "修改失败！",
              type: "is-danger",
              position: "top-center"
            });
            isSubmit = false;
          }
        },
        error: function(response, error) {
          isSubmit = false;
          console.log(error);
        }
      });
    }
  });

  $('#password').change(function() {
    $('#password').removeClass('is-danger');
    $('#password-help').addClass('hidden');
  });

  $('#password-repeat').change(function() {
    $('#password-repeat').removeClass('is-danger');
    $('#password-repeat-help').addClass('hidden');
  });

  var clickBurger = false;
  $('.navbar-burger[role="button"]').click(function() {
    if (clickBurger) {
      clickBurger = false;
      $(this).removeClass('is-active');
      $('#navbar-content').removeClass('is-active');
    } else {
      clickBurger = true;
      $(this).addClass('is-active');
      $('#navbar-content').addClass('is-active');
    }
  });
});
