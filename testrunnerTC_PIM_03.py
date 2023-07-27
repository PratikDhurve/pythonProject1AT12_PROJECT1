from TC_PIM_03 import Test_login
import unittest

def main():
    loader = unittest.loader()
    loader.loadTestFromTestCase(Test_login)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == '__main__':
    main()
