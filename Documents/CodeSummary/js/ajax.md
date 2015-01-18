// From Workday_Data_Toolkit_Schema_and_Workbook_Frontend

## AJAX
**这是一个标准的JQuery AJAX请求**
```js
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
```
