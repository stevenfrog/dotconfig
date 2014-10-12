#!/usr/bin/env python3

from frog_java_util import get_java_structure
import frog_util
import frog_xml_util
import frog_sql_util
import os

LS = os.linesep
JAVA_FILE = '''
/home/stevenfrog/TC_Assembly_2014/SRT_Phase_3_Pilot-Mozy_and_Xtrem_and_Vipr_Tabs/src/main/java/com/emc/gs/tools/srf/model/vipr/ViprFeature.java
/home/stevenfrog/TC_Assembly_2014/SRT_Phase_3_Pilot-Mozy_and_Xtrem_and_Vipr_Tabs/src/main/java/com/emc/gs/tools/srf/model/vipr/ViprScopeDetails.java
/home/stevenfrog/TC_Assembly_2014/SRT_Phase_3_Pilot-Mozy_and_Xtrem_and_Vipr_Tabs/src/main/java/com/emc/gs/tools/srf/model/vipr/ViprPhysicalAndVirtualAssetConf.java
/home/stevenfrog/TC_Assembly_2014/SRT_Phase_3_Pilot-Mozy_and_Xtrem_and_Vipr_Tabs/src/main/java/com/emc/gs/tools/srf/model/vipr/ViprPlanningDesignImpl.java

/home/stevenfrog/TC_Assembly_2014/SRT_Phase_3_Pilot-Mozy_and_Xtrem_and_Vipr_Tabs/src/main/java/com/emc/gs/tools/srf/model/vipr/ViprPlaningAndDesign.java
/home/stevenfrog/TC_Assembly_2014/SRT_Phase_3_Pilot-Mozy_and_Xtrem_and_Vipr_Tabs/src/main/java/com/emc/gs/tools/srf/model/vipr/ViprImplAndMigration.java
/home/stevenfrog/TC_Assembly_2014/SRT_Phase_3_Pilot-Mozy_and_Xtrem_and_Vipr_Tabs/src/main/java/com/emc/gs/tools/srf/model/vipr/ViprDataMigrationPPME.java

/home/stevenfrog/TC_Assembly_2014/SRT_Phase_3_Pilot-Mozy_and_Xtrem_and_Vipr_Tabs/src/main/java/com/emc/gs/tools/srf/model/vipr/ViprDSCommodityFeatures.java
/home/stevenfrog/TC_Assembly_2014/SRT_Phase_3_Pilot-Mozy_and_Xtrem_and_Vipr_Tabs/src/main/java/com/emc/gs/tools/srf/model/vipr/ViprDSCommodityScopeDetails.java
/home/stevenfrog/TC_Assembly_2014/SRT_Phase_3_Pilot-Mozy_and_Xtrem_and_Vipr_Tabs/src/main/java/com/emc/gs/tools/srf/model/vipr/ViprCommoditySysConf.java
/home/stevenfrog/TC_Assembly_2014/SRT_Phase_3_Pilot-Mozy_and_Xtrem_and_Vipr_Tabs/src/main/java/com/emc/gs/tools/srf/model/vipr/ViprDSCommodityServices.java

/home/stevenfrog/TC_Assembly_2014/SRT_Phase_3_Pilot-Mozy_and_Xtrem_and_Vipr_Tabs/src/main/java/com/emc/gs/tools/srf/model/vipr/ViprECSFeature.java
/home/stevenfrog/TC_Assembly_2014/SRT_Phase_3_Pilot-Mozy_and_Xtrem_and_Vipr_Tabs/src/main/java/com/emc/gs/tools/srf/model/vipr/ViprECSScopeDetails.java
/home/stevenfrog/TC_Assembly_2014/SRT_Phase_3_Pilot-Mozy_and_Xtrem_and_Vipr_Tabs/src/main/java/com/emc/gs/tools/srf/model/vipr/ViprECSConf.java
/home/stevenfrog/TC_Assembly_2014/SRT_Phase_3_Pilot-Mozy_and_Xtrem_and_Vipr_Tabs/src/main/java/com/emc/gs/tools/srf/model/vipr/ViprECSServices.java

/home/stevenfrog/TC_Assembly_2014/SRT_Phase_3_Pilot-Mozy_and_Xtrem_and_Vipr_Tabs/src/main/java/com/emc/gs/tools/srf/model/vipr/ViprRequestData.java
'''

for f in JAVA_FILE.splitlines():
     if not f:
         print('||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
         continue
     print()
     java_structure = get_java_structure(f)

     print('========= package =================')
     print(java_structure['package'])
     print()
     print('========= class ===================')
     print(java_structure['class'][1])
     print()
     print('========= fields ==================')
     frog_util.printAlignedArray(java_structure['fields'])
     print()
     print(frog_sql_util.generateCreateSQL(java_structure))
     print()
     print()



