#!/usr/bin/env python3

from frog_java_util import get_java_structure
import frog_util
import frog_xml_util
import frog_sql_util
import os

INPUT_NAMES = '''
 AvamarTemplateType serverTemplate
 boolean planningOption
 boolean apiPackageInstallOption
 boolean solutionOption
 BigDecimal planningHours
 BigDecimal apiPackageInstallHours
 BigDecimal solutionDeployHours
 BigDecimal solutionValidateHours
 BigDecimal overviewHours
'''


java_structure = {}
java_structure['package'] = 'com.emc.gs.tools.srf.model.dpad'
java_structure['classdoc'] = []
java_structure['class'] = 'DataProtectionAdvisor'
java_structure['fields'] = []
java_structure['methods'] = []

for f in INPUT_NAMES.splitlines():
    if not f:
        print('||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
        continue
    print()
    strs = f.split()

    java_structure['fields'].append((strs[0], strs[1]))


#print(frog_sql_util.generateCreateSQL(java_structure))
#print()
#print()

CREATE_TABLE = '''
CREATE TABLE a (
    id BIGINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    srv_template_id BIGINT,
    planning_option BOOLEAN NOT NULL,
    api_package_install_option BOOLEAN NOT NULL,
    solution_option BOOLEAN NOT NULL,
    planning_hours DECIMAL(20,2),
    api_package_install_hours DECIMAL(20,2),
    solution_deploy_hours DECIMAL(20,2),
    solution_validate_hours DECIMAL(20,2),
    overview_hours DECIMAL(20,2),
    FOREIGN KEY (srv_template_id) REFERENCES AvamarTemplateType(id)
)

'''



INPUT_ORM_DATA = '''
----- com.emc.gs.tools.srf.model.dpad -----
===== a =====
AvamarTemplateType  |  serverTemplate           |  srv_template_id             |  ManyToOne
boolean             |  planningOption           |  planning_option             |  BOOLEAN NOT NULL
boolean             |  apiPackageInstallOption  |  api_package_install_option  |  BOOLEAN NOT NULL
boolean             |  solutionOption           |  solution_option             |  BOOLEAN NOT NULL
BigDecimal          |  planningHours            |  planning_hours              |  DECIMAL(20,2)
BigDecimal          |  apiPackageInstallHours   |  api_package_install_hours   |  DECIMAL(20,2)
BigDecimal          |  solutionDeployHours      |  solution_deploy_hours       |  DECIMAL(20,2)
BigDecimal          |  solutionValidateHours    |  solution_validate_hours     |  DECIMAL(20,2)
BigDecimal          |  overviewHours            |  overview_hours              |  DECIMAL(20,2)
'''

print()
print('===========================================================')
print(frog_sql_util.generateORMEntity(INPUT_ORM_DATA))
