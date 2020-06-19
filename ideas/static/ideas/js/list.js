$(document).ready(function() {
  // For datetime picker
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

  $('.datetimepicker-clear-button').attr('type', 'button');

  ideaDate.on('select:start', function(datepicker) {
    console.log('start');
    $('[name="start"]').val(datepicker.data.startDate.getTime());
    $('[name="end"]').val(null);
  });

  ideaDate.on('select', function(datepicker) {
    $('[name="start"]').val(datepicker.data.startDate.getTime());
    $('[name="end"]').val(datepicker.data.endDate.getTime());
  });

  ideaDate.on('clear', function(datepicker) {
    $('[name="start"]').val('');
    $('[name="end"]').val('');
  });
  // End for datetime picker

  // Start for modal
  var isAddIdea = true;
  $('.add-idea').click(function() {
    isAddIdea = true;
    $('#idea-modal').addClass('is-active');
  });

  var currentIdeaId = null;
  var currentIdeaNode = null;
  $('.edit-idea').click(function() {
    isAddIdea = false;
    currentIdeaId = $(this).attr('data-idea-id');
    currentIdeaNode = $(this).parent().parent();
    $('#title').val($(this).attr('data-idea-title'));
    $('#description').val($(this).attr('data-idea-description'));
    $('#idea-modal').addClass('is-active');
  });

  function closeModal() {
    $('#idea-modal').removeClass('is-active');
    $('#title').val('');
    $('#title').removeClass('is-danger');
    $('#title-help').addClass('hidden');
    $('#description').val('');
    $('#description').removeClass('is-danger');
    $('#description-help').addClass('hidden');
  }

  $('#close-modal').click(function() {
    closeModal();
  });

  var isSubmitting = false;
  $('#submit-idea').click(function() {
    var title = $('#title').val();
    var description = $('#description').val();
    var data = {
      'title': title,
      'description': description
    };
    var url = '/ideas/create/';
    if (!isAddIdea) {
      data.id = currentIdeaId;
      url = '/ideas/edit/';
    }

    if (title === '' || !title) {
      $('#title').addClass('is-danger');
      $('#title-help').removeClass('hidden');
    } else if (description === '' || !description) {
      $('#description').addClass('is-danger');
      $('#description-help').removeClass('hidden');
    } else if (!isSubmitting) {
      isSubmitting = true;
      var csrftoken = $("[name=csrfmiddlewaretoken]").val();
      $.ajax({
        type: "POST",
        headers: { "X-CSRFToken": csrftoken },
        url: url,
        data: data,
        success: function (data) {
          if (data.is_success) {
            /*
            bulmaToast.toast({
              message: "创建成功！",
              type: "is-success",
              position: "top-center"
            });
            */
            isSubmitting = false;
            closeModal();
            if (isAddIdea) {
              window.location.href = '/ideas/list/';
            } else {
              currentIdeaNode.find('h4').text(title);
              currentIdeaNode.find('.idea-description').text(description);
            }
          } else {
            bulmaToast.toast({
              message: "操作失败！",
              type: "is-danger",
              position: "top-center"
            });
            isSubmitting = false;
          }
        },
        error: function(response, error) {
          isSubmitting = false;
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
  // End for modal
  
  // For accept idea
  $('.accept-idea').click(function() {
    var isAccept = confirm('确认采纳此建议！');
    if (isAccept) {
      var actionNode = $(this).parent();
      var ideaContainer = $(this).parent().parent();
      $.ajax({
        type: "GET",
        url: '/ideas/accept/' + $(this).attr('data-idea-id') + '/',
        success: function (data) {
          if (data.is_success) {
            /*
            bulmaToast.toast({
              message: "创建成功！",
              type: "is-success",
              position: "top-center"
            });
            */
            actionNode.remove();
            ideaContainer.append(
              '<div class="ribbon ribbon-top-right"><span>已采纳</span></div>'
            );
          } else {
            bulmaToast.toast({
              message: data.error_message,
              type: "is-error",
              position: "top-center"
            });
          }
        },
        error: function(response, error) {
          console.log(error);
        }
      });
    } else {
      console.log('calcel accept');
    }
  });
  // End for accept idea

  // For infiniteScroll
  function getPageUrl(page) {
    pageUrl = '?page=' + page;
    var department = $('input[name="department"]').val();
    if (department) {
      pageUrl += '&department=' + department;
    }
    var keywords = $('input[name="keywords"]').val();
    if (keywords) {
      pageUrl += '&keywords=' + keywords;
    }
    var start = $('input[name="start"]').val();
    if (start) {
      pageUrl += '&start=' + start;
    }
    var end = $('input[name="end"]').val();
    if (end) {
      pageUrl += '&end=' + end;
    }
    var order = $('input[name="order"]').val();
    if (order) {
      pageUrl += '&order=' + order;
    }

    return pageUrl;
  }

  function getPagePath() {
    if (this.pageIndex < pageCount) {
      return getPageUrl(this.pageIndex + 1);
    }
  }

  $('.ideas').infiniteScroll({
    path: getPagePath,
    append: '.idea-item',
    status: '.page-load-status',
  });
  // End for infiniteScroll
  
  // For sort
  $('.order').click(function() {
    var order = $('input[name="order"]').val();
    if (order === 'asc') {
      $('input[name="order"]').val('desc');
      $('.fa-long-arrow-up').addClass('is-light');
      $('.fa-long-arrow-down').removeClass('is-light');
    } else {
      $('input[name="order"]').val('asc');
      $('.fa-long-arrow-down').addClass('is-light');
      $('.fa-long-arrow-up').removeClass('is-light');
    }

    window.location.href = getPageUrl(1);
  });
  // End for sort
});
