#Logica para la generacion de sentencias para creacion de zonas brocade

def wwnparse(wwn):
    lista_wwn = wwn.split()
    lista_wwn_result = list()
    for wwn_lpar in lista_wwn:
        print(wwn_lpar)
        #wwn_lpar = line.rstrip() 
        wwn = wwn_lpar[0:2]+":"+wwn_lpar[2:4]+":"+wwn_lpar[4:6]+":"+wwn_lpar[6:8]+":"+wwn_lpar[8:10]+":"+wwn_lpar[10:12]
        lista_wwn_result.append(wwn)
    wwn1 = lista_wwn_result[0]
    wwn2 = lista_wwn_result[1]
    wwn3 = lista_wwn_result[2]
    wwn4 = lista_wwn_result[3]
    return wwn1, wwn2, wwn3, wwn4

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

