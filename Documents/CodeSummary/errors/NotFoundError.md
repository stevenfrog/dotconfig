```javascript
/*
 * Copyright (c) 2014 TopCoder, Inc. All rights reserved.
 */
"use strict";

/**
 * This file defines NotFoundError
 *
 * @author TCSASSEMBLER
 * @version 1.0
 */

/**
 * Constructor of NotFoundError
 * @param {Object} message the error message
 * @param {Object} cause the error cause
 */
var NotFoundError = function (message, cause) {
    //captureStackTrace
    Error.call(this);
    Error.captureStackTrace(this);
    this.message = message || "NotFoundError";
    this.status = 404;
    this.errorCode = 404;
    this.cause = cause;
};

//use Error as prototype
require('util').inherits(NotFoundError, Error);
NotFoundError.prototype.name = 'NotFoundError';

module.exports = NotFoundError;
```
