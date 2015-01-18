#!/usr/bin/env python3
"""
This class provide util method for SQL.
"""

import os
import frog_util

LS = os.linesep



def generateCreateSQL(java_structure):

    SQL_TYPE_MAP = {
        'boolean'    : 'BOOLEAN NOT NULL',
        'int'        : 'INT NOT NULL',
        'long'       : 'BIGINT NOT NULL',
        'Integer'    : 'INT',
        'Long'       : 'BIGINT',
        'String'     : 'VARCHAR(255)',
        'Boolean'    : 'BOOLEAN',
        'Date'       : 'TIMESTAMP',
        'BigDecimal' : 'DECIMAL(20,2)'
    }

    TEMPLATE_TABLE_MANY_TO_ONE = '''
    CREATE TABLE %(class_one)s_%(class_two)s (
        id BIGINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
        %(class_one_id)s BIGINT,
        %(class_two_id)s BIGINT,
        FOREIGN KEY (%(class_one_id)s) REFERENCES %(class_one)s (id),
        FOREIGN KEY (%(class_two_id)s) REFERENCES %(class_two)s (id)
    );
    '''


    #res  = ('CREATE TABLE %s (' % java_structure['class'][1]) + LS
    #res += '    id BIGINT AUTO_INCREMENT NOT NULL PRIMARY KEY,' + LS

    # For SRT HTML5
    res = ('CREATE SEQUENCE S%s INCREMENT BY 1 START WITH 1000;' % java_structure['class'][1]) + LS
    res += LS
    res += ('CREATE TABLE %s (' % java_structure['class'][1]) + LS
    res += ("    id BIGINT NOT NULL PRIMARY KEY DEFAULT nextval('S%s')," % java_structure['class'][1]) + LS

    all_keys = []
    foreign_keys = []
    list_keys = []
    for var_type, var_value in java_structure['fields']:
        tmp_name = frog_util.abbreviate(var_value)
        sql_var_name = frog_util.uncamel_name(tmp_name, split_char='_')

        if var_type in SQL_TYPE_MAP:
            res += ('    %s %s,' %  (sql_var_name, SQL_TYPE_MAP[var_type]))+ LS
            all_keys.append((var_type, var_value, sql_var_name, SQL_TYPE_MAP[var_type]))
        elif var_type.startswith('List'):
            list_keys.append((var_type, var_value))
        else:
            sql_var_name += '_id'
            res += ('    %s BIGINT,' %  sql_var_name)+ LS
            foreign_keys.append((var_type, sql_var_name))
            #all_keys.append((var_type, var_value, sql_var_name, 'ManyToOne'))
            all_keys.append((var_type, var_value, sql_var_name, 'OneToOne'))

    for var_type, sql_var_name in foreign_keys:
        res += ('    FOREIGN KEY (%s) REFERENCES %s(id),' % (sql_var_name, var_type))+ LS

    # remove the last comma
    res = res[:-2] + LS + ');' + LS


    # create realted table for List
    for var_type, var_value in list_keys:
        classOne = java_structure['class'][1]
        classOneId = frog_util.uncamel_name(classOne, split_char='_') + '_id'
        classTwo = var_type[5:-1]
        classTwoId = frog_util.uncamel_name(classTwo, split_char='_') + '_id'

        res += LS
        res += TEMPLATE_TABLE_MANY_TO_ONE % {'class_one':classOne, 'class_one_id':classOneId, 'class_two':classTwo, 'class_two_id':classTwoId}

        all_keys.append((var_type, var_value, classOne+'_'+classTwo, 'OneToMany'))


    # show all java variable and sql column name
    print('-----', java_structure['package'], '-----')
    print('=====', java_structure['class'][1], '=====')
    frog_util.printAlignedArray(all_keys, all_column_char='|')
    print()

    return res



"""
================================================================================
The is example for super abstract class

<mapped-superclass class="com.emc.gs.tools.srf.model.IdentifiableEntity">
    <attributes>
        <id name="id">
            <column name="id" />
            <generated-value strategy="IDENTITY" />
        </id>
    </attributes>
</mapped-superclass>

<mapped-superclass class="com.emc.gs.tools.srf.model.LookupEntity">
    <attributes>
        <basic name="name">
            <column name="name" />
        </basic>
    </attributes>
</mapped-superclass>

================================================================================
This is example for embedded, we can use it to improve effective.
Because DB just need fetch one table instead of two.
Just put variable in one table directly.

fax_country_code VARCHAR(256),
fax_number VARCHAR(256),

<embedded name="officePhone">
    <attribute-override name="countryCode">
        <column name="office_phone_country_code" nullable="true"/>
    </attribute-override>
    <attribute-override name="phoneNumber">
        <column name="office_phone_number" nullable="true"/>
    </attribute-override>
</embedded>

================================================================================
This is a lookup entity, the result is always same, so use 'cacheable' is effective.

<entity name="RiskLevel" class="com.emc.gs.tools.srf.model.RiskLevel" cacheable="true">
    <table name="RiskLevel" />
</entity>
"""



INPUT_ORM_DATA = '''
----- com.emc.gs.tools.srf.model.dpad -----
===== DataProtectionAdvisorDesign =====
Boolean  |  includeDPAExtDB                    |  include_dpa_ext_db
Boolean  |  includeDPAAnalysisJobs             |  include_dpa_analysis_jobs
Boolean  |  includeDPARecoverabilityAnalysis   |  include_dpa_recoverability_analysis
Boolean  |  includeDPACustomReportDev          |  include_dpa_custom_report_dev
Boolean  |  includeDPAInterfaceCustomization   |  include_dpa_interface_customization
Boolean  |  includeDPAScalePlan                |  include_dpa_scale_plan
Integer  |  dpaCollectionNodes                 |  dpa_collection_nodes
Integer  |  dpaCollectionNodesConfig           |  dpa_collection_nodes_config
'''

INPUT_ORM_DATA2 = '''
----- com.emc.gs.tools.srf.model.dpad -----
===== DataProtectionAdvisor =====
BigDecimal                                 |  knowledgeTransferHours          |  knowledge_transfer_hours
String                                     |  implService                     |  impl_service
int                                        |  operationalAssuranceService     |  operational_assurance_service
Integer                                    |  customizationService            |  customization_service
boolean                                    |  upgradeMigrationService         |  upgrade_migration_service
boolean                                    |  healthCheckService              |  health_check_service
boolean                                    |  ddaDesign                       |  dda_design
boolean                                    |  ddaImplementation               |  dda_impl
Boolean                                    |  retentionLockingOption          |  retention_locking_option
DataProtectionAdvisorDesign                |  dpaDesignService                |  dpa_design_service_id                 |M2O
DataProtectionAdvisorImplementation        |  dpaImplementationService        |  dpa_impl_service_id                   |M2O
DataProtectionAdvisorOperationalAssurance  |  dpaOperationalAssuranceService  |  dpa_operational_assurance_service_id  |O2O
DataProtectionAdvisorCustomization         |  dpaCustomizationService         |  dpa_customization_service_id          |O2O
DataProtectionAdvisorUpgradeMigration      |  dpaUpgradeMigrationService      |  dpa_upgrade_migration_service_id      |O2O
DataProtectionAdvisorHealthCheck           |  dpaHealthCheckService           |  dpa_health_check_service_id
'''

INPUT_ORM_DATA3 = '''
----- com.emc.gs.tools.srf.model.dpad -----
===== DataProtectionAdvisor =====
'''

INPUT_ORM_DATA4 = '''
----- com.emc.gs.tools.srf.model -----
===== Customer =====
String                  |  contactName              |  contact_name                |  VARCHAR(255)
String                  |  formalName               |  formal_name                 |  VARCHAR(255)
String                  |  address1                 |  address1                    |  VARCHAR(255)
String                  |  address2                 |  address2                    |  VARCHAR(255)
String                  |  city                     |  city                        |  VARCHAR(255)
GeoState                |  geoState                 |  geo_state_id                |  O2O
String                  |  zip                      |  zip                         |  VARCHAR(255)
Country                 |  country                  |  country_id                  |  M2O
String                  |  title                    |  title                       |  VARCHAR(255)
Phone                   |  officePhone              |  office_phone_id             |  M2O
Phone                   |  mobilePhone              |  mobile_phone_id             |  M2O
Phone                   |  fax                      |  fax_id                      |  M2O
String                  |  email                    |  email                       |  VARCHAR(255)
ServicesAgreementType   |  servicesAgreementType    |  services_agreement_type_id  |  M2O
String                  |  servicesAgreementNumber  |  services_agreement_number   |  VARCHAR(255)
Date                    |  servicesAgreementDate    |  services_agreement_date     |  TIMESTAMP
String                  |  partnerInformation       |  partner_info                |  VARCHAR(255)
boolean                 |  template                 |  template                    |  BOOLEAN NOT NULL
List<CustomerWorkSite>  |  customerWorkSites        |  Customer_CustomerWorkSite   |  O2M
'''



def generateORMEntity(input_values):
    TEMPLATE_ORM_ENTITY = '''
    <entity name="%(class)s" class="%(package)s.%(class)s">
        <table name="%(class)s"/>
        <sequence-generator name="idgen" sequence-name="S%(class)s" allocation-size="1"/>
        <attributes>%(content)s
        </attributes>
    </entity>
    '''

    TEMPLATE_ORM_ENTITY_NO_CONTENT = '''
    <entity name="%(class)s" class="%(package)s.%(class)s" cacheable="true">
        <table name="%(class)s"/>
    </entity>
    '''

    TEMPLATE_ORM_BASIC = '''
            <basic name="%(var_name)s">
                <column name="%(table_column)s" nullable="%(nullable)s" />
            </basic>
    '''

    TEMPLATE_ORM_ONE_TO_ONE = '''
            <one-to-one name="%(var_name)s" fetch="LAZY">
                <join-column name="%(table_column)s" />
                <cascade>
                    <cascade-all/>
                </cascade>
            </one-to-one>
    '''

    TEMPLATE_ORM_MANY_TO_ONE = '''
            <many-to-one name="%(var_name)s" fetch="LAZY">
                <join-column name="%(table_column)s" />
            </many-to-one>
    '''

    TEMPLATE_ORM_ONE_TO_MANY = '''
            <one-to-many name="%(var_name)s" fetch="LAZY">
                <join-table name="%(related_table)s">
                    <join-column name="%(table_one_id)s" referenced-column-name="id" />
                    <inverse-join-column name="%(table_two_id)s" referenced-column-name="id" unique="true" />
                </join-table>
                <cascade>
                    <cascade-all/>
                </cascade>
            </one-to-many>
    '''

    TEMPLATE_EMBEDDED = '''
            <embedded name="%(var_name)s">%(content)s
            </embedded>
    '''

    TEMPLATE_EMBEDDED_BASIC = '''
                <attribute-override name="%(var_name)s">
                    <column name="%(table_column)s" nullable="%(nullable)s" />
                </attribute-override>
    '''

    TYPE_NOTNULL = ['int', 'long', 'double', 'boolean', 'char']
    TYPE_NULLABLE = ['Integer', 'Long', 'Boolean', 'String', 'Double', 'Date', 'BigDecimal']

    all_content = ''
    package = ''
    class_name = ''
    content = ''
    content_many_to_one = ''
    content_one_to_many = ''
    content_one_to_one = ''
    content_embedded = ''

    """
  <xsd:sequence>
      <xsd:element name="description" type="xsd:string" minOccurs="0"/>
      <xsd:choice>
        <xsd:element name="id" type="orm:id"
                     minOccurs="0" maxOccurs="unbounded"/>
        <xsd:element name="embedded-id" type="orm:embedded-id"
                     minOccurs="0"/>
      </xsd:choice>
      <xsd:element name="basic" type="orm:basic"
                   minOccurs="0" maxOccurs="unbounded"/>
      <xsd:element name="version" type="orm:version"
                   minOccurs="0" maxOccurs="unbounded"/>
      <xsd:element name="many-to-one" type="orm:many-to-one"
                   minOccurs="0" maxOccurs="unbounded"/>
      <xsd:element name="one-to-many" type="orm:one-to-many"
                   minOccurs="0" maxOccurs="unbounded"/>
      <xsd:element name="one-to-one" type="orm:one-to-one"
                   minOccurs="0" maxOccurs="unbounded"/>
      <xsd:element name="many-to-many" type="orm:many-to-many"
                   minOccurs="0" maxOccurs="unbounded"/>
      <xsd:element name="element-collection" type="orm:element-collection"
                   minOccurs="0" maxOccurs="unbounded"/>
      <xsd:element name="embedded" type="orm:embedded"
                   minOccurs="0" maxOccurs="unbounded"/>
      <xsd:element name="transient" type="orm:transient"
                   minOccurs="0" maxOccurs="unbounded"/>
    </xsd:sequence>
  </xsd:complexType>
    """
    
    for line in input_values.splitlines():
        if len(line.strip()) == 0:
            continue
        if line.startswith('-----'):
            # if we meet ----- again, we need add current content to all
            if package != '':
                content += content_many_to_one
                content += content_one_to_many
                content += content_one_to_one
                if content_embedded:
                    content += TEMPLATE_EMBEDDED.rstrip() % {'var_name':'XXX', 'content':content_embedded}

                template_orm_data = {'package':package, 'class':class_name, 'content':content}
                if content == '':
                    all_content += TEMPLATE_ORM_ENTITY_NO_CONTENT % template_orm_data
                else:
                    all_content += TEMPLATE_ORM_ENTITY % template_orm_data
                    
                # clear all virables
                package = ''
                class_name = ''
                content = ''
                content_many_to_one = ''
                content_one_to_many = ''
                content_one_to_one = ''
                content_embedded = ''
                
            package = line[6:-6]
            continue
        if line.startswith('====='):
            class_name = line[6:-6]
            continue

        values = line.split('|')
        # remove useless white space
        for i in range(len(values)):
            values[i] = values[i].strip()

        type_nullable = 'true'
        if values[0] in TYPE_NOTNULL:
            type_nullable = 'false'


        template_data = {'var_name':values[1], 'table_column':values[2], 'nullable':type_nullable}
        basic_content = ''
        if 'ManyToOne' == values[3]:
            content_many_to_one += TEMPLATE_ORM_MANY_TO_ONE.rstrip() % template_data
        elif 'OneToOne' == values[3]:
            content_one_to_one += TEMPLATE_ORM_ONE_TO_ONE.rstrip() % template_data
        elif 'OneToMany' == values[3]:
            class_names = values[2].split('_')
            classOneId = frog_util.uncamel_name(class_names[0], split_char='_') + '_id'
            classTwoId = frog_util.uncamel_name(class_names[1], split_char='_') + '_id'
            template_data = {'var_name':values[1], 'related_table':values[2], 'table_one_id':classOneId, 'table_two_id':classTwoId}
            content_one_to_many += TEMPLATE_ORM_ONE_TO_MANY.rstrip() % template_data
        elif 'Embedded' == values[3]:
            content_embedded += TEMPLATE_EMBEDDED_BASIC.rstrip() % template_data
        elif values[0] in TYPE_NOTNULL or values[0] in TYPE_NULLABLE:
            basic_content = TEMPLATE_ORM_BASIC.rstrip() % template_data
        else:
            basic_content = TEMPLATE_ORM_MANY_TO_ONE.rstrip() % template_data
        content += basic_content

    # at last, add last content to all
    content += content_many_to_one
    content += content_one_to_many
    content += content_one_to_one
    if content_embedded:
        content += TEMPLATE_EMBEDDED.rstrip() % {'var_name':'XXX', 'content':content_embedded}

    template_orm_data = {'package':package, 'class':class_name, 'content':content}
    if content == '':
        all_content += TEMPLATE_ORM_ENTITY_NO_CONTENT % template_orm_data
    else:
        all_content += TEMPLATE_ORM_ENTITY % template_orm_data
        
    return all_content

