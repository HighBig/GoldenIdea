$(document).ready(function() {
  $('form.vote-form').submit(function() {
    var checkedCount = $("input[name='option_id']:checked").length;
    if (checkedCount < 1) {
      alert('请勾选您喜欢的选项！');
      return false;
    } else if (checkedCount > remaining_vote_num) {
      alert('您的投票超出限制，您还能投' + remaining_vote_num + '票！');
      return false;
    }
  });
});
