# 딕셔너리 성적 리스트
grade_dic = {
        '국어': [98, 88, 68, 64, 120],
        '영어': [None, 90, 60, 20, 50], 
        '수학': [90, 70, None, 31, None],
        '과학': [120, 50, None, 60, 88]
}

from pandas import DataFrame
from Data import grade_dic
from print_df import print_df
df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# print_df(df)

# 리스트 행 추가
df.loc['짱구'] = [90, 80, 70, 30]

# 누락되는 값(결측치) 또는 초과에 경우 에러 발생
#df.loc['짱구'] = [70, 20, 34, 10, 49]

from pandas import DataFrame
from Data import grade_dic
from print_df import print_df

df=DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# print_df(df)

# 행 복사
df.loc['짱구'] = df.loc['도라에몽']

print_df(df)