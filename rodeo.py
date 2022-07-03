def rename_rodeo_columns(columns):
    out_list=[]
    for name in columns:
        new_name = name.lower().replace(' ','_').strip('data')
        out_list.append(new_name)
    
    return out_list