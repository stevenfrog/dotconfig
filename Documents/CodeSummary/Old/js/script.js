// Workday_Data_Toolkit_Schema_and_Workbook_Frontend

// 这段是用xhr上传文件的例子
/**
 * Ajax upload the schemaDefinition file to server only.
 */
function ajaxUploadFile(fileName) {
    // Set up the request.
    var xhr = new XMLHttpRequest();
    var fileHtmlId = "schemaFile";

    // Open the connection.
    xhr.open('POST', datactx +  '/extract/schemaDefinitions/external?projectId='+projectId+'&fileHtmlId='+fileHtmlId, true);

    var formData = new FormData();

    var fileSelect = document.getElementById(fileHtmlId);

    // Get the selected files from the input
    var files = fileSelect.files;

    // Files
    formData.append(fileHtmlId, files[0], files[0].name);

    // Set up a handler for when the request finishes.
    xhr.onload = function () {
        if (xhr.status === 200) {
            // File uploaded.
            if(xhr.response.indexOf('<div class="error-content">') > 0){
                showErrorContent(xhr.response);
            }else if(xhr.response.indexOf('form class="login-form"') > 0){
                window.location.href = datactx + '/login';
            }else{
                var popup = $('#message-fileupload-popup');
                $("span.blue-name", popup).text(files[0].name);
                popups.show(popup, function (result) {
                    if (result === 'cancel') {
                        window.location.href = datactx + '/projects/'+ $("#projectId").val() + "?tab=tab-schema-input-files";
                    }
                });
            }

        }else{
            alert('An error occurred while uploading file!');
        }
    };

    xhr.onerror = function () {
        alert('The server is no response while uploading file!');
    };

    // Send the Data.
    xhr.send(formData);
}

// jsp文件部分
<div class="row select-file-row">
    <p>Select Input File</p>
    <div class="file-container">
        <input type="text" name="schemaFileText" readonly>
        <input type="file" name="schemaFile" id="schemaFile">
        <a href="javascript:;" class="action-browse">Browse</a>
    </div>
    <span class="validation_errors"></span>
</div>

// 补充browse file的部分
//browse file
$(".file-container :file").css("opacity", "0.001");
$(".file-container").on("click", ".action-browse", function(){
    $(this).closest(".file-container").find(":file").trigger("click");
});

// Java端的Controller并不复杂
@RequestMapping(value = "extract/schemaDefinitions/external", method = RequestMethod.POST)
@ResponseStatus(HttpStatus.OK)
@ResponseBody
public List<SchemaDefinition> extractFromInputFile(@RequestParam long projectId, @RequestParam String fileHtmlId,
        MultipartHttpServletRequest request)
    throws WDTServiceException, IOException {
    ...
    MultipartFile file = request.getFile(fileHtmlId);
    ...
}

===============================================================================

// 这里是popups的设计
// 它设计啦一个popups类专门控制popup的显示
function popupInit() {
    var resultCallback;

    $(document)
        .on('click', '.popup-close, .popup .popup-actions .button', function () {
            // 知道是关闭或点击啦按钮, 都会跳到这里
            var popup = $(this).closest('.popup');

            var errorSpan = $("span.validation_errors", popup);

            // 如果popup id是某个, 进行一些必要的处理
            // 这里主要是错误的提示
            if(popup.attr('id') === 'reset-password-popup' && $(this).data('result') == 'save') {
                return;
            }
            if(popup.attr('id') === 'upload-file-popup' && ($(this).data('result') == 'add' || $(this).data('result') == 'generate')){
                var fileName = $('input:text[name="schemaFileText"]', popup).val();

                if(fileName.trim().length === 0){
                    errorSpan.html("File is required").show();
                    return;
                }
            }
            if(!$(this).hasClass("never")){
                popups.hide(popup);
            }
        })
        .on('click', '.popup .popup-actions .button', function () {
            // 再次绑定popup-actions的按钮, 调用绑定的resultCallback上的函数
            // 有些按钮只能按一次, 需要清空resultCallback上的函数
            // 但如果有recall class就不用
            var popup = $(this).closest('.popup'),
                callback = popup.data('resultCallback');

            if (typeof callback === 'function') {
                callback(this.getAttribute('data-result'));
                if(popup.attr('id') == 'reset-password-popup' && $(this).data('result') == 'save') {
                    return;
                }
                if(!$(this).hasClass("recall")){
                    popup.data('resultCallback', null);
                }
            }
        });

    // 如果resize, 重新把窗口放到center
    $(window).on('resize scroll', function () {
        if (!displayedPopup) {
            return;
        }
        var popup = displayedPopup;
        if (popup.outerHeight() < $(window).height() - 30) {
            popups.center(popup);
        }
    });

    var displayedPopup = null;

    // 这里才是popups类, 并返回
    var popups = {
        show: function (id, callback) {
            var popup = $(id);
            $('.popup-shadow').show();
            popup.show();
            popup.data('resultCallback', callback);
            displayedPopup = popup;
            this.center(popup);
            return popup;
        },
        center: function (id) {
            var popup = $(id);
            popup.css({
                "margin-left": "-" + (popup.outerWidth() / 2) + 'px',
                "top": Math.max(($(window).scrollTop() + ($(window).height() - popup.outerHeight()) / 2), 15) + 'px'
            });
        },
        hide: function (id) {
            $(id).hide();
            if(typeof id==='undefined') $(".popup").hide();
            $('.popup-shadow').hide();
            $('.show-cases').hide();
            displayedPopup = null;
        }
    };
    return popups;
}

// popups初始化
var popups = popupInit();


// 这里是个标准的delete popup
<div id="delete-data-gathering-workbook-popup" class="popup no-table">
    <span class="popup-close"></span>
    <h2>
        Delete Data Gathering Workbook
    </h2>
    <div class="popup-content">
        <p>
            Are you sure you want to delete <span class="blue-name">Data Gathering Workbook Name</span>?
        </p>
    </div>
    <div class="popup-actions">
        <span class="button gray-button" data-result="cancel">Cancel</span>
        <span class="button blue-button" data-result="delete">Delete</span>
    </div>
</div>

// 触发的js 函数
// delete data gathering workbook
function deleteDataWorkbook(rows, table) {
    var templates = table.rows(rows).data(), userElems = templates.map(
            function(template) {
                return '<span class="blue-name">' + template.name + '</span>';
            });
    var popup = $('#delete-data-gathering-workbook-popup');
    $('.template-names', popup).html(userElems.join(', '));
    popups.show(popup, function(result) {
        if (result === 'delete') {

            var templateIds = [];
            templates.each(function(template) {
                    templateIds.push(template['id']);
                });

            $.ajax({
                    url : datactx + '/dataGatheringWorkbooks?ids='
                            + templateIds,
                    type : 'DELETE',
                    contentType : 'application/json',
                    cache : false,
                    success : function(data) {
                        // window.location = datactx + '/projects/'
                        // + $("#projectId").val()
                        // + '?tab=tab-gathering-workbooks';
                        table.rows(rows).remove().draw();
                    },
                    error : errorHandler
                });
        }
    });
}

===============================================================================

// 这是一个标准的JQuery AJAX请求
$.ajax({
    url : datactx + '/search/schemaInputFiles',
    type : 'GET',
    contentType : 'application/json',
    cache : false,
    async : false,   // 是否异步, false就是js必须等待, 默认为true, 异步调用, 不用等待返回
    data : {
        'projectId' : projectId,
        'pageSize' : 0,
        'pageNumber' : 0,
        sortBy : 'name',
        sortType : 'ASC'
    },
    success : function(res) {
        $.each(res.values, function(idx, schema) {
                var content = '<div class="input-group"><label class="radio"><input type="radio" name="sub-external-file" data="'
                    + schema.id + '"><span class="radio-wrapper"><span></span></span> '
                    + schema.name + '</label></div>';
                sdlist.append(content);


        });
    },
    error : errorHandler
});

===============================================================================

// jquery.dataTables.min.js
// dataTables 是jquery的一个插件, 主要用于显示table, 很方便
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

===============================================================================
// 错误处理
/**
 * The error handler.
 *
 * @param request the xml http request
 * @param status the status code
 * @param error the error object
 */
var errorHandler = function(request, status, error) {
    if($('#validation_errors, .login-form .error').length) {
        if(($('#create-new-project').length || $('#project-details').length) && (request.responseText.indexOf('project_name_key') >= 0)) {
            return $('#validation_errors, .login-form .error').html('Project name has been taken.').show();
        }
        if($('#create-new-user').length || $('#user-details').length) {
            if(request.responseText.indexOf('User_username_key') >= 0) {
                return $('#validation_errors, .login-form .error').html('Username has been taken.').show();
            }
            if(request.responseText.indexOf('User_email_key') >= 0) {
                return $('#validation_errors, .login-form .error').html('Email has been taken.').show();
            }
        }
        return $('#validation_errors, .login-form .error').html(request.responseText).show();
    }
    alert(request.responseText);
};

===============================================================================

// Selection action state handler
function updateSelectionActionState(table, selected) {
    // 这里是控制多选, 单选的部分
    // 只有在是多选时, 有些按钮才可用
    if (table.closest('.table-content').length) {
        $('.table-row-actions .selection-action').toggleClass('disabled', !selected);

        // checked is use to get how many table checked
        // but in fact updateSelectionActionState will be called in different place
        // so it sometimes return 0 when u just click one row, it only used when you click the checkbox for all
        // checked = $('tbody .selection input', table);
        // $('.table-row-actions .action-export').toggleClass('disabled', !(selected == 1) || (checked.length != 0));
    }

    // 每个row有一个tindex, 记录被选row的行数
    // 如果是在第一行或最后一行, 该行就不能上下移动
    if(selected===1){
        if(parseInt($('.table-row-actions .single-action.down').attr("tindex")) !== $(".dataTable tbody tr").length-1)
            $('.table-row-actions .single-action.down').toggleClass('disabled', !selected);
        if(parseInt($('.table-row-actions .single-action.up').attr("tindex")) !== 0){
            $('.table-row-actions .single-action.up').removeClass('disabled');
        }else{
            $('.table-row-actions .single-action.up').addClass('disabled');
        }
    }else{
        $('.table-row-actions .single-action').addClass('disabled');
    }
}

===============================================================================
// Table事件处理
//============================= Common event handlers ===============================================
$(function () {
    // Document 事件请都用$(function () {})；包裹, 可以减少全局量

    // Common page handlers
    $(document)
        // Table redraw handler (to clear all selection when table redrawn)
        .on('draw.dt', function (e) {
            var tableElem = $(e.target);

            $('.selection input', tableElem).prop('checked', false);

            var table = $(tableElem).DataTable(),
                info = table.page.info(),
                isContentTable = tableElem.closest('.table-content').length;

            tableElem.closest('.dataTables_wrapper').toggleClass('table-is-empty', !info.recordsTotal);
            if (isContentTable) {
                $('.table-row-actions').toggleClass('table-is-empty', !info.recordsTotal);
            }

            updateSelectionActionState(tableElem, false);
        })
        // Header selection checkbox change handler
        .on('change', '.dataTable thead .selection input', function () {
            var table = $(this).closest('.dataTable');
            $('tbody .selection input', table).prop('checked', this.checked);

            // Update selection action state when table in table-content block
            updateSelectionActionState(table, this.checked);
        });

    $('.table-content, .popup-content')
        // Table checkbox change handler
        .on('change', '.dataTable tbody .selection input', function () {
            var tIndex, table = $(this).closest('.dataTable').DataTable(),
                body = table.table().body(),
                checked = $('.selection input:checked', body);

                // 控制tindex
                tIndex = $('.selection input:checked', body).closest("td").attr("data-eindex");
                if(checked.length ===1){
                    $(".table-row-actions .action.up").attr("tindex", tIndex);
                    $(".table-row-actions .action.down").attr("tindex", tIndex);
                }else{
                    $(".table-row-actions .action.up").removeAttr("tindex");
                    $(".table-row-actions .action.down").removeAttr("tindex");
                }

            updateSelectionActionState($(body), checked.length);
            $('.selection input', table.table().header()).prop('checked', checked.length === $('tr', body).length);
        });

    // filter change
    $('.main-content').on('change keyup', '.table-filter .field-value', function (e) {
        var columnIndex = this.getAttribute('data-index'),
            table = $('.table-content .dataTable', e.delegateTarget);
        table.DataTable().column(columnIndex).search('^' + this.value, true).draw();
    });

    $('.popup').on('change keyup', '.filter-panel .field-value', function (e) {
        var columnIndex = this.getAttribute('data-index'),
            table = $('.popup-table', e.delegateTarget);
        table.DataTable().column(columnIndex).search('^' + this.value, true).draw();
    });

    $('body')
        .on('change keyup', '.input input', function () {
            $(this).parent().toggleClass('input-clearable', !!this.value);
        })
        .on('click', '.input .clear', function () {
            $(this).parent().find('input').val('').change();
        });

    //custom select
    $('select').customSelect();

    if($( ".multiple-panel").length>0){
        $( ".multiple-panel .option-list ul" ).selectable();
    }

    //show cases
    $(".action-show-case").on('click', function () {
        var pos = $(this).offset();
        var target = $(this).data('target');
        if(typeof target !== 'undefined' && target.length>0){
            $('#'+target)
            .show()
            .css({
                left:pos.left+10,
                top:pos.top+30
            });
        }else{
            $('.show-cases')
            .show()
            .css({
                left:pos.left+10,
                top:pos.top+30
            });
        }
    });

    //modal action
    $(".modal-action").on('click', function () {
        var modal = $("#"+$(this).data("modal"));
        popups.hide();
        popups.show(modal);
        $('.show-cases').hide();
    });

    //multiple panel
    $(".multiple-panel").each(function(index, element) {
        var that = $(this);
        var panel = that.closest(".multiple-panel");
        var leftColumn = panel.find(".multiple-source");
        var rightColumn = panel.find(".multiple-object");
        var leftList = leftColumn.find(".option-wrapper ul");
        var rightList = rightColumn.find(".option-wrapper ul");

        leftList.data("options", leftList.html());
        rightList.data("options", rightList.html());

        that
            .on('change keyup', '.filter', function () {
                var filterWrapper = $(this).parent();
                var val = $.trim($(this).val()).toLowerCase();
                var column = $(this).closest(".multiple-column").find(".option-wrapper ul");
                column.find("li").removeClass("hide");
                if(val.length>0){
                    filterWrapper.addClass("input-clearable");
                    column.find("li").each(function(){
                        var text = $(this).text().toLowerCase();
                        var vindex = text.indexOf(val);
                        if(vindex<0){
                            $(this).addClass("hide");
                        }
                    });
                }else{
                    filterWrapper.removeClass("input-clearable");
                }
            })
            .on("click", ".action-move-all", function(){
                leftList.find("li:not('.hide')").removeClass("ui-selected ui-selecting").appendTo(rightList);
            })
            .on("click", ".action-move-left", function(){
                rightList.find("li.ui-selected").removeClass("ui-selected ui-selecting").appendTo(leftList);
            })
            .on("click", ".action-move-right", function(){
                if(leftList.find("li.ui-selected").length >0)
                leftList.find("li.ui-selected").removeClass("ui-selected ui-selecting").appendTo(rightList);
            })
            .on("click", ".action-move-clear", function(){
                rightList.find("li:not('.hide')").removeClass("ui-selected ui-selecting").appendTo(leftList);
            });
        that
            .on('click', '.filter-wrapper .placeholder', function () {
                var filterWrapper = $(this).parent();
                var val = $.trim($(this).siblings(":text").val()).toLowerCase();
                $(this).siblings(":text").focus();
                if(val.length>0){
                    filterWrapper.addClass("input-clearable");
                }else{
                    filterWrapper.removeClass("input-clearable");
                }
            })
    });

    //browse file
    $(".file-container :file").css("opacity", "0.001");
    $(".file-container").on("click", ".action-browse", function(){
        $(this).closest(".file-container").find(":file").trigger("click");
    });

    //select all
    $('.select-schema-panel')
        .on('change', 'header :checkbox', function(){
            var optionsList = $(this).closest('.select-schema-panel').find('.select-options :checkbox');
            if($(this).prop('checked')){
                optionsList.prop('checked', true);
            }else{
                optionsList.prop('checked', false);
            }
        })
        .on('change', '.select-options :checkbox', function(){
            var optionsList = $(this).closest('.select-options').find(':checkbox');
            var selectall = $(this).closest('.select-schema-panel').find('header :checkbox');
            var flag = false;
            optionsList.each(function(index, element) {
                if(!$(this).prop('checked')){
                    flag = true;
                }
            });
            if(flag){
                selectall.prop('checked', false);
            }else{
                selectall.prop('checked', true);
            }
        })

    if(mozilla){
        $("html").addClass('mozilla');
    }
});

===============================================================================
// 对不同的页面调用不同的init函数
//============================= Page dispatcher ===============================================
$(function () {
    var pageId = $('.main-content').attr('id');

    switch (pageId) {
        case 'login':
            initLogin();
            break;
        ...
        case 'workbook-detail-preview' :
            initWorkBookDetail();
    }
});

// Login page
function initLogin() {
    // Login form behavior
    $('#login-form')
        .on('submit', function () {
            if (!(this.username.value && this.password.value)) {
                $('.error', this).show();
            } else {
                $.ajax({
                    url: datactx + '/login',
                    type: 'POST',
                    cache: false,
                    data: {
                        'username':this.username.value,
                        'password':this.password.value,
                        'rememberMe':this.rememberMe.checked
                    },
                    success: function(data) {
                        window.location.href = datactx + '/dashboard';
                    },
                    error: function() {
                        return $('.login-form .error').html('Please provide valid username/password.').show();
                    }
                });
            }
            return false;
        })
        .on('focus', 'input', function (e) {
            $('.error', e.delegateTarget).hide();
        });
}

// Project Details page
function initPublicProjectDetails() {
    var tabs = $(".table-tabs");
    var tabContents = $(".table-tab-contents");
    var currentTab = tabs.find("li.current").data("tab");
    tabContents.find('.tab-content').hide();
    $("#"+currentTab).show();

    initTab(currentTab);

    attachProjectPagesHandlers();

    tabs.on("click", ".tabs li", function(){
        var dataSrc = $(this).data("tab");
        tabContents.find('.tab-content').hide();
        $("#"+dataSrc).show();

        tabs.find('li').removeClass('current');
        $(this).addClass('current');
        initTab(dataSrc);
    });

    if (location.href.indexOf("?tab=") != -1) {
        var tabid = (location.href.substring(location.href.indexOf("?tab=") + 5, location.href.length));
        $(".tabs li[data-tab='" + tabid + "']").trigger("click");

    }

    if (window.location.search === '?create') {

    }
}

//tab config
function initTab(tabId){
    switch (tabId) {
        case 'tab-project-users':
            initTabProjectUsers(tabId);
            break;
        ...
        case 'tab-gathering-workbooks':
            initTabGatheringWorkbooks(tabId);
            break;
    }
}

//tab project users
function initTabProjectUsers(tab){
    var tableElem = $('#'+tab).find('table');
    if (!tableElem.hasClass('dataTable')) {
        initTable(tableElem, tableConfigs.publicProjectUsers);
    }else{
        tableElem.DataTable().page( 0 ).draw( false );
    }
}
