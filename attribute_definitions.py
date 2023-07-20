from cantools.database.can.attribute_definition import AttributeDefinition
  
attribute_def_list = []

m_cd_hidden = AttributeDefinition('CanDootDecode',
                                    default_value='Yes',
                                    kind='BO_',
                                    type_name='ENUM',
                                    minimum=None,
                                    maximum=None,
                                    choices=['No', 'Yes'])
attribute_def_list.append(m_cd_hidden)

m_cd_decode_bus = AttributeDefinition('CanDootDecodeBus',
                                        default_value=1,
                                        kind='BO_',
                                        type_name='INT',
                                        minimum=0,
                                        maximum=6,
                                        choices=None)
attribute_def_list.append(m_cd_decode_bus)

m_cd_paused = AttributeDefinition('CanDootPaused',
                                    default_value='No',
                                    kind='BO_',
                                    type_name='ENUM',
                                    minimum=None,
                                    maximum=None,
                                    choices=['No', 'Yes'])
attribute_def_list.append(m_cd_paused)

m_cd_simulate = AttributeDefinition('CanDootSimulate',
                                    default_value='No',
                                    kind='BO_',
                                    type_name='ENUM',
                                    minimum=None,
                                    maximum=None,
                                    choices=['No', 'Yes'])
attribute_def_list.append(m_cd_simulate)

m_cd_simulate_bus = AttributeDefinition('CanDootSimulateBus',
                                        default_value=1,
                                        kind='BO_',
                                        type_name='INT',
                                        minimum=0,
                                        maximum=6,
                                        choices=None)
attribute_def_list.append(m_cd_simulate_bus)

m_cd_simulate_cycle_time = AttributeDefinition('CanDootSimulateCycleTime',
                                                default_value=100,
                                                kind='BO_',
                                                type_name='INT',
                                                minimum=0,
                                                maximum=50000,
                                                choices=None)
attribute_def_list.append(m_cd_simulate_cycle_time)

m_cg_message_inst_name = AttributeDefinition('CG_MessageInstName',
                                   default_value="",
                                   kind='BO_',
                                   type_name='STRING',
                                   minimum=None,
                                   maximum=None,
                                   choices=None)
attribute_def_list.append(m_cg_message_inst_name)

s_cd_group = AttributeDefinition('CanDootGroup',
                                    default_value='None',
                                    kind='SG_',
                                    type_name='ENUM',
                                    minimum=None,
                                    maximum=None,
                                    choices=['None', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'g9', 'gA', 'gB', 'gC', 'gD', 'gE', 'gF'])
attribute_def_list.append(s_cd_group)

s_cd_hidden = AttributeDefinition('CanDootHidden',
                                    default_value='No',
                                    kind='SG_',
                                    type_name='ENUM',
                                    minimum=None,
                                    maximum=None,
                                    choices=['No', 'Yes'])
attribute_def_list.append(s_cd_hidden)

s_cd_broadcast = AttributeDefinition('CanDootBroadcast',
                                    default_value='Yes',
                                    kind='SG_',
                                    type_name='ENUM',
                                    minimum=None,
                                    maximum=None,
                                    choices=['No', 'Yes'])
attribute_def_list.append(s_cd_broadcast)

s_cg_vartype = AttributeDefinition('CG_VarType',
                                    default_value='uint8_t',
                                    kind='SG_',
                                    type_name='ENUM',
                                    minimum=None,
                                    maximum=None,
                                    choices=['bool', 'uint8_t', 'int8_t',
                                             'uint16_t', 'int16_t', 'uint32_t',
                                             'int32_t', 'float', 'double'])
attribute_def_list.append(s_cg_vartype)
