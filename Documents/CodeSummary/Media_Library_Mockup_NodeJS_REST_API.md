**Media_Library_Mockup_NodeJS_REST_API**

#这个winner是ibraaaa, 他在refactor方面做的很不错! 多学习学习.
===============================================================================

#这个Winner首先用了一个sh script来import data
```sh
# Copyright (C) 2014 TopCoder Inc., All Rights Reserved.

# Linux shell script to import data into MongoDB

# Please modify HOST and PORT to match your mongoDB instance setup.
HOST=localhost
PORT=27017


mongoimport --host $HOST --port $PORT --db media_library --type json --jsonArray --collection media --file json_data/media.json
mongoimport --host $HOST --port $PORT --db media_library --type json --jsonArray --collection comments --file json_data/comment.json
mongoimport --host $HOST --port $PORT --db media_library --type json --jsonArray --collection mediasets --file json_data/mediaSet.json
```

```json
[
    {
        "_id": {
            "$oid": "54673fdf2b30ab1f0554497e"
        },
        "added": {
            "$date": "2014-04-03T20:38:18.143+0200"
        },
        "author": {
            "email": "janet.freud111@gmail.com",
            "name": "Janet Freud"
        },
        "comment": "This is hillarious and funny",
        "mediaID": 103,
        "title": "Funny"
    },

]

```

===============================================================================
#然后是在model里面, 他用了: mongoose-paginate, mongoose-auto-increment

```javascript
var mongoose = require('mongoose');
var autoIncrement = require('mongoose-auto-increment');

var mediaSetSchema = new mongoose.Schema({
    id: Number,
    title: String,
    hasImage: Boolean,
    media: Number,
    added: Date,
    updated: Date,
    downloads: Number,
    avgRating: Number,
    author: {
        name: String,
        email: String
    },
    summary: String,
    description: String
});

mediaSetSchema.plugin(require('mongoose-paginate'));
mediaSetSchema.plugin(autoIncrement.plugin, { model: 'MediaSet', field: 'id', startAt: 200 });
```

# mongoose-auto-increment 就是一个自增插件
# 然后在这里可以直接分页, 简化了程序

```javascript
mongoose.connect(config.appConfig.DB_URL);
var db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
autoIncrement.initialize(db);
```

```javascript

MediaSet.paginate(filter, pageNum, perPage, function(err, pageCount, mediaSet) {
    if (err) return helper.handleError(err, res);

    if (pageCount && pageNum > pageCount) {
        paginate(pageCount, filter);
        return;
    }

    var plainMediaSet = mediaSet.map(function(item) {
       var plainItem = item.toObject();
       delete plainItem._id;
       delete plainItem.__v;
       return plainItem;
    });

    res.send({
        status: 'ok',
        medias: {
            page: !plainMediaSet.length ? 0 : pageNum,
            pages: !plainMediaSet.length ? 0 : pageCount,
            perPage: perPage,
            count: plainMediaSet.length,
            media: plainMediaSet
        }
    });
}, { columns: helper.mediaSeriesVerbosityLevel[level].join(' '), sortBy: sortBy });

```

===============================================================================
#有关validate
```javascript
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
```

#前面部分是设定默认值
#如果validation没通过, 就直接res.send(...), 然后return false
```javascript
var level = req.query.level || mediaDefaults.getByOwner.level;
var perPage = req.query.perPage || mediaDefaults.getByOwner.perPage;
var page = req.query.page || mediaDefaults.getByOwner.page;


if (!helper.validateRequiredParameter(req.query['userId'], res, 'userId') ||
    !helper.validateVerbosity(level, false, res) ||
    !helper.validatePerPage(perPage, mediaDefaults.getByOwner.maxPerPage, res) ||
    !helper.validatePage(page, res)) {
    return;
}
```
===============================================================================
#有关Config

#用env设定默认环境, 这个已经是默认了

#然后是把所有的默认值, 甚至controller都设定在configuration中, 方便修改
```javascript
var env = require('node-env-file');
env('./config/.env');

// Load configuration.
module.exports = {
    apiVersions: [ 'v1' ],
    appConfig: JSON.parse(JSON.stringify(process.env)),
    errorCodes: {
        missingRequiredMethodParameter: 120,
        invalidParameterValue: 121,
        apiVersionNotFound: 141,
        methodNotFound: 142
    },
    stat: {
        paramDefaults: {
            getTopTaggers: {
                count: 15,
                maxCount: 100
            },
            getTopRaters: {
                count: 15,
                maxCount: 100
            }
        }
    },
    mediaSeries: {
        paramDefaults: {
            browse: {
                orderBy: 'rating',
                order: 'asc',
                perPage: 15,
                page: 1,
                maxPerPage: 40,
                level: 'default'
            },
            getByIds: {
                level: 'default',
                maxNumberOfIds: 40
            },
            getByOwner: {
                level: 'default',
                perPage: 15,
                maxPerPage: 40,
                page: 1
            },
            search: {
                searchIn: 'all',
                allowedSearchInFields: [ 'author.name', 'description', 'summary' ],
                orderBy: 'rating',
                order: 'asc',
                perPage: 15,
                maxPerPage: 40,
                page: 1,
                level: 'default'
            }
        },
        verbosity: {
            defaultLevel: [
                           'id',
                           'title',
                           'hasImage',
                           'media',
                           'added',
                           'updated',
                           'downloads',
                           'avgRating'
            ],
            extendedLevel: [
                            'author',
                            'summary'
            ],
            completeLevel: [ 'description']
        }
    },
    media: {
        paramDefaults: {
            browse: {
                orderBy: 'rating',
                order: 'asc',
                perPage: 15,
                maxPerPage: 40,
                page: 1,
                level: 'default'
            },
            getByIds: {
                level: 'default',
                maxNumberOfIds: 40
            },
            getByOwner: {
                level: 'default',
                perPage: 15,
                maxPerPage: 40,
                page: 1
            },
            search: {
                searchIn: 'all',
                allowedSearchInFields: [ 'author.name', 'description', 'summary' ],
                orderBy: 'rating',
                order: 'asc',
                perPage: 15,
                maxPerPage: 40,
                page: 1,
                level: 'default'
            }
        },
        verbosity: {
            defaultLevel: [
                            'id',
                            'seriesId',
                            'title',
                            'added',
                            'updated',
                            'downloads',
                            'rating',
                            'ratings',
                            'isLinkedMedia',
                            'link',
                            'ext'
            ],
            extendedLevel: [
                             'comments',
                             'duration',
                             'size',
                             'mimeType',
                             'hasTranscript',
                             'transcriptExt',
                             'transcriptSize',
                             'transcriptMimeType',
                             'additionalFiles',
                             'author',
                             'summary',
                             'language',
                             'hasCaptions',
                             'captionsExt',
                             'captionsRating',
                             'captionsRatings'
            ],
            completeLevel: [ 'pulseId', 'tags', 'description']
        }
    }
};
```
===============================================================================
#关于router, 他是先把 ?method=XXX 转化为对应的/XXX/AAA
#然后再调用express.router分配
#如果还没有对应的router, 就会调到404, 然后send 404 message
#最后是处理error的, 注意 app.use(function(err, req, res, next), 多了err, 只要有error都会直接跳到这里

```javascript
app.use('/', function(req, res, next) {
    var baseUrl = req.url.split('?')[0];
    req.url = (baseUrl + '/' + req.query.method.replace(/\./g, '/')).replace(/\/+/g, '/');
    next();
});

// Configure routes for available API versions.
config.apiVersions.forEach(function(version) {
    app.use('/medialibrary/api/' + version + '/rest/stat', require('routes/' + version + '/stat'));
    app.use('/medialibrary/api/' + version + '/rest/mediaSeries', require('routes/' + version + '/media-series'));
    app.use('/medialibrary/api/' + version + '/rest/media/comment', require('routes/' + version + '/media/comment'));
    app.use('/medialibrary/api/' + version + '/rest/media/tag', require('routes/' + version + '/media/tag'));
    app.use('/medialibrary/api/' + version + '/rest/media', require('routes/' + version + '/media'));
});

// catch 404 and forward to error handler
app.use(function(req, res, next) {
    res.send({
        status: 'fail',
        error: {
            code: config.errorCodes.methodNotFound,
            message: "Method '" + req.query['method'] + "' is not found."
        }
    });
});

app.use(function(err, req, res, next) {
    console.log(err);
    res.status(err.status || 500);
    res.send({
        message: err.message,
        error: {}
    });
});

```

#NOTE: 这种可以一次处理多个url
```javascript
// Handle GET /medialibrary/api/v1/rest?method=stat.getTopTaggers
// and
// Handle GET /medialibrary/api/v1/rest?method=stat.getTopRaters
//
// Both return a list of authors since we don't keep track of these statistics:
// http://apps.topcoder.com/forums/?module=Thread&threadID=838298&start=0
router.get([ '/getTopTaggers', '/getTopRaters' ], function(req, res) {
    var countDefault = statDefaults.getTopTaggers.count;
    var maxCountDefault = statDefaults.getTopTaggers.maxCount;
    var topAuthor = 'topTagger';
    if (req.path === '/getTopRaters') {
        countDefault = statDefaults.getTopRaters.count;
        maxCountDefault = statDefaults.getTopRaters.maxCount;
        topAuthor = 'topRater';
    }

    var count = req.query.count || countDefault;
    if (!helper.validateUpperBoundedInteger('count', count, maxCountDefault, res)) {
        return;
    }
    Media.distinct('author', {}, function(err, authors) {
        if (err) return helper.handleError(err, res);

        var response = { status: 'ok' };
        response[topAuthor + 's'] = { count: authors.length };
        response[topAuthor + 's'][topAuthor] = authors;
        res.send(response);
    });
});
```
===============================================================================

===============================================================================

===============================================================================

===============================================================================

===============================================================================
