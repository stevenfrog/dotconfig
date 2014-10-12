package com.pzr.models;

import java.util.*;
import java.lang.*;
import com.pzr.models.*;

/**
 * This class represents site cost.
 * This is a JPA embeddable of Site entity.
 * It is a simple JavaBean (POJO) that provides getters and setters for all private attributes and performs no argument validation in the setters.
 * 
 * Thread Safety:
 * This class is mutable and not thread safe.
 */
public class SiteCost {
    /**
     */
    private BigDecimal approvalRequiredOnCostOver;

    /**
     */
    private BigDecimal costApprovedByClient;

    /**
     */
    private Date dateApproved;

    /**
     */
    private CostToBeInvoiced costToBeInvoiced;

    /**
     */
    private String notes;

    /**
     */
    private List<Check> checks;
}

