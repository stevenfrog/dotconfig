




# 当ngRepeat结束时,触发

```javascript
directives.directive('repeatDone', function() {
    return {
        restrict: 'A',
        link: function(scope, element, attrs, ngModel) {
            if (scope.$last) {
                scope.$eval(attrs.repeatDone);
            }
        }
    };
});
```
