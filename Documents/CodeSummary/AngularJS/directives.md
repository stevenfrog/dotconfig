#目录
#[1. input只输入数字]
#[2. 当ngRepeat结束时,触发函数]
#[3. input:radio 用ngRepeat实现]

#1. 这个只允许input中输入数字, 还可以指定最大, 最小值
```html
<input type="text" allowNumber/>
```

```javascript
/**
 * Only allow the number input.
 * Attributes:
 * "min" : the minimal allowed value
 * "max" : the maximal allowed value
 */
directives.directive('allowNumber', function() {
    return {
        restrict: 'A',
        require: '?ngModel',
        link: function(scope, element, attrs, ngModel) {
            if (!ngModel) {
                return;
            }
            // check input value whether valid
            function isValid(val) {
                var asInt = parseInt(val, 10);
                if (isNaN(asInt) || asInt.toString() !== val) {
                    return false;
                }
                var min = parseInt(attrs.min);
                if (!isNaN(min) && asInt < min) {
                    return false;
                }
                var max = parseInt(attrs.max);
                if (!isNaN(max) && max < asInt) {
                    return false;
                }
                return true;
            }
            // store the previous value
            var prev = scope.$eval(attrs.ngModel);
            if (prev === undefined) {
                prev = "";
            }
            ngModel.$parsers.push(function(val) {
                // short-circuit infinite loop
                if (val === prev) {
                    return val;
                }
                if (!isValid(val)) {
                    ngModel.$setViewValue(prev);
                    ngModel.$render();
                    return prev;
                }
                prev = val;
                return val;
            });
        }
    };
});
```


---------------------------------------------------------------------------------------------------
#2. 当ngRepeat结束时,触发一个函数
```html
<div ng-repeat="(key, value) in dataset" repeat-done="fun1()">
    ...
</div>
```

```javascript
directives.directive('repeatDone', function() {
    return {
        restrict: 'A',
        link: function(scope, element, attrs, ngModel) {
            if (scope.$last) {
                $timeout(function () {
                    scope.$eval(attrs.repeatDone);
                });
            }
        }
    };
});
```

# 这里还有为什么不能加`require: 'ngRepeat'`的详细讨论[link](http://stackoverflow.com/questions/28386289/directive-can-not-requirengrepeat)


---------------------------------------------------------------------------------------------------
#3. input:radio 用ngRepeat实现
```html
<!doctype html>
<html>
    <head>
        <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.3.3/angular.js"></script>
    </head>
    <body ng-app="testApp">
        <div ng-controller="controller">
            <div class="control-group" ng-repeat="answer in answers">
                <label>
                    {{answer.DESCRIPTION}}
                    <input type="radio" ng-model="$parent.correctAnswer" ng-value="answer" name="correct_answer">
                </label>
            </div>
            Correct Answer: {{correctAnswer.DESCRIPTION}}
        </div>
    </body>
    <script>
    var app = angular.module('testApp', []);
    app.controller('controller', function($scope) {
        $scope.answers = [
           { "ANSWER_ID": 5, "DESCRIPTION": "Answer 3"},
           { "ANSWER_ID": 4, "DESCRIPTION": "Answer 2"},
           { "ANSWER_ID": 3, "DESCRIPTION": "Answer 1"}
        ];
        $scope.correctAnswer = $scope.answers[1];
    });
    </script>
</html>
```

http://stackoverflow.com/questions/28419562/data-binding-between-radio-button-and-other-elements-not-working-as-expected


