/*
 * Copyright (C) 2015 TopCoder, Inc. All Rights Reserved.
 */
/**
 * Contains validation functions
 *
 * @author TCSASSEMBLER
 * @version 1.0
 */
"use strict";

var errors = require('./errors');
var validator = require('rox').validator;

var EMAIL_REG = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;


/**
 * Define a global function used for validation.
 * @param {Object} input the object to validate
 * @param {Object} definition the definition object. Refer to rox module for more details.
 * @param {String} [prefix] the prefix for error message.
 * @returns {Error|Null} error if validation failed or null if validation passed.
 */
function validate(input, definition, prefix) {
    var error = validator.validate(prefix || "prefix-to-remove", input, definition);
    if (!error) {
        return null;
    }
    //remove prefix in error message
    error.message = error.message.replace("prefix-to-remove.", "");
    //if input is invalid then change the name to input
    error.message = error.message.replace("prefix-to-remove", "input");
    return new errors.ValidationError(error.message);
}

validator.registerAlias('IntegerId', {type: 'Integer', min: 1, castString: true});
validator.registerAlias('IntegerId?', {type: 'Integer', min: 1, required: false, castString: true});

validator.registerAlias('String?', {type: String, required: false});
validator.registerAlias('Boolean?', {type: Boolean, required: false});
validator.registerAlias('Integer?', {type: 'Integer', required: false, castString: true});
validator.registerAlias('Number?', {type: 'Number', required: false});

// email
validator.registerType({
    name: 'email',
    validate: function (name, value, params, validator) {
        var notString = validator.validate(name, value, 'string');
        if (notString || !EMAIL_REG.test(value)) {
            return new Error(name + ' should be a valid email address');
        }
        return null;
    }
});

validator.registerType({
    name: "date",
    /**
     * Validate if value is valid date
     * @param {String} name the property name
     * @param {*} value the value to check
     * @returns {Error|Null} null if type is valid or error if invalid
     */
    validate: function (name, value) {
        if (value instanceof Date) {
            return null;
        }
        return new Error(name + " should be a Date");
    }
});

module.exports = {
    validate: validate
};
