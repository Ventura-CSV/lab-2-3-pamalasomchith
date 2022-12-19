import main
import io
import sys
import re


def test_main_50():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '50'
    sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    res = re.search('730', lines[0])
    assert res != None
    print(res.group())
    assert res.group() == '730', 'Expected 730'

    res = re.search('277.8', lines[1])
    assert res != None
    print(res.group())
    assert res.group() == '277.8', 'Expected 277.8'

    res = re.search('1007.8', lines[2])
    assert res != None, 'The final price error'
    print(res.group())
    assert res.group() == '1007.8', 'Expected 1007.8'


def test_main_70():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '70'
    sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    res = re.search('730', lines[0])
    assert res != None
    print(res.group())
    assert res.group() == '730', 'Expected 730'

    res = re.search('833.4', lines[1])
    assert res != None
    print(res.group())
    assert res.group() == '833.4', 'Expected 833.4'

    res = re.search('1563.4', lines[2])
    assert res != None, 'The final price error'
    print(res.group())
    assert res.group() == '1563.4', 'Expected 1563.4'
