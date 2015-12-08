### @passport @auth @login @logout ==================================================================
# 有关passport工作原理

passport管理了有关auth的所有部分, 首先是定义passport初始化部分

先在app.js中调用

```javascript
var session = require('express-session');
var passport = require('passport');

// Bootstrap passport config
require('./config/passport')(passport);

app.use(session({
  secret: config.SESSION_SECRET,
  resave: false,
  saveUninitialized: true
}));
app.use(passport.initialize());
app.use(passport.session());
```

这个是文件`./config/passport`

```javascript
module.exports = function(passport) {
  // serialize sessions
  passport.serializeUser(function(user, done) {
    done(null, user.id);
  });

  passport.deserializeUser(function(id, done) {
    User.findById(id).then(function(user) {
      done(null, user.dataValues);
    })
      .catch(function(err) {
        done(err);
      });
  });

  // use these strategies
  passport.use(new LocalStrategy(
    {usernameField: 'email', passwordField: 'password'},
    function(email, password, done) {
      User.findOne({where: {email: email}}).then(function(user) {
        if (!user) {
          return done(null, false, {message: 'User is not found'});
        }

        user.comparePassword(password, function(err, match) {
          if (!match) {
            return done(null, false, {message: 'Password is not match'});
          }
          return done(null, user);
        });
      })
      .catch(function(err) {
        done(err);
      });
    });
  );
};
```

这里的`serializeUser`, `deserializeUser`表示从`server session`中怎么取出需要的部分
上面的代码是, 只把`user.id`保存在`session`中, 需要时就让`User.findById`找出来

`session`在这里是个很重要的概念, 没有他就没办法用passport
session只是保存在server中, 但是还是需要cookie才能确认客户端的身份, 因为request是无状态的
这个时候cookie保存的是`sessionId`, 每次request都会附带cookie, 也就是提交了sessionId
这样passport就是访问的request是否合法了

AngularJS默认是在request附带cookie的

如果用户需要其他Authentication, 有可能需要在客户端保留token


## 检查response cookie
查看`response.headers['set-cookie'])`就可以了



## login, logout部分代码
注意`req.logIn`, `req.logout`这个是passport附加的
有了这两个语句才保证passport对session的管理
_`logout`请一定不要只是跳转页面_

```javascript
/**
 * Login user.
 * @param {Object} req the request
 * @param {Object} res the response
 * @param {Function} next the next middleware
 */
function signin(req, res, next) {
  var error = validator.validate(
    {email: req.body.email, password: req.body.password},
    {email: String, password: String}
  );
  if (error) {
    next(error);
  }

  passport.authenticate('local', function(err, user, info) {
    if (err) {
      return next(err);
    }
    if (!user) {
      return next(new errors.UnauthorizedError(info.message));
    }
    req.logIn(user, function(err) {
      if (err) {
        return next(err);
      }
      res.json(user);
    });
  })(req, res, next);
}

/**
 * Logout user.
 * @param {Object} req the request
 * @param {Object} res the response
 * @param {Function} next the next middleware
 */
function signout(req, res, next) {
  req.logout();
  res.json({
    loggedIn: false
  });
}
```
