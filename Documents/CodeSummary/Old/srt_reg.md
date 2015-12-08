**REGEX**

~~Delete~~

_There may be og_

**SRT checkbox**
@checkbox
```html
<input type="checkbox" id="data-domain-upgrade-chk" data-key="upgradeService"
  <c:if test="${request.dpadRequestData.dataDomain.upgradeService}">checked="checked"</c:if>
  class="content-toggle" data-toggle=".data-domain-upgrade"/>
```

```html
<input type="checkbox" id="data-domain-upgrade-chk" data-key="upgradeService"
  <c:if test="${request.dpadRequestData.dataDomain.upgradeService}">checked="checked"</c:if> />
```

```html
<input type="checkbox" id="data-domain-activity-design-chk" data-key="designActivity" <c:if test="${request.dpadRequestData.dataDomain.designActivity}">checked="checked"</c:if> />
```

```html
<input type="checkbox" id="data-domain-upgrade-dd890-chk" data-key="dd890" <c:if test="${request.dpadRequestData.dataDomain.upgrade.dd890}">checked="checked"</c:if>
  class="content-toggle" data-toggle=".data-domain-upgrade-system-controller-dd890 .right-toggle" />
```

-->

```html
<input type="checkbox" id="data-domain-upgrade-chk" data-ng-model="request.dpadRequestData.dataDomain.upgradeService" />
```


--------------------


```html
<input type="checkbox" id="([\w-]+)" data-key="\w+"(?: |\n +)<c:if test="\$\{([\w\.]+)\}">checked="checked"</c:if>(?: ?/>|\n\s+[\S ]+/>| ?[\S ]+\n\s+[\S ]+/>)

<input type="checkbox" id="([\w-]+)" data-key="\w+"(?: |\n +)<c:if test="\$\{([\w\.]+)\}">checked="checked"</c:if>(?: |\n +)class="[\w-]+"(?: |\n +)data-toggle="([.\w-]+)" ?/>
```

-->

```html
<input type="checkbox" id="$1" data-ng-model="$2" />
```

========================================================================================

**SRT radio**

```html
<input type="radio" name="data-domain-prerack-integrate-sap-hana" id="data-domain-prerack-integrate-sap-hana1" value="true"
  class="content-toggle" data-toggle=".data-domain-prerack-integrate-sap-hana-toggled"
  data-key="integrateSapHana" <c:if test="${request.dpadRequestData.dataDomain.preRack.integrateSapHana == true}">checked="checked"</c:if> />
<label class="rad-lbl rad-lbl-first" for="data-domain-prerack-integrate-sap-hana1">Yes</label>
<input type="radio" name="data-domain-prerack-integrate-sap-hana" id="data-domain-prerack-integrate-sap-hana2" value="false"
  class="content-toggle" data-toggle=".data-domain-prerack-integrate-sap-hana-toggled"
  data-key="integrateSapHana" <c:if test="${request.dpadRequestData.dataDomain.preRack.integrateSapHana == false}">checked="checked"</c:if> />
<label class="rad-lbl" for="data-domain-prerack-integrate-sap-hana2">No</label>
```

-->

```html
<label class="form-group" enter-press>
  <input type="radio" id="data-domain-prerack-integrate-sap-hana-1" name="data-domain-prerack-integrate-sap-hana" data-ng-model="request.dpadRequestData.dataDomain.preRack.integrateSapHana" data-ng-value="true"/>
  <i></i><span>Yes</span>
</label>
<label class="form-group" enter-press>
  <input type="radio" id="data-domain-prerack-integrate-sap-hana-2" name="data-domain-prerack-integrate-sap-hana" data-ng-model="request.dpadRequestData.dataDomain.preRack.integrateSapHana" data-ng-value="false"/>
  <i></i><span>No</span>
</label>
```


--------------------


```html
( +)<input type="radio" name="([\w-]+)" id="[\w-]+" value="true"(?: |\n\s+)data-key="[\w]+"(?: |\n\s+)<c:if test="\$\{([\w\.]+) == true\}">checked="checked"</c:if> ?/>
\s+<label[\S ]+>Yes</label>
\s+<input type="radio" name="([\w-]+)" id="[\w-]+" value="false"(?: |\n\s+)data-key="[\w]+"(?: |\n\s+)<c:if test="\$\{([\w\.]+) == false\}">checked="checked"</c:if> ?/>
\s+<label[\S ]+>No</label>
```

-->

```html
$1<label class="form-group" enter-press>
$1  <input type="radio" id="$2-1" name="$2" data-ng-model="$3" data-ng-value="true"/>
$1  <i></i><span>Yes</span>
$1</label>
$1<label class="form-group" enter-press>
$1  <input type="radio" id="$2-2" name="$2" data-ng-model="$3" data-ng-value="false"/>
$1  <i></i><span>No</span>
$1</label>
```

========================================================================================

**SRT input**

```html
<input type="text" class="text number-only" maxlength="9" id="data-domain-sap-hana-integration-dbs-num"
  data-key="sapHanaDatabasesNum" value="${request.dpadRequestData.dataDomain.sapHana.sapHanaDatabasesNum}" />
```

-->

```html
<input type="text" class="text number-only" maxlength="9" id="data-domain-sap-hana-integration-dbs-num" data-ng-model="request.dpadRequestData.dataDomain.sapHana.sapHanaDatabasesNum" allownumber />
```


--------------------


```html
<input type="text" class="text number-only" maxlength="9" id="([\w-]+)"(?: |\n +)data-key="\w+"(?: |\n +)value="\$\{([\w.]+)\}" />
```

-->

```html
<input type="text" class="text number-only" maxlength="9" id="$1" data-ng-model="$2" allownumber />
```



====================================================================================================
```html
<c\:out value="\$\{request.([\S]+)\}" ?/>

{{serviceRequest.$1}}
```

```html
<fmt\:formatNumber value="\$\{request.([\S]+)\}" groupingUsed="false" maxFractionDigits="2" minFractionDigits="2" ?/>

{{serviceRequest.$1 | number:2}}
```

```html
<fmt\:formatNumber value="\$\{request.([\S]+)\}" pattern="00" />

{{serviceRequest.$1 | zeroEmptyPattern}}
```

```html
( +)<c\:choose>
\s+<c\:when test="\$\{request.([\S]+) == true\}">Yes</c\:when>
\s+<c\:when test="\$\{request.[\S]+ (== false|!= true)\}">No</c\:when>
\s+<c\:otherwise></c\:otherwise>
\s+</c\:choose>

$1{{serviceRequest.$2 | true_false}}
```

```html
<c\:out value="\$\{request.([\S]+)\}" />

{{serviceRequest.$1}}
```

```html
<c\:out value="\$\{request.([\S]+)\}" />

{{serviceRequest.$1}}
```
