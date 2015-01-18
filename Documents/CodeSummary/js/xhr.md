// From Workday_Data_Toolkit_Schema_and_Workbook_Frontend

# xhr

**这段是用xhr上传文件的例子**

```js
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

    // Get the selected files from the input.
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
```

```html
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
```

```js
// 补充browse file的部分
//browse file
$(".file-container :file").css("opacity", "0.001");
$(".file-container").on("click", ".action-browse", function(){
    $(this).closest(".file-container").find(":file").trigger("click");
});
```

```java
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
```
