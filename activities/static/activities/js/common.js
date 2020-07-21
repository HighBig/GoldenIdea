$(document).ready(function() {
  $('.option-container').on('mouseenter', '.image-box', function () {
      $(this).find('.actions').removeClass('is-hidden');
  }).on('mouseleave', '.image-box', function () {
      $(this).find('.actions').addClass('is-hidden');
  });

  $('.option-container').on('click', '.preview-image', function() {
    $('#image-modal').addClass('is-active');
    $('.modal-image').attr(
      'src',
      $(this).parent().parent().find('.option-image').attr('src')
    );
  });

  $('.modal-close').click(function() {
    $('#image-modal').removeClass('is-active');
  });

  $(document).click(function(event) {
    if (!$(event.target).closest(".preview-image").length) {
      $('#image-modal').removeClass('is-active');
    }
  });
});
