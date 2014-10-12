#!/usr/bin/env python3

from frog_java_util import get_java_structure
import frog_util
import frog_xml_util
import frog_sql_util
import os

LS = os.linesep
MAX_CHECKBOX_ONE_LINE = 2

TEMPLATE_RADIO = '''
  <p>
    <label>
      <span class="tip"></span>
      %(label)s
    </label>
    <span class="sep">:</span>
    <input type="radio" name="%(prefix)s-%(id)s" id="%(prefix)s-%(id)s1" value="true"
        data-key="%(var_name)s" <c:if test="${%(package)s.%(var_name)s == true}">checked="checked"</c:if> />
    <label class="rad-lbl rad-lbl-first" for="%(prefix)s-%(id)s1">Yes</label>
    <input type="radio" name="%(prefix)s-%(id)s" id="%(prefix)s-%(id)s2" value="false"
        data-key="%(var_name)s" <c:if test="${%(package)s.%(var_name)s == false}">checked="checked"</c:if> />
    <label class="rad-lbl" for="%(prefix)s-%(id)s2">No</label>
  </p>
'''


TEMPLATE_NUM = '''
  <p>
    <label>
      <span class="tip"></span>
      %(label)s
    </label>
    <span class="sep">:</span>
    <input type="text" class="text number-only" maxlength="9" id="%(prefix)s-%(id)s-num"
        data-key="%(var_name)s" value="${%(package)s.%(var_name)s}" />
  </p>
'''


TEMPLATE_CHECKBOX = '''
                  <input type="checkbox" id="%(prefix)s-%(id)s" data-key="%(var_name)s"
                    <c:if test="${%(package)s.%(var_name)s}">checked="checked"</c:if>
                    class="content-toggle" data-toggle=".%(prefix)s-%(id)s-toggled"/>
                  <label class="chk-lbl" for="%(prefix)s-%(id)s">%(label)s</label>
'''

TEMPLATE_CHECKBOX_LAST_POS = '''
                  <input type="checkbox" id="%(prefix)s-%(id)s" data-key="%(var_name)s"
                    <c:if test="${%(package)s.%(var_name)s}">checked="checked"</c:if>
                    class="content-toggle" data-toggle=".%(prefix)s-%(id)s-toggled"/>
                  <label class="chk-lbl chk-lbl-last" for="%(prefix)s-%(id)s">%(label)s</label>
                </div>
'''

TEMPLATE_SELECT_CHECKBOXES = '''
            <div class="check-set check-set-inline" id="XXX-services" data-num-per-row="1">
              <p>
                <label>
                  <span class="tip"></span>
                  %(label)s
                </label>
                <span class="sep">:</span>
              </p>
              %(content)s
            </div>
'''


INPUT_VALUES4 = '''
PACKAGE = request.viprRequestData.planningDesignImpl.feature
PREFIX  = vipr-pdi
=RADIO==  |  newImplType   |  new_impl_type     |  Implementation Type
=RADIO== |  dsForObject        |  ds_for_object         |  Include Data Services for Object?
=RADIO== |  dsForHDFS          |  ds_for_hdfs           |  Include Data Services for HDFS?
=RADIO== |  activeDirectory    |  active_directory      |  Include integration with Active Directory/LDAP?
=RADIO== |  kerberosForViPRFS  |  kerberos_for_vi_prfs  |  Include Kerberos Authentication Mode for ViPR FS?
=RADIO== |  casAPISupport      |  cas_api_support       |  Include ViPR Content Address Storage (CAS) API Support?
=RADIO== |  watch4net          |  watch4net             |  Does a Watch4net platform exist on site that meets ViPR requirements?
=RADIO== |  blockServices      |  block_services        |  Include Block Services Storage Ingestion?
=RADIO== |  thirdPartySystem   |  third_party_system    |  Include installations of ViPR software for third party system integrat
=RADIO== |  vCOps              |  v_c_ops               |  Include integration with VMware vCenter Operations (vCOps)?
=RADIO== |  vCO                |  v_co                  |  Include integration with VMware vCenter Orchestrator (vCO)?
=RADIO== |  vCAC               |  v_cac                 |  Include integration with VMware vCloud Automation Center (vCAC)?
=RADIO== |  microsoftSCVMM     |  microsoft_scvmm       |  Include integration with Microsoft SCVMM ?
=RADIO== |  emcVSI             |  emc_vsi               |  Include integration with EMC VSI (for VMware vSphere Web Client)?
'''




input_values = INPUT_VALUES4.replace('_', '-')
PACKAGE = ''
PREFIX = ''
checkbox_content = ''
checkbox_label = ''
checkbox_index = 0

print("======================================================")
print()
print(input_values)
print()
print("======================================================")

for line in input_values.splitlines():
  line = line.strip()
  if len(line) == 0:
    continue
  if line.startswith('PACKAGE'):
    PACKAGE = line[10:]
    continue
  if line.startswith('PREFIX'):
    PREFIX = line[10:]
    continue

  values = line.split('|')
  # remove useless white space
  for i in range(len(values)):
    values[i] = values[i].strip()

  if not values[0].startswith('=CHECK==') and checkbox_content:
    print(TEMPLATE_SELECT_CHECKBOXES.rstrip() % {'content':checkbox_content,'label':checkbox_label})
    checkbox_content = ''
    checkbox_label = ''
    checkbox_index = 0

  if values[1].endswith('-selected'):
    values[1] = values[1][:-9]
  fx_vals = {'package':PACKAGE, 'prefix':PREFIX, 'var_name':values[1],'id':values[2],'label':values[3]}
  if values[0].startswith('========'):
    if fx_vals['id'].endswith('s'):
      fx_vals['id'] = fx_vals['id'][:-1]
    print(TEMPLATE_NUM.rstrip() % fx_vals)
  elif values[0].startswith('=RADIO=='):
    print(TEMPLATE_RADIO.rstrip() % fx_vals)
  elif values[0].startswith('=CHECK=='):
    if checkbox_index == 0:
      checkbox_content += LS + '                <div>'

    checkbox_index += 1
    if checkbox_index % MAX_CHECKBOX_ONE_LINE == 0:
      checkbox_content += TEMPLATE_CHECKBOX_LAST_POS.rstrip() % fx_vals
      checkbox_index = 0
    else:
      checkbox_content += TEMPLATE_CHECKBOX.rstrip() % fx_vals

if checkbox_content:
  if not checkbox_content.endswith('</div>'):
    checkbox_content += LS + '                </div>'
  print(checkbox_content)



