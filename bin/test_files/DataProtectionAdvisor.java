/*
 * This code is copyright (c) 2014 EMC Corporation
 */
package com.emc.gs.tools.srf.model.dpad;

import java.math.BigDecimal;

import com.emc.gs.tools.srf.model.IdentifiableEntity;

/**
 * <p>
 * This is DataProtectionAdvisor entity class.
 * </p>
 * <p>
 * <strong>Thread safety</strong>: This class is mutable, it is not thread safety.
 * </p>
 *
 * @author TCSASSEMBLER
 * @version 1.0
 * @since SRT Phase 3-5 - BRS Tabs Part 2 Assembly
 */
public class DataProtectionAdvisor extends IdentifiableEntity {
    /**
     * # hours of knowledge transfer.
     */
    private BigDecimal knowledgeTransferHours;

    /**
     * Represents whether "Implement Data Protection Advisor" service is selected.
     */
    private String implService;

    /**
     * Represents whether "Operational Assurance for Data Protection Advisor" service is selected.
     */
    private int operationalAssuranceService;

    /**
     * Represents whether "Customization for Data Protection Advisor" service is selected.
     */
    private Integer customizationService;

    /**
     * Represents whether "Upgrade and Migration for Data Protection Advisor" service is selected.
     */
    private boolean upgradeMigrationService;

    /**
     * Represents whether "Health Check for Data Protection Advisor" service is selected.
     */
    private boolean healthCheckService;

    /**
     * Represents whether "Data Domain Activity Type Design" service is selected.
     */
    private boolean ddaDesign;

    /**
     * Represents whether "Data Domain Activity Type Implementation" service is selected.
     */
    private boolean ddaImplementation;

    /**
     * Represents whether "Enable and Configure Retention Locking Compliance License" deliver option is
     * selected.
     */
    private Boolean retentionLockingOption;

    /**
     * Design Service.
     */
    private DataProtectionAdvisorDesign dpaDesignService;

    /**
     * Implementation Service.
     */
    private DataProtectionAdvisorImplementation dpaImplementationService;

    /**
     * Operational Assurance Service.
     */
    private DataProtectionAdvisorOperationalAssurance dpaOperationalAssuranceService;

    /**
     * Customization Service.
     */
    private DataProtectionAdvisorCustomization dpaCustomizationService;

    /**
     * Upgrade and Migration Service.
     */
    private DataProtectionAdvisorUpgradeMigration dpaUpgradeMigrationService;

    /**
     * Health Check Service.
     */
    private DataProtectionAdvisorHealthCheck dpaHealthCheckService;

    /**
     * <p>
     * The default constructor.
     * </p>
     */
    public DataProtectionAdvisor() {
    }

    /**
     * Getter method for property <b>knowledgeTransferHours</b>.
     *
     * @return property value of knowledgeTransferHours
     */
    public BigDecimal getKnowledgeTransferHours() {
        return knowledgeTransferHours;
    }

    /**
     * Setter method for property <b>knowledgeTransferHours</b>.
     *
     * @param knowledgeTransferHours
     *            value to be assigned to property knowledgeTransferHours
     */
    public void setKnowledgeTransferHours(BigDecimal knowledgeTransferHours) {
        this.knowledgeTransferHours = knowledgeTransferHours;
    }

    /**
     * Getter method for property <b>implService</b>.
     *
     * @return property value of implService
     */
    public boolean isImplService() {
        return implService;
    }

    /**
     * Setter method for property <b>implService</b>.
     *
     * @param implService
     *            value to be assigned to property implService
     */
    public void setImplService(boolean implService) {
        this.implService = implService;
    }

    /**
     * Getter method for property <b>operationalAssuranceService</b>.
     *
     * @return property value of operationalAssuranceService
     */
    public boolean isOperationalAssuranceService() {
        return operationalAssuranceService;
    }

    /**
     * Setter method for property <b>operationalAssuranceService</b>.
     *
     * @param operationalAssuranceService
     *            value to be assigned to property operationalAssuranceService
     */
    public void setOperationalAssuranceService(boolean operationalAssuranceService) {
        this.operationalAssuranceService = operationalAssuranceService;
    }

    /**
     * Getter method for property <b>customizationService</b>.
     *
     * @return property value of customizationService
     */
    public boolean isCustomizationService() {
        return customizationService;
    }

    /**
     * Setter method for property <b>customizationService</b>.
     *
     * @param customizationService
     *            value to be assigned to property customizationService
     */
    public void setCustomizationService(boolean customizationService) {
        this.customizationService = customizationService;
    }

    /**
     * Getter method for property <b>upgradeMigrationService</b>.
     *
     * @return property value of upgradeMigrationService
     */
    public boolean isUpgradeMigrationService() {
        return upgradeMigrationService;
    }

    /**
     * Setter method for property <b>upgradeMigrationService</b>.
     *
     * @param upgradeMigrationService
     *            value to be assigned to property upgradeMigrationService
     */
    public void setUpgradeMigrationService(boolean upgradeMigrationService) {
        this.upgradeMigrationService = upgradeMigrationService;
    }

    /**
     * Getter method for property <b>healthCheckService</b>.
     *
     * @return property value of healthCheckService
     */
    public boolean isHealthCheckService() {
        return healthCheckService;
    }

    /**
     * Setter method for property <b>healthCheckService</b>.
     *
     * @param healthCheckService
     *            value to be assigned to property healthCheckService
     */
    public void setHealthCheckService(boolean healthCheckService) {
        this.healthCheckService = healthCheckService;
    }

    /**
     * Getter method for property <b>ddaDesign</b>.
     *
     * @return property value of ddaDesign
     */
    public boolean isDdaDesign() {
        return ddaDesign;
    }

    /**
     * Setter method for property <b>ddaDesign</b>.
     *
     * @param ddaDesign
     *            value to be assigned to property ddaDesign
     */
    public void setDdaDesign(boolean ddaDesign) {
        this.ddaDesign = ddaDesign;
    }

    /**
     * Getter method for property <b>ddaImplementation</b>.
     *
     * @return property value of ddaImplementation
     */
    public boolean isDdaImplementation() {
        return ddaImplementation;
    }

    /**
     * Setter method for property <b>ddaImplementation</b>.
     *
     * @param ddaImplementation
     *            value to be assigned to property ddaImplementation
     */
    public void setDdaImplementation(boolean ddaImplementation) {
        this.ddaImplementation = ddaImplementation;
    }

    /**
     * Getter method for property <b>retentionLockingOption</b>.
     *
     * @return property value of retentionLockingOption
     */
    public Boolean getRetentionLockingOption() {
        return retentionLockingOption;
    }

    /**
     * Setter method for property <b>retentionLockingOption</b>.
     *
     * @param retentionLockingOption
     *            value to be assigned to property retentionLockingOption
     */
    public void setRetentionLockingOption(Boolean retentionLockingOption) {
        this.retentionLockingOption = retentionLockingOption;
    }

    /**
     * Getter method for property <b>dpaDesignService</b>.
     *
     * @return property value of dpaDesignService
     */
    public DataProtectionAdvisorDesign getDpaDesignService() {
        return dpaDesignService;
    }

    /**
     * Setter method for property <b>dpaDesignService</b>.
     *
     * @param dpaDesignService
     *            value to be assigned to property dpaDesignService
     */
    public void setDpaDesignService(DataProtectionAdvisorDesign dpaDesignService) {
        this.dpaDesignService = dpaDesignService;
    }

    /**
     * Getter method for property <b>dpaImplementationService</b>.
     *
     * @return property value of dpaImplementationService
     */
    public DataProtectionAdvisorImplementation getDpaImplementationService() {
        return dpaImplementationService;
    }

    /**
     * Setter method for property <b>dpaImplementationService</b>.
     *
     * @param dpaImplementationService
     *            value to be assigned to property dpaImplementationService
     */
    public void setDpaImplementationService(DataProtectionAdvisorImplementation dpaImplementationService) {
        this.dpaImplementationService = dpaImplementationService;
    }

    /**
     * Getter method for property <b>dpaOperationalAssuranceService</b>.
     *
     * @return property value of dpaOperationalAssuranceService
     */
    public DataProtectionAdvisorOperationalAssurance getDpaOperationalAssuranceService() {
        return dpaOperationalAssuranceService;
    }

    /**
     * Setter method for property <b>dpaOperationalAssuranceService</b>.
     *
     * @param dpaOperationalAssuranceService
     *            value to be assigned to property dpaOperationalAssuranceService
     */
    public void setDpaOperationalAssuranceService(
        DataProtectionAdvisorOperationalAssurance dpaOperationalAssuranceService) {
        this.dpaOperationalAssuranceService = dpaOperationalAssuranceService;
    }

    /**
     * Getter method for property <b>dpaCustomizationService</b>.
     *
     * @return property value of dpaCustomizationService
     */
    public DataProtectionAdvisorCustomization getDpaCustomizationService() {
        return dpaCustomizationService;
    }

    /**
     * Setter method for property <b>dpaCustomizationService</b>.
     *
     * @param dpaCustomizationService
     *            value to be assigned to property dpaCustomizationService
     */
    public void setDpaCustomizationService(DataProtectionAdvisorCustomization dpaCustomizationService) {
        this.dpaCustomizationService = dpaCustomizationService;
    }

    /**
     * Getter method for property <b>dpaUpgradeMigrationService</b>.
     *
     * @return property value of dpaUpgradeMigrationService
     */
    public DataProtectionAdvisorUpgradeMigration getDpaUpgradeMigrationService() {
        return dpaUpgradeMigrationService;
    }

    /**
     * Setter method for property <b>dpaUpgradeMigrationService</b>.
     *
     * @param dpaUpgradeMigrationService
     *            value to be assigned to property dpaUpgradeMigrationService
     */
    public void setDpaUpgradeMigrationService(DataProtectionAdvisorUpgradeMigration dpaUpgradeMigrationService) {
        this.dpaUpgradeMigrationService = dpaUpgradeMigrationService;
    }

    /**
     * Getter method for property <b>dpaHealthCheckService</b>.
     *
     * @return property value of dpaHealthCheckService
     */
    public DataProtectionAdvisorHealthCheck getDpaHealthCheckService() {
        return dpaHealthCheckService;
    }

    /**
     * Setter method for property <b>dpaHealthCheckService</b>.
     *
     * @param dpaHealthCheckService
     *            value to be assigned to property dpaHealthCheckService
     */
    public void setDpaHealthCheckService(DataProtectionAdvisorHealthCheck dpaHealthCheckService) {
        this.dpaHealthCheckService = dpaHealthCheckService;
    }

}
