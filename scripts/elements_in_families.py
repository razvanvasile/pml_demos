import sys
import mock
sys.path.insert(0, '/home/cxa78676/pml/pml')
import pml.load_csv

def main():
    lattice = pml.load_csv.load('/home/cxa78676/pml/pml/test/data/VMX', 'VMX', mock.MagicMock())
    q1b = lattice.get_elements('Q1B')
    q1d = lattice.get_elements('Q1D')
    q2b = lattice.get_elements('Q2B')
    q2d = lattice.get_elements('Q2D')
    q3b = lattice.get_elements('Q3B')
    q3d = lattice.get_elements('Q3D')
    for element in q1b:
        print "Q1B pv:", element.get_pv_name('b1', 'readback'), "Position s =", lattice.get_s(element)
    for element in q1d:
        print "Q1D pv:", element.get_pv_name('b1', 'readback'), "Position s =", lattice.get_s(element)
    for element in q2b:
        print "Q2B pv:", element.get_pv_name('b1', 'readback'), "Position s =", lattice.get_s(element)
    for element in q2d:
        print "Q2D pv:", element.get_pv_name('b1', 'readback'), "Position s =", lattice.get_s(element)
    for element in q3b:
        print "Q3B pv:", element.get_pv_name('b1', 'readback'), "Position s =", lattice.get_s(element)
    for element in q3d:
        print "Q3D pv:", element.get_pv_name('b1', 'readback'), "Position s =", lattice.get_s(element)



if __name__ == '__main__':
    main()
