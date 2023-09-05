import pandas as pd
def read_handicap(fn):
    ''' 
    read handicap table.
    
    Parameters:
    -----------
    fn: string
        File name of handicap table.
    
    Return:
    -------
    pd.DataFrame
    '''
    df = pd.read_csv(fn, delim_whitespace=True, index_col="name")
    return df

if __name__=='__main__':
    fn = "data/handicap_table.csv"
    df = read_handicap(fn)
    print(df)
    # print(df.at["张三", "王五"])
    