package com.pzr.models;

import java.util.*;
import java.lang.*;
import com.pzr.models.*;

/**
 * This class represents building violations information.
 * It is a simple JavaBean (POJO) that provides getters and setters for all private attributes and performs no argument validation in the setters.
 * 
 * Thread Safety:
 * This class is mutable and not thread safe.
 */
public class BuildingViolations {
    /**
     */
    private BuildingViolationType type;

    /**
     */
    private Date dateEmailedCM;

    /**
     */
    private Boolean canGetInWRT;
}

