#Logica para la generacion de sentencias para creacion de zonas brocade

def wwnparse(wwn):
    lista_wwn = wwn.split()
    lista_wwn_result = list()
    for wwn_lpar in lista_wwn:
        print(wwn_lpar)
        #wwn_lpar = line.rstrip() 
        wwn = wwn_lpar[0:2]+":"+wwn_lpar[2:4]+":"+wwn_lpar[4:6]+":"+wwn_lpar[6:8]+":"+wwn_lpar[8:10]+":"+wwn_lpar[10:12]+":"+wwn_lpar[12:14]+":"+wwn_lpar[14:16]
        lista_wwn_result.append(wwn)
    wwn1 = lista_wwn_result[0]
    wwn2 = lista_wwn_result[1]
    wwn3 = lista_wwn_result[2]
    wwn4 = lista_wwn_result[3]
    return wwn1, wwn2, wwn3, wwn4

def wwnparsepure(wwn):
    lista_wwn = wwn.split()
    lista_wwn_result = list()
    for wwn_lpar in lista_wwn:
        wwn = wwn_lpar[0:2]+":"+wwn_lpar[2:4]+":"+wwn_lpar[4:6]+":"+wwn_lpar[6:8]+":"+wwn_lpar[8:10]+":"+wwn_lpar[10:12]+":"+wwn_lpar[12:14]+":"+wwn_lpar[14:16]
        lista_wwn_result.append(wwn)
    wwn1 = lista_wwn_result[0]
    wwn2 = lista_wwn_result[1]
    return wwn1, wwn2

# Generacion de Alias para POWER Lpars
def lpar_alias(hostname, vios):
    hostname = hostname.upper()
    if vios == 'viochp11_12':
        lpar_alias1 = "VIOCHP11_" + hostname + "_FCSV0"
        lpar_alias2 = "VIOCHP11_" + hostname + "_FCSV1"
        lpar_alias3 = "VIOCHP12_" + hostname + "_FCSV0"
        lpar_alias4 = "VIOCHP12_" + hostname + "_FCSV1"
        return lpar_alias1, lpar_alias2, lpar_alias3, lpar_alias4
    if vios == 'violmp11_12':
        lpar_alias1 = "VIOLMP11_" + hostname + "_FCSV0"
        lpar_alias2 = "VIOLMP11_" + hostname + "_FCSV1"
        lpar_alias3 = "VIOLMP12_" + hostname + "_FCSV0"
        lpar_alias4 = "VIOLMP12_" + hostname + "_FCSV1"
        return lpar_alias1, lpar_alias2, lpar_alias3, lpar_alias4
    if vios == 'viochp08_09':
        lpar_alias1 = "VIOCHP08_" + hostname + "_FCSV0"
        lpar_alias2 = "VIOCHP08_" + hostname + "_FCSV1"
        lpar_alias3 = "VIOCHP09_" + hostname + "_FCSV0"
        lpar_alias4 = "VIOCHP09_" + hostname + "_FCSV1"
        return lpar_alias1, lpar_alias2, lpar_alias3, lpar_alias4
    if vios == 'violmp08_09':
        lpar_alias1 = "VIOLMP08_" + hostname + "_FCSV0"
        lpar_alias2 = "VIOLMP08_" + hostname + "_FCSV1"
        lpar_alias3 = "VIOLMP09_" + hostname + "_FCSV0"
        lpar_alias4 = "VIOLMP09_" + hostname + "_FCSV1"
        return lpar_alias1, lpar_alias2, lpar_alias3, lpar_alias4

# Generacion de Alias para PUREFLEX Lpars
def alias_pure(hostname, vios):
    hostname = hostname.upper()
    if vios == 'pvioschp01':
        lpar_alias1 = "PVIOSCHP01_" + hostname + "_FCSV0"
        lpar_alias2 = "PVIOSCHP01_" + hostname + "_FCSV1"
        return lpar_alias1, lpar_alias2
    if vios == 'pvioschd01':
        lpar_alias1 = "PVIOSCHD01_" + hostname + "_FCSV0"
        lpar_alias2 = "PVIOSCHD01_" + hostname + "_FCSV1"
        return lpar_alias1, lpar_alias2
    if vios == 'pvioschd03':
        lpar_alias1 = "PVIOSCHD03_" + hostname + "_FCSV0"
        lpar_alias2 = "PVIOSCHD03_" + hostname + "_FCSV1"
        return lpar_alias1, lpar_alias2
    if vios == 'pvioslmp01':
        lpar_alias1 = "PVIOSLMP01_" + hostname + "_FCSV0"
        lpar_alias2 = "PVIOSLMP01_" + hostname + "_FCSV1"
        return lpar_alias1, lpar_alias2
    if vios == 'pvioslmd01':
        lpar_alias1 = "PVIOSLMD01_" + hostname + "_FCSV0"
        lpar_alias2 = "PVIOSLMD01_" + hostname + "_FCSV1"
        return lpar_alias1, lpar_alias2
    if vios == 'pvioslmd03':
        lpar_alias1 = "PVIOSLMD03_" + hostname + "_FCSV0"
        lpar_alias2 = "PVIOSLMD03_" + hostname + "_FCSV1"
        return lpar_alias1, lpar_alias2
    if vios == 'pvioslmd05':
        lpar_alias1 = "PVIOSLMD05_" + hostname + "_FCSV0"
        lpar_alias2 = "PVIOSLMD05_" + hostname + "_FCSV1"
        return lpar_alias1, lpar_alias2

## Generacion de ZONAS para Power
def zonename1(lpar_alias):
    if "VIOCHP11_" in lpar_alias:
        vsp_port_vios1_1 = "VSP6456_1A"
        zone_vios1_fab1 = lpar_alias + "_" +vsp_port_vios1_1
        fabric1 = "P_Fabric1"
        return zone_vios1_fab1,vsp_port_vios1_1,fabric1
    elif "VIOLMP11_" in lpar_alias:
        vsp_port_vios1_1 = "VSP6547_AA"
        zone_vios1_fab1 = lpar_alias + "_" +vsp_port_vios1_1
        fabric1 = "P_Fabric1"
        return zone_vios1_fab1,vsp_port_vios1_1,fabric1
    elif "VIOCHP08_" in lpar_alias:
        vsp_port_vios1_1 = "VSP6456_9A"
        zone_vios1_fab1 = lpar_alias + "_" +vsp_port_vios1_1
        fabric1 = "P_Fabric1"
        return zone_vios1_fab1,vsp_port_vios1_1,fabric1
    elif "VIOLMP08_" in lpar_alias:
        vsp_port_vios1_1 = "VSP6547_9A"
        zone_vios1_fab1 = lpar_alias + "_" +vsp_port_vios1_1
        fabric1 = "P_Fabric1"
        return zone_vios1_fab1,vsp_port_vios1_1,fabric1

def zonename2(lpar_alias):    
    if "VIOCHP11_" in lpar_alias:
        vsp_port_vios1_2 = "VSP6456_1C"
        zone_vios1_fab2 = lpar_alias + "_" +vsp_port_vios1_2
        fabric2 = "P_Fabric2"
        return zone_vios1_fab2,vsp_port_vios1_2,fabric2            
    elif "VIOLMP11_" in lpar_alias:
        vsp_port_vios1_2 = "VSP6547_1C"
        zone_vios1_fab2 = lpar_alias + "_" +vsp_port_vios1_2
        fabric2 = "P_Fabric2"
        return zone_vios1_fab2,vsp_port_vios1_2,fabric2            
    elif "VIOCHP08_" in lpar_alias:
        vsp_port_vios1_2 = "VSP6456_2C"
        zone_vios1_fab2 = lpar_alias + "_" +vsp_port_vios1_2
        fabric2 = "P_Fabric2"
        return zone_vios1_fab2,vsp_port_vios1_2,fabric2            
    elif "VIOLMP08_" in lpar_alias:
        vsp_port_vios1_2 = "VSP6547_2C"
        zone_vios1_fab2 = lpar_alias + "_" +vsp_port_vios1_2
        fabric2 = "P_Fabric2"
        return zone_vios1_fab2,vsp_port_vios1_2,fabric2            

def zonename3(lpar_alias):    
    if "VIOCHP12_" in lpar_alias:
        vsp_port_vios2_1 = "VSP6456_AA"
        zone_vios2_fab1 = lpar_alias + "_" +vsp_port_vios2_1
        return zone_vios2_fab1,vsp_port_vios2_1
    elif "VIOLMP12_" in lpar_alias:
        vsp_port_vios2_1 = "VSP6547_1A"
        zone_vios2_fab1 = lpar_alias + "_" +vsp_port_vios2_1
        return zone_vios2_fab1,vsp_port_vios2_1
    elif "VIOCHP09_" in lpar_alias:
        vsp_port_vios2_1 = "VSP6456_GB"
        zone_vios2_fab1 = lpar_alias + "_" +vsp_port_vios2_1
        return zone_vios2_fab1,vsp_port_vios2_1
    elif "VIOLMP09_" in lpar_alias:
        vsp_port_vios2_1 = "VSP6547_GB"
        zone_vios2_fab1 = lpar_alias + "_" +vsp_port_vios2_1
        return zone_vios2_fab1,vsp_port_vios2_1

def zonename4(lpar_alias):    
    if "VIOCHP12_" in lpar_alias:
        vsp_port_vios2_2 = "VSP6456_AC"
        zone_vios2_fab2 = lpar_alias + "_" +vsp_port_vios2_2
        return zone_vios2_fab2,vsp_port_vios2_2
    if "VIOLMP12_" in lpar_alias:
        vsp_port_vios2_2 = "VSP6547_AC"
        zone_vios2_fab2 = lpar_alias + "_" +vsp_port_vios2_2
        return zone_vios2_fab2,vsp_port_vios2_2
    if "VIOCHP09_" in lpar_alias:
        vsp_port_vios2_2 = "VSP6456_FD"
        zone_vios2_fab2 = lpar_alias + "_" +vsp_port_vios2_2
        return zone_vios2_fab2,vsp_port_vios2_2
    if "VIOLMP09_" in lpar_alias:
        vsp_port_vios2_2 = "VSP6547_FD"
        zone_vios2_fab2 = lpar_alias + "_" +vsp_port_vios2_2
        return zone_vios2_fab2,vsp_port_vios2_2

def zonepure1(lpar_alias):
    if "PVIOSCHP01_" in lpar_alias:
        vsp_port_vios1_1 = "VSP6456_EB"
        zone_vios1_fab1 = lpar_alias + "_" +vsp_port_vios1_1
        fabric1 = "P_Fabric1"
        return zone_vios1_fab1,vsp_port_vios1_1,fabric1
    elif "PVIOSCHD01_" in lpar_alias:
        vsp_port_vios1_1 = "VSP6456_EB"
        zone_vios1_fab1 = lpar_alias + "_" +vsp_port_vios1_1
        fabric1 = "P_Fabric1"
        return zone_vios1_fab1,vsp_port_vios1_1,fabric1
    elif "PVIOSCHD03_" in lpar_alias:
        vsp_port_vios1_1 = "VSP6456_EB"
        zone_vios1_fab1 = lpar_alias + "_" +vsp_port_vios1_1
        fabric1 = "P_Fabric1"
        return zone_vios1_fab1,vsp_port_vios1_1,fabric1
    elif "PVIOSCHD03_" in lpar_alias:
        vsp_port_vios1_1 = "VSP6456_EB"
        zone_vios1_fab1 = lpar_alias + "_" +vsp_port_vios1_1
        fabric1 = "P_Fabric1"
        return zone_vios1_fab1,vsp_port_vios1_1,fabric1
    elif "PVIOSLMP01_" in lpar_alias:
        vsp_port_vios1_1 = "VSP6547_XXXXX"
        zone_vios1_fab1 = lpar_alias + "_" +vsp_port_vios1_1
        fabric1 = "P_Fabric1"
        return zone_vios1_fab1,vsp_port_vios1_1,fabric1
    elif "PVIOSLMD01_" in lpar_alias:
        vsp_port_vios1_1 = "VSP6547_XXXXX"
        zone_vios1_fab1 = lpar_alias + "_" +vsp_port_vios1_1
        fabric1 = "P_Fabric1"
        return zone_vios1_fab1,vsp_port_vios1_1,fabric1
    elif "PVIOSLMD03_" in lpar_alias:
        vsp_port_vios1_1 = "VSP6547_XXXXX"
        zone_vios1_fab1 = lpar_alias + "_" +vsp_port_vios1_1
        fabric1 = "P_Fabric1"
        return zone_vios1_fab1,vsp_port_vios1_1,fabric1
    elif "PVIOSLMD05_" in lpar_alias:
        vsp_port_vios1_1 = "VSP6547_XXXXX"
        zone_vios1_fab1 = lpar_alias + "_" +vsp_port_vios1_1
        fabric1 = "P_Fabric1"
        return zone_vios1_fab1,vsp_port_vios1_1,fabric1
    elif "PVIOSLMD05_" in lpar_alias:
        vsp_port_vios1_1 = "VSP6547_XXXXX"
        zone_vios1_fab1 = lpar_alias + "_" +vsp_port_vios1_1
        fabric1 = "P_Fabric1"
        return zone_vios1_fab1,vsp_port_vios1_1,fabric1


def zonepure2(lpar_alias):
    if "PVIOSCHP01_" in lpar_alias:
        vsp_port_vios1_2 = "VSP6456_3D"
        zone_vios1_fab2 = lpar_alias + "_" +vsp_port_vios1_2
        fabric2 = "P_Fabric2"
        return zone_vios1_fab2,vsp_port_vios1_2,fabric2            
    elif "PVIOSCHD01_" in lpar_alias:
        vsp_port_vios1_2 = "VSP6456_3D"
        zone_vios1_fab2 = lpar_alias + "_" +vsp_port_vios1_2
        fabric2 = "P_Fabric2"
        return zone_vios1_fab2,vsp_port_vios1_2,fabric2            
    elif "PVIOSCHD03_" in lpar_alias:
        vsp_port_vios1_2 = "VSP6456_3D"
        zone_vios1_fab2 = lpar_alias + "_" +vsp_port_vios1_2
        fabric2 = "P_Fabric2"
        return zone_vios1_fab2,vsp_port_vios1_2,fabric2            
    elif "PVIOSLMP01_" in lpar_alias:
        vsp_port_vios1_2 = "VSP6547_XXXXX"
        zone_vios1_fab2 = lpar_alias + "_" +vsp_port_vios1_2
        fabric2 = "P_Fabric2"
        return zone_vios1_fab2,vsp_port_vios1_2,fabric2 
    elif "PVIOSLMD01_" in lpar_alias:
        vsp_port_vios1_2 = "VSP6547_XXXXX"
        zone_vios1_fab2 = lpar_alias + "_" +vsp_port_vios1_2
        fabric2 = "P_Fabric2"
        return zone_vios1_fab2,vsp_port_vios1_2,fabric2 
    elif "PVIOSLMD03_" in lpar_alias:
        vsp_port_vios1_2 = "VSP6547_XXXXX"
        zone_vios1_fab2 = lpar_alias + "_" +vsp_port_vios1_2
        fabric2 = "P_Fabric2"
        return zone_vios1_fab2,vsp_port_vios1_2,fabric2 
    elif "PVIOSLMD05_" in lpar_alias:
        vsp_port_vios1_2 = "VSP6547_XXXXX"
        zone_vios1_fab2 = lpar_alias + "_" +vsp_port_vios1_2
        fabric2 = "P_Fabric2"
        return zone_vios1_fab2,vsp_port_vios1_2,fabric2 

