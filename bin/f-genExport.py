#!/usr/bin/env python3

import frog_util

TEMPLATE_CHECKBOX_EXPORT = '''
    row = writeAnswer(contentStream, row, questionWidth, "%s",
        boolChk2String(%s.is%s()));
'''

TEMPLATE_RADIO_EXPORT = '''
    row = writeAnswer(contentStream, row, questionWidth, "%s",
        %s.get%s().toString());
'''

TEMPLATE_RADIO2_EXPORT = '''
    row = writeAnswer(contentStream, row, questionWidth, "%s",
        bool2StringNewOrExisting(%s.get%s()));
'''

TEMPLATE_NUM_EXPORT = '''
    row = writeAnswer(contentStream, row, questionWidth, "%s",
        int2String(%s.get%s()));
'''

TEMPLATE_CHKINF_EXPORT = '''
    row = writeFont(contentStream, "%s", ++row, 0, false);
    row = writeOptions(contentStream, get%sOptions(%s), row, questionWidth, 1, 180f);
'''

TEMPLATE_CHKELM_EXPORT = '''
        if (%s.is%s()) {
            options.add("%s");
        }
'''

TEMPLATE_GETOPTIONS_EXPORT = '''
    /**
     * Get %(type)s Options.
     *
     * @param %(param)s
     *            the %(param)s
     * @return the options list
     */
    private List<String> get%(type)sOptions(%(type)s %(param)s) {
        List<String> options = new ArrayList<String>();
        %(optionContent)s

        return options;
    }
'''



def generate_export(input_values):
    currentVar = 'XXX'
    optionContent = ''
    optionMethodName = ''
    for line in input_values.splitlines():
        line = line.strip()
        #line = line.replace('?', '')
        line = line.replace('&amp', '&')

        values = line.split('|')
        # remove useless white space
        for i in range(len(values)):
            values[i] = values[i].strip()

        if not values[0].startswith('=CHKELM=') and optionContent:
            print(TEMPLATE_GETOPTIONS_EXPORT.rstrip() % {'type': optionMethodName, 'param': currentVar, 'optionContent': optionContent})
            optionContent = ''
            optionMethodName = ''

        if line.startswith('###'):
            print('########################################')
            print(line)
            print('########################################')
            print()
        elif line.startswith('======== PACKAGE'):
            print('========================================')
            print(line)
            line = line[len('======== PACKAGE'):]
            package = line.split(',')
            lastPt = package[0].rfind('.') + 1
            currentVar = package[0][lastPt:].strip()
        elif line.startswith('========'):
            print('========================================')
            print(line)
        elif values[0].startswith('=CHECK=='):
            valFirstCharUpper = values[1][0].upper() + values[1][1:]
            print((TEMPLATE_CHECKBOX_EXPORT % (values[3], currentVar, valFirstCharUpper)).rstrip())
        elif values[0].startswith('=RADIO=='):
            valFirstCharUpper = values[1][0].upper() + values[1][1:]
            if values[3].find('New or Existing') > -1:
                print((TEMPLATE_RADIO2_EXPORT % (values[3], currentVar, valFirstCharUpper)).rstrip())
            else:
                print((TEMPLATE_RADIO_EXPORT % (values[3], currentVar, valFirstCharUpper)).rstrip())
        elif values[0].startswith('=NUM===='):
            valCapitaled = values[1][0].upper() + values[1][1:]
            print((TEMPLATE_NUM_EXPORT % (values[3], currentVar, valCapitaled)).rstrip())
        elif values[0].startswith('=CHKINF='):
            optionMethodName = currentVar[0].upper() + currentVar[1:]
            print(TEMPLATE_CHKINF_EXPORT % (values[3], optionMethodName, currentVar))
        elif values[0].startswith('=CHKELM='):
            valCapitaled = values[1][0].upper() + values[1][1:]
            optionContent += (TEMPLATE_CHKELM_EXPORT % (currentVar, valCapitaled, values[3])).rstrip()




INPUT_BLOCK = '''
######## UNIFIED - Software Features (Block Only)


======== PACKAGE: serviceRequest.coreUnifiedRequestData.feature.serviceBundles, core-unified-feature
=NUM====  |  fastLunArrays         |  fast-lun-array-num              |  How many arrays?                                                                                                                                         
=NUM====  |  fastLunLuns           |  fast-lun-lun-num                |  How many luns?                                                                                                                                           
=NUM====  |  mirrorViewArrays      |  mirror-view-array-num           |  How many arrays?                                                                                                                                         
=NUM====  |  mirrorViewHosts       |  mirror-view-host-num            |  How many hosts?                                                                                                                                          
=NUM====  |  mirrorViewRemote      |  mirror-view-remote-num          |  How many remote mirrors?                                                                                                                                 
=NUM====  |  mirrorViewImages      |  mirror-view-image-num           |  How many secondary images created?                                                                                                                       
=NUM====  |  mirrorViewGroups      |  mirror-view-group-num           |  How many consistency groups?                                                                                                                             
=NUM====  |  sanCopyArrays         |  san-copy-array-num              |  How many arrays?                                                                                                                                         
=NUM====  |  sanCopyHosts          |  san-copy-host-num               |  How many hosts?                                                                                                                                          
=NUM====  |  sanCopyRemote         |  san-copy-remote-num             |  How many snapshots?                                                                                                                                      
=NUM====  |  sanCopyImages         |  san-copy-image-num              |  How many consistency groups?                                                                                                                             
=CHECK==  |  sanCopyGroups         |  san-copy-groups-chk             |  Include Snapview for the incremental San Copy Feature?                                                                                                   
=NUM====  |  snapViewArrays        |  snap-view-arrays-num            |  How many arrays?                                                                                                                                         
=NUM====  |  snapViewHosts         |  snap-view-host-num              |  How many hosts?                                                                                                                                          
=NUM====  |  snapViewSnapshots     |  snap-view-snapshot-num          |  How many snapshots?                                                                                                                                      
=NUM====  |  snapViewGroups        |  snap-view-group-num             |  How many consistency groups?                                                                                                                             
=CHECK==  |  snapViewFeature       |  is-snap-view-feature-chk        |  Include Snapview for the incremental San Copy Feature?                                                                                                   
=NUM====  |  vnxArrays             |  vnx-array-num                   |  How many arrays?                                                                                                                                         
=NUM====  |  vnxHosts              |  vnx-host-num                    |  How many hosts?                                                                                                                                          
=NUM====  |  vnxSnapshots          |  vnx-snapshot-num                |  How many snapshots?                                                                                                                                      
=NUM====  |  vnxGroups             |  vnx-group-num                   |  How many consistency groups?                                                                                                                             

======== MULTISELECT
======== PACKAGE: serviceRequest.coreUnifiedRequestData.feature.serviceBundles, core-unified-feature
=CHKINF=  |  xxxxx                 |  xxxxx                           |  Add Unified Service Bundles                                                                                                                              
=CHKELM=  |  datProAdv             |  is-dat-pro-adv-chk              |  Data Protection Advisor                                                                                                                                  
=CHKELM=  |  fastLunMig            |  is-fast-lun-mig-chk             |  FAST LUN Migrator                                                                                                                                        
=CHKELM=  |  mirrorView            |  is-mirror-view-chk              |  MirrorView                                                                                                                                               
=CHKELM=  |  quaSerMag             |  is-qua-ser-mag-chk              |  Quality of Service Manager - Installation &amp Overview                                                                                                  
=CHKELM=  |  replMag               |  is-repl-mag-chk                 |  Replication Manager                                                                                                                                      
=CHKELM=  |  recoverPt             |  is-recover-pt-chk               |  RecoverPoint                                                                                                                                             
=CHKELM=  |  sanCopy               |  is-san-copy-chk                 |  SAN Copy                                                                                                                                                 
=CHKELM=  |  snapView              |  is-snap-view-chk                |  SnapView                                                                                                                                                 
=CHKELM=  |  vnxSnapshot           |  is-vnx-snapshot-chk             |  VNX Snapshots                                                                                                                                            
=CHKELM=  |  virProvision          |  is-vir-provision-chk            |  Virtual Provisioning                                                                                                                                     
=CHKELM=  |  uniAnalyzer           |  is-uni-analyzer-chk             |  Unisphere Analyzer - Installation &amp Overview                                                                                                          
=CHKELM=  |  uniRemote             |  is-uni-remote-chk               |  Unisphere Remote                                                                                                                                         

######## UNIFIED - Upgrades or Conversations


======== PACKAGE: serviceRequest.coreUnifiedRequestData.upgrade, core-unified-upgrade
=CHECK==  |  conversionsChk        |  is-conversions-chk              |  Unified Conversions                                                                                                                                      

======== PACKAGE: serviceRequest.coreUnifiedRequestData.upgrade.conversion, core-unified-upgrade
=NUM====  |  numFileUnified        |  num-file-unified-num            |  How many VNX systems for conversion?                                                                                                                     
=NUM====  |  numBlockUnified       |  num-block-unified-num           |  How many VNX systems for conversion?                                                                                                                     
=CHECK==  |  dpeSpeRerackChk       |  is-dpe-spe-rerack-chk           |  Will EMC personnel re-rack existing customer hardware in the cabinet to accommodate the Unified Data-in-Place conversion?                                
=NUM====  |  numDpeSpe             |  num-dpe-spe-num                 |  Number of storage arrays that will have SP or DPE-to-SPE conversions?                                                                                    
=CHECK==  |  spRerackChk           |  is-sp-rerack-chk                |  Will EMC personnel re-rack existing customer hardware in the cabinet to accommodate the Unified Data-in-Place conversion?                                
=NUM====  |  numSp                 |  num-sp-num                      |  Number of storage arrays that will have SP or DPE-to-SPE conversions?                                                                                    

======== PACKAGE: serviceRequest.coreUnifiedRequestData.upgrade, core-unified-upgrade
=CHECK==  |  upgradesChk           |  is-upgrades-chk                 |  Unified Upgrades                                                                                                                                         

======== PACKAGE: serviceRequest.coreUnifiedRequestData.upgrade.upgrade, core-unified-upgrade
=CHECK==  |  controlStationChk     |  is-control-station-chk          |  Secondary Control Station?                                                                                                                               
=NUM====  |  numControlStation     |  num-control-station-num         |  How many control stations?                                                                                                                               
=CHECK==  |  dataMoverChk          |  is-data-mover-chk               |  Data Movers for preexisting Unified systems?                                                                                                             
=NUM====  |  numFileBlock          |  num-file-block-num              |  Number of VNX Unified File &amp Block Storage Systems?                                                                                                   
=NUM====  |  numDataMover          |  num-data-mover-num              |  Number of Data Movers?                                                                                                                                   
=CHECK==  |  spUpgradeChk          |  is-sp-upgrade-chk               |  SP Memory Upgrade?                                                                                                                                       
=NUM====  |  numSpUpgrade          |  num-sp-upgrade-num              |  Number of Unified storage arrays that will have SP memory upgrades?                                                                                      

======== MULTISELECT
======== PACKAGE: serviceRequest.coreUnifiedRequestData.upgrade.conversion, core-unified-upgrade
=CHKINF=  |  xxxxx                 |  xxxxx                           |  Pull down selection and chose one                                                                                                                        
=CHKELM=  |  fileUnifiedChk        |  is-file-unified-chk             |  File to Unified                                                                                                                                          
=CHKELM=  |  blockUnifiedChk       |  is-block-unified-chk            |  Block to Unified                                                                                                                                         
=CHKELM=  |  dpeSpeChk             |  is-dpe-spe-chk                  |  Data-In-Place DPE-to-SPE Conversion                                                                                                                      
=CHKELM=  |  spChk                 |  is-sp-chk                       |  Data-In-Place SP conversion                                                                                                                              


######## UNIFIED - Implementation for ESI with SAP LVM


======== PACKAGE: serviceRequest.coreUnifiedRequestData.esi, core-unified-esi
=NUM====  |  numLvmInstance        |  num-lvm-instance-num            |  Number of ESI for SAP LVM Instances being installed and configured?                                                                                      
=NUM====  |  numSapSystem          |  num-sap-system-num              |  Number of SAP Systems?                                                                                                                                   
=NUM====  |  numLvmHosts           |  num-lvm-host-num                |  Number of SAP LVM Managed Hosts?                                                                                                                         
=NUM====  |  numEmcStorage         |  num-emc-storage-num             |  Number of EMC Storage Systems?                                                                                                                           
                                                                                                              




'''

generate_export(INPUT_BLOCK)
print('=======================================')
