/*
 * Copyright (C) 2013 TopCoder Inc., All Rights Reserved.
 */
package com.emc.gs.tools.srf.models.bc;

import java.util.Map;

import com.emc.gs.tools.srf.models.IdentifiableEntity;

/**
 * <p>
 * This is ReplicationManagerInformation entity class.
 * </p>
 * <p>
 * <strong>Thread safety</strong>: This class is mutable, it is not thread safety.
 * </p>
 *
 * @author faeton, TCSASSEMBLER
 * @version 1.0
 */
public class ReplicationManagerInformation extends IdentifiableEntity {
    /**
     * <p>
     * The timeFinderManaged.
     * </p>
     */
    private boolean timeFinderManaged;

    /**
     * <p>
     * The openReplicatorManaged.
     * </p>
     */
    private boolean openReplicatorManaged;

    /**
     * <p>
     * The snapViewManaged.
     * </p>
     */
    private boolean snapViewManaged;

    /**
     * <p>
     * The recoverPointManaged.
     * </p>
     */
    private boolean recoverPointManaged;

    /**
     * <p>
     * The sanCopyManaged.
     * </p>
     */
    private boolean sanCopyManaged;

    /**
     * <p>
     * The celerraManaged.
     * </p>
     */
    private boolean celerraManaged;

    /**
     * <p>
     * The snapSureManaged.
     * </p>
     */
    private boolean snapSureManaged;

    /**
     * <p>
     * The replicationInstalled.
     * </p>
     */
    private boolean replicationInstalled;

    /**
     * <p>
     * The replicationManagerImplementation.
     * </p>
     */
    private ReplicationManagerImplementation replicationManagerImplementation;

    /**
     * <p>
     * The replicatedStorageSize.
     * </p>
     */
    private Integer replicatedStorageSize;

    /**
     * <p>
     * The configChangeType.
     * </p>
     */
    private ConfigChangeType configChangeType;

    /**
     * <p>
     * The managerServersNumber.
     * </p>
     */
    private Integer managerServersNumber;

    /**
     * <p>
     * The clusteredRmServerOption.
     * </p>
     */
    private boolean clusteredRmServerOption;

    /**
     * <p>
     * The Integer>.
     * </p>
     */
    private Map<String, Integer> databaseNumber;

    /**
     * <p>
     * The Integer>.
     * </p>
     */
    private Map<String, Integer> sourceHostNumber;

    /**
     * <p>
     * The Integer>.
     * </p>
     */
    private Map<String, Integer> targetHostNumber;

    /**
     * <p>
     * The customScriptingRequired.
     * </p>
     */
    private boolean customScriptingRequired;

    /**
     * <p>
     * The customScriptingDetails.
     * </p>
     */
    private String customScriptingDetails;

    /**
     * <p>
     * The default constructor.
     * </p>
     */
    public ReplicationManagerInformation() {
        // Empty
    }

    /**
     * <p>
     * Retrieves the timeFinderManaged field.
     * </p>
     *
     * @return the value of timeFinderManaged
     */
    public boolean isTimeFinderManaged() {
        return timeFinderManaged;
    }

    /**
     * <p>
     * Sets the value to timeFinderManaged field.
     * </p>
     *
     * @param timeFinderManaged
     *            the value of timeFinderManaged to set
     */
    public void setTimeFinderManaged(boolean timeFinderManaged) {
        this.timeFinderManaged = timeFinderManaged;
    }

    /**
     * <p>
     * Retrieves the openReplicatorManaged field.
     * </p>
     *
     * @return the value of openReplicatorManaged
     */
    public boolean isOpenReplicatorManaged() {
        return openReplicatorManaged;
    }

    /**
     * <p>
     * Sets the value to openReplicatorManaged field.
     * </p>
     *
     * @param openReplicatorManaged
     *            the value of openReplicatorManaged to set
     */
    public void setOpenReplicatorManaged(boolean openReplicatorManaged) {
        this.openReplicatorManaged = openReplicatorManaged;
    }

    /**
     * <p>
     * Retrieves the snapViewManaged field.
     * </p>
     *
     * @return the value of snapViewManaged
     */
    public boolean isSnapViewManaged() {
        return snapViewManaged;
    }

    /**
     * <p>
     * Sets the value to snapViewManaged field.
     * </p>
     *
     * @param snapViewManaged
     *            the value of snapViewManaged to set
     */
    public void setSnapViewManaged(boolean snapViewManaged) {
        this.snapViewManaged = snapViewManaged;
    }

    /**
     * <p>
     * Retrieves the recoverPointManaged field.
     * </p>
     *
     * @return the value of recoverPointManaged
     */
    public boolean isRecoverPointManaged() {
        return recoverPointManaged;
    }

    /**
     * <p>
     * Sets the value to recoverPointManaged field.
     * </p>
     *
     * @param recoverPointManaged
     *            the value of recoverPointManaged to set
     */
    public void setRecoverPointManaged(boolean recoverPointManaged) {
        this.recoverPointManaged = recoverPointManaged;
    }

    /**
     * <p>
     * Retrieves the sanCopyManaged field.
     * </p>
     *
     * @return the value of sanCopyManaged
     */
    public boolean isSanCopyManaged() {
        return sanCopyManaged;
    }

    /**
     * <p>
     * Sets the value to sanCopyManaged field.
     * </p>
     *
     * @param sanCopyManaged
     *            the value of sanCopyManaged to set
     */
    public void setSanCopyManaged(boolean sanCopyManaged) {
        this.sanCopyManaged = sanCopyManaged;
    }

    /**
     * <p>
     * Retrieves the celerraManaged field.
     * </p>
     *
     * @return the value of celerraManaged
     */
    public boolean isCelerraManaged() {
        return celerraManaged;
    }

    /**
     * <p>
     * Sets the value to celerraManaged field.
     * </p>
     *
     * @param celerraManaged
     *            the value of celerraManaged to set
     */
    public void setCelerraManaged(boolean celerraManaged) {
        this.celerraManaged = celerraManaged;
    }

    /**
     * <p>
     * Retrieves the snapSureManaged field.
     * </p>
     *
     * @return the value of snapSureManaged
     */
    public boolean isSnapSureManaged() {
        return snapSureManaged;
    }

    /**
     * <p>
     * Sets the value to snapSureManaged field.
     * </p>
     *
     * @param snapSureManaged
     *            the value of snapSureManaged to set
     */
    public void setSnapSureManaged(boolean snapSureManaged) {
        this.snapSureManaged = snapSureManaged;
    }

    /**
     * <p>
     * Retrieves the replicationInstalled field.
     * </p>
     *
     * @return the value of replicationInstalled
     */
    public boolean isReplicationInstalled() {
        return replicationInstalled;
    }

    /**
     * <p>
     * Sets the value to replicationInstalled field.
     * </p>
     *
     * @param replicationInstalled
     *            the value of replicationInstalled to set
     */
    public void setReplicationInstalled(boolean replicationInstalled) {
        this.replicationInstalled = replicationInstalled;
    }

    /**
     * <p>
     * Retrieves the replicationManagerImplementation field.
     * </p>
     *
     * @return the value of replicationManagerImplementation
     */
    public ReplicationManagerImplementation getReplicationManagerImplementation() {
        return replicationManagerImplementation;
    }

    /**
     * <p>
     * Sets the value to replicationManagerImplementation field.
     * </p>
     *
     * @param replicationManagerImplementation
     *            the value of replicationManagerImplementation to set
     */
    public void setReplicationManagerImplementation(ReplicationManagerImplementation replicationManagerImplementation) {
        this.replicationManagerImplementation = replicationManagerImplementation;
    }

    /**
     * <p>
     * Retrieves the replicatedStorageSize field.
     * </p>
     *
     * @return the value of replicatedStorageSize
     */
    public Integer getReplicatedStorageSize() {
        return replicatedStorageSize;
    }

    /**
     * <p>
     * Sets the value to replicatedStorageSize field.
     * </p>
     *
     * @param replicatedStorageSize
     *            the value of replicatedStorageSize to set
     */
    public void setReplicatedStorageSize(Integer replicatedStorageSize) {
        this.replicatedStorageSize = replicatedStorageSize;
    }

    /**
     * <p>
     * Retrieves the configChangeType field.
     * </p>
     *
     * @return the value of configChangeType
     */
    public ConfigChangeType getConfigChangeType() {
        return configChangeType;
    }

    /**
     * <p>
     * Sets the value to configChangeType field.
     * </p>
     *
     * @param configChangeType
     *            the value of configChangeType to set
     */
    public void setConfigChangeType(ConfigChangeType configChangeType) {
        this.configChangeType = configChangeType;
    }

    /**
     * <p>
     * Retrieves the managerServersNumber field.
     * </p>
     *
     * @return the value of managerServersNumber
     */
    public Integer getManagerServersNumber() {
        return managerServersNumber;
    }

    /**
     * <p>
     * Sets the value to managerServersNumber field.
     * </p>
     *
     * @param managerServersNumber
     *            the value of managerServersNumber to set
     */
    public void setManagerServersNumber(Integer managerServersNumber) {
        this.managerServersNumber = managerServersNumber;
    }

    /**
     * <p>
     * Retrieves the clusteredRmServerOption field.
     * </p>
     *
     * @return the value of clusteredRmServerOption
     */
    public boolean isClusteredRmServerOption() {
        return clusteredRmServerOption;
    }

    /**
     * <p>
     * Sets the value to clusteredRmServerOption field.
     * </p>
     *
     * @param clusteredRmServerOption
     *            the value of clusteredRmServerOption to set
     */
    public void setClusteredRmServerOption(boolean clusteredRmServerOption) {
        this.clusteredRmServerOption = clusteredRmServerOption;
    }

    /**
     * <p>
     * Retrieves the databaseNumber field.
     * </p>
     *
     * @return the value of databaseNumber
     */
    public Map<String, Integer> getDatabaseNumber() {
        return databaseNumber;
    }

    /**
     * <p>
     * Sets the value to databaseNumber field.
     * </p>
     *
     * @param databaseNumber
     *            the value of databaseNumber to set
     */
    public void setDatabaseNumber(Map<String, Integer> databaseNumber) {
        this.databaseNumber = databaseNumber;
    }

    /**
     * <p>
     * Retrieves the sourceHostNumber field.
     * </p>
     *
     * @return the value of sourceHostNumber
     */
    public Map<String, Integer> getSourceHostNumber() {
        return sourceHostNumber;
    }

    /**
     * <p>
     * Sets the value to sourceHostNumber field.
     * </p>
     *
     * @param sourceHostNumber
     *            the value of sourceHostNumber to set
     */
    public void setSourceHostNumber(Map<String, Integer> sourceHostNumber) {
        this.sourceHostNumber = sourceHostNumber;
    }

    /**
     * <p>
     * Retrieves the targetHostNumber field.
     * </p>
     *
     * @return the value of targetHostNumber
     */
    public Map<String, Integer> getTargetHostNumber() {
        return targetHostNumber;
    }

    /**
     * <p>
     * Sets the value to targetHostNumber field.
     * </p>
     *
     * @param targetHostNumber
     *            the value of targetHostNumber to set
     */
    public void setTargetHostNumber(Map<String, Integer> targetHostNumber) {
        this.targetHostNumber = targetHostNumber;
    }

    /**
     * <p>
     * Retrieves the customScriptingRequired field.
     * </p>
     *
     * @return the value of customScriptingRequired
     */
    public boolean isCustomScriptingRequired() {
        return customScriptingRequired;
    }

    /**
     * <p>
     * Sets the value to customScriptingRequired field.
     * </p>
     *
     * @param customScriptingRequired
     *            the value of customScriptingRequired to set
     */
    public void setCustomScriptingRequired(boolean customScriptingRequired) {
        this.customScriptingRequired = customScriptingRequired;
    }

    /**
     * <p>
     * Retrieves the customScriptingDetails field.
     * </p>
     *
     * @return the value of customScriptingDetails
     */
    public String getCustomScriptingDetails() {
        return customScriptingDetails;
    }

    /**
     * <p>
     * Sets the value to customScriptingDetails field.
     * </p>
     *
     * @param customScriptingDetails
     *            the value of customScriptingDetails to set
     */
    public void setCustomScriptingDetails(String customScriptingDetails) {
        this.customScriptingDetails = customScriptingDetails;
    }

    /**
     * The toString method.
     *
     * @return the string for this entity
     */
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("{").append(super.toString());
        sb.append(", timeFinderManaged:").append(timeFinderManaged);
        sb.append(", openReplicatorManaged:").append(openReplicatorManaged);
        sb.append(", snapViewManaged:").append(snapViewManaged);
        sb.append(", recoverPointManaged:").append(recoverPointManaged);
        sb.append(", sanCopyManaged:").append(sanCopyManaged);
        sb.append(", celerraManaged:").append(celerraManaged);
        sb.append(", snapSureManaged:").append(snapSureManaged);
        sb.append(", replicationInstalled:").append(replicationInstalled);
        sb.append(", replicationManagerImplementation:").append(replicationManagerImplementation);
        sb.append(", replicatedStorageSize:").append(replicatedStorageSize);
        sb.append(", configChangeType:").append(configChangeType);
        sb.append(", managerServersNumber:").append(managerServersNumber);
        sb.append(", clusteredRmServerOption:").append(clusteredRmServerOption);
        sb.append(", databaseNumber:").append(databaseNumber);
        sb.append(", sourceHostNumber:").append(sourceHostNumber);
        sb.append(", targetHostNumber:").append(targetHostNumber);
        sb.append(", customScriptingRequired:").append(customScriptingRequired);
        sb.append(", customScriptingDetails:").append(customScriptingDetails).append("}");
        return sb.toString();
    }
}
