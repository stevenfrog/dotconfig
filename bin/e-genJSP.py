#!/usr/bin/env python3

import frog_util
import os

LS = os.linesep
MAX_CHECKBOX_ONE_LINE = 2

TEMPLATE_RADIO = '''
    <p>
      <label>
        <span class="tip" data-tooltips="infoTip"></span>
        %(label)s
      </label>
      <span class="sep">:</span>
      <input type="radio" name="%(prefix)s-%(id)s" id="%(prefix)s-%(id)s-true" data-ng-value="true"
          data-ng-model="%(package)s.%(var_name)s" />
      <label class="rad-lbl rad-lbl-first" for="%(prefix)s-%(id)s-true">Yes</label>
      <input type="radio" name="%(prefix)s-%(id)s" id="%(prefix)s-%(id)s-false" data-ng-value="false"
          data-ng-model="%(package)s.%(var_name)s" />
      <label class="rad-lbl" for="%(prefix)s-%(id)s-false">No</label>
    </p>
'''


TEMPLATE_NUM = '''
    <p>
      <label for="%(prefix)s-%(id)s-num">
        <span class="tip"></span>
        %(label)s
      </label>
      <span class="sep">:</span>
      <input type="text" class="text" maxlength="9" id="%(prefix)s-%(id)s-num"
          data-ng-model="%(package)s.%(var_name)s" data-allownumber />
    </p>
'''

TEMPLATE_CHECKBOX = '''
    <p>
      <label>
        <span class="tip" data-tooltips="infoTip"></span>
        %(label)s
      </label>
      <span class="sep">:</span>
      <input type="checkbox" id="%(prefix)s-%(id)s-chk"
        data-ng-model="%(package)s.%(var_name)s" />
      <label class="chk-lbl" for="%(prefix)s-%(id)s-chk">Yes</label>
    </p>
'''


TEMPLATE_CHECKBOX_ELE = '''
          <input type="checkbox" id="%(prefix)s-%(id)s-chk" data-ng-model="%(package)s.%(var_name)s" />
          <label class="chk-lbl" for="%(prefix)s-%(id)s-chk">%(label)s</label>
'''


TEMPLATE_CHECKBOX_LAST_POS = '''
          <input type="checkbox" id="%(prefix)s-%(id)s-chk" data-ng-model="%(package)s.%(var_name)s" />
          <label class="chk-lbl chk-lbl-last" for="%(prefix)s-%(id)s-chk">%(label)s</label>
        </div>
'''

TEMPLATE_SELECT_CHECKBOXES = '''
      <div class="check-set check-set-inline">
        <p>
          <label>
            <span class="tip"></span>
            %(label)s
          </label>
          <span class="sep">:</span>
        </p>
        %(content)s
      </div>
'''




INPUT_TEMP = '''
######## UNIFIED - BLOCK


======== PACKAGE: serviceRequest.coreUnifiedRequestData.block, core-unified-block
=CHECK==  |  planDesign            |  plan-design-chk                 |  Planning and Design                                                                                                                                      
=CHECK==  |  impl                  |  impl-chk                        |  Implementation                                                                                                                                           
=NUM====  |  knowledgeTrHours      |  knowledge-tr-hour-num           |  # hours of knowledge transfer                                                                                                                            
=NUM====  |  newVnxBlock           |  new-vnx-block-num               |  # of new VNX arrays to be installed                                                                                                                      
=NUM====  |  newVnxBlockStorage    |  new-vnx-block-storage-num       |  Number of new LUNs to create on NEW VNX Block storage arrays                                                                                             
=NUM====  |  existVnxBlockStorage  |  exist-vnx-block-storage-num     |  Number of new LUNs for Existing VNX Block storage arrays                                                                                                 
=CHECK==  |  iscsi                 |  iscsi-chk                       |  ISCSI?                                                                                                                                                   
=CHECK==  |  sapHana               |  is-sap-hana-chk                 |  Sap Hana Required                                                                                                                                        
=CHECK==  |  sanSwitch             |  is-san-switch-chk               |  Include San Switch or Director Installation (IDE role)                                                                                                   
=CHECK==  |  vnxFastVp             |  is-vnx-fast-vp-chk              |  Include VNX FAST VP and / or FAST Cache                                                                                                                  
=NUM====  |  vnxFast               |  vnx-fast-num                    |  Number of VNX existing or new arrays considered for FAST?                                                                                                
=NUM====  |  storagePool           |  storage-pool-num                |  Number of storage pools to be created?                                                                                                                   
=NUM====  |  vnxVirtual            |  vnx-virtual-num                 |  Number of VNX Virtual Provisioning thin LUNs for Block to be created                                                                                     
=NUM====  |  storageGroup          |  storage-group-num               |  Number of Storage groups created for this engagement                                                                                                     
=CHECK==  |  watch4net             |  is-watch4net-chk                |  Include Watch4net for VNX Monitoring and Reporting Software                                                                                              
=CHECK==  |  storageAnalytics      |  is-storage-analytics-chk        |  Include Storage Analytics                                                                                                                                

======== PACKAGE: serviceRequest.coreUnifiedRequestData.block.serviceBundles, core-unified-block
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

======== PACKAGE: serviceRequest.coreUnifiedRequestData.block, core-unified-block
=CHECK==  |  dialhome              |  is-dialhome-chk                 |  Include Dialhome Activties                                                                                                                               
=CHECK==  |  hardwareInstall       |  is-hardware-install-chk         |  Include Hardware Install activities                                                                                                                      
=CHECK==  |  powerPath             |  is-power-path-chk               |  Include PowerPath Installation                                                                                                                           
=CHECK==  |  eSXHosts              |  is-esx-hosts-chk                |  Include PowerPath VE installation for ESX Hosts                                                                                                          
=CHECK==  |  deployment            |  is-deployment-chk               |  Include Virtual Storage Integrator Deployment                                                                                                            
=CHECK==  |  hardwareDeInstall     |  is-hardware-de-install-chk      |  Hardware de-install options                                                                                                                              
=CHECK==  |  deInstallHardware     |  is-de-install-hardware-chk      |  De-Install Hardware                                                                                                                                      
=CHECK==  |  crateShipHardware     |  is-crate-ship-hardware-chk      |  Crate and Ship Hardwar                                                                                                                                   

======== MULTISELECT
======== PACKAGE: serviceRequest.coreUnifiedRequestData.block.serviceBundles, core-unified-block
=CHKINF=  |  xxxxx                 |  xxxxx                           |  Add Unified Service Bundles                                                                                                                              
=CHKELM=  |  datProAdv             |  is-dat-pro-adv-chk              |  Data Protection Advisor                                                                                                                                  
=CHKELM=  |  fastLunMig            |  is-fast-lun-mig-chk             |  FAST LUN Migrator                                                                                                                                        
=CHKELM=  |  mirrorView            |  is-mirror-view-chk              |  MirrorView                                                                                                                                               
=CHKELM=  |  quaSerMag             |  is-qua-ser-mag-chk              |  Quality of Service Manager - Installation & Overview                                                                                                     
=CHKELM=  |  replMag               |  is-repl-mag-chk                 |  Replication Manager                                                                                                                                      
=CHKELM=  |  recoverPt             |  is-recover-pt-chk               |  RecoverPoint                                                                                                                                             
=CHKELM=  |  sanCopy               |  is-san-copy-chk                 |  SAN Copy                                                                                                                                                 
=CHKELM=  |  snapView              |  is-snap-view-chk                |  SnapView                                                                                                                                                 
=CHKELM=  |  vnxSnapshot           |  is-vnx-snapshot-chk             |  VNX Snapshots                                                                                                                                            
=CHKELM=  |  virProvision          |  is-vir-provision-chk            |  Virtual Provisioning                                                                                                                                     
=CHKELM=  |  uniAnalyzer           |  is-uni-analyzer-chk             |  Unisphere Analyzer - Installation & Overview                                                                                                             
=CHKELM=  |  uniRemote             |  is-uni-remote-chk               |  Unisphere Remote                                                                                                                                         


======== MULTISELECT
======== PACKAGE: serviceRequest.coreUnifiedRequestData.block.sanNetConn, core-unified-block
=CHKINF=  |  xxxxx                 |  xxxxx                           |  Select SAN Storage Network connectivity options                                                                                                          
=CHKELM=  |  fibreChannel          |  is-fibre-channel-chk            |  Fibre Channel                                                                                                                                            
=CHKELM=  |  fcoe                  |  is-fcoe-chk                     |  Fibre Channel over Ethernet (FCoE)                                                                                                                       
=CHKELM=  |  sanIscsi              |  is-san-iscsi-chk                |  iSCSI                                                                                                                                                    
=CHKELM=  |  sanExt                |  is-san-ext-chk                  |  SAN Extension                                                                                                                                            
=CHKELM=  |  vsan                  |  is-vsan-chk                     |  Virtual SANs - VSAN/LSAN                                                                                                                                 
=CHKELM=  |  fcRouting             |  is-fc-routing-chk               |  FC Routing       

'''


input_values = INPUT_TEMP.replace('_', '-')
PACKAGE = ''
PREFIX = ''
checkbox_content = ''
checkbox_label = ''
checkbox_index = 0

print("======================================================")
print()
print(input_values)
print()
print("======================================================")

for line in input_values.splitlines():
    line = line.strip()
    if len(line) == 0:
        continue
    if line.startswith('PACKAGE'):
        PACKAGE = line[10:]
        continue
    if line.startswith('PREFIX'):
        PREFIX = line[10:]
        continue

    values = line.split('|')
    # remove useless white space
    for i in range(len(values)):
        values[i] = values[i].strip()

    if not values[0].startswith('=CHKELM=') and checkbox_content:
        # Add </div> for end line of checkboxes
        if not checkbox_content.rstrip().endswith('</div>'):
            checkbox_content += LS + '        </div>'

        print(TEMPLATE_SELECT_CHECKBOXES.rstrip() % {'content': checkbox_content, 'label': checkbox_label})
        checkbox_content = ''
        checkbox_label = ''
        checkbox_index = 0

    if values[1].endswith('-selected'):
        values[1] = values[1][:-9]
    fx_vals = {'package': PACKAGE, 'prefix': PREFIX, 'var_name': values[1], 'id': values[2], 'label': values[3]}

    if values[0].startswith('=NUM===='):
        if fx_vals['id'].endswith('s'):
            fx_vals['id'] = fx_vals['id'][:-1]
        if fx_vals['id'].endswith('-num'):
            fx_vals['id'] = fx_vals['id'][:-4]
        print(TEMPLATE_NUM.rstrip() % fx_vals)
    elif values[0].startswith('=RADIO=='):
        print(TEMPLATE_RADIO.rstrip() % fx_vals)
    elif values[0].startswith('=CHECK=='):
        print(TEMPLATE_CHECKBOX.rstrip() % fx_vals)
    elif values[0].startswith('=CHKINF='):
        checkbox_label = values[3]
    elif values[0].startswith('=CHKELM='):
        if checkbox_index == 0:
            checkbox_content += LS + '        <div>'

        checkbox_index += 1
        if checkbox_index % MAX_CHECKBOX_ONE_LINE == 0:
            checkbox_content += TEMPLATE_CHECKBOX_LAST_POS.rstrip() % fx_vals
            checkbox_index = 0
        else:
            checkbox_content += TEMPLATE_CHECKBOX_ELE.rstrip() % fx_vals

        checkbox_content += LS

