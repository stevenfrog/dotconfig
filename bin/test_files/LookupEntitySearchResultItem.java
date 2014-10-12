package com.pzr.models.dto;

import java.lang.*;
import com.ptr.models.Map;

/**
 * This class represents lookup entity search result item.
 * It is a simple JavaBean (POJO) that provides getters and setters for all private attributes and performs no argument validation in the setters.
 * 
 * Thread Safety:
 * This class is mutable and not thread safe.
 */
public class LookupEntitySearchResultItem {
    /**
     */
    private String name;

    /**
     */
    private Class<? extends LookupEntity> lookupEntityClass;

    /**
     */
    private int numberOfValues;
}

