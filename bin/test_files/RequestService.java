/*
 * Copyright (C) 2013 TopCoder Inc., All Rights Reserved.
 */
package com.emc.gs.tools.srf.services;

import com.emc.gs.tools.srf.models.Request;
import com.emc.gs.tools.srf.models.RequestSearchCriteria;
import com.emc.gs.tools.srf.models.SearchResult;
import com.emc.gs.tools.srf.models.StartRequestData;
import com.emc.gs.tools.srf.models.bc.BcRequestData;
import com.emc.gs.tools.srf.models.infrastructure.InfrastructureRequestData;
import com.emc.gs.tools.srf.models.mainframe.MainframeRequestData;
import com.emc.gs.tools.srf.models.unified.UnifiedRequestData;

/**
 * <p>
 * This interface defines a contract for managing a request. It is simply extends GenericService to provide
 * necessary create, update, delete and get methods and additionally provides a search method based on
 * criteria.
 * </p>
 * <p>
 * <strong>Thread safety</strong>: The implementation are required to be thread safe.
 * </p>
 *
 * @author faeton, TCSASSEMBLER
 * @version 1.0
 */
public interface RequestService extends GenericService<Request> {
    /**
     * Returns StartRequestData instance for the request id.
     *
     * @param requestId
     *            the request id to retrieve request data
     * @return the request data details
     * @throws IllegalArgumentException
     *             if requestId is not positive
     * @throws ServiceRequestToolException
     *             if any other error occurred during the operation
     */
    public StartRequestData getStartRequestData() throws ServiceRequestToolException;

    /**
     * Returns BcRequestData instance for the request id.
     *
     * @param requestId
     *            the request id to retrieve request data
     * @return the request data details
     * @throws IllegalArgumentException
     *             if requestId is not positive
     * @throws ServiceRequestToolException
     *             if any other error occurred during the operation
     */
    public BcRequestData getBcRequestData(long requestId);

    /**
     * Returns MainframeRequestData instance for the request id.
     *
     * @param requestId
     *            the request id to retrieve request data
     * @return the request data details
     * @throws IllegalArgumentException
     *             if requestId is not positive
     * @throws ServiceRequestToolException
     *             if any other error occurred during the operation
     */
    public MainframeRequestData getMainframeRequestData(long requestId) throws ServiceRequestToolException;

    /**
     * Returns UnifiedRequestData instance for the request id.
     *
     * @param requestId
     *            the request id to retrieve request data
     * @return the request data details
     * @throws IllegalArgumentException
     *             if requestId is not positive
     * @throws ServiceRequestToolException
     *             if any other error occurred during the operation
     */
    public UnifiedRequestData getUnifiedRequestData(long requestId) throws ServiceRequestToolException;

    /**
     * Returns InsfrastructureRequestData instance for the request id.
     *
     * @param requestId
     *            the request id to retrieve request data
     * @return the request data details
     * @throws IllegalArgumentException
     *             if requestId is not positive
     * @throws ServiceRequestToolException
     *             if any other error occurred during the operation
     */
    public InfrastructureRequestData getInfrastructureRequestData(long requestId)
        throws ServiceRequestToolException;

    /**
     * Search requests based on the search criteria.
     *
     * @param criteria
     *            the search criteria
     * @return the search result
     * @throws IllegalArgumentException
     *             if criteria is null, or if criteria.pageNumber is positive, criteria.pageSize is not
     *             positive
     * @throws ServiceRequestToolException
     *             if any other error occurred during the operation
     */
    public SearchResult<Request> search(RequestSearchCriteria criteria) throws ServiceRequestToolException;
}
