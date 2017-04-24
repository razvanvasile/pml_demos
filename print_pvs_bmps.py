import mock
import sys
sys.path.insert(0, '/home/cxa78676/pml/pml')
import pml.load_csv

def print_pvs_bpms():
    lat = pml.load_csv.load('/home/cxa78676/pml/pml/test/data/VMX', 'vmx', mock.MagicMock())
    bpms = lat.get_elements('BPM')
    print 'The pvs for each bpm in the lattice are:'
    for bpm in bpms:
        print bpm.get_pv_name('x')[0]
        print bpm.get_pv_name('y')[0]

def main():
    print_pvs_bpms()

if __name__ == '__main__':
    main()
