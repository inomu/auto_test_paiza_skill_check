# -*- coding: utf-8 -*-
from enum import Enum , IntEnum, auto


print("#1 Read TestDataFile")
test_data = []
# データ読み取り{{{
class R_MODE(Enum):
    INIT = 0
    TEST_START = auto()
    INPUT_DATA = auto()
    INPUT_EXPECT = auto()

# EOFまでループする
# TEST_STARTのタグを見つけたら読み取りを開始
    # -までINPUTデータとして読み取り
    # ENDまでEXPECTデータとして読み取り
r_file = "./test_data.txt"
with open(r_file, 'r') as rf:
    t_read_mode = R_MODE.INIT
    t_test_num = 0          # 何番目のテストか
    for r_line in rf:
        # 読み取りモードの状態遷移
        if( 'TEST_START\n' == r_line ):
            t_read_mode = R_MODE.INPUT_DATA
            continue
        elif( '-\n' == r_line ):
            t_read_mode = R_MODE.INPUT_EXPECT
            t_input_data_num = 0
            continue
        elif( 'END\n' == r_line ):
            t_read_mode = R_MODE.INIT
            t_test_num += 1
            t_input_data_num = 0
            continue
        else:
            pass

        # 読み取った値をモードごとに振り分け
        if( R_MODE.INPUT_DATA == t_read_mode ):
            is_add_num = False
            if ( len(test_data) == t_test_num ): is_add_num = True

            if(is_add_num):
                test_data.append( [ r_line ]  )

            else:
                test_data[t_test_num][0] += r_line

        elif( R_MODE.INPUT_EXPECT == t_read_mode ):
            is_add_num = False

            if( len(test_data[t_test_num]) != 2 ): is_add_num = True

            if( is_add_num ):
                test_data[t_test_num].append(r_line)
                pass
            else:
                test_data[t_test_num][1] += r_line
                pass

        else:
            pass
# }}}

print("Read Data")
for line in test_data:
    print(line)


print("#2 Execute Test")
# 読み取ったデータをプログラムに流し込む
import os
import subprocess
from subprocess import PIPE
# テストデータの数だけループする
# inputデータをテスト対象の標準出力として流し込む
# テスト対象から結果を取得し、expectデータと比較判定する
if True:
    for t_test_num in range( len(test_data)):
        # 事前にコンパイル
        cmd = '' 
        cmd += "gcc main.c -o main.out"
        proc = subprocess.run( cmd , shell=True, stdout=PIPE, stderr=PIPE, text=True)

        if(proc.returncode != 0):
            print("Compile Error")
            print(proc)
            break

        # echo "testdata" | program.c でデータを入力する
        cmd = '' 
        cmd += "echo '"
        cmd += test_data[t_test_num][0]
        cmd += "' | "
        cmd += "./main.out"

        proc = subprocess.run( cmd , shell=True, stdout=PIPE, stderr=PIPE, text=True)
        stdout = proc.stdout
        #print('STDOUT: {}'.format(stdout))

        # テストデータと比較
        if( stdout == test_data[t_test_num][1] ):
            print("TEST:{} comp".format(t_test_num+1))
            print("Expect:" ,  test_data[t_test_num][1] )
        else:
            print("TEST:{} not comp".format(t_test_num+1))
            print("Expect:" ,  test_data[t_test_num][1] )
            print(proc)
            print(proc.stdout)

    
