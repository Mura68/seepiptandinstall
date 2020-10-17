import subprocess
import sys
import pkg_resources

required = {'XlsxWriter','python-dotenv'}
upd2=[x for x in required]
upd=[x.lower() for x in upd2]

installed = [pkg.key for pkg in pkg_resources.working_set]
for pippack in installed:
    if pippack in upd:
        required-={upd2.pop(upd.index(pippack))}
        upd.pop(upd.index(pippack))
nothere={x for x in required}


try:
   if nothere:

    python = sys.executable
    print('Downloading.....')
    subprocess.check_call([python, '-m', 'pip', 'install', *nothere], stdout=subprocess.DEVNULL)
    print('Downloaded!!')
    #RErun program
    print('Rerun the program')
    exit()
except Exception as es:
    print('UNEXPECTED ERROR :',es)
    exit()