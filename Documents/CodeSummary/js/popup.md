// From Workday_Data_Toolkit_Schema_and_Workbook_Frontend

# Popups

**这里是popups的设计, 它设计啦一个popups类专门控制popup的显示**
```js
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
```

```html
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
```

```js
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
```
