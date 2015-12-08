/**
 * The javascript using in the search page.
 * @author TCSASSEMBLER
 * @version 1.0
 */
"use strict";

$(document).ready(function() {
    // load the first page data
    var searcher = new Searcher({});

    // // load the first page
    // searcher.search();

    var searchTable = new AsteroidTable($('.search-list-table'));
    searchTable.changePageCallBack = function(pageIndex) {
        searcher.pageNumber = pageIndex;
        searcher.search();
    };

    // 他这个sort只是比较了当前页面的项,这里还是应该用ajax来搞定
    searchTable.onSortColumn = function(sortBy, sortType) {
        // if (sortBy == 'timestamp') {
        //     searcher.sortBy = 'timestamp'
        //     searcher.sortType = sortType
        //     searcher.search()
        //     return
        // }

        // if (sortBy == 'rightAscension') {
            searcher.sortBy = sortBy;
            // item.frames[0].rightAscension
            searcher.sortType = sortType;
            searcher.search();
        //     return
        // }

        // var rows = []
        // $('.search-list-table tbody tr').each(function() {
        //     rows.push($(this).clone(true, true))
        // })
        // $('.search-list-table tbody').html('')

        // var columnIndex = 0
        // var index = 0
        // $('.search-list-table thead').find('th').each(function() {

        //     if ($(this).data('sort-by') == sortBy) {
        //         columnIndex = index
        //     }
        //     index++
        // })

        // rows.sort(function(item1, item2) {
        //     var v1 = item1.find("td:eq(" + columnIndex + ")").text()
        //     var v2 = item2.find("td:eq(" + columnIndex + ")").text()
        //     var t = v1 < v2 ? (-1) : (v1 > v2 ? 1 : 0)

        //     if (sortType == 'DESC') {
        //         t = -1 * t
        //     }
        //     return t
        // })
        // for (var i = 0; i < rows.length; i++) {
        //     $('.search-list-table tbody').append(rows[i])
        // }

        // searchTable.renderSortColumns(sortBy, sortType)

    };
    searchTable.renderCell = function(item, columnIndex, cell) {
        var text = "";
        if (columnIndex === 0) {
            text = formatDate(item.timestamp, 'MM/dd/yyyy');
        } else if (columnIndex === 1) {
            text = formatDate(item.timestamp, 'hh:mma');
        } else if (columnIndex === 2) {
            text = formatHMS(item.frames[0].rightAscension);
        } else if (columnIndex === 3) {
            text = formatDMS(item.frames[0].declination);
        } else if (columnIndex === 4) {
            text = formatLatitude(item.frames[0].observationLatitude);
        } else if (columnIndex === 5) {
            text = formatLogitude(item.frames[0].observationLongitude);
        } else if (columnIndex === 6) {
            text = item.submitted ? "Yes" : "No";
            cell.removeClass("blue-text");
            if (item.submitted) {
                cell.addClass("green-text");
            } else {
                cell.addClass("red-text");
            }
        }

        cell.text(text);
        cell.closest('tr').addClass('clickable');
        cell.closest('tr').data('item-id', item.id);
    };
    $(document).on('click', '.search-list-table tbody tr', function() {
        window.location.href = '/detectionItems/' + $(this).data('item-id');
    });

    function Searcher(criteria) {
        this.pageSize = 11;
        this.pageNumber = 1;
        this.sortBy = 'timestamp';
        this.sortType = 'DESC';
        var that = this;
        this.search = function() {
            var options = $.extend(criteria, {
                    pageSize: that.pageSize,
                    pageNumber: that.pageNumber,
                    sortBy: that.sortBy,
                    sortType: that.sortType});
            // $.ajax({
            //     url:'/search/detectionItems?' + $.param(options),
            //     type: "GET",
            //     headers: {
            //         'Accept': 'application/json'
            //     },
            //     dataType : 'json',
            //     success:function(result) {
            //         searchTable.renderTable(result.values)
            //         searchTable.renderPaging(result.totalPages, result.pageNumber)
            //         searchTable.renderSortColumns(that.sortBy, that.sortType)
            //     },
            //     error: function() {
            //         alert('error failed...')
            //     }
            // })
            var result = getSearchData(criteria);
            searchTable.renderTable(result.values);
            searchTable.renderPaging(result.totalPages, result.pageNumber);
            searchTable.renderSortColumns(that.sortBy, that.sortType);
        };
    }

    // load the first page
    searcher.search();

   $(document).on('click', '.search-filter', function() {
        var that = this;
        function hideFilter() {
            $(".filter-panel").addClass("hidden");
            $(that).removeClass("filter-on");
            $(".scrollwrapper").removeClass("shorter");
        }
        function showFilter() {
            $(".filter-panel").removeClass("hidden");
            $(that).addClass("filter-on");
            $(".scrollwrapper").addClass("shorter");
        }
         if ($(this).hasClass('filter-on')) {
            hideFilter();
         } else {
            showFilter();
         }

   });

    $(document).on('click', '.do-filter-btn', function() {
        searcher = new Searcher(getFilterCriteria());
        searcher.search();
    });

    // the filter
    AnyTime.picker('dateStart', {format: "%m/%d/%Y"});
    AnyTime.picker('dateEnd', {format: "%m/%d/%Y"});
    AnyTime.picker('timeStart', {format: "%h:%i %p"});
    AnyTime.picker('timeEnd', {format: "%h:%i %p"});

    // 增加 clear
    $('.AnyTime-pkr').each(function() {
        var dashLine = $('<div class="dash-separate-line"></div>');
        var clearBtn = $('<button>Clear</button>');
        clearBtn.addClass('date-clear-btn');
        $(this).append(dashLine);
        $(this).append(clearBtn);
    });
    // 清空input
    $('#AnyTime--dateStart').on('click', '.date-clear-btn', function() {
         $('#dateStart').val('').change();
    });
    $('#AnyTime--dateEnd').on('click', '.date-clear-btn', function() {
        $('#dateEnd').val('').change();
    });
    $('#AnyTime--timeStart').on('click', '.date-clear-btn', function() {
        $('#timeStart').val('').change();
    });
    $('#AnyTime--timeEnd').on('click', '.date-clear-btn', function() {
        $('#timeEnd').val('').change();
    });
    $('#dateStart, #dateEnd').on('change', function() {
        var startDateStr = $('#dateStart').val();
        var endDateStr = $('#dateEnd').val();
        if (startDateStr && endDateStr) {
            var startDate = new Date(startDateStr);
            var endDate = new Date(endDateStr);
            if (startDate > endDate) {
                alert("Start Date must be before the End Date");
                $(this).val('').change();
            }
        }
    });

    $('.AnyTime-pkr').each(function() {
        var el = $(this).find('.AnyTime-hdr');
        /*el.contents().filter(function(){
            return (this.nodeType == 3);
        }).remove();*/
        el.find('.AnyTime-x-btn').each(function() {
            $(this).contents().filter(function(){
                return (this.nodeType === 3);
            }).remove();
        });
    });
    $('#timeStart, #timeEnd').on('change', function() {
        var datePrefix = formatDate(new Date(), 'MM/dd/yyyy ');
        var startDateStr = datePrefix + ' ' + $('#timeStart').val();
        var endDateStr = datePrefix + ' ' +  $('#timeEnd').val();
        if ($('#timeStart').val() && $('#timeEnd').val()) {
            var startDate = new Date(startDateStr);
            var endDate = new Date(endDateStr);
            if (startDate > endDate) {
                alert("Start Time must be before the Time Date");
                $(this).val('').change();
            }
        }
    });

    function getFilterCriteria() {
        var criteria = {};
        if ($('#dateStart').val()) {
            criteria['dateStart'] = $('#dateStart').val();
        }
        if ($('#dateEnd').val()) {
            criteria['dateEnd'] = $('#dateEnd').val();
        }
        var datePrefix = formatDate(new Date(), 'MM/dd/yyyy ');
        if ($('#timeStart').val()) {

            var timeValue = new Date(datePrefix + $('#timeStart').val());

            criteria['hourStart'] = timeValue.getHours();
            criteria['minuteStart'] = timeValue.getMinutes();
        }
        if ($('#timeEnd').val()) {
            var timeValue = new Date(datePrefix + $('#timeEnd').val());
            criteria['hourEnd'] = timeValue.getHours();
            criteria['minuteEnd'] = timeValue.getMinutes();
        }

        var submitted = $('#submittedOptions option:selected').text();
        if (submitted === 'Yes') {
            criteria['submitted'] = true;
        }  else if (submitted === 'No') {
            criteria['submitted'] = false;
        }
        return criteria;
    }
})
