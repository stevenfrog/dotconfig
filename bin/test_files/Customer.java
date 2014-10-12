/*
 * This code is copyright (c) 2013 - 2014 EMC Corporation.
 */
package com.emc.gs.tools.srf.model;

import java.util.Date;
import java.util.List;

/**
 * <p>
 * This is Customer entity class.
 * </p>
 * <p>
 * <strong>Thread safety</strong>: This class is mutable, it is not thread safety.
 * </p>
 * 
 * <p>
 * <strong>Changes:</strong> <strong>SRT Release Assembly - Base</strong>
 * <ul>
 * <li>Release_assembly_tasks.xls Row#5: Renamed name to contactName</li>
 * <li>Release_assembly_tasks.xls Row#6: Renamed servicesAgreementNote to partnerInformation</li>
 * </ul>
 * </p>
 * 
 * <p>
 * <strong>Changes V1.2:</strong>
 * <ul>
 * <li>Removed shortName field.</li>
 * </ul>
 * </p>
 *
 * <p>
 * <strong>Changes V1.3:</strong>
 * <strong>SRT Phase 2 Release Assembly</strong>
 * <ul>
 * <li>Change officePhone/mobilePhone/fax fields to Phone type</li>
 * </ul>
 * </p>
 * 
 * @author faeton, stevenfrog, TCSASSEMBLER, MonicaMuranyi
 * @version 1.3
 */
public class Customer extends IdentifiableEntity {
    /**
     * <p>
     * The contactName.
     * </p>
     * 
     * @since 1.1
     */
    private String contactName;

    /**
     * <p>
     * The formalName.
     * </p>
     */
    private String formalName;

    /**
     * <p>
     * The address1.
     * </p>
     */
    private String address1;

    /**
     * <p>
     * The address2.
     * </p>
     */
    private String address2;

    /**
     * <p>
     * The city.
     * </p>
     */
    private String city;
    
    /**
     * <p>
     * The geoState.
     * </p>
     */
    private GeoState geoState;

    /**
     * <p>
     * The zip.
     * </p>
     */
    private String zip;

    /**
     * <p>
     * The country.
     * </p>
     */
    private Country country;

    /**
     * <p>
     * The title.
     * </p>
     */
    private String title;

    /**
     * <p>
     * The officePhone.
     * </p>
     */
    private Phone officePhone;

    /**
     * <p>
     * The mobilePhone.
     * </p>
     */
    private Phone mobilePhone;

    /**
     * <p>
     * The fax.
     * </p>
     */
    private Phone fax;

    /**
     * <p>
     * The email.
     * </p>
     */
    private String email;

    /**
     * <p>
     * The servicesAgreementType.
     * </p>
     */
    private ServicesAgreementType servicesAgreementType;

    /**
     * <p>
     * The servicesAgreementNumber.
     * </p>
     */
    private String servicesAgreementNumber;

    /**
     * <p>
     * The servicesAgreementDate.
     * </p>
     */
    private Date servicesAgreementDate;

    /**
     * <p>
     * The partnerInformation.
     * </p>
     * @since 1.1
     */
    private String partnerInformation;

    /**
     * <p>
     * The customerWorkSites.
     * </p>
     */
    private List<CustomerWorkSite> customerWorkSites;

    /**
     * <p>
     * Indicates whether this is a "template" customer.
     * </p>
     */
    private boolean template;

    /**
     * <p>
     * The default constructor.
     * </p>
     */
    public Customer() {
        // Empty
    }

    /**
     * <p>
     * Retrieves the contactName field.
     * </p>
     * 
     * @return the contactName
     * @since 1.1
     */
    public String getContactName() {
        return contactName;
    }

    /**
     * <p>
     * Sets the value to contactName field.
     * </p>
     * 
     * @param contactName the contactName to set
     * @since 1.1
     */
    public void setContactName(String contactName) {
        this.contactName = contactName;
    }

    /**
     * <p>
     * Retrieves the formalName field.
     * </p>
     * 
     * @return the formalName
     */
    public String getFormalName() {
        return formalName;
    }

    /**
     * <p>
     * Sets the value to formalName field.
     * </p>
     * 
     * @param formalName the formalName to set
     */
    public void setFormalName(String formalName) {
        this.formalName = formalName;
    }

    /**
     * <p>
     * Retrieves the address1 field.
     * </p>
     * 
     * @return the address1
     */
    public String getAddress1() {
        return address1;
    }

    /**
     * <p>
     * Sets the value to address1 field.
     * </p>
     * 
     * @param address1 the address1 to set
     */
    public void setAddress1(String address1) {
        this.address1 = address1;
    }

    /**
     * <p>
     * Retrieves the address2 field.
     * </p>
     * 
     * @return the address2
     */
    public String getAddress2() {
        return address2;
    }

    /**
     * <p>
     * Sets the value to address2 field.
     * </p>
     * 
     * @param address2 the address2 to set
     */
    public void setAddress2(String address2) {
        this.address2 = address2;
    }

    /**
     * <p>
     * Retrieves the city field.
     * </p>
     * 
     * @return the city
     */
    public String getCity() {
        return city;
    }

    /**
     * <p>
     * Sets the value to city field.
     * </p>
     * 
     * @param city the city to set
     */
    public void setCity(String city) {
        this.city = city;
    }

    /**
     * <p>
     * Retrieves the geoState field.
     * </p>
     * 
     * @return the state
     */
    public GeoState getGeoState() {
        return this.geoState;
    }

    /**
     * <p>
     * Sets the value to geoState field.
     * </p>
     * 
     * @param geoState the geoState to set
     */
    public void setGeoState(GeoState geoState) {
        this.geoState = geoState;
    }

    /**
     * <p>
     * Retrieves the zip field.
     * </p>
     * 
     * @return the zip
     */
    public String getZip() {
        return zip;
    }

    /**
     * <p>
     * Sets the value to zip field.
     * </p>
     * 
     * @param zip the zip to set
     */
    public void setZip(String zip) {
        this.zip = zip;
    }

    /**
     * <p>
     * Retrieves the title field.
     * </p>
     * 
     * @return the title
     */
    public String getTitle() {
        return title;
    }

    /**
     * <p>
     * Sets the value to title field.
     * </p>
     * 
     * @param title the title to set
     */
    public void setTitle(String title) {
        this.title = title;
    }

    /**
     * <p>
     * Retrieves the officePhone field.
     * </p>
     * 
     * @return the officePhone
     */
    public Phone getOfficePhone() {
        return officePhone;
    }

    /**
     * <p>
     * Sets the value to officePhone field.
     * </p>
     * 
     * @param officePhone the officePhone to set
     */
    public void setOfficePhone(Phone officePhone) {
        this.officePhone = officePhone;
    }

    /**
     * <p>
     * Retrieves the mobilePhone field.
     * </p>
     * 
     * @return the mobilePhone
     */
    public Phone getMobilePhone() {
        return mobilePhone;
    }

    /**
     * <p>
     * Sets the value to mobilePhone field.
     * </p>
     * 
     * @param mobilePhone the mobilePhone to set
     */
    public void setMobilePhone(Phone mobilePhone) {
        this.mobilePhone = mobilePhone;
    }

    /**
     * <p>
     * Retrieves the fax field.
     * </p>
     * 
     * @return the fax
     */
    public Phone getFax() {
        return fax;
    }

    /**
     * <p>
     * Sets the value to fax field.
     * </p>
     * 
     * @param fax the fax to set
     */
    public void setFax(Phone fax) {
        this.fax = fax;
    }

    /**
     * <p>
     * Retrieves the email field.
     * </p>
     * 
     * @return the email
     */
    public String getEmail() {
        return email;
    }

    /**
     * <p>
     * Sets the value to email field.
     * </p>
     * 
     * @param email the email to set
     */
    public void setEmail(String email) {
        this.email = email;
    }

    /**
     * <p>
     * Retrieves the servicesAgreementType field.
     * </p>
     * 
     * @return the servicesAgreementType
     */
    public ServicesAgreementType getServicesAgreementType() {
        return servicesAgreementType;
    }

    /**
     * <p>
     * Sets the value to servicesAgreementType field.
     * </p>
     * 
     * @param servicesAgreementType the servicesAgreementType to set
     */
    public void setServicesAgreementType(ServicesAgreementType servicesAgreementType) {
        this.servicesAgreementType = servicesAgreementType;
    }

    /**
     * <p>
     * Retrieves the servicesAgreementNumber field.
     * </p>
     * 
     * @return the servicesAgreementNumber
     */
    public String getServicesAgreementNumber() {
        return servicesAgreementNumber;
    }

    /**
     * <p>
     * Sets the value to servicesAgreementNumber field.
     * </p>
     * 
     * @param servicesAgreementNumber the servicesAgreementNumber to set
     */
    public void setServicesAgreementNumber(String servicesAgreementNumber) {
        this.servicesAgreementNumber = servicesAgreementNumber;
    }

    /**
     * <p>
     * Retrieves the servicesAgreementDate field.
     * </p>
     * 
     * @return the servicesAgreementDate
     */
    public Date getServicesAgreementDate() {
        return servicesAgreementDate;
    }

    /**
     * <p>
     * Sets the value to servicesAgreementDate field.
     * </p>
     * 
     * @param servicesAgreementDate the servicesAgreementDate to set
     */
    public void setServicesAgreementDate(Date servicesAgreementDate) {
        this.servicesAgreementDate = servicesAgreementDate;
    }

    /**
     * <p>
     * Retrieves the partnerInformation field.
     * </p>
     * 
     * @return the partnerInformation
     * @since 1.1
     */
    public String getPartnerInformation() {
        return partnerInformation;
    }

    /**
     * <p>
     * Sets the value to partnerInformation field.
     * </p>
     * 
     * @param partnerInformation the partnerInformation to set
     * @since 1.1
     */
    public void setPartnerInformation(String partnerInformation) {
        this.partnerInformation = partnerInformation;
    }

    /**
     * <p>
     * Retrieves the customerWorkSites field.
     * </p>
     * 
     * @return the customerWorkSites
     */
    public List<CustomerWorkSite> getCustomerWorkSites() {
        return customerWorkSites;
    }

    /**
     * <p>
     * Sets the value to customerWorkSites field.
     * </p>
     * 
     * @param customerWorkSites the customerWorkSites to set
     */
    public void setCustomerWorkSites(List<CustomerWorkSite> customerWorkSites) {
        this.customerWorkSites = customerWorkSites;
    }

    /**
     * <p>
     * Retrieves the country field.
     * </p>
     * 
     * @return the value of country
     */
    public Country getCountry() {
        return country;
    }

    /**
     * <p>
     * Sets the value to country field.
     * </p>
     * 
     * @param country the value of country to set
     */
    public void setCountry(Country country) {
        this.country = country;
    }

    /**
     * Getter method for property <tt>template</tt>.
     * @return property value of template
     */
    public boolean isTemplate() {
        return template;
    }

    /**
     * Setter method for property <tt>template</tt>.
     * @param template value to be assigned to property template
     */
    public void setTemplate(boolean template) {
        this.template = template;
    }

    /**
     * The toString method.
     * 
     * @return the string of this entity
     */
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("{").append(super.toString());
        sb.append(", template:").append(template);
        sb.append(", contactName:").append(contactName);
        sb.append(", formalName:").append(formalName);
        sb.append(", address1:").append(address1);
        sb.append(", address2:").append(address2);
        sb.append(", city:").append(city);
        sb.append(", zip:").append(zip);
        sb.append(", geoState:").append(geoState);
        sb.append(", country:").append(country);
        sb.append(", title:").append(title);
        sb.append(", officePhone:").append(officePhone);
        sb.append(", mobilePhone:").append(mobilePhone);
        sb.append(", fax:").append(fax);
        sb.append(", email:").append(email);
        sb.append(", servicesAgreementType:").append(servicesAgreementType);
        sb.append(", servicesAgreementNumber:").append(servicesAgreementNumber);
        sb.append(", servicesAgreementDate:").append(servicesAgreementDate);
        sb.append(", partnerInformation:").append(partnerInformation).append("}");
        return sb.toString();
    }

}
