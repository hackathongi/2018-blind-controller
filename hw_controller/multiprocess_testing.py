import click
from multiprocessing import Pool
import hw_controller
import time



@click.command()
def testing():

    print("Start of the execution!")
    stop = 0
    pool = Pool(processes=1)

    while not stop:
        action = raw_input('Action?: ')
        if action == "open":
            t = raw_input('Time: ')
            if t == '':
                t = '0'
            pool.close()
            pool.terminate()
            pool = Pool(processes=1)
            pool.apply_async(hw_controller.blind_open, (int(t),))
        elif action == "close":
            t = raw_input('Time: ')
            if t == '':
                t = '0'
            pool.close()
            pool.terminate()
            pool = Pool(processes=1)
            pool.apply_async(hw_controller.blind_close, (int(t),))
        elif action == "purge":
            pool.close()
            pool.terminate()
            pool = Pool(processes=1)
        elif action == "stop":
            stop = 1
        else:
            print(action+" is not a valid option...")
        time.sleep(0.5)
        
    print("End of the execution...")


if __name__ == '__main__':
    testing()
