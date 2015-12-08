/*
 * Copyright (c) 2015 TopCoder, Inc. All rights reserved.
 */
/**
 * Gulp configuration file
 *
 * @author TCSASSEMBLER
 * @version 1.0
 */
'use strict';


var gulp = require('gulp');
var jshint = require('gulp-jshint');

gulp.task('lint', function() {
  return gulp.src([
    'config/*.js',
    'controllers/*.js',
    'helpers/*.js',
    'models/*.js',
    'services/*.js',
    'app.js'
  ])
    .pipe(jshint())
    .pipe(jshint.reporter('default'))
    .pipe(jshint.reporter('fail'));
});


gulp.task('default', ['lint']);
