import sys
import mock
sys.path.insert(0, '/home/cxa78676/pml/pml')
import pml.load_csv


def print_pv_names(elements, lattice):
    for element in elements:
        print element.get_pv_name('b1', 'readback'), "Position s =", lattice.get_s(element)


def main():
    lattice = pml.load_csv.load('/home/cxa78676/pml/pml/test/data/VMX', 'VMX', mock.MagicMock())
    q1b = lattice.get_elements('Q1B')
    q1d = lattice.get_elements('Q1D')
    q2b = lattice.get_elements('Q2B')
    q2d = lattice.get_elements('Q2D')
    q3b = lattice.get_elements('Q3B')
    q3d = lattice.get_elements('Q3D')
    print "Q1B pvs:"
    print_pv_names(q1b, lattice)
    print "Q1D pvs:"
    print_pv_names(q1d, lattice)
    print "Q2B pvs:"
    print_pv_names(q2b, lattice)
    print "Q2D pvs:"
    print_pv_names(q2d, lattice)
    print "Q3B pvs:"
    print_pv_names(q3b, lattice)
    print "Q3D pvs:"
    print_pv_names(q3d, lattice)


if __name__ == '__main__':
    main()
