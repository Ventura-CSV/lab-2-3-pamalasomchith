import main
import io
import sys
import re


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '10 \n 20 \n 30'
    sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    p = re.compile(r'[\w,\W]*10[\w,\W]*20[\w,\W]*30[\w,\W]*')
    res = p.match(lines[0])
    assert res != None
    print(res.group())

    p = re.compile(r'[\w,\W]*60[\w,\W]*')
    res = p.match(lines[1])
    assert res != None
    print(res.group())

    # p = re.compile('[\w,\W]*20\.00[\w,\W]*')
    res = re.search(r'[\w,\W]*20\.00[\w,\W]*', lines[2])
    # res = p.match(lines[2])
    assert res != None
    print(res.group())


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '10 \n 15 \n 25'
    sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    p = re.compile(r'[\w,\W]*10[\w,\W]*15[\w,\W]*25[\w,\W]*')
    res = p.match(lines[0])
    assert res != None
    print(res.group())

    p = re.compile(r'[\w,\W]*50[\w,\W]*')
    res = p.match(lines[1])
    assert res != None
    print(res.group())

    p = re.compile(r'[\w,\W]*16\.67[\w,\W]*')
    res = p.match(lines[2])
    assert res != None
    print(res.group())
