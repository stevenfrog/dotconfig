#这个是tc-user-setting的SavedSearches.js

```javascript
/*
 * Copyright (C) 2014 TopCoder Inc., All Rights Reserved.
 */
/**
 * Represents controller for Saved Searches.
 *
 * @version 1.0
 * @author TCSASSEMBLER
 */
"use strict";

/*jslint unparam: true */

var express = require('express'),
    _ = require('underscore'),
    async = require('async'),
    SavedSearchType = require("../models/Setting").SavedSearchType,
    Setting = require('../models').Setting,
    User = require('../models').User,
    NotFoundError = require("../errors/NotFoundError"),
    validator = require("../helpers/validator"),
    helper = require("../helpers/helper"),
    FILTER_MAX_LENGTH = 2000,
    router = express.Router();

```

#这里定义了一个middleware, 用于每次检查req, 等等

```javascript
/**
 * Get setting and savedSearch for current user and set it to req object
 * @param {Object} req the request
 * @param {Object} res the response
 * @param {Function} next the callback function
 */
function fetchSavedSearchMiddleware(req, res, next) {
    var error, savedSearch;
    Setting.findOne({user: req.user.id}, function (err, setting) {
        if (err) {
            return next(err);
        }
        if (!setting) {
            return next(new NotFoundError("Setting not found for user"));
        }
        error = validator.validateObject({id: {type: "objectId"}}, {id: req.params.id});
        if (error) {
            return next(error);
        }
        savedSearch = _.find(setting.savedSearches, function (item) {
            return String(item.id) === req.params.id;
        });
        if (!savedSearch) {
            return next(new NotFoundError("Saved Search not found with id = " + req.params.id));
        }
        req.setting = setting;
        req.savedSearch = savedSearch;
        next();
    });
}


// get all saved searches
router.get("/", helper.offsetAndLimitMiddleware, function (req, res, next) {
    Setting.findOne({user: req.user.id}, function (err, setting) {
        if (err) {
            return next(err);
        }
        if (!setting) {
            res.json([]);
        } else {
            res.json(setting.savedSearches.toObject({transform: true}).slice(req.offset, req.offset + req.limit));
        }
    });
});

// get single saved search
router.get("/:id", fetchSavedSearchMiddleware, function (req, res) {
    res.json(req.savedSearch.toObject({transform: true}));
});

// create saved search
router.post("/", function (req, res, next) {
    var error = validator.validateObject({
            type: {type: "enum", values: _.values(SavedSearchType)},
            filter: {type: "string", length: FILTER_MAX_LENGTH}
        }, req.body),
        result;
    if (error) {
        return next(error);
    }
    async.waterfall([
        function (cb) {
            async.parallel({
                user: helper.getOrCreate.bind(null, User, {_id: req.user.id}),
                setting: helper.getOrCreate.bind(null, Setting, {user: req.user.id})
            }, cb);
        }, function (results, cb) {
            var setting = results.setting;
            result = setting.savedSearches.create({
                type: req.body.type,
                filter: req.body.filter
            });
            setting.savedSearches.push(result);
            setting.save(cb);
        }, function () {
            res.json(result.toObject({transform: true}));
        }
    ], next);
});

// update saved search
router.put("/:id", fetchSavedSearchMiddleware, function (req, res, next) {
    var error = validator.validateObject({
            type: {type: "enum", values: _.values(SavedSearchType), optional: true},
            filter: {type: "string", length: FILTER_MAX_LENGTH, optional: true}
        }, req.body);
    if (error) {
        return next(error);
    }
    if (req.body.hasOwnProperty('type')) {
        req.savedSearch.type = req.body.type;
    }
    if (req.body.hasOwnProperty('filter')) {
        req.savedSearch.filter = req.body.filter;
    }
    req.setting.save(function (err) {
        if (err) {
            return next(err);
        }
        res.json(req.savedSearch.toObject({transform: true}));
    });
});

// delete saved search
router.delete("/:id", fetchSavedSearchMiddleware, function (req, res, next) {
    req.savedSearch.remove();
    req.setting.save(function (err) {
        if (err) {
            return next(err);
        }
        res.statusCode = 204;
        res.end();
    });
});



module.exports = router;
```
