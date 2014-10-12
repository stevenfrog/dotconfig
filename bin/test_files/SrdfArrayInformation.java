/*
 * Copyright (C) 2013 TopCoder Inc., All Rights Reserved.
 */
package com.emc.gs.tools.srf.models.bc;

import java.util.List;

import com.emc.gs.tools.srf.models.IdentifiableEntity;

/**
 * <p>
 * This is SrdfArrayInformation entity class.
 * </p>
 * <p>
 * <strong>Thread safety</strong>: This class is mutable, it is not thread safety.
 * </p>
 *
 * @author faeton, TCSASSEMBLER
 * @version 1.0
 */
public class SrdfArrayInformation extends IdentifiableEntity {
    /**
     * <p>
     * The symmetrixModel.
     * </p>
     */
    private List<SymmetrixModel> symmetrixModel;

    /**
     * <p>
     * The existingOptionEnabled.
     * </p>
     */
    private List<Boolean> existingOptionEnabled;

    /**
     * <p>
     * The microcodeFamily.
     * </p>
     */
    private List<MicrocodeFamily> microcodeFamily;

    /**
     * <p>
     * The replicateSize.
     * </p>
     */
    private List<Integer> replicateSize;

    /**
     * <p>
     * The srdfInstalledStatus.
     * </p>
     */
    private List<Boolean> srdfInstalledStatus;

    /**
     * <p>
     * The currentSrdfMode.
     * </p>
     */
    private List<SrdfMode> currentSrdfMode;

    /**
     * <p>
     * The newSrdfMode.
     * </p>
     */
    private List<SrdfMode> newSrdfMode;

    /**
     * <p>
     * The uniOptionEnabled.
     * </p>
     */
    private List<Boolean> uniOptionEnabled;

    /**
     * <p>
     * The srdfConnectionType.
     * </p>
     */
    private List<SrdfConnectionType> srdfConnectionType;

    /**
     * <p>
     * The targetName.
     * </p>
     */
    private List<String> targetName;

    /**
     * <p>
     * The default constructor.
     * </p>
     */
    public SrdfArrayInformation() {
        // Empty
    }

    /**
     * <p>
     * Retrieves the symmetrixModel field.
     * </p>
     *
     * @return the value of symmetrixModel
     */
    public List<SymmetrixModel> getSymmetrixModel() {
        return symmetrixModel;
    }

    /**
     * <p>
     * Sets the value to symmetrixModel field.
     * </p>
     *
     * @param symmetrixModel
     *            the value of symmetrixModel to set
     */
    public void setSymmetrixModel(List<SymmetrixModel> symmetrixModel) {
        this.symmetrixModel = symmetrixModel;
    }

    /**
     * <p>
     * Retrieves the existingOptionEnabled field.
     * </p>
     *
     * @return the value of existingOptionEnabled
     */
    public List<Boolean> getExistingOptionEnabled() {
        return existingOptionEnabled;
    }

    /**
     * <p>
     * Sets the value to existingOptionEnabled field.
     * </p>
     *
     * @param existingOptionEnabled
     *            the value of existingOptionEnabled to set
     */
    public void setExistingOptionEnabled(List<Boolean> existingOptionEnabled) {
        this.existingOptionEnabled = existingOptionEnabled;
    }

    /**
     * <p>
     * Retrieves the microcodeFamily field.
     * </p>
     *
     * @return the value of microcodeFamily
     */
    public List<MicrocodeFamily> getMicrocodeFamily() {
        return microcodeFamily;
    }

    /**
     * <p>
     * Sets the value to microcodeFamily field.
     * </p>
     *
     * @param microcodeFamily
     *            the value of microcodeFamily to set
     */
    public void setMicrocodeFamily(List<MicrocodeFamily> microcodeFamily) {
        this.microcodeFamily = microcodeFamily;
    }

    /**
     * <p>
     * Retrieves the replicateSize field.
     * </p>
     *
     * @return the value of replicateSize
     */
    public List<Integer> getReplicateSize() {
        return replicateSize;
    }

    /**
     * <p>
     * Sets the value to replicateSize field.
     * </p>
     *
     * @param replicateSize
     *            the value of replicateSize to set
     */
    public void setReplicateSize(List<Integer> replicateSize) {
        this.replicateSize = replicateSize;
    }

    /**
     * <p>
     * Retrieves the srdfInstalledStatus field.
     * </p>
     *
     * @return the value of srdfInstalledStatus
     */
    public List<Boolean> getSrdfInstalledStatus() {
        return srdfInstalledStatus;
    }

    /**
     * <p>
     * Sets the value to srdfInstalledStatus field.
     * </p>
     *
     * @param srdfInstalledStatus
     *            the value of srdfInstalledStatus to set
     */
    public void setSrdfInstalledStatus(List<Boolean> srdfInstalledStatus) {
        this.srdfInstalledStatus = srdfInstalledStatus;
    }

    /**
     * <p>
     * Retrieves the currentSrdfMode field.
     * </p>
     *
     * @return the value of currentSrdfMode
     */
    public List<SrdfMode> getCurrentSrdfMode() {
        return currentSrdfMode;
    }

    /**
     * <p>
     * Sets the value to currentSrdfMode field.
     * </p>
     *
     * @param currentSrdfMode
     *            the value of currentSrdfMode to set
     */
    public void setCurrentSrdfMode(List<SrdfMode> currentSrdfMode) {
        this.currentSrdfMode = currentSrdfMode;
    }

    /**
     * <p>
     * Retrieves the newSrdfMode field.
     * </p>
     *
     * @return the value of newSrdfMode
     */
    public List<SrdfMode> getNewSrdfMode() {
        return newSrdfMode;
    }

    /**
     * <p>
     * Sets the value to newSrdfMode field.
     * </p>
     *
     * @param newSrdfMode
     *            the value of newSrdfMode to set
     */
    public void setNewSrdfMode(List<SrdfMode> newSrdfMode) {
        this.newSrdfMode = newSrdfMode;
    }

    /**
     * <p>
     * Retrieves the uniOptionEnabled field.
     * </p>
     *
     * @return the value of uniOptionEnabled
     */
    public List<Boolean> getUniOptionEnabled() {
        return uniOptionEnabled;
    }

    /**
     * <p>
     * Sets the value to uniOptionEnabled field.
     * </p>
     *
     * @param uniOptionEnabled
     *            the value of uniOptionEnabled to set
     */
    public void setUniOptionEnabled(List<Boolean> uniOptionEnabled) {
        this.uniOptionEnabled = uniOptionEnabled;
    }

    /**
     * <p>
     * Retrieves the srdfConnectionType field.
     * </p>
     *
     * @return the value of srdfConnectionType
     */
    public List<SrdfConnectionType> getSrdfConnectionType() {
        return srdfConnectionType;
    }

    /**
     * <p>
     * Sets the value to srdfConnectionType field.
     * </p>
     *
     * @param srdfConnectionType
     *            the value of srdfConnectionType to set
     */
    public void setSrdfConnectionType(List<SrdfConnectionType> srdfConnectionType) {
        this.srdfConnectionType = srdfConnectionType;
    }

    /**
     * <p>
     * Retrieves the targetName field.
     * </p>
     *
     * @return the value of targetName
     */
    public List<String> getTargetName() {
        return targetName;
    }

    /**
     * <p>
     * Sets the value to targetName field.
     * </p>
     *
     * @param targetName
     *            the value of targetName to set
     */
    public void setTargetName(List<String> targetName) {
        this.targetName = targetName;
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
        sb.append(", symmetrixModel:").append(symmetrixModel);
        sb.append(", existingOptionEnabled:").append(existingOptionEnabled);
        sb.append(", microcodeFamily:").append(microcodeFamily);
        sb.append(", replicateSize:").append(replicateSize);
        sb.append(", srdfInstalledStatus:").append(srdfInstalledStatus);
        sb.append(", currentSrdfMode:").append(currentSrdfMode);
        sb.append(", newSrdfMode:").append(newSrdfMode);
        sb.append(", uniOptionEnabled:").append(uniOptionEnabled);
        sb.append(", srdfConnectionType:").append(srdfConnectionType);
        sb.append(", targetName:").append(targetName).append("}");
        return sb.toString();
    }
}
