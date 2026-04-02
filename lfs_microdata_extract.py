import pandas as pd
import zipfile as zf

def get_year_data(year,condition=''):
    df_result = pd.DataFrame()
    bStarted = False
    filelist = ''
    key = ''
    value = ''
    test = ''
    if len(condition)>0 and condition.find('=') > -1:
        key,value = condition.split('=')        
    fname = f'{str(year)}-CSV.zip'    
    with zf.ZipFile(fname,'r') as zip_file:
        filelist = zip_file.namelist()
        for file in filelist:
            if file.startswith('pub') and file.endswith('.csv'):
                try:
                    print(f'filename = {file}')
                    with zip_file.open(file) as f:
                        df = pd.read_csv(f)
                        if not bStarted:
                            df_result = df
                            bStarted = True
                        else:
                            df_result = pd.concat([df_result,df],ignore_index=True)                        
                except:
                    print(f'ERROR: {file} failed')
    
    df_final = df_result

    if len(condition) > 0:
        if key in df_final.columns:
            test = df_final[key] == int(value)
            df_final = df_final[test]
        else:
            print(f'{key} not found in dataframe')
        
    return df_final

df_complete = pd.DataFrame()
bFirst = True

for year in range(2015,2027):
    print(f'Current year: {year}')
    df_data = get_year_data(year,'PROV=35')
    if bFirst:
        df_complete = df_data
        bFirst = False
    else:
        df_complete = pd.concat([df_complete,df_data],ignore_index=True)

df_complete.to_csv('LFS_Ontario_2015-2026.csv')

