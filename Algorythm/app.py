
from subprocess import call

call('pwd')

call(['hexdump','-v','../split_by_1min/2020-08-24_10-00-1.csv'])
