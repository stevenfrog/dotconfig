**这里是一个典型的express server.js**

```javascript
/*
 * Copyright (C) 2014 TopCoder Inc., All Rights Reserved.
 */
/**
 * Represents main application file.
 *
 * @version 1.0
 * @author TCSASSEMBLER
 */
"use strict";

/*jslint unparam: true */

var express = require('express'),
    winston = require('winston'),
    morgan = require('morgan'),
    bodyParser = require('body-parser'),
    methodOverride = require('method-override'),
    session = require('express-session'),
    errorHandler = require('errorhandler'),
    cookieParser = require('cookie-parser'),
    compression = require('compression'),
    config = require("./config.js");

var app = express();

app.use(morgan('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(methodOverride());
app.use(cookieParser());

app.use(session({
    resave: true,
    saveUninitialized: true,
    cookie: { domain: configuration.main.COOKIE_DOMAIN},
    store: sessionStore,
    secret: configuration.main.SESSION_SECRET,
    key: configuration.main.SESSION_KEY
}));

app.set('env', "development");

// app.use(compression());
// app.use(express["static"](__dirname + '/public', { maxAge: 3.15569e10 }));
// app.set('views', __dirname + '/views');
// app.set('view engine', 'jade');



// stub authentication middleware
app.use(function (req, res, next) {
    req.user = {
        id: config.MOCK_USER_ID
    };

    next();
});

// 其实就是router.md中的express.router
app.use('/saved-searches', require("./controllers/SavedSearches.js"));

if ('development' === app.get('env')) {
  app.use(errorHandler({
        dumpExceptions : true,
        showStack : true
    }));
}

if ('production' === app.get('env')) {
  app.use(errorHandler());
}

// error handler
app.use(function (err, req, res, next) {
    winston.error(err.stack || JSON.stringify(err));
    res.statusCode = err.status || 500;
    res.json({
        status: res.statusCode,
        developerMessage: err.message,
        errorCode: err.errorCode || res.statusCode
    });
});

// Start the server
app.listen(config.API_PORT);
winston.info('Express server listening on port ' + config.API_PORT);
```
