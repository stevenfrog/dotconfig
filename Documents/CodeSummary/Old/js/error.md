// From Workday_Data_Toolkit_Schema_and_Workbook_Frontend

## 错误处理
```js
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
```
