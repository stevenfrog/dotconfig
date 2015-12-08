// From Workday_Data_Toolkit_Schema_and_Workbook_Frontend

## dataTables
**jquery.dataTables.min.js**
**dataTables 是jquery的一个插件, 主要用于显示table, 很方便**
```js
// 下面是一段table config 的定义
var tableConfigs = {
    // datagatheringWorkbooks table config
    datagatheringWorkbooks : {
        dom : 'i<"wrapper"t>lp<"pages">',
        columns : [{
                    "title": "#",
                    "orderable": false,
                    "width": "19px",
                    "defaultContent": "",
                    "indexRow": true
                }, {
                    "data" : "name",
                    "title" : "Workbook Name",
                    "width" : "201px",
                    "customFilter" : {
                        "placeholder" : "Filter Workbook Name"
                    },
                    "render" : function(data, type, row) {
                        return '<a href="' + datactx + '/dataGatheringWorkbooks/'
                                + row['id'] + '">' + data + '</a>';
                    }
                }, {
                    "data" : "updatedBy",
                    "width" : "99px",
                    "title" : "Updated By"
                }, {
                    "data" : "updatedDate",
                    "title" : "Updated On",
                    "width" : "121px",
                    "render" : function(data) {
                        return formatDate(data, 'mm/dd/yyyy hh:MM AM');
                }, {
                    //"data": "dataType",
                    //"title": "Data Type",
                    //"render": function (data, type, row) {
                    //   var html = new Array();
                    //    var options = ["NUMBER","STRING","DATE","BOOLEAN","CURRENCY"];
                    //   var optionsShow = {"NUMBER":"Number","STRING":"String","DATE":"Date","BOOLEAN":"Boolean","CURRENCY":"Currency"};
                    //    if(row['options']) options = row['options'];
                    //    html.push('<select style="width:130px" name="data-type">');
                    //    html.push('<option>Select</option>');
                    //    html.push(options.map(function (option) {
                    //        return '<option '+(data===option? 'selected':'')+ ' value="' + option + '">' + optionsShow[option] + '</option>';
                    //    }).join(''));
                    //    html.push('</select>');
                    //    return html.join('');
                    //}
                }, {
                    "orderable" : true,
                    "title" : "Validation Status",
                    "width" : "126px",
                    "data" : "validationStatus"
                }, {
                    "orderable" : false,
                    "title" : "Action",

                    "defaultContent" : '<a class="link view" href="javascript:;">View</a><a data="validate"  class="link" href="javascript:;">Validate</a><a class=" download link" href="javascript:;">DownLoad</a><a class="action delete" href="javascript:;">Remove</a>',
                    "render" : function(data, type, row) {

                        if (row.validationStatus == "Valid"
                                || row.validationStatus == "Invalid")
                            return '<a class="link view" href="javascript:;">View</a><a data="validate"  class="link disabled" href="javascript:;">Validate</a><a class=" download link" href="javascript:;">DownLoad</a><a class="action delete" href="javascript:;">Remove</a>';
                        else
                            return '<a class="link view disabled" href="javascript:;">View</a><a data="validate"  class="link" href="javascript:;">Validate</a><a class=" download link" href="javascript:;">DownLoad</a><a class="action delete" href="javascript:;">Remove</a>';
                    }
                }],
        language : {
            info : 'Displaying&nbsp;&nbsp;_START_&nbsp;&nbsp;-&nbsp;&nbsp;_END_&nbsp;&nbsp;'
                    + 'of&nbsp;&nbsp;_TOTAL_&nbsp;&nbsp;Data Gathering <span class="user_info">Workbooks</span>&nbsp;:'
        },
        order : [[1, 'asc']],

        ajax : {
            url : datactx + '/search/dataGatheringWorkbooks',
            type : 'GET',
            contentType : 'application/json',
            cache : false,
            data : {
                'pageSize' : 0,
                'pageNumber' : 0,
                sortBy : 'name',
                sortType : 'ASC',
                'projectId' : projectId
            },
            dataSrc : "values",
            error : errorHandler
        },
        "infoCallback" : function(settings, start, end, max, total, pre) {
            return 'Displaying&nbsp;&nbsp;' + (total == 0 ? 0 : start)
                    + '&nbsp;&nbsp;-&nbsp;&nbsp;' + end + '&nbsp;&nbsp;'
                    + 'of&nbsp;&nbsp;' + total + '&nbsp;&nbsp;Data Gathering  '
                    + (total > 1 ? 'Workbooks' : 'Workbook') + '&nbsp;:';
        },
        "initComplete": function(settings, json) {
            // We have to add index only when data table finished
            $("#tab-gathering-workbooks table.dataTable tbody tr td:first-child").each(function (i, cell) {
                cell.innerHTML = i+1;
            });
        }
    }
}

// 这里还有一段对table的初始化
// Table initialization routine
function initTable(elem, config) {
    // Common config extension
    config.language = config.language || {};
    config.language.infoEmpty = config.language.infoEmpty || 'No Display Data';
    config.language.lengthMenu = '<strong>Show :</strong> _MENU_ Per Page';
    config.language.paginate = {
        previous: 'Prev'
    };

    var table = elem.dataTable(config);
    var wrapper = elem.closest('.dataTables_wrapper');

    $('.pages', wrapper).text('Pages :');
    $('.dataTables_length select', wrapper).customSelect();

    var hasCustomFilter = false;
    var filter = config.columns.map(function (column, index) {
        var result = ['<th class="filter-cell">'];
        if (column.customFilter) {
            hasCustomFilter = true;
            if (column.customFilter.select) {
                result.push('<select class="filter" data-index="' + index + '">');
                result.push('<option value="">All</option>');
                result.push(column.customFilter.select.map(function (option) {
                    return '<option value="' + option + '">' + option + '</option>';
                }).join(''));
                result.push('</select>');
            } else {
                result.push('<label class="input"><input type="text" class="filter" placeholder="' +
                    (column.customFilter.placeholder || '') +
                    '" data-index="' + index + '"/><span class="clear"></span><span class="placeholder">' +
                    (column.customFilter.placeholder || '') +
                    '</span></label>');
            }

        }
        result.push('</th>');
        return result.join('');
    });

    if (hasCustomFilter) {
        $(elem)
            .on('init.dt', function () {
                $(table.DataTable().table().header()).append('<tr>' + filter.join('') + '</tr>');
                $('select', table.DataTable().table().header()).customSelect();
            });

        $(elem)
            .on('change keyup', '.filter', function () {
                var columnIndex = this.getAttribute('data-index');
                table.DataTable().column(columnIndex).search(this.value, true).draw();
            });
    }

    config.columns.map(function (column, index) {
        if (column.indexRow) {
            $(elem).on( 'order.dt search.dt', function () {
                table.DataTable().column(index, {search:'applied', order:'applied'}).nodes().each( function (cell, i) {
                    cell.innerHTML = i+1;
                });
            });
        }
        if (column.indexCheckbox) {
            $(elem).on( 'draw.dt', function () {
                table.DataTable().column(index, {search:'applied', order:'applied'}).nodes().each( function (cell, i) {
                    cell.setAttribute('data-eindex',i);
                });
            });
        }
    });

    return table;
}

// 显示table, if else 主要用于如果table已经渲染过啦, 就只需要重新draw一次
// 不能删除后, 重复构建, 会出问题, 而且浪费资源
var tableElem = $('#'+tab).find('table');
if (!tableElem.hasClass('dataTable')) {
    initTable($('#gathering-workbooks'), tableConfigs.datagatheringWorkbooks);
}else{
    tableElem.DataTable().page( 0 ).draw( false );
}
```

