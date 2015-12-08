/**
 * The javascript using in the common pages.
 * @author TCSASSEMBLER
 * @version 1.0
 */
"use strict";

function paddingZero(num, size) {
  var s = num + "";
  while (s.length < size) {
    s = "0" + s;
  }
  return s;
}

function formatDate(timestamp, formatString) {
  if (!formatString) {
    formatString = "MM/dd/yyyy hh:mma";
  }
  return $.format.date(new Date(timestamp), formatString);
}

function convertDMS(v, delims) {
  // assume v >= 0
  var d = Math.floor(v);
  var m = Math.floor((v - d) * 60);
  var s = Math.floor((v - d - m / 60) * 3600);
  return paddingZero(d, 2) + delims[0] + paddingZero(m) + delims[1] + paddingZero(s) + delims[2];
}

function formatHMS(v) {
  if (v >= 0) {
    return convertDMS(v, 'hms');
  } else {
    return '-' + convertDMS(-v, 'hms');
  }
}

function formatDMS(v) {
  if (v >= 0) {
    return '+' + convertDMS(v, '\xB0\'\"');
  } else {
    return '-' + convertDMS(-v, '\xB0\'\"');
  }
}

function formatLatitude(v) {
  if (v >= 0) {
    return convertDMS(v, '\xB0\'\"') + "N";
  } else {
    return convertDMS(-v, '\xB0\'\"') + "S";
  }
}

function formatLogitude(v) {
  if (v >= 0) {
    return convertDMS(v, '\xB0\'\"') + "E";
  } else {
    return convertDMS(-v, '\xB0\'\"') + "W";
  }
}


function AsteroidTable(tableContainer) {
  // 这是一种技巧,避免this指针出错
  var that = this;
  this.columnNum = tableContainer.find("thead tr:eq(0) th").length;
  this.renderCell = function(item, columnIndex, cell) {
    // should be override
  };
  this.changePageCallBack = function(pageIndex) {
    // should be override
  };
  this.onSortColumn = function(sortBy, sortType) {

  };
  var theTable = tableContainer.find('table');
  var pageSection = tableContainer.find('.page-section');
  this.renderTable = function(items) {
    // copy the row from template
    var tbody = theTable.find('tbody');
    // clear old
    tbody.html('');
    for (var i = 0; i < items.length; i++) {
      var item = items[i];
      var row = $('<tr></tr>');
      tbody.append(row);
      for (var j = 0; j < that.columnNum; j++) {
        var cell = $('<td></td>');
        cell.addClass('blue-text');
        row.append(cell);
        that.renderCell(item, j, cell);
      }
    }

  };

  this.renderSortColumns = function(sortBy, sortType) {
    theTable.find("thead th").each(function() {
      // clear old
      $(this).find("img.sort-arrow").remove();

      if ($(this).data('sort-by') === sortBy) {

        var arrow = $('<img />');
        arrow.addClass('sort-arrow');
        if (sortType === 'ASC') {
          arrow.addClass('sort-asc');
          arrow[0].src = 'i/up-arrow.png';
        } else {
          arrow.addClass('sort-desc');
          arrow[0].src = 'i/down-arrow.png';
        }
        $(this).append(arrow);
      } else {
        var arrow = $('<img />');
        arrow.addClass('sort-arrow');
        arrow[0].src = 'i/sortable-arrow.png';
        $(this).append(arrow);
      }
    });
  };

  this.renderPaging = function(totalPages, pageNumber) {
    if (pageSection === null) {
      return;
    }
    // clear old
    pageSection.html('');
    if (totalPages === 0) {
      return;
    }

    var btn = createPageBtn(1, "|<");
    if (pageNumber <= 1) {
      // disable the prev button
      btn.addClass("disabled");
    }
    pageSection.append(btn);

    var prevPage = pageNumber - 1 >= 1 ? pageNumber - 1 : 1;
    btn = createPageBtn(prevPage, "<");
    if (pageNumber <= 1) {
      // disable the prev button
      btn.addClass("disabled");
    }
    pageSection.append(btn);

    var btnsNum = 8;
    var beginIndex = pageNumber - parseInt(btnsNum / 2);
    if (beginIndex <= 1) {
      beginIndex = 1;
    }
    var endIndex = beginIndex + btnsNum;
    if (endIndex > totalPages) {
      endIndex = totalPages;
    }
    if (beginIndex !== 1) {
      btn = createPageBtn(beginIndex - 1, '...');
      pageSection.append(btn);
    }
    for (var i = beginIndex; i <= endIndex; i++) {
      btn = createPageBtn(i, i + "");
      if (i === pageNumber) {
        btn.addClass('page-current-btn');
      }
      pageSection.append(btn);
    }
    if (endIndex !== totalPages) {
      btn = createPageBtn(endIndex + 1, '...');
      pageSection.append(btn);
    }
    var nextPage = pageNumber + 1 <= totalPages ? pageNumber + 1 : totalPages;
    btn = createPageBtn(nextPage, '>');
    if (pageNumber >= totalPages) {
      // disable the prev button
      btn.addClass("disabled");
    }
    pageSection.append(btn);

    btn = createPageBtn(totalPages, '>|');
    if (pageNumber >= totalPages) {
      // disable the prev button
      btn.addClass("disabled");
    }
    pageSection.append(btn);
  };

  function createPageBtn(gotoPage, text) {
    var btn = $('<a class="page-btn" href="javascript:void(0);"></a>').text(text);
    btn.data('goto', gotoPage);
    pageSection.append(btn);
    return btn;
  }

  tableContainer.on('click', '.page-btn', function() {
    if ($(this).hasClass("disabled")) {
      return;
    }
    that.changePageCallBack($(this).data('goto'));
  });

  tableContainer.on('click', 'thead th.sortable', function() {
    var sortBy = $(this).data('sort-by');
    var sortType = 'ASC';
    if ($(this).find('img.sort-arrow.sort-asc').length > 0) {
      sortType = 'DESC';
    }
    that.onSortColumn(sortBy, sortType);
  });

}

// function onSliderChange() {
//     var contrastValue = $('.constrast-slider .slider').slider("value")
//     var item = $('.jcarousel').jcarousel('first').find('img');
//     var vjsAPI = item.data('vintageJS');

//     vjsAPI = item.data('vintageJS');
//     vjsAPI.vintage({
//         contrast  : contrastValue
//     })
// }

$(document).ready(function() {
  // setup the headers
  $(document).on('click', '.header-tab', function() {
    var page = $(this).data('page');
    window.location.href = '/' + page;
  });

  // $('.slider').slider({"value": 0, "max":255, change:onSliderChange,
  //     slide: function() {
  //         var contrastValue = $('.constrast-slider .slider').slider("value")
  //         $('.customMarker').css('width', contrastValue / 255.0 * 100 + '%');
  //     }
  // });
  // $('.slider').prepend("<div class='customMarker'></div>");

  // $('.jcarousel img').each(function() {
  //     $(this).vintage({}, null)
  // })
});
