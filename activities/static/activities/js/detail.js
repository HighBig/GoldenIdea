$(document).ready(function() {
  $('form.vote-form').submit(function() {
    var optionId = $("input[name='option_id']:checked").val();
    if (optionId === '' || !optionId) {
      alert('请勾选您喜欢的选项！');
      return false;
    }
  });
});
