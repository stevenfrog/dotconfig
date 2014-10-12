#!/usr/bin/env python3

import re
import frog_util


def generate_java(input_values):
    checkInfo = ''
    for line in input_values.splitlines():
        line = line.strip()
        i = line.replace('?', '')
        if i.startswith('###'):
            print('########################################')
            print(i)
            print('########################################')
        elif i.startswith('=RADIO=='):
            i = i[9:]
            print('/**')
            print(' * Represents whether "%s" service is selected.' % i)
            print(' */')
            name = i.replace('Include ', '')
            name = name.replace('integration with ', '')
            name = name.replace('Data Services ', 'DS ') 
            name = rmNoUseCharAndCamelName(name)
            print('private Boolean %s;' % frog_util.abbreviate(name))
            print()
        elif i.startswith('=CHECK=='):
            i = i[9:]
            print('/**')
            print(' * Represents whether "%s" service is selected.' % i)
            print(' */')
            name = rmNoUseCharAndCamelName(i)
            print('private boolean %s;' % (frog_util.abbreviate(name)+"Chk"))
            print()
        elif i.startswith('=SELECT='):
            i = i[9:]
            print('/**')
            print(' * %s.' % i)
            print(' */')
            name = rmNoUseCharAndCamelName(i)
            print('private XXX %s;' % frog_util.abbreviate(name))
            print()
        elif i.startswith('========'):
            i = i[9:]
            print('/**')
            print(' * %s.' % i)
            print(' */')
            name = i
            if (i.startswith("# of")):
                name = i[5:]
            elif (i.startswith("% of")):
                name = i[5:]
            elif (i.startswith("% for")):
                name = i[6:]
            elif (i.startswith("Total # of")):
                name = "Total " + i[11:]
            elif (i.startswith("Number of")):
                name = i[10:]
            name = rmNoUseCharAndCamelName(name)
            print('private Integer %s;' % frog_util.abbreviate(name))
            print()
        elif i.startswith('=CHKINF='):
            checkInfo = i[9:]
        elif i.startswith('=CHKELM='):
            i = i[9:]
            print('/**')
            print(' * Represents whether "%s" service is selected.' % (checkInfo+': '+ i))
            print(' */')
            name = rmNoUseCharAndCamelName(i)
            print('private Boolean %s;' % (frog_util.abbreviate(name)+"Chk"))
            print()
            
            
def rmNoUseCharAndCamelName(input_name):
    result = input_name.replace('/ ', '')
    result = result.replace('- ', '')
    result = result.replace(',', '')
    result = result.replace(' a ', ' ')
    result = result.replace(' to be ', ' ')
    if (result.find(' (') > -1 and result.find(')') > -1):
        result = result[:result.index(' (')] + result[result.index(')')+1:]
    return frog_util.camel_name(result, split_char=' ')



INPUT_ELEMENT = '''

=CHECK== ViPR Planning, Design, and Implementation
=CHECK== ViPR Data Migration with PPME
=CHECK== Design & Implementation for VIPR Data Service on Commodity
=CHECK== ECS Applicance Design & Implementation

### VIPR PLANNING, DESIGN, AND IMPLEMENTATION

=RADIO== Implementation Type

### VIPR FEATURES

=RADIO== Include Data Services for Object?
=RADIO== Include Data Services for HDFS?
=RADIO== Include integration with Active Directory/LDAP?
=RADIO== Include Kerberos Authentication Mode for ViPR FS?
=RADIO== Include ViPR Content Address Storage (CAS) API Support?
=RADIO== Does a Watch4net platform exist on site that meets ViPR requirements?
=RADIO== Include Block Services Storage Ingestion?
=RADIO== Include installations of ViPR software for third party system integration?
=RADIO== Include integration with VMware vCenter Operations (vCOps)?
=RADIO== Include integration with VMware vCenter Orchestrator (vCO)?
=RADIO== Include integration with VMware vCloud Automation Center (vCAC)?
=RADIO== Include integration with Microsoft SCVMM ?
=RADIO== Include integration with EMC VSI (for VMware vSphere Web Client)?

### VIPR SCOPE DETAILS

======== # of Hadoop Clusters
======== Total # of Hadoop Cluster Nodes (Where ViPR HDFS Clients are to be deployed)
======== # of ViPR Controller instances
======== # of Tenants defined
======== # of physical Unix hosts (targeted for provisioning)
======== # of physical Windows hosts (targeted for provisioning)
======== # of VMware vCenter hosts
======== # of File-only arrays natively discovered (VNX, NetApp, Isilon)
======== # of EMC Block arrays natively discovered (VMAX / VNX)
======== # of EMC VPLEX arrays discovered
======== # of EMC RecoverPoint systems discovered
======== # of Cisco switch fabrics
======== # of Brocade switch fabrics
======== # of 3rd Party Arrays Integrated via OpenStack Cinder
======== # of ScaleIO Protection Domains

### VIPR PHYSICAL AND VIRTUAL ASSET CONFIGURATION

======== # of Virtual Arrays
======== # of Block and File Virtual Pools
======== # of Catalog Services to Customize
======== # of User Roles defined
======== # of Projects
======== # of Data Services Buckets
======== # of Object Virtual Pools
======== # of Data Stores
======== # of DS File Ingestions performed
======== # of hours for additional knowledge transfer (SA effort)
======== # of additional hours for testing to be faciliated

### VIPR DATA MIGRATION WITH PPME

=CHKINF= Select the level of EMC involvement for the data migration
=CHKELM= Planning and Design
=CHKELM= Implementation and Migration
=RADIO== Does the customer want to do the migration work themselves?
=RADIO== Will EMC provide onsite support? (EMC does not perform the actual migration work)
=SELECT= Choose the host-based migration tool to be used
Select
Host-based LVM
Open Migrator LM
PowerPath Migration Enabler (PPME)
=RADIO== Include ESX host migration via Storage vMotion?
=RADIO== Include second round of data gathering (for larger or long migration projects)?
=RADIO== Include Environment Collection Appliance (ECA)?
=CHKINF= Select Storage Arrays involved
=CHKELM= VNX or CLARiiON
=CHKELM= VMAX, DMX, or SYMM
=CHKELM= 3rd Party or Non-EMC Storage
=CHKELM= No Source Array
=CHKELM= XtremIO Cluster
======== # of existing physical hosts
======== # of existing ESX Servers (not Virtual Machines)
=RADIO== Swing frame required for migration?
======== Total # of source arrays involved in a migration
======== Total # of target arrays involved in a migration
=RADIO== Does the data migration include device-size changes?
======== % of servers requiring LUN size changes
======== Amount of source data to be migrated in TB
======== # of hosts to be migrated via PowerPath Migration Enabler by EMC
======== # of VMware Virtual Machines to Storage vMontion

### PLANNING AND DESIGN

======== # of source and target sites (total)
======== # of new physical hosts included in design
======== # of new ESX Servers in design
======== # of New Enterprise Directors
======== # of New Departmental Switches
======== # of new VNX Block storage arrays
======== % for Data Migration Complexity Factor
======== # of new Symmetrix storage arrays
======== # of VNX Block arrays to be upgraded
======== # of Symmetrix to be upgraded
======== # of XtremIO clusters
======== # of non-EMC storage arrays

### IMPLEMENTATION AND MIGRATION

=CHKINF= Include the Following Hardware Activites
=CHKELM= Remove Existing EMC Storage
=CHKELM= Relocate and Reinstall Existing EMC Storage
=RADIO== Include Data Erasure of Storage?
=RADIO== Include Additional BIN File work?
======== # of BIN Files to be designed and implemented
======== # of hours per BIN File for design and implementation
=RADIO== Include XtremIO clusters 2-brick or 4-brick configurations?
======== Amount of source data to be migrated in TB
======== % for Data Migration Complexity Factor
======== Total # of hosts (physical hosts & ESX Servers) to be migrated by EMC
======== # of new physical hosts included in design
======== # of new ESX Servers in design
=RADIO== Will the customer do the zoning work on the switches?
======== # of existing SAN fabrics
======== # of hosts to be booted from the SAN
=RADIO== Will the customer do the LUN or device allocation work on the storage?
======== # of new VNX Block storage arrays
======== # of VNX Block arrays to be upgraded
======== # of XtremIO clusters
======== # of XtremIO Bricks per cluster
======== # of hosts to be migrated via PowerPath Migration Enabler by EMC
=RADIO== Does the data migration include device-size changes?
======== % of servers requiring LUN size changes
======== # of VNX arrays to have data erased
======== Enter the Serial Number(s) of the Array(s)
======== # of Symmetrix storage to have data erased
======== Enter the Serial Number(s) of the Array(s)

### VIPR DATA SERVICE FOR COMMODITY FEATURES

=RADIO== Include Data Services for HDFS?
=RADIO== Include integration with Active Directory/LDAP?
=RADIO== Include Kerberos Authentication Mode for ViPR FS?
=RADIO== Include ViPR Content Address Storage (CAS) API Support?
=RADIO== Does a Watch4net platform exist on site that meets ViPR requirements?

### VIPR DATA SERVICE FOR COMMODITY SCOPE DETAILS

======== # of Commodity Storage Systems
======== # of Tenants defined
======== # of Hadoop Clusters
======== Total # of Hadoop Cluster Nodes (Where ViPR HDFS Clients are to be deployed)

### VIPR COMMODITY SYSTEM CONFIGURATION

======== # of Virtual Arrays
======== # of Object Virtual Pools
======== # of Projects
======== # of User Roles defined
======== # of Catalog Services to Customize
======== # of ViPR Commodity or ECS Systems Requiring CAS

### ECS APPLICANCE DESIGN & IMPLEMENTATION FEATURES

=RADIO== Include Data Services for HDFS?
=RADIO== Include integration with Active Directory/LDAP?
=RADIO== Include Kerberos Authentication Mode for ViPR FS?
=RADIO== Include ViPR Content Address Storage (CAS) API Support?
=RADIO== Does a Watch4net platform exist on site that meets ViPR requirements?

### ECS APPLICANCE DESIGN & IMPLEMENTATION SCOPE DETAILS

======== # of ECS systems containing Block (Block-only or Mixed Block-and-Unstructured)
======== # of ECS Unstructured systems
======== # of Tenants defined
======== # of Hadoop Clusters
======== Total # of Hadoop Cluster Nodes (Where ViPR HDFS Clients are to be deployed)

### ECS IN VIPR CONFIGURATION

======== # of Virtual Arrays
======== # of Block Virtual Pools
======== # of Object Virtual Pools
======== # of Projects
======== # of Data Services Buckets
======== # of User Roles defined
======== # of Catalog Services to Customize
======== # of ViPR Commodity or ECS Systems Requiring CAS

'''


generate_java(INPUT_ELEMENT)
print('=======================================')
