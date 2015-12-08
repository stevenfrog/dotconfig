#建立模型:

```javascript
/*
 * Copyright (c) 2012 - 2014 TopCoder, Inc. All rights reserved.
 *
 */
"use strict";
var mongoose = require('mongoose');
var Schema = mongoose.Schema, ObjectId = Schema.ObjectId;

var WikiPageSchema = new Schema({
    spaceKey:{ type:String, required:true, index:true},
    labels:[{
        type: ObjectId,
        ref: 'WikiTag',
        required: false
    }],
    count:{ type:Number, required:true},
    readPermission:{
        type:{type:String, 'enum':[ "PUBLIC", "REGISTERED", "SPECIFIED", "PRIVATE", "GROUP"], required:true},
        values:{ type:[String], 'default':[]}
    },
    attachments: [{ type: ObjectId, ref: 'WikiAttachment' }],
    comments:[{
        text:{ type:String, required:true},
        commentedBy:{ type:String, required:true},
        commentedOn:{ type:Date, required:true}
    }] ,
    titleWords:{type:[String], 'default':[],index:true},
    createdBy:{ type:String, required:true,index:true },
    createdOn:{ type:Date, required:true, default: Date.now },
    publishedOn:{ type:Date},
    deleted :{ type:Boolean, required:true,'default':false},
    deletedBy:{ type:String },
    deletedOn:{ type:Date},
    favoredBy:{type:[String], 'default':[]},
    status:{type:String, 'enum':[ "PUBLISHED", "DRAFT"], required:false},
    binary:  Buffer,
});

/**
 * Makes each wikipage combination unique.
 * see readable and writable will find one result using spaceKey and title.
 */
WikiPageSchema.index({ spaceKey: 1, title: 1}, {unique : true});

// rename _id to id when calling toObject({transform: true}))
SavedSearchSchema.options.toObject = {
    transform: function (doc, ret) {
        ret.id = doc._id;
        delete ret._id;
    }
};

module.exports = {
    WikiPageSchema:WikiPageSchema
};

```
