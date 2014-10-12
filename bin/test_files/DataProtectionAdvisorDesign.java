/*
 * This code is copyright (c) 2014 EMC Corporation
 */
package com.emc.gs.tools.srf.model.dpad;

import com.emc.gs.tools.srf.model.IdentifiableEntity;

/**
 * <p>
 * This is DataProtectionAdvisorDesign entity class.
 * </p>
 * <p>
 * <strong>Thread safety</strong>: This class is mutable, it is not thread safety.
 * </p>
 *
 * @author TCSASSEMBLER
 * @version 1.0
 * @since SRT Phase 3-5 - BRS Tabs Part 2 Assembly
 */
public class DataProtectionAdvisorDesign extends IdentifiableEntity {
    /**
     * Install Data Protection Advisor on Extended Database (Oracle, MS SQL, etc.).
     */
    private Boolean includeDPAExtDB;

    /**
     * Include Data Protection Advisor Analysis Jobs.
     */
    private Boolean includeDPAAnalysisJobs;

    /**
     * Include Data Protection Advisor Recoverability Analysis.
     */
    private Boolean includeDPARecoverabilityAnalysis;

    /**
     * Include Data Protection Advisor Custom Report Development.
     */
    private Boolean includeDPACustomReportDev;

    /**
     * Include Data Protection Advisor Interface Customization.
     */
    private Boolean includeDPAInterfaceCustomization;

    /**
     * Include Data Protection Advisor Scale Plan
     */
    private Boolean includeDPAScalePlan;

    /**
     * # of Data Protection Advisor Collection Nodes
     */
    private Integer dpaCollectionNodes;

    /**
     * # of Data Protection Collector Nodes to Configure
     */
    private Integer dpaCollectionNodesConfig;

    /**
     * <p>
     * The default constructor.
     * </p>
     */
    public DataProtectionAdvisorDesign() {
    }

    /**
     * Getter method for property <b>includeDPAExtDB</b>.
     *
     * @return property value of includeDPAExtDB
     */
    public Boolean getIncludeDPAExtDB() {
        return includeDPAExtDB;
    }

    /**
     * Setter method for property <b>includeDPAExtDB</b>.
     *
     * @param includeDPAExtDB
     *            value to be assigned to property includeDPAExtDB
     */
    public void setIncludeDPAExtDB(Boolean includeDPAExtDB) {
        this.includeDPAExtDB = includeDPAExtDB;
    }

    /**
     * Getter method for property <b>includeDPAAnalysisJobs</b>.
     *
     * @return property value of includeDPAAnalysisJobs
     */
    public Boolean getIncludeDPAAnalysisJobs() {
        return includeDPAAnalysisJobs;
    }

    /**
     * Setter method for property <b>includeDPAAnalysisJobs</b>.
     *
     * @param includeDPAAnalysisJobs
     *            value to be assigned to property includeDPAAnalysisJobs
     */
    public void setIncludeDPAAnalysisJobs(Boolean includeDPAAnalysisJobs) {
        this.includeDPAAnalysisJobs = includeDPAAnalysisJobs;
    }

    /**
     * Getter method for property <b>includeDPARecoverabilityAnalysis</b>.
     *
     * @return property value of includeDPARecoverabilityAnalysis
     */
    public Boolean getIncludeDPARecoverabilityAnalysis() {
        return includeDPARecoverabilityAnalysis;
    }

    /**
     * Setter method for property <b>includeDPARecoverabilityAnalysis</b>.
     *
     * @param includeDPARecoverabilityAnalysis
     *            value to be assigned to property includeDPARecoverabilityAnalysis
     */
    public void setIncludeDPARecoverabilityAnalysis(Boolean includeDPARecoverabilityAnalysis) {
        this.includeDPARecoverabilityAnalysis = includeDPARecoverabilityAnalysis;
    }

    /**
     * Getter method for property <b>includeDPACustomReportDev</b>.
     *
     * @return property value of includeDPACustomReportDev
     */
    public Boolean getIncludeDPACustomReportDev() {
        return includeDPACustomReportDev;
    }

    /**
     * Setter method for property <b>includeDPACustomReportDev</b>.
     *
     * @param includeDPACustomReportDev
     *            value to be assigned to property includeDPACustomReportDev
     */
    public void setIncludeDPACustomReportDev(Boolean includeDPACustomReportDev) {
        this.includeDPACustomReportDev = includeDPACustomReportDev;
    }

    /**
     * Getter method for property <b>includeDPAInterfaceCustomization</b>.
     *
     * @return property value of includeDPAInterfaceCustomization
     */
    public Boolean getIncludeDPAInterfaceCustomization() {
        return includeDPAInterfaceCustomization;
    }

    /**
     * Setter method for property <b>includeDPAInterfaceCustomization</b>.
     *
     * @param includeDPAInterfaceCustomization
     *            value to be assigned to property includeDPAInterfaceCustomization
     */
    public void setIncludeDPAInterfaceCustomization(Boolean includeDPAInterfaceCustomization) {
        this.includeDPAInterfaceCustomization = includeDPAInterfaceCustomization;
    }

    /**
     * Getter method for property <b>includeDPAScalePlan</b>.
     *
     * @return property value of includeDPAScalePlan
     */
    public Boolean getIncludeDPAScalePlan() {
        return includeDPAScalePlan;
    }

    /**
     * Setter method for property <b>includeDPAScalePlan</b>.
     *
     * @param includeDPAScalePlan
     *            value to be assigned to property includeDPAScalePlan
     */
    public void setIncludeDPAScalePlan(Boolean includeDPAScalePlan) {
        this.includeDPAScalePlan = includeDPAScalePlan;
    }

    /**
     * Getter method for property <b>dpaCollectionNodes</b>.
     *
     * @return property value of dpaCollectionNodes
     */
    public Integer getDpaCollectionNodes() {
        return dpaCollectionNodes;
    }

    /**
     * Setter method for property <b>dpaCollectionNodes</b>.
     *
     * @param dpaCollectionNodes
     *            value to be assigned to property dpaCollectionNodes
     */
    public void setDpaCollectionNodes(Integer dpaCollectionNodes) {
        this.dpaCollectionNodes = dpaCollectionNodes;
    }

    /**
     * Getter method for property <b>dpaCollectionNodesConfig</b>.
     *
     * @return property value of dpaCollectionNodesConfig
     */
    public Integer getDpaCollectionNodesConfig() {
        return dpaCollectionNodesConfig;
    }

    /**
     * Setter method for property <b>dpaCollectionNodesConfig</b>.
     *
     * @param dpaCollectionNodesConfig
     *            value to be assigned to property dpaCollectionNodesConfig
     */
    public void setDpaCollectionNodesConfig(Integer dpaCollectionNodesConfig) {
        this.dpaCollectionNodesConfig = dpaCollectionNodesConfig;
    }

}
