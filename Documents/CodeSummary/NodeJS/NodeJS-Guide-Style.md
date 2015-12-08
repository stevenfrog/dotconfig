#NodeJS Guide Style

__使用`Ctrl+H`可以查找所有文件, 使用`Reg Search`还可以查找标签__
__查找`@model|@sequen`(@表示标签), 然后范围是`CodeSummary/*.md,CodeSummary/*.js`__

## 经验

## `$resource`与`$http`
`$resource`与`$http`可以互换,
他们都能发送`cookie`的信息,这样就会自带`sessionId`, 可以直接使用`password session`






## 文件结构
    * config/ 各种常量, default, passport, routes等都放到这里
    * controllers/
    * helpers/
    * models/
    * public/
    * services/
    * tests/
    * .jshintc
    * README.md
    * app.js
    * env-sample
    * gulpfile.js
    * package.json


### package.json版本号
    * `version` 必须完全和version一致
    * `>version` 必须比version大, >=, <, <=同
    * `version1 - version2` 等价于 >=version1 <=version2.
    * `~version` 大约一样, 1.2.x, 1.2.0, 1.2.1等, 但1.3.0不行
    * `^version` 与当前版本兼容, `^1.2.3`, 1.5.1可以, 2.0.0, 1.2.2 不行
    * `*` 所有, `""`也是这个意思
    * `range1 || range2` 满足任意一个即可



### @validate ==================================================================
### 使用validator.js
```javascript
var error = validate(
  {body: body},
  {
    body: {
      email: 'email',
      password: 'String?',
      firstname: String,
      lastname: String,
      company: 'String?',
      role: {'enum': _.values(constant.USER_ROLE), required: true}
    }
  }
);
if (error) {
  cb(new errors.ValidationError(error.message));
} else {
  cb();
}



//////////////////////////////////////////////////////////////////////////////
// rox对多层结构支持一般, 不如分开validate
if (body.houseInfo) {
  var houseInfo = body.houseInfo;
  delete body.houseInfo;
}
if (body.interestedHouses) {
  var interestedHouses = body.interestedHouses;
  delete body.interestedHouses;
}


var error = validate(
  {body: body, houseInfo: houseInfo, interestedHouses: interestedHouses},
  {
    body: {
      address: String,
      city: String,
      state: String,
      zip: String,
      status: {'enum': _.values(constant.HOUSE_STATUS), required: false}
    },
    houseInfo: {type: 'HouseInfo', required: false},
    interestedHouses: {
      empty: true, required: false,
      type: [{
        address: String,
        city: String,
        state: String,
        zip: String,
        status: {'enum': _.values(constant.HOUSE_STATUS), required: false}
      }]
    }
  }
);
if (error) {
  return cb(new errors.ValidationError(error.message));
}
cb();
```


### @test ==================================================================
### 测试nodejs controller
### request中的`json`表示req, res的body都是json, 会自动设置 `Content-Type: application/json`
### request中的`jar`表示保存cookies, 否则request就不包含`sessionID`, passport就无法确认这个request是否登陆过

```javascript
request({
  method: 'POST',
  url: 'http://localhost:3000/' + 'signin',
  json: true,
  body: {
    "email": "homeowner@gmail.com",
    "password": "password"
  },
  jar: true
}, function(error, response, body) {
  should.not.exist(error);
  response.statusCode.should.equal(200);
  body.id.should.equal(2);
  done();
});

request({
  method: 'GET',
  url: 'http://localhost:3000/' + 'getMe',
  json: true,
  jar: true
}, function(error, response, body) {
  should.not.exist(error);
  response.statusCode.should.equal(200);

  body.email.should.equal('homeowner@gmail.com');
  done();
});
```




### @$routeProvider @$stateProvider ==================================================================
## `$routeProvider`与`$stateProvider`

[wiki](https://github.com/angular-ui/ui-router/wiki)

## `$routeProvider`是ngRouter默认的router, 提供了页面跳转
## `$stateProvider`是`ui.router`提供了router, 增强了功能
## `$stateProvider`首先提供了层级, 允许一个页面多个`ngView`
## 还有就是对router也提供了层级:
## 如果用户访问'/admin'
## router先处理'base', 这里在`resolve`中检查了用户是否登陆, 还在$scope中设置了states, stateCities, stateTaxes
## 然后再处理'base.admin', 再检查一下用户的role
## _注意:_ 如果`url: '^/admin'`没有那个`^`, 用户需要访问`/base/admin`才能访问admin.html


```javascript
.state('base', {
  url: '/base',
  abstract: true,
  template: '<div data-ui-view></div>',
  controller: 'baseCtrl',
  resolve: {
    user: checkLogin,
    states: ['$http', 'API', function($http, API) {
      return API.states().$promise;
    }],
    stateCities: ['$http', 'API', function($http, API) {
      return API.cities().$promise;
    }],
    stateTaxes: ['$http', 'API', function($http, API) {
      return API.stateTaxes().$promise;
    }]
  }
})
.state('base.admin', {
  url: '^/admin',
  templateUrl: 'partials/admin.html',
  controller: 'adminPage',
  resolve: {
    checkRole: checkRole('admin')
  }
})
.state('base.homeowner', {
  url: '^/homeowner',
  templateUrl: 'partials/homeowner.html',
  controller: 'homeownerPage',
  resolve: {
    checkRole: checkRole('homeOwner'),
    utilities: ['$http', 'API', function($http, API) {
      return API.utilities().$promise;
    }]
  }
})
.state('base.financier', {
  url: '^/financier',
  templateUrl: 'partials/financier.html',
  controller: 'financierPage',
  resolve: {
    checkRole: checkRole('financier')
  }
 })
```

## 有关`utilities`
>utilities: ['$http', 'API', function($http, API) {
  return API.utilities().$promise;
}]

## 本来`utilities`是个函数,用$resource访问了'/utilities', 他增加了一个`$promise`, 就能直接得到结果



### @angularjs @config ==================================================================
## 初始化Angularjs

## 首先定义了一个`Config`, 专门是客户端的不变量
## 然后`API.constants()`用于获取服务器段的不变量
## `$rootScope.signout`是每个页面都要用到的, 直接在`$rootscope`定义
## `$rootScope.$on '$stateChangeError'`是防止页面错误,`event.preventDefault();`是取消事件默认行为
## 其实还可以接着导向错误页面, 见最后代码


```javascript
app.js


.run(['$rootScope', '$log', '$location', 'Config', 'API',
  function($rootScope, $log, $location, Config, API) {
    window.$log = $log;
    $rootScope.$config = Config;

    API.constants().$promise.then(function(constant) {
      window.$constant = constant;
      $rootScope.$constant = constant;
    });

    $rootScope.signout = function() {
      API.signout().$promise.then(function(data) {
        $rootScope.currentUser = null;
        $location.path('/landing');
      })
        .catch(function(err) {
          $log.error(err);
        });
    };

    $rootScope.$on('$stateChangeError', function(event) {
      event.preventDefault();
    });

  }])
```


```javascript
config.js

(function () {
  'use strict';

  window.$config = {
    ZIPCODE_REGEX: '^\\d{5}([\\-]?\\d{4})?$', // US zip code

    FEDERAL_TX_RATE: 0.30,        // Financial configuration
    STATE_INCENTIVE: 1332,
    FEDERAL_INCENTIVE: 2100
  };

  angular.module('SUNSHOT.config', [])
    .constant('Config', window.$config);

})();
```


```javascript
$rootScope.$on('$stateChangeError', function (event, toState, toParams, fromState, fromParams, error) {
  event.preventDefault();
  $state.get('error').error = { code: 123, description: 'Exception stack trace' }
  return $state.go('error');
});

.state('error', {
    url: 'error',
    resolve: {
        errorObj: [function () {
            return this.self.error;
        }]
    },
    controller: 'ErrorCtrl',
    templateUrl: 'error.html' // displays an error message
});
```
