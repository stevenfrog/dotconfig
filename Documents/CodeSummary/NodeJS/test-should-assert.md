### @should @test @assert ==================================================================
# 有关Test Case中的should

## `.equal(value)` 是恒等, 等于===, 所以不能用来确认array, object

```javascript
should('hello').be.equal('hello');
should(42).be.equal(42);
should(1).be.not.equal(true);
should({ foo: 'bar' }).be.not.equal({ foo: 'bar' });
```

## `.eql(value)` 是值等, 等于==, 可以用来确认array, object

```javascript
should({ foo: 'bar' }).be.eql({ foo: 'bar' });
should([ 1, 2, 3 ]).be.eql([ 1, 2, 3 ]);
```


```javascript
var should = require('should');

should.not.exist(null);
should(null).not.be.ok();
should(null).not.ok();

var body = {id: 2, email: 'test@tc.com'};
should(body).be.ok();
should(body).ok();
should(body.id).equal(2);
should(body.email).equal('test@tc.com');

should({a: 1, b: 1}).not.equal({a: 1, b: 1});
should({a: 1, b: 1}).eql({a: 1, b: 1});
should([1, 2, 3]).eql([1, 2, 3]);
should('ab').equalOneOf(['a', 10, 'ab']);


should('abcd').startWith('a');
should('abcd').endWith('d');

should([1, 2, 3].indexOf(3)).be.equal(2);
should([1, 2, 3]).have.length(3);

should({a: 10}).keys('a');
should({a: 10, b: 20}).have.keys('a', 'b');
should({a: 10, b: 20}).have.properties({b: 20});


should([1, 2]).be.Array();
should(true).be.Boolean();
// should(xxx).be.Error();
// should(xxx).be.Function();
should(1).be.Number();
should(body).be.Object();
should('abc').be.String();
should('abc').be.instanceof(String);
should(null).be.null();
should(undefined).be.undefined();
should(NaN).not.be.Infinity();
should(NaN).be.NaN();

should('').empty();
should([]).empty();
should({}).be.empty();

should('foobar').match(/^foo/);
should('foobar').not.match(/^bar/);

should('abc').String().and.match(/abc|bcd/);

should(5).match(function(n) {
  return n > 0;
});
should(5).not.match(function(it) {
  it.should.be.an.Array();
});
```


### @test ==================================================================
## Test Suit 的格式
一般来说文件的名字是`user.test.js`

```javascript
'use strict'

var should = require('should');

before(function(done) {
  _runTestServer({}, function(srvInstance) {
    serverInstance = srvInstance;
    console.log('=== node server started ===');
    done();
  });
});

after(function(done) {
  var pid = serverInstance.pid;
  // The pid of child process is just next to serverInstance
  process.kill(pid + 1);
  serverInstance.kill();
  console.log('=== node server closed ===');
  done();
});

describe('Service Tests For User controllers', function() {

  context('This is second description', function() {

    it('should return -1 when the value is not present', function() {
      should([1, 2, 3].indexOf(0)).be.equal(-1);
      should([1, 2, 3].indexOf(5)).be.equal(-1);
    });

    it.skip('这个是被忽略的Test', function(done) {
       done();
    }

    it.only('只有这个Test会被执行, 整个文件中其余的都被忽略', function(done) {
       done();
    }

  });

});
```
