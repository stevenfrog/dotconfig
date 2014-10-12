CREATE TABLE NetworkerServer (
    id BIGINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    impl_env_new BOOLEAN,
    impl_env_existing BOOLEAN,
    networker_srvs INT,
    networker_mgmt_consoles INT
);

CREATE TABLE NetworkerStorageNodes (
    id BIGINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    storage_node_selected BOOLEAN,
    dedicated_storage_node_selected BOOLEAN,
    de_duplication_node_selected BOOLEAN,
    storage_nodes INT,
    dedicated_storage_nodes INT,
    de_duplication_nodes INT
);

CREATE TABLE NetworkerMediaDevices (
    id BIGINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    auto_changer_selected BOOLEAN,
    dd_boost_selected BOOLEAN,
    tape_device_selected BOOLEAN,
    atmos_selected BOOLEAN,
    advanced_file_type_device_selected BOOLEAN,
    auto_changers INT,
    tape_devices INT,
    advanced_file_type_devices INT,
    dd_boost_devices INT,
    atmos_devices INT
);

CREATE TABLE NetworkerAdvancedBackupTechnology (
    id BIGINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    snmp_selected BOOLEAN,
    vmware_selected BOOLEAN,
    snapshot_mgmt_selected BOOLEAN,
    nas_selected BOOLEAN,
    snmp_modules INT,
    vmware_protection_bu_selected BOOLEAN,
    virtual_machine_clients INT,
    vmware_v_sphere_hosts INT,
    vmware_bu_apps INT,
    vmware_protection_app INT,
    snapshot_mgmt_app_hosts INT,
    snapshot_mgmt_mount_hosts INT,
    nas INT,
    emc_disk_arrays INT
);

CREATE TABLE NetworkerFileSystemClientBackups (
    id BIGINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    firewall_support_selected BOOLEAN,
    clients INT,
    cluster_client_conns INT
);

CREATE TABLE NetworkerApplicationBackups (
    id BIGINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    ms_sql_selected BOOLEAN,
    ms_exchange_selected BOOLEAN,
    ms_sharepoint_selected BOOLEAN,
    ms_hyper_v_selected BOOLEAN,
    oracle_selected BOOLEAN,
    mysql_selected BOOLEAN,
    lotus_notes_selected BOOLEAN,
    sap_selected BOOLEAN,
    emc_vss_hardware_provider_selected1 BOOLEAN,
    module_for_ms_proxy_nodes1 INT,
    ms_sql_srv_cluster_selected1 BOOLEAN,
    ms_sql_srv_cluster_nodes1 INT,
    ms_sql_srvs1 INT,
    sql_databases1 INT,
    emc_vss_hardware_provider_selected2 BOOLEAN,
    module_for_ms_proxy_nodes2 INT,
    exchange_granular_bu_selected BOOLEAN,
    clustered_exchange_srvs_selected BOOLEAN,
    ms_exchange_mailbox_srvs INT,
    ms_exchange_database_stores INT,
    exchange_database_stores_selected BOOLEAN,
    exchange_cluster_nodes_included INT,
    ccr_clusters_included INT,
    emc_vss_hardware_provider_selected3 BOOLEAN,
    module_for_ms_proxy_nodes3 INT,
    data_domain_boost_selected1 BOOLEAN,
    ms_sql_srv_cluster_selected2 BOOLEAN,
    granular_sharepoint_bu_selected BOOLEAN,
    sharepoint_distributed_env_selected BOOLEAN,
    ms_sql_srv_cluster_nodes2 INT,
    ms_sql_srvs2 INT,
    physical_srvs_in_sharepoint_env INT,
    sql_databases2 INT,
    sharepoint_farms INT,
    sharepoint_web_apps INT,
    sharepoint_sites INT,
    sharepoint_sub_sites INT,
    emc_vss_hardware_provider_selected4 BOOLEAN,
    module_for_ms_proxy_nodes4 INT,
    data_domain_boost_selected2 BOOLEAN,
    hyper_v_envs_clustered_selected BOOLEAN,
    bu_individual_hyper_v_machines_selected BOOLEAN,
    ms_hyper_v_srvs INT,
    physical_srvs_in_hyper_v_cluster INT,
    hyper_vvm_bu_individually INT,
    clustered_oracle_srvs_selected BOOLEAN,
    physical_srvs_in_oracle_env INT,
    extensive_rman_scripting_selected BOOLEAN,
    oracle_database_srvs_for_bu INT,
    oracle_databases_for_bu_conf INT,
    mysql_env_clustered_selected BOOLEAN,
    physical_srvs_in_my_sql_cluster INT,
    mysql_srvs INT,
    lotus_notes_apps_clustered_selected BOOLEAN,
    physical_lotus_notes_srvs INT,
    ibm_lotus_domino_instances INT,
    sap_env_clustered_selected BOOLEAN,
    physical_srvs_in_the_sap_env INT,
    sap_app_srvs INT
);

CREATE TABLE NetworkerDesign (
    id BIGINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    srv_id BIGINT,
    advanced_bu_tech_id BIGINT,
    storage_nodes_id BIGINT,
    fs_client_bu_id BIGINT,
    media_devices_id BIGINT,
    app_bu_id BIGINT,
    FOREIGN KEY (srv_id) REFERENCES NetworkerServer(id),
    FOREIGN KEY (advanced_bu_tech_id) REFERENCES NetworkerAdvancedBackupTechnology(id),
    FOREIGN KEY (storage_nodes_id) REFERENCES NetworkerStorageNodes(id),
    FOREIGN KEY (fs_client_bu_id) REFERENCES NetworkerFileSystemClientBackups(id),
    FOREIGN KEY (media_devices_id) REFERENCES NetworkerMediaDevices(id),
    FOREIGN KEY (app_bu_id) REFERENCES NetworkerApplicationBackups(id)
);

CREATE TABLE NetworkerImpl (
    id BIGINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    srv_id BIGINT,
    advanced_bu_tech_id BIGINT,
    storage_nodes_id BIGINT,
    fs_client_bu_id BIGINT,
    media_devices_id BIGINT,
    app_bu_id BIGINT,
    FOREIGN KEY (srv_id) REFERENCES NetworkerServer(id),
    FOREIGN KEY (advanced_bu_tech_id) REFERENCES NetworkerAdvancedBackupTechnology(id),
    FOREIGN KEY (storage_nodes_id) REFERENCES NetworkerStorageNodes(id),
    FOREIGN KEY (fs_client_bu_id) REFERENCES NetworkerFileSystemClientBackups(id),
    FOREIGN KEY (media_devices_id) REFERENCES NetworkerMediaDevices(id),
    FOREIGN KEY (app_bu_id) REFERENCES NetworkerApplicationBackups(id)
);


CREATE TABLE NetworkerUpgradeServer (
    id BIGINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    current_networker76_selected BOOLEAN,
    current_networker80_selected BOOLEAN,
    upgrade_networker80_selected BOOLEAN,
    upgrade_networker81_selected BOOLEAN,
    upgraded_to_new_hardware_selected BOOLEAN,
    networker_srvs_to_be_upgraded INT
);

CREATE TABLE NetworkerUpgrade (
    id BIGINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    networker_srv_selected BOOLEAN,
    networker_storage_nodes_selected BOOLEAN,
    networker_clients_selected BOOLEAN,
    networker_mgmt_console_selected BOOLEAN,
    srv_id BIGINT,
    networker_storage_nodes INT,
    networker_clients INT,
    networker_mgmt_consoles INT,
    FOREIGN KEY (srv_id) REFERENCES NetworkerUpgradeServer(id)
);

CREATE TABLE Networker (
    id BIGINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    hours_of_knowledge_transfer DECIMAL(20,2),
    services BOOLEAN NOT NULL,
    impl BOOLEAN NOT NULL,
    upgrade_planning BOOLEAN NOT NULL,
    healthcheck BOOLEAN NOT NULL,
    upgrade BOOLEAN NOT NULL,
    activity_type_design BOOLEAN NOT NULL,
    activity_type_impl BOOLEAN NOT NULL,
    design_service_id BIGINT,
    impl_service_id BIGINT,
    upgrade_service_id BIGINT,
    FOREIGN KEY (design_service_id) REFERENCES NetworkerDesign(id),
    FOREIGN KEY (impl_service_id) REFERENCES NetworkerImpl(id),
    FOREIGN KEY (upgrade_service_id) REFERENCES NetworkerUpgrade(id)
);


CREATE TABLE DPADRequestData (
    id bigint auto_increment NOT NULL PRIMARY KEY,
    sites_involved VARCHAR(256),
    general_comments VARCHAR(256),
    services_scope_id bigint,
    avamar_id bigint,
    edl_id bigint,
    recover_point_id bigint,
    vplex_id bigint,
    data_domain_id bigint,
    dpa_id bigint,
    networker_id bigint,
    FOREIGN KEY (services_scope_id) REFERENCES DPADServicesScope (id),
    FOREIGN KEY (vplex_id) REFERENCES Vplex (id),
    FOREIGN KEY (recover_point_id) REFERENCES RecoverPoint (id),
    FOREIGN KEY (edl_id) REFERENCES EDL (id),
    FOREIGN KEY (avamar_id) REFERENCES Avamar (id),
    FOREIGN KEY (data_domain_id) REFERENCES DataDomain (id),
    FOREIGN KEY (dpa_id) REFERENCES DPA (id),
    FOREIGN KEY (networker_id) REFERENCES Networker (id)
);
