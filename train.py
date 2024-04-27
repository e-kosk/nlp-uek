from pathlib import Path

from core import train

if __name__ == '__main__':
    BASE_DIR = Path('data/training')
    train(BASE_DIR)
