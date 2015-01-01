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
----- com.emc.gs.tools.srf.model.vipr -----
===== ViprFeature =====
Boolean  |  dsForObject        |  ds_for_object         |  BOOLEAN
Boolean  |  dsForHDFS          |  ds_for_hdfs           |  BOOLEAN
Boolean  |  activeDirectory    |  active_directory      |  BOOLEAN
Boolean  |  kerberosForViPRFS  |  kerberos_for_vi_prfs  |  BOOLEAN
Boolean  |  casAPISupport      |  cas_api_support       |  BOOLEAN
Boolean  |  watch4net          |  watch4net             |  BOOLEAN
Boolean  |  blockServices      |  block_services        |  BOOLEAN
Boolean  |  thirdPartySystem   |  third_party_system    |  BOOLEAN
Boolean  |  vCOps              |  vcops                 |  BOOLEAN
Boolean  |  vCO                |  vco                   |  BOOLEAN
Boolean  |  vCAC               |  vcac                  |  BOOLEAN
Boolean  |  microsoftSCVMM     |  microsoft_scvmm       |  BOOLEAN

----- com.emc.gs.tools.srf.model.vipr -----
===== ViprScopeDetails =====
Integer  |  hadoopClusters            |  hadoop_clusters             |  INT
Integer  |  hadoopClusterNodes        |  hadoop_cluster_nodes        |  INT
Integer  |  viprCtrllerInstances      |  vipr_ctrller_instances      |  INT
Integer  |  tenantsDefined            |  tenants_defined             |  INT
Integer  |  physicalUnixHosts         |  physical_unix_hosts         |  INT
Integer  |  physicalWinsHosts         |  physical_wins_hosts         |  INT
Integer  |  vmwareVCenterHosts        |  vmware_v_center_hosts       |  INT
Integer  |  fileOnlyArrays            |  file_only_arrays            |  INT
Integer  |  emcBlockArrays            |  emc_block_arrays            |  INT
Integer  |  emcVPLEXArrays            |  emc_vplex_arrays            |  INT
Integer  |  emcRecoverPtSystems       |  emc_recover_pt_systems      |  INT
Integer  |  ciscoSwitchFabrics        |  cisco_switch_fabrics        |  INT
Integer  |  brocadeSwitchFabrics      |  brocade_switch_fabrics      |  INT
Integer  |  openStackCinder           |  open_stack_cinder           |  INT
Integer  |  scaleioProtectionDomains  |  scaleio_protection_domains  |  INT

----- com.emc.gs.tools.srf.model.vipr -----
===== ViprPhysicalAndVirtualAssetConf =====
Integer  |  virtualArrays                |  virtual_arrays                 |  INT
Integer  |  blockAndFileVirtualPools     |  block_and_file_virtual_pools   |  INT
Integer  |  catalogServices              |  catalog_services               |  INT
Integer  |  userRolesDefined             |  user_roles_defined             |  INT
Integer  |  projects                     |  projects                       |  INT
Integer  |  dataServicesBuckets          |  data_services_buckets          |  INT
Integer  |  objectVirtualPools           |  object_virtual_pools           |  INT
Integer  |  dataStores                   |  data_stores                    |  INT
Integer  |  dsFileIngestionsPerformed    |  ds_file_ingestions_performed   |  INT
Integer  |  additionalKnowledgeTransfer  |  additional_knowledge_transfer  |  INT
Integer  |  testingFacilitated           |  testing_facilitated            |  INT

----- com.emc.gs.tools.srf.model.vipr -----
===== ViprPlanningDesignImpl =====
Boolean                          |  newImplType   |  new_impl_type     |  BOOLEAN
ViprFeature                      |  feature       |  feature_id        |  OneToOne
ViprScopeDetails                 |  scopeDetails  |  scope_details_id  |  OneToOne
ViprPhysicalAndVirtualAssetConf  |  assetConf     |  asset_conf_id     |  OneToOne

----- com.emc.gs.tools.srf.model.vipr -----
===== ViprPlaningAndDesign =====
Integer  |  srcAndTargetSites          |  src_and_target_sites          |  INT
Integer  |  newPhysicalHosts           |  new_physical_hosts            |  INT
Integer  |  newESXSrvs                 |  new_esx_srvs                  |  INT
Integer  |  newEnterpriseDirectors     |  new_enterprise_directors      |  INT
Integer  |  newDepartmentalSwitches    |  new_departmental_switches     |  INT
Integer  |  newVNXBlockStorageArrays   |  new_vnx_block_storage_arrays  |  INT
Integer  |  complexityFactor           |  complexity_factor             |  INT
Integer  |  newSymmetrixStorageArrays  |  new_symmetrix_storage_arrays  |  INT
Integer  |  vnxBlockArrays             |  vnx_block_arrays              |  INT
Integer  |  symmetrix                  |  symmetrix                     |  INT
Integer  |  xtremioClusters            |  xtremio_clusters              |  INT
Integer  |  nonEMCStorageArrays        |  non_emc_storage_arrays        |  INT

----- com.emc.gs.tools.srf.model.vipr -----
===== ViprImplAndMigration =====
Boolean  |  removeEMCStorageChk            |  remove_emc_storage_chk             |  BOOLEAN
Boolean  |  relocateEMCStorageChk          |  relocate_emc_storage_chk           |  BOOLEAN
Boolean  |  dataErasure                    |  data_erasure                       |  BOOLEAN
Boolean  |  bINFileWork                    |  b_in_file_work                     |  BOOLEAN
Integer  |  binFiles                       |  bin_files                          |  INT
Integer  |  hoursPerBINFile                |  hours_per_bin_file                 |  INT
Boolean  |  clustersConfs                  |  clusters_confs                     |  BOOLEAN
Integer  |  amountOfSrcData                |  amount_of_src_data                 |  INT
Integer  |  complexityFactor               |  complexity_factor                  |  INT
Integer  |  hostsMigrated                  |  hosts_migrated                     |  INT
Integer  |  newPhysicalHosts               |  new_physical_hosts                 |  INT
Integer  |  newESXSrvs                     |  new_esx_srvs                       |  INT
Boolean  |  doTheZoningWork                |  do_the_zoning_work                 |  BOOLEAN
Integer  |  existingSANFabrics             |  existing_san_fabrics               |  INT
Integer  |  hostsBooted                    |  hosts_booted                       |  INT
Boolean  |  doLUNWork                      |  do_lun_work                        |  BOOLEAN
Integer  |  newVNXBlock                    |  new_vnx_block                      |  INT
Integer  |  vnxBlockArrays                 |  vnx_block_arrays                   |  INT
Integer  |  xtremioClusters                |  xtremio_clusters                   |  INT
Integer  |  bricksPerCluster               |  bricks_per_cluster                 |  INT
Integer  |  powerPathMigrationEnabler      |  power_path_migration_enabler       |  INT
Boolean  |  deviceSizeChanges              |  device_size_changes                |  BOOLEAN
Integer  |  srvsRequiringLUNSizeChanges    |  srvs_requiring_lun_size_changes    |  INT
Integer  |  vnxArraysDataErased            |  vnx_arrays_data_erased             |  INT
Integer  |  enterTheSerialNumberVNX        |  enter_the_serial_number_vnx        |  INT
Integer  |  symmetrixStorageDataErased     |  symmetrix_storage_data_erased      |  INT
Integer  |  enterTheSerialNumberSymmetrix  |  enter_the_serial_number_symmetrix  |  INT

----- com.emc.gs.tools.srf.model.vipr -----
===== ViprDataMigrationPPME =====
Boolean               |  planningAndDesignChk          |  planning_and_design_chk             |  BOOLEAN
Boolean               |  implAndMigrationChk           |  impl_and_migration_chk              |  BOOLEAN
Boolean               |  doMigrationWorkThemselves     |  do_migration_work_themselves        |  BOOLEAN
Boolean               |  onsiteSupport                 |  onsite_support                      |  BOOLEAN
MigrationToolType     |  migrationTool                 |  migration_tool_id                   |  ManyToOne
Boolean               |  esxHostMigration              |  esx_host_migration                  |  BOOLEAN
Boolean               |  secondRoundOfDataGathering    |  second_round_of_data_gathering      |  BOOLEAN
Boolean               |  eca                           |  eca                                 |  BOOLEAN
Boolean               |  vnxOrCLARiiONChk              |  vnx_or_cla_rii_on_chk               |  BOOLEAN
Boolean               |  vmaxDMXOrSYMMChk              |  vmax_dmx_or_symm_chk                |  BOOLEAN
Boolean               |  thirdPartyOrNonEMCStorageChk  |  third_party_or_non_emc_storage_chk  |  BOOLEAN
Boolean               |  noSrcArrayChk                 |  no_src_array_chk                    |  BOOLEAN
Boolean               |  xtremioClusterChk             |  xtremio_cluster_chk                 |  BOOLEAN
Integer               |  existingPhysicalHosts         |  existing_physical_hosts             |  INT
Integer               |  existingESXSrvs               |  existing_esx_srvs                   |  INT
Boolean               |  swingFrame                    |  swing_frame                         |  BOOLEAN
Integer               |  srcArrays                     |  src_arrays                          |  INT
Integer               |  targetArrays                  |  target_arrays                       |  INT
Boolean               |  deviceSizeChanges             |  device_size_changes                 |  BOOLEAN
Integer               |  lunSizeChanges                |  lun_size_changes                    |  INT
Integer               |  amountOfSrcData               |  amount_of_src_data                  |  INT
Integer               |  powerPathMigrationEnabler     |  power_path_migration_enabler        |  INT
Integer               |  vmwareVirtualMachines         |  vmware_virtual_machines             |  INT
ViprPlaningAndDesign  |  planingAndDesign              |  planing_and_design_id               |  OneToOne
ViprImplAndMigration  |  implAndMigration              |  impl_and_migration_id               |  OneToOne

----- com.emc.gs.tools.srf.model.vipr -----
===== ViprDSCommodityFeatures =====
Boolean  |  dsForHDFS        |  ds_for_hdfs       |  BOOLEAN
Boolean  |  activeDirectory  |  active_directory  |  BOOLEAN
Boolean  |  viPRFS           |  vi_prfs           |  BOOLEAN
Boolean  |  cas              |  cas               |  BOOLEAN
Boolean  |  watch4net        |  watch4net         |  BOOLEAN

----- com.emc.gs.tools.srf.model.vipr -----
===== ViprDSCommodityScopeDetails =====
Integer  |  commodity          |  commodity            |  INT
Integer  |  tenantsDefined     |  tenants_defined      |  INT
Integer  |  clusters           |  clusters             |  INT
Integer  |  totalClusterNodes  |  total_cluster_nodes  |  INT

----- com.emc.gs.tools.srf.model.vipr -----
===== ViprCommoditySysConf =====
Integer  |  virtualArrays       |  virtual_arrays        |  INT
Integer  |  objectVirtualPools  |  object_virtual_pools  |  INT
Integer  |  projects            |  projects              |  INT
Integer  |  userRolesDefined    |  user_roles_defined    |  INT
Integer  |  catalogServices     |  catalog_services      |  INT
Integer  |  viprCommodity       |  vipr_commodity        |  INT

----- com.emc.gs.tools.srf.model.vipr -----
===== ViprDSCommodityServices =====
ViprDSCommodityFeatures      |  features      |  features_id       |  OneToOne
ViprDSCommodityScopeDetails  |  scopeDetails  |  scope_details_id  |  OneToOne
ViprCommoditySysConf         |  sysConf       |  sys_conf_id       |  OneToOne

----- com.emc.gs.tools.srf.model.vipr -----
===== ViprECSFeature =====
Boolean  |  dsForHDFS        |  ds_for_hdfs       |  BOOLEAN
Boolean  |  activeDirectory  |  active_directory  |  BOOLEAN
Boolean  |  viPRFS           |  vi_prfs           |  BOOLEAN
Boolean  |  cas              |  cas               |  BOOLEAN
Boolean  |  watch4net        |  watch4net         |  BOOLEAN

----- com.emc.gs.tools.srf.model.vipr -----
===== ViprECSScopeDetails =====
Integer  |  containingBlock      |  containing_block      |  INT
Integer  |  unstructuredSystems  |  unstructured_systems  |  INT
Integer  |  tenantsDefined       |  tenants_defined       |  INT
Integer  |  clusters             |  clusters              |  INT
Integer  |  totalClusterNodes    |  total_cluster_nodes   |  INT

----- com.emc.gs.tools.srf.model.vipr -----
===== ViprECSConf =====
Integer  |  virtualArrays        |  virtual_arrays         |  INT
Integer  |  blockVirtualPools    |  block_virtual_pools    |  INT
Integer  |  objectVirtualPools   |  object_virtual_pools   |  INT
Integer  |  projects             |  projects               |  INT
Integer  |  dataServicesBuckets  |  data_services_buckets  |  INT
Integer  |  userRolesDefined     |  user_roles_defined     |  INT
Integer  |  catalogServices      |  catalog_services       |  INT
Integer  |  viprCommodity        |  vipr_commodity         |  INT

----- com.emc.gs.tools.srf.model.vipr -----
===== ViprECSServices =====
ViprECSFeature       |  features      |  features_id       |  OneToOne
ViprECSScopeDetails  |  scopeDetails  |  scope_details_id  |  OneToOne
ViprECSConf          |  sysConf       |  sys_conf_id       |  OneToOne

----- com.emc.gs.tools.srf.model.vipr -----
===== ViprRequestData =====
BigDecimal               |  knowledgeTransferHours  |  knowledge_transfer_hours  |  DECIMAL(20,2)
String                   |  generalComment          |  general_comment           |  VARCHAR(255)
boolean                  |  planningDesignImplChk   |  planning_design_impl_chk  |  BOOLEAN NOT NULL
boolean                  |  dataMigrationPPMEChk    |  data_migration_ppme_chk   |  BOOLEAN NOT NULL
boolean                  |  dsCommodityChk          |  ds_commodity_chk          |  BOOLEAN NOT NULL
boolean                  |  ecsApplianceChk         |  ecs_app_chk               |  BOOLEAN NOT NULL
ViprPlanningDesignImpl   |  planningDesignImpl      |  planning_design_impl_id   |  OneToOne
ViprDataMigrationPPME    |  dataMigrationPPME       |  data_migration_ppme_id    |  OneToOne
ViprDSCommodityServices  |  dsCommodity             |  ds_commodity_id           |  OneToOne
ViprECSServices          |  ecsAppliance            |  ecs_app_id                |  OneToOne
'''


ttte

print()
print(frog_sql_util.generateORMEntity(INPUT_ORM_DATA))
