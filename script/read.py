import pandas as pd
def read_handicap(path):
    ''' 
    read handicap table.
    
    Parameters:
    -----------
    path: string
        Path of handicap table.
    
    Return:
    -------
    pd.DataFrame
    '''
    df = pd.read_csv(path, delim_whitespace=True, index_col="name")
    return df

if __name__=='__main__':
    path = "data/handicap_table.csv"
    df = read_handicap(path)
    print(df)
    # print(df.at["张三", "王五"])
    