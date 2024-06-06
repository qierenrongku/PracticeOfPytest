def test_tmpdir(tmpdir):
    a_file = tmpdir.join('something.txt')
    a_sub_dir = tmpdir.mkdir('anything')
    another_file = a_sub_dir.join('something_else.txt')
    a_file.write('a file')
    another_file.write('contents')
    assert a_file.read() == 'a file'
    assert another_file.read() == 'contents'

def test_tmpdir_factory(tmpdir_factory):
    a_dir = tmpdir_factory.mktemp('mydir')
    base_temp = tmpdir_factory.getbasetemp()
    print('base:', base_temp)
    a_file = a_dir.join('something.txt')
    a_sub_dir = a_dir.mkdir('anything')
    another_file = a_sub_dir.join('something_else.txt')
    a_file.write('a file')
    another_file.write('contents')
    assert a_file.read() == 'a file'
    assert another_file.read() == 'contents'
