$(document).ready(function() {
  var calendarOptions = {
    'type': 'date',
    'color': 'link',
    'lang': 'zh_cn',
    'isRange': true,
    'dateFormat': 'YYYY-MM-DD',
    'showHeader': false,
    'cancelLabel': '取消',
    'clearLabel': '清除',
    'todayLabel': '今天'
  };

  var startTimestamp = $('[name="start"]').val();
  if (startTimestamp) {
    calendarOptions.startDate = new Date(parseInt(startTimestamp));
  }
  var endTimestamp = $('[name="end"]').val();
  if (endTimestamp) {
    calendarOptions.endDate = new Date(parseInt(endTimestamp));
  }

  var ideaDate = bulmaCalendar.attach('#idea-date', calendarOptions)[0];

  console.log(ideaDate);
  $('.datetimepicker-clear-button').attr('type', 'button');

  ideaDate.on('select:start', function(datepicker) {
    console.log('start');
    $('[name="start"]').val(datepicker.data.startDate.getTime());
  });

  ideaDate.on('select', function(datepicker) {
    $('[name="start"]').val(datepicker.data.startDate.getTime());
    $('[name="end"]').val(datepicker.data.endDate.getTime());
  });

  ideaDate.on('clear', function(datepicker) {
    $('[name="start"]').val('');
    $('[name="end"]').val('');
  });

  $('.add-idea').click(function() {
    $('#add-idea-modal').addClass('is-active');
  });

  function closeModal() {
    $('#add-idea-modal').removeClass('is-active');
    $('#title').val('');
    $('#title').removeClass('is-danger');
    $('#title-help').addClass('hidden');
    $('#description').val('');
    $('#description').removeClass('is-danger');
    $('#description-help').addClass('hidden');
  }

  $('#cancel-add-idea').click(function() {
    closeModal();
  });

  var isAdding = false;
  $('#submit-idea').click(function() {
    var title = $('#title').val();
    var description = $('#description').val();

    if (title === '' || !title) {
      $('#title').addClass('is-danger');
      $('#title-help').removeClass('hidden');
    } else if (description === '' || !description) {
      $('#description').addClass('is-danger');
      $('#description-help').removeClass('hidden');
    } else if (!isAdding) {
      isAdding = true;
      var csrftoken = $("[name=csrfmiddlewaretoken]").val();
      $.ajax({
        type: "POST",
        headers: { "X-CSRFToken": csrftoken },
        url: '/ideas/create/',
        data: {
          'title': title,
          'description': description
        },
        success: function (data) {
          if (data.is_success) {
            /*
            bulmaToast.toast({
              message: "创建成功！",
              type: "is-success",
              position: "top-center"
            });
            */
            isAdding = false;
            closeModal();
            window.location.href = '/ideas/list/';
          } else {
            bulmaToast.toast({
              message: "修改失败！",
              type: "is-danger",
              position: "top-center"
            });
            isAdding = false;
          }
        },
        error: function(response, error) {
          isAdding = false;
          console.log(error);
        }
      });
    }
  });

  $('#title').change(function() {
    $('#title').removeClass('is-danger');
    $('#title-help').addClass('hidden');
  });

  $('#description').change(function() {
    $('#description').removeClass('is-danger');
    $('#description-help').addClass('hidden');
  });

  function goToPage(page) {
    pageUrl = '?page=' + page;
    var keywords = $('input[name="keywords"]').val();
    if (keywords) {
      pageUrl += '&keywords=' + keywords;
    }
     window.location.href = pageUrl;
  }

  $('#first-page').click(function() {
    var page = $(this).attr('data-page');
    goToPage(page);
  });

  $('#previous-page').click(function() {
    var page = $(this).attr('data-page');
    goToPage(page);
  });

  $('#next-page').click(function() {
    var page = $(this).attr('data-page');
    goToPage(page);
  });

  $('#last-page').click(function() {
    var page = $(this).attr('data-page');
    goToPage(page);
  });
});
