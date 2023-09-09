import pandas as pd

def save_handicap(df, path):
    '''
    Save handicap to csv.
    
    Parameters
    ----------
    df: pd.DataFrame
        dataframe of handicap.
    fn: string
        file name.
    '''
    core_data = 'handicap_table_all.csv'
    fn = path.split('/',-1)[-1]

    if fn == core_data:
        comfirm = input('正在保存总让分表，确认覆盖保吗？[y/n]:')
        if comfirm != 'y':
            return
    df.to_csv(path, sep=' ')
    return print("保存文件{}".format(fn))

if __name__ == '__main__':
    from read import read_handicap
    print("测试函数：读取总表并保存成test格式")
    test_path = 'data/test.csv'
    core_path = "data/handicap_table_all.csv"
    df = read_handicap(core_path)
    print("读取{}让分表".format(core_path))

    save_handicap(df, test_path)
    print("保存成测试文件：{}".format(test_path))

    save_handicap(df, core_path)
    