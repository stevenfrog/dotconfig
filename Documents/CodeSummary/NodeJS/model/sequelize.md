### @sequenlize @model =========================================================
# sequelize.js是nodejs用于关系数据库的中间件
# 主要支持MySQL, PostgreSQL, MariaDB, SQLite and MSSQL


```javascript
var constant = {
  HOUSE_STATUS: {
    pending: 'pending',
    completed: 'completed'
  }
}

module.exports = function(sequelize, DataTypes) {
  return sequelize.define('House', {
    id: {type: DataTypes.INTEGER, primaryKey: true, autoIncrement: true},

    address: {type: DataTypes.STRING, allowNull: false},
    zip: {type: DataTypes.STRING, allowNull: false},

    flag: { type: DataTypes.BOOLEAN, allowNull: false, defaultValue: true},
    myDate: { type: DataTypes.DATE, defaultValue: DataTypes.NOW },

    someUnique: {type: DataTypes.STRING, unique: true},
    uniqueOne: { type: DataTypes.STRING,  unique: 'compositeIndex'},
    uniqueTwo: { type: DataTypes.INTEGER, unique: 'compositeIndex'}

    systemCost: DataTypes.DOUBLE,
    solarProduction: DataTypes.ARRAY(DataTypes.DOUBLE),

    houseOfInterest: DataTypes.ARRAY(DataTypes.INTEGER),  // ids of interested houses

    status: {type: DataTypes.ENUM, allowNull: false, values: _.values(constant.HOUSE_STATUS), defaultValue: constant.HOUSE_STATUS.pending }
  }, {
    tableName: 'houses',
    timestamps: false
  });
};
```


### @sequenlize @model =========================================================
# 尽量不使用belongsTo, belongsToMany, 主次关系混乱, 可以直接定义中间Table
**注意`references model: 'users'`这个是指sequenlize理解的model, 一般是名字小写加上s**

```javascript
module.exports = function(sequelize, DataTypes) {
  return sequelize.define('FinancierCustomer', {
    id: {type: DataTypes.INTEGER, primaryKey: true, autoIncrement: true},

    financierUserId: {
      type: DataTypes.INTEGER,
      references: {model: 'users', key: 'id'}
    },
    houseInfoId: {
      type: DataTypes.INTEGER,
      references: {model: 'houseInfos', key: 'id'}
    },
    authorizedAccess: {type: DataTypes.BOOLEAN, defaultValue: false}
  }, {
    tableName: 'financier_customers',
    timestamps: false
  });
};
```


### @sequenlize @model @hash ===================================================
# 这段是有关User的定义, 在`User`内部实现了`hash password`

```javascript
var bcrypt = require("bcrypt-nodejs");

/**
 * Hash a user's password.
 * @param password the raw password
 * @returns {*}
 */
function _hashPassword(password) {
  bcrypt.genSaltAsync(config.SALT_FACTOR)
    .then(function(salt) {
      return bcrypt.hashAsync(password, salt, null);
    });
}


module.exports = function(sequelize, DataTypes) {
  var schema = sequelize.define('User', {
    id: {type: DataTypes.INTEGER, primaryKey: true, autoIncrement: true},
    email: {type: DataTypes.STRING, allowNull: false, unique: true},
    password: {type: DataTypes.STRING, allowNull: true},
    firstname: {type: DataTypes.STRING, allowNull: false},
    lastname: {type: DataTypes.STRING, allowNull: false},
    role: {type: DataTypes.ENUM, allowNull: false, values: _.values(constant.USER_ROLE)}
  }, {
    tableName: 'users',
    timestamps: false,
    instanceMethods: {
      comparePassword: function(candidatePassword, callback) {
        bcrypt.compareAsync(candidatePassword, this.password).then(function(isMatch) {
          callback(null, isMatch);
        }).catch(callback);
      }
    }
  });

  schema.beforeCreate(function(user) {
    return _hashPassword(user.password).then(function(hashedPw) {
      user.password = hashedPw;
    }).catch(function(err) {
      console.log('Error on hashing password:', err);
      return sequelize.Promise.rejected();
    });

  });

  schema.beforeUpdate(function(user) {
    if (user.changed('password')) {
      return _hashPassword(user.password).then(function(hashedPw) {
        user.password = hashedPw;
      }).catch(function(err) {
        console.log('Error on hashing password:', err);
        return sequelize.Promise.rejected();
      });
    }
  });

  return schema;
};
```
