// From Workday_Data_Toolkit_Schema_and_Workbook_Frontend

## Table事件处理

```js
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
```


