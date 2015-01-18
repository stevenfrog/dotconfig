#!/usr/bin/env python3

import frog_sql_util

INPUT_ORM_DATA_EXAMPLE1 = '''
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

INPUT_ORM_DATA_EXAMPLE2 = '''
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

INPUT_ORM_DATA_EXAMPLE3 = '''
----- com.emc.gs.tools.srf.model.dpad -----
===== DataProtectionAdvisor =====
'''

INPUT_ORM_DATA_EXAMPLE4 = '''
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

INPUT_ORM_DATA_EXAMPLE5 = '''
----- com.emc.gs.tools.srf.model.dpad -----
===== NetworkerDesign =====
boolean                            |  serverSelected          |  srv_selected               |  BOOLEAN NOT NULL
boolean                            |  advancedBuTechSelected  |  advanced_bu_tech_selected  |  BOOLEAN NOT NULL
boolean                            |  storageNodesSelected    |  storage_nodes_selected     |  BOOLEAN NOT NULL
boolean                            |  fsClientBuSelected      |  fs_client_bu_selected      |  BOOLEAN NOT NULL
boolean                            |  mediaDevicesSelected    |  media_devices_selected     |  BOOLEAN NOT NULL
boolean                            |  appBuSelected           |  app_bu_selected            |  BOOLEAN NOT NULL
NetworkerServer                    |  server                  |  srv_id                     |  ManyToOne
NetworkerAdvancedBackupTechnology  |  advancedBuTech          |  advanced_bu_tech_id        |  ManyToOne
NetworkerStorageNodes              |  storageNodes            |  storage_nodes_id           |  ManyToOne
NetworkerFileSystemClientBackups   |  fsClientBu              |  fs_client_bu_id            |  ManyToOne
NetworkerMediaDevices              |  mediaDevices            |  media_devices_id           |  ManyToOne
NetworkerApplicationBackups        |  appBu                   |  app_bu_id                  |  ManyToOne
'''


INPUT_ORM_DATA = '''
----- com.emc.gs.tools.srf.model.coreunified -----
===== UnifiedFeatureBlock =====
UnifiedServiceBundles  |  serviceBundles  |  service_bundles_id  |  OneToOne  

----- com.emc.gs.tools.srf.model.coreunified -----
===== UnifiedConversion =====
boolean  |  fileUnifiedChk   |  file_unified_chk    |  BOOLEAN NOT NULL  
boolean  |  blockUnifiedChk  |  block_unified_chk   |  BOOLEAN NOT NULL  
boolean  |  dpeSpeChk        |  dpe_spe_chk         |  BOOLEAN NOT NULL  
boolean  |  spChk            |  sp_chk              |  BOOLEAN NOT NULL  
Integer  |  numFileUnified   |  num_file_unified    |  INT               
Integer  |  numBlockUnified  |  num_block_unified   |  INT               
boolean  |  dpeSpeRerackChk  |  dpe_spe_rerack_chk  |  BOOLEAN NOT NULL  
Integer  |  numDpeSpe        |  num_dpe_spe         |  INT               
boolean  |  spRerackChk      |  sp_rerack_chk       |  BOOLEAN NOT NULL  
Integer  |  numSp            |  num_sp              |  INT              

----- com.emc.gs.tools.srf.model.coreunified -----
===== UnifiedUpgrade =====
boolean  |  controlStationChk  |  ctrl_station_chk  |  BOOLEAN NOT NULL  
Integer  |  numControlStation  |  num_ctrl_station  |  INT               
boolean  |  dataMoverChk       |  data_mover_chk    |  BOOLEAN NOT NULL  
Integer  |  numFileBlock       |  num_file_block    |  INT               
Integer  |  numDataMover       |  num_data_mover    |  INT               
boolean  |  spUpgradeChk       |  sp_upgrade_chk    |  BOOLEAN NOT NULL  
Integer  |  numSpUpgrade       |  num_sp_upgrade    |  INT              

----- com.emc.gs.tools.srf.model.coreunified -----
===== UnifiedUpgradeConversion =====
boolean            |  conversionsChk  |  conversions_chk  |  BOOLEAN NOT NULL  
boolean            |  upgradesChk     |  upgrades_chk     |  BOOLEAN NOT NULL  
UnifiedConversion  |  conversion      |  conversion_id    |  OneToOne          
UnifiedUpgrade     |  upgrade         |  upgrade_id       |  OneToOne  

----- com.emc.gs.tools.srf.model.coreunified -----
===== UnifiedESI =====
Integer  |  numLvmInstance  |  num_lvm_instance  |  INT  
Integer  |  numSapSystem    |  num_sap_system    |  INT  
Integer  |  numLvmHosts     |  num_lvm_hosts     |  INT  
Integer  |  numEmcStorage   |  num_emc_storage   |  INT  
'''



print()
print(frog_sql_util.generateORMEntity(INPUT_ORM_DATA))
