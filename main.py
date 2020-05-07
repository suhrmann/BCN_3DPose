#!/usr/bin/python

import sys
from os import path
from bcn import BCN


def main():
    if len(sys.argv) == 1:  # binary + arguments => 1 + n
        print_help()
        exit()

    # Parse command line arguments
    case = sys.argv[1:][0]  # Parse operation (train, test, test_video)
    # Parse data directory
    data_dir = None
    if len(sys.argv) == 3:
        _data_dir = sys.argv[1:][1]
        data_dir = path.abspath(_data_dir) if _data_dir else None

    # Run BCN
    if case == 'train':
        restore = False
        s = BCN(restore=restore, data_dir=data_dir)
        s.train()
    elif case == 'test':
        restore = True
        s = BCN(restore)
        s.test()
    elif case == 'test_video':
        restore = True
        s = BCN(restore)
        s.predict_video()
    elif case == 'help' or case == '--help' or case == 'h':
        print_help()

    else:
        # No a valid command -> Print help and exit
        print("BCN_3DPose: '"+str(case)+"' is not a command. See 'BCN_3DPose --help'.")


def print_help():
    print("""BCN_3DPose
usage: python main.py train [DATA_DIR]
       python main.py test
       python main.py test_video

Bayesian Capsule Networks for 3D human pose estimation from single 2D images

optional arguments:
  DATA_DIR       The path to "Data3D" that contains training data - defaults to \'./Data3D\'
""")


if __name__ == "__main__":
    main()
