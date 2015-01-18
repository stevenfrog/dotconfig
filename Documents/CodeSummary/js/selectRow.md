// From Workday_Data_Toolkit_Schema_and_Workbook_Frontend


## 多选单选
**控制Table多选, 单选**

```js
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
```
