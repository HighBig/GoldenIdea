$(document).ready(function() {
  // For infiniteScroll
  function getPageUrl(page) {
    pageUrl = '?page=' + page;
    var status = $('input[name="status"]').val();
    if (status) {
      pageUrl += '&status=' + status;
    }
    return pageUrl;
  }

  function getPagePath() {
    if (this.pageIndex < pageCount) {
      return getPageUrl(this.pageIndex + 1);
    }
  }

  if (pageCount > 1) {
    $('.activities').infiniteScroll({
      path: getPagePath,
      append: '.activity-item',
      status: '.page-load-status',
      prefill: true
    });
  }
  // End for infiniteScroll
});
