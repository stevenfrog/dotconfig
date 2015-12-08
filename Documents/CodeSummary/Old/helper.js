/*
 * Copyright (C) 2014 TopCoder Inc., All Rights Reserved.
 */
"use strict";

/**
 * This module contains helper functions.
 *
 * @author ibraaaa
 * @version 1.0
 */
var mongoose = require('mongoose');
var Media = mongoose.model('Media');
var config = require('config/configuration');

var helper = {};

var extendedVerbosity = config.media.verbosity.defaultLevel.concat(config.media.verbosity.extendedLevel);
helper.mediaVerbosityLevel = {
    'default': config.media.verbosity.defaultLevel,
    'extended': extendedVerbosity,
    'complete': extendedVerbosity.concat(config.media.verbosity.completeLevel)
};

extendedVerbosity = config.mediaSeries.verbosity.defaultLevel.concat(config.mediaSeries.verbosity.extendedLevel);
helper.mediaSeriesVerbosityLevel = {
    'default': config.mediaSeries.verbosity.defaultLevel,
    'extended': extendedVerbosity,
    'complete': extendedVerbosity.concat(config.mediaSeries.verbosity.completeLevel)
};

helper.handleError = function(err, res) {
    console.log('Error occurred:\n' + err);
    res.send({
        status: 'fail',
        error: {
            code: 1,
            message: err.message
        }
    });
};

helper.validateRequiredParameter = function(paramValue, res, param) {
    if (!paramValue) {
        res.send({
            status: 'fail',
            error: {
                code: config.errorCodes.missingRequiredMethodParameter,
                message: "Required parameter '" + param + "' is missing."
            }
        });
        return false;
    }

    return true;
};

helper.validateRequiredIntParameter = function(paramValue, res, param) {
    if (!helper.validateRequiredParameter(paramValue, res, param))
        return false;

    if (isNaN(parseInt(paramValue))) {
        res.send({
            status: 'fail',
            error: {
                code: config.errorCodes.invalidParameterValue,
                message: param + " should be an Integer but '" + paramValue + "' was provided."
            }
        });
        return false;
    }

    return true;
};

helper.getOrder = function(order) {
    return order === 'asc' ? 1 : -1;
};

helper.getDateParam = function(req, res, paramName) {
    var date = req.query[paramName];
    if (/(\d{4})-(\d{2})-(\d{2})/.exec(date)) {
        var d = new Date(date);
        if (d != 'Invalid Date') {
            return d;
        }
    }

    res.send({
        status: 'fail',
        error: {
            code: config.errorCodes.invalidParameterValue,
            message: "A parameter value is invalid, which may mean it is out of range.",
            detailedMessage: "Date parameter '" + paramName + "' should have the format YYYY-MM-DD."
        }
    });
    return null;
};

helper.validateVerbosity = function(level, completeAllowed, res) {
    var allowed = ['default', 'extended'].concat(completeAllowed ? ['complete'] : []);
    if (allowed.indexOf(level) !== -1)
        return true;

    res.send({
       status: 'fail',
       error: {
           code: config.errorCodes.invalidParameterValue,
           message: "A parameter value is invalid, which may mean it is out of range.",
           detailedMessage: "Verbosity level should be in: [" + allowed.join(', ') + "]"
       }
    });
    return false;
};

helper.validatePerPage = function(perPage, maxPerPage, res) {
    return helper.validateUpperBoundedInteger('perPage', perPage, maxPerPage, res);
};

helper.validatePage = function(page, res) {
    page = parseInt(page);
    if (isNaN(page) || page <= 0) {
        res.send({
            status: 'fail',
            message: "A parameter value is invalid, which may mean it is out of range.",
            detailedMessage: "page should be a positive integer."
        });
        return false;
    }

    return true;
};

helper.validateOrderBy = function(orderBy, res) {
    var allowed = ['rating', 'downloads', 'title', 'added', 'updated'];
    if (allowed.indexOf(orderBy) === -1) {
        res.send({
            status: 'fail',
            error: {
                code: config.errorCodes.invalidParameterValue,
                message: "A parameter value is invalid, which may mean it is out of range.",
                detailedMessage: "orderBy should be in: [" + allowed.join(', ') + "]"
            }
         });
        return false;
    }

    return true;
};

helper.validateOrder = function(order, res) {
    var allowed = ['asc', 'desc'];
    if (allowed.indexOf(order) === -1) {
        res.send({
            status: 'fail',
            error: {
                code: config.errorCodes.invalidParameterValue,
                message: "A parameter value is invalid, which may mean it is out of range.",
                detailedMessage: "order should be in: [" + allowed.join(', ') + "]"
            }
         });
        return false;
    }

    return true;
};

helper.validateSearchIn = function(searchIn, allowed, res) {
    if (allowed.indexOf(searchIn) === -1) {
        res.send({
            status: 'fail',
            error: {
                code: config.errorCodes.invalidParameterValue,
                message: "A parameter value is invalid, which may mean it is out of range.",
                detailedMessage: "searchIn should be in: [" + allowed.join(', ') + "]"
            }
         });
        return false;
    }

    return true;
};

helper.validateUpperBoundedInteger = function(paramName, paramValue, upperBound, res) {
    var value = parseInt(paramValue);
    if (isNaN(value) || value <= 0 || value > upperBound) {
        res.send({
            status: 'fail',
            message: "A parameter value is invalid, which may mean it is out of range.",
            detailedMessage: paramName + " should be in: [1, " + upperBound + "]"
        });
        return false;
    }

    return true;
};

helper.getMediaImpl = function(req, res, defaults, filter, sortOrder) {
    var level = req.query.level || defaults.level;
    var count = req.query.count || defaults.count;
    var maxCount = defaults.maxCount;
    if (!helper.validateVerbosity(level, false, res) ||
        !helper.validateUpperBoundedInteger('count', count, maxCount, res)) {
        return;
    }
    count = parseInt(count);

    Media.find(filter, helper.mediaVerbosityLevel[level].join(' '))
    .sort(sortOrder)
    .limit(count)
    .exec(function(err, media) {
        if (err) return helper.handleError(err, res);

        var plainMedia = media.map(function(item) {
            var plainItem = item.toObject();
            delete plainItem._id;
            if (plainItem['additionalFiles']) {
                plainItem.additionalFiles = item.additionalFiles.length;
            }
            return plainItem;
        });

        res.send({
            status: 'ok',
            medias: {
                count: plainMedia.length,
                media: plainMedia
            }
        });
    });
};

helper.getTagFilter = function(req, filter) {
    if (req.query['tagFilter']) {
        var tags = [];
        if (Array.isArray(req.query.tagFilter)) {
            req.query.tagFilter.forEach(function(tag) {
                tags.push(tag);
            });
        } else {
            tags.push(req.query.tagFilter);
        }

        filter['tags.tag'] = { $all: tags };
    }
};

helper.getCommonFilters = function(req, filter) {
    helper.getTagFilter(req, filter);

    if (req.query['seriesId']) {
        filter['seriesId'] = req.query.seriesId;
    }

    if (req.query['author']) {
        filter['author.email'] = req.query.author;
    }
};

helper.getTagsImpl = function(count, filter, res, prefix, prefixFilter) {
    Media.distinct('tags', filter, function(err, tags) {
        if (err) return helper.handleError(err, res);

        // Accumulate usage count in two dictionaries one for
        // tags with exact match and the other for tags with prefix match.
        var exactTags = {};
        var prefixTags = {};
        tags.forEach(function(tag) {
            // If prefix is undefined then we are not doing prefix matching
            // hence just add all to the same array.
            if (prefix === undefined || tag.tag == prefix) {
                if (!exactTags[tag.tag]) {
                    exactTags[tag.tag] = 0;
                }
                exactTags[tag.tag] = tag.usageCount;
            } else if (prefixFilter && prefixFilter.test(tag.tag)) {
                if (!prefixTags[tag.tag]) {
                    prefixTags[tag.tag] = 0;
                }
                prefixTags[tag.tag] = tag.usageCount;
            }
        });

        // Converts a tag dictionary in the format of tagName: usageCount
        // to a tag array where each tag has the format { tag: tagName, usageCount: usageCount }
        // It then returns this array sorted in descending order by the usage count.
        var sortTagsDic = function(tagsDic) {
            return Object.keys(tagsDic)
            .map(function(tagName) {
                return { tag: tagName, usageCount: tagsDic[tagName] };
            })
            .sort(function(a, b) {
                return a.usageCount == b.usageCount ? 0 : a.usageCount > b.usageCount ? -1 : 1;
            });
        };

        // Exact matches come first followed by prefix matches both sorted by usage count.
        var tagsArray = sortTagsDic(exactTags).concat(sortTagsDic(prefixTags)).slice(0, count);
        res.send({
            status: 'ok',
            tags: {
                count : tagsArray.length,
                tag: tagsArray
            }
        });
    });
};

helper.getMediaById = function(mediaId, res, successCallback, level) {
    var columns = level === undefined ? 'id' : helper.mediaVerbosityLevel[level].join(' ');
    Media.findOne({ id: mediaId }, columns, function(err, media) {
        if (err) return helper.handleError(err, res);

        if (!media) {
            res.send({
                status: 'fail',
                error: {
                    code: 1,
                    message: 'Media not found.',
                    detailedMessage: 'The specified media could not be found.'
                }
            });
        } else {
            successCallback(media);
        }
    });
};

helper.formatMediaFileName = function(timestamp, title) {
    var pad = function(v) {
        v = '0' + v;
        return v.substring(v.length - 2);
    };
    var year = timestamp.getFullYear();
    var month = pad(timestamp.getMonth() + 1);
    var day = pad(timestamp.getDate());

    var fileName = year + '%20' + month + '%20' + day + '_';
    var newTitle = title.substring(0, Math.min(30, title.length));
    newTitle = newTitle.replace(/[^a-z0-9_$'\" \\\/]/ig, '');
    newTitle = newTitle.replace(/'/g, '%27');
    newTitle = newTitle.replace(/\"/g, '%22');
    newTitle = newTitle.replace(/[ \/\\]/g, '_');

    return fileName + newTitle;
};

module.exports = helper;