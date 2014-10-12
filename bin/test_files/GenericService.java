/*
 * Copyright (C) 2013 TopCoder Inc., All Rights Reserved.
 */
package com.emc.gs.tools.srf.services;

import com.emc.gs.tools.srf.models.IdentifiableEntity;

/**
 * <p>
 * This interface defines a generic contract for managing an entity. It is responsible for creating, updating, deleting
 * and retrieving the entity in the persistence.
 * </p>
 * <p>
 * <strong>Thread safety</strong>: The implementation are required to be thread safe.
 * </p>
 *
 * @param <T>
 *            the class type
 * @author faeton, TCSASSEMBLER
 * @version 1.0
 */
public interface GenericService<T extends IdentifiableEntity> {
    /**
     * Creates an entity.
     *
     * @param entity
     *            the entity to create
     * @return The created entity
     * @throws IllegalArgumentException
     *             if entity is null
     * @throws ServiceRequestToolException
     *             if any other error occurred during the operation
     */
    public T create(T entity) throws ServiceRequestToolException;

    /**
     * Updates an entity.
     *
     * @param entity
     *            the entity to update
     * @return The updated entity
     * @throws IllegalArgumentException
     *             if entity is null
     * @throws EntityNotFoundException
     *             if the entity to update doesn't exist
     * @throws ServiceRequestToolException
     *             if any other error occurred during the operation
     */
    public T update(T entity) throws ServiceRequestToolException;

    /**
     * Deletes one or more entities.
     *
     * @param ids
     *            the IDs of the entities to delete
     * @throws IllegalArgumentException
     *             if ids array is empty, or any element in ids array is not positive
     * @throws EntityNotFoundException
     *             if any entity to delete doesn't exist
     * @throws ServiceRequestToolException
     *             if any other error occurred during the operation
     */
    public void delete(long[] ids) throws ServiceRequestToolException;

    /**
     * Retrieves an entity.
     *
     * @param id
     *            the ID of the entity to retrieve
     * @return The entity for the id or null will, if there's no such entity
     * @throws IllegalArgumentException
     *             if id is not positive
     * @throws ServiceRequestToolException
     *             if any other error occurred during the operation
     */
    public T get(long id);
}
