import pandas as pd

def getfirstlook(df,nrows=5,uniqueids=None):                # 데이터 처음 보기
    out={}
    out['head']=df.head(nrows)
    out['dtypes']=df.dtypes
    out['nrows']=df.shape[0]
    out['ncols']=df.shape[1]
    out['index']=df.index

    if (uniqueids is not None):
        out['uniqueids']=df[uniqueids].nunique()
    return out

def displaydict(dicttodisplay):                             # 딕셔너리를 보기 좋게
    print(*(': '.join(map(str,x))
            for x in dicttodisplay.items()), sep='\n\n')
    
def gettots(df):                                            # 요약 통계
    out={}

    out['min']=df.min()
    out['per15']=df.quantile(0.15)
    out['qr1']=df.quantile(0.25)
    out['med']=df.median()
    out['qr3']=df.quantile(0.75)
    out['per85']=df.quantile(0.85)
    out['max']=df.max()
    out['count']=df.count()
    out['mean']=df.mean()
    out['iqr']=out['qr3'] - out['qr1']

    return pd.DataFrame(out)

def getmissings(df, byrowperc=False):                       # 열, 행 결측값
    return df.isnull().sum(), df.isnull().sum(axis=1).value_counts(normalize=byrowperc).sort_index()

def makefreqs(df, outfile):                                 # 범주형 변수 전체 빈도
    freqout=open(outfile,'w')
    for col in df.select_dtypes(include=['category']):
        print(col,'-----------------','frequencies',
              df[col].value_counts().sort_index(),'percentages',
              df[col].value_counts(normalize=True).sort_index(),
              sep='\n\n',end='\n\n\n',file=freqout)
    
    freqout.close()

def getcnts(df, cats, rowsel=None):
    tots = cats[:-1]
    catcnt = df.groupby(cats).size().reset_index(name='catcnt')
    totcnt = df.groupby(tots).size().reset_index(name='totcnt')
    percs = pd.merge(catcnt, totcnt, left_on=tots, right_on=tots, how="left")
    percs['percent'] = percs.catcnt / percs.totcnt
    if (rowsel is not None):
      percs = percs.loc[eval("percs." + rowsel)]
    return percs