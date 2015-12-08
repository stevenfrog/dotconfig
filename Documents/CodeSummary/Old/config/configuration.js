/*
 * Copyright (C) 2014 TopCoder Inc., All Rights Reserved.
 */
"use strict";

/**
 * This module represents application configuration.
 * @author ibraaaa
 * @version 1.0
 */
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
            getById: {
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
            getById: {
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
            getFeaturedSelections: {
                level: 'default',
                count: 15,
                maxCount: 40
            },
            getHighestRatedNewMedia: {
                level: 'default',
                count: 15,
                maxCount: 40
            },
            getMostPopularNewMedia: {
                level: 'default',
                count: 15,
                maxCount: 40
            },
            getMostRecentNewMedia: {
                level: 'default',
                count: 15,
                maxCount: 40
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
        },
        tag: {
            paramDefaults: {
                autoComplete: {
                    count: 15,
                    maxCount: 40
                },
                getPopular: {
                    count: 15,
                    maxCount: 40
                }
            }
        },
        comment: {
            paramDefaults: {
                browse: {
                    page: 1,
                    perPage: 15,
                    maxPerPage: 40
                }
            }
        }
    }
};