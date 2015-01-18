// From Workday_Data_Toolkit_Schema_and_Workbook_Frontend

## 对不同的页面调用不同的init函数

```js
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
```

