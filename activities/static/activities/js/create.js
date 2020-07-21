$(document).ready(function() {
  // For datetime picker
  var calendarOptions = {
    'type': 'datetime',
    'color': 'link',
    'lang': 'zh_cn',
    'dateFormat': 'YYYY-MM-DD',
    'showHeader': false,
    'validateLabel': '确定',
    'cancelLabel': '取消',
    'clearLabel': '清除',
    'todayLabel': '今天',
    'minDate': new Date()
  };

  var ideaDate = bulmaCalendar.attach('[name="end_datetime"]', calendarOptions)[0];

  ideaDate.on('select', function(datepicker) {
    $('.datetimepicker-dummy-wrapper').removeClass('is-danger');
    $('#end-datetime-help').text('');
    $('#end-datetime-help').addClass('hidden');
  });

  $('.datetimepicker-clear-button').attr('type', 'button');
  // End for datetime picker

  // For upload image
  var optionNode = '<div class="column is-one-third">' +
                     '<div class="card option">' +
                       '<div class="card-image">' +
                         '<label class="file-label option-image-label">' +
                           '<input ' +
                             'class="file-input"' +
                             'type="file"' +
                             'accept="image/jpeg, image/png"' +
                             'name="option_image"' +
                           '/>' +
                           '<span class="file-cta upload-box">' +
                             '<span class="file-icon">' +
                               '<i class="fa fa-upload"></i>' +
                             '</span>' +
                             '<span class="file-label">' +
                               '点击上传图片' +
                             '</span>' +
                           '</span>' +
                         '</label>' +
                         '<figure class="image is-4by3 is-hidden image-box">' +
                           '<img class="option-image" />' +
                           '<div class="actions is-hidden">' +
                             '<a ' +
                               'class="button is-primary is-light preview-image"' +
                               'title="预览图片"' +
                             '>' +
                               '<span class="icon">' +
                                 '<i class="fa fa-eye" aria-hidden="true"></i>' +
                               '</span>' +
                             '</a>' +
                             '<a ' +
                               'class="button is-primary is-light clear-image"' +
                               'title="删除图片"' +
                             '>' +
                               '<span class="icon">' +
                                 '<i class="fa fa-trash" aria-hidden="true"></i>' +
                               '</span>' +
                             '</a>' +
                           '</div>' +
                         '</figure>' +
                       '</div>' +
                       '<div class="card-content">' +
                         '<div class="content">' +
                           '<input class="input" name="option_content" placeholder="图片描述">' +
                         '</div>' +
                       '</div>' +
                       '<footer class="card-footer">' +
                         '<a href="#" class="card-footer-item has-text-danger delete-option">删除</a>' +
                       '</footer>' +
                     '</div>' +
                     '<p class="help option-help is-danger hidden"></p>' +
                   '</div>';

  function addOption() {
    $('.option-container').append(optionNode);
  }

  var initialOptionAmount = 2;
  for (var i = 0; i < initialOptionAmount; i ++) {
    addOption();
  }

  $('.add-option-icon').click(function() {
    addOption();
  });

  $('.option-container').on('click', '.delete-option', function() {
    console.log($('.delete-option').length);
    if ($('.delete-option').length < 3) {
      alert('至少两个选项！');
      return;
    }

    var isSure = confirm('确认删除此选项！');
    if (isSure) {
      $(this).parent().parent().parent().remove();
    } else {
      console.log('cancel delete option');
    }
  });

  $('.option-container').on('change', '[name=option_image]', function() {
    console.log('option image change');
    var optionNode = $(this).parent().parent().parent();
    var optionHelpNode = optionNode.parent().find('.option-help');
    var content = optionNode.find('[name=option_content]').val();
    if (content === '' || !content) {
      optionHelpNode.text('请输入图片描述！');
    } else {
      optionHelpNode.text('');
      optionNode.removeClass('is-danger');
      optionHelpNode.addClass('hidden');
    }

    if (this.files && this.files[0]) {
      var reader = new FileReader();

      var imageNode = optionNode.find('.option-image');
      var figureNode = optionNode.find('figure.image');
      var uploadNode = optionNode.find('.option-image-label');
      reader.onload = function (e) {
        imageNode.attr('src', e.target.result);
        figureNode.removeClass('is-hidden');
        uploadNode.addClass('is-hidden');
      };

      reader.readAsDataURL(this.files[0]);
    }
  });

  $('.option-container').on('click', '.clear-image', function() {
    var isSure = confirm('确认删除图片！');
    if (isSure) {
      var imageBoxNode = $(this).parent().parent();
      var cardImageNode = imageBoxNode.parent();
      imageBoxNode.addClass('is-hidden');
      imageBoxNode.find('.option-image').attr('src', '');
      cardImageNode.find('[name=option_image]').val('');
      cardImageNode.find('.option-image-label').removeClass('is-hidden');
    } else {
      console.log('cancel clear image');
    }
  });
  // End for upload image

  // For submit form
  $('form.activity-form').submit(function() {
    var isValid = true;
    var title = $('[name=title]').val();
    if (title === '' || !title) {
      isValid = false;
      $('[name=title]').addClass('is-danger');
      $('#title-help').text('请输入主题！');
      $('#title-help').removeClass('hidden');
    }

    var endDatetime = $('[name=end_datetime]').val();
    if (endDatetime === '' || !endDatetime) {
      isValid = false;
      $('').addClass('is-danger');
      $('#end-datetime-help').text('请选择截止时间！');
      $('#end-datetime-help').removeClass('hidden');
    } else if (new Date() > new Date(endDatetime)) {
      isValid = false;
      $('.datetimepicker-dummy-wrapper').addClass('is-danger');
      $('#end-datetime-help').text('截止时间须大于当前时间！');
      $('#end-datetime-help').removeClass('hidden');
    }

    var options = $('.option');

    $('.option').each(function() {
      var image = $(this).find('[name=option_image]').val();
      var content = $(this).find('[name=option_content]').val();

      var optionHelp = '';
      var isImageEmpty = false;
      if (image === '' || !image) {
        isImageEmpty = true;
        optionHelp = '请上传图片！';
      }

      var isContentEmpty = false;
      if (content === '' || !content) {
        isContentEmpty = true;
        optionHelp = '请输入图片描述！';
      }

      if (isImageEmpty && isContentEmpty) {
        optionHelp = '请上传图片并输入图片描述！';
      }

      if (isImageEmpty || isContentEmpty) {
        isValid = false;
        var optionHelpNode = $(this).parent().find('.option-help');
        optionHelpNode.text(optionHelp);
        optionHelpNode.removeClass('hidden');
        $(this).addClass('is-danger');
      }
    });

    return isValid;
  });

  $('[name=title]').change(function() {
    $('[name=title]').removeClass('is-danger');
    $('#title-help').text('');
    $('#title-help').addClass('hidden');
  });

  $('.option-container').on('change', '[name=option_content]', function() {
    console.log('option content change');
    var optionNode = $(this).parent().parent().parent();
    var optionHelpNode = optionNode.parent().find('.option-help');
    var image = optionNode.find('[name=option_image]').val();
    if (image === '' || !image) {
      optionHelpNode.text('请上传图片！');
    } else {
      optionHelpNode.text('');
      optionNode.removeClass('is-danger');
      optionHelpNode.addClass('hidden');
    }
  });
  // End for submit form

  // For leave page warning

  /*
  window.onload = function() {
    window.addEventListener("beforeunload", function (e) {
      if (formSubmitting) {
        return undefined;
      }

      var confirmationMessage = '离开后你所做的更改将不被保存！';

      (e || window.event).returnValue = confirmationMessage; //Gecko + IE
      console.log((e || window.event).returnValue);
      return confirmationMessage; //Gecko + Webkit, Safari, Chrome etc.
    });
  };
  */
  // End for leave page warning
});
