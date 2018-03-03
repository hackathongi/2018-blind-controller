import click
from multiprocessing import Pool
import hw_controller



@click.command()
def testing():
    print("Start of the execution!")
    pool = Pool(processes=1)
    try:
        while True:
            action = raw_input('So?: ')
            if action == "open":
                pool.close()
                pool = Pool(processes=1)
                pool.apply_async(hw_controller.blind_open())
            elif action == "close":
                pool.close()
                pool = Pool(processes=1)
                pool.apply_async(hw_controller.blind_open())
            else:
                print(action+" is not a valid option...")
    except KeyboardInterrupt:
        print("End of the execution...")


if __name__ == '__main__':
    testing()
