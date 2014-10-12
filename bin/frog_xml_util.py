#!/usr/bin/env python3

from pyquery import PyQuery as pq
import frog_util


"""
Example of template and input values
"""

TEMPLATE = '''
  <p>
    <label>
      <span class="tip"></span>
      %(c)s
    </label>
    <span class="sep">:</span>

    <input type="radio" name="%(b)s" id="%(b)s1" value="true"
        data-key="%(a)s" <c:if test="${request.dpadRequestData.dpa.dpaDesignService.%(a)s == true}">checked="checked"</c:if> />
    <label class="rad-lbl rad-lbl-first" for="%(b)s1">Yes</label>
    <input type="radio" name="%(b)s" id="%(b)s2" value="false"
          data-key="%(a)s" <c:if test="${request.dpadRequestData.dpa.dpaDesignService.%(a)s == false}">checked="checked"</c:if> />
    <label class="rad-lbl" for="%(b)s2">No</label>
  </p>
'''

INPUT_VALUES = '''
includeDPAExtDB                   |  include_dpa_ext_db                   |  Install Data Protection Advisor on Extended Database (Oracle, MS SQL, etc.)
includeDPAAnalysisJobs            |  include_dpa_analysis_jobs            |  Include Data Protection Advisor Analysis Jobs
includeDPARecoverabilityAnalysis  |  include_dpa_recoverability_analysis  |  Include Data Protection Advisor Recoverability Analysis
includeDPACustomReportDev         |  include_dpa_custom_report_dev        |  Include Data Protection Advisor Custom Report Development
includeDPAInterfaceCustomization  |  include_dpa_interface_customization  |  Include Data Protection Advisor Interface Customization
includeDPAScalePlan               |  include_dpa_scale_plan               |  Include Data Protection Advisor Scale Plan
'''


TEMPLATE2 = '''
  <p>
    <label>
      <span class="tip"></span>
      %(c)s
    </label>
    <span class="sep">:</span>
    <input type="text" class="text number-only" maxlength="9" id="%(b)s-num"
        data-key="%(a)s" value="${request.dpadRequestData.dpa.dpaDesignService.%(a)s}" />
  </p>
'''

INPUT_VALUES2 = '''
dpaCollectionNodes                |  dpa_collection_nodes                 |  # of Data Protection Advisor Collection Nodes
dpaCollectionNodesConfig          |  dpa_collection_nodes_config          |  # of Data Protection Collector Nodes to Configure
'''


def applyTemplate(tempate, input_values):
    PARAM_NAMES = ['a', 'b', 'c', 'd', 'e']

    for line in input_values.splitlines():
        if len(line.strip()) == 0:
            continue
        values = line.split('|')

        # a='abcd,abcd|abcd:abcd'
        # import re
        # re.split(r",|\||:", 'abcd,abcd|abcd:abcd')
        # ['abcd', 'abcd', 'abcd', 'abcd']
        fx_vals = {}
        for idx, val in enumerate(values):
            fx_vals[PARAM_NAMES[idx]] = val.strip()

        print(tempate.rstrip() % fx_vals)


if __name__ == '__main__':

    """
    Example that how to query xml file like jQuery
    """

    d = pq(filename='test_files/dpad.html')

    print('=======================================')
    print()

    elements = []
    for subtitle in d('div.general-info-sec div.sub-title'):
        elements.append('### '+ pq(subtitle).text())
        elements.append("")

        for elm in pq(subtitle).parent().find('p label span.tip'):
            elements.append(pq(elm).parent().text())

        elements.append("")

    for ele in elements:
        print(ele)
