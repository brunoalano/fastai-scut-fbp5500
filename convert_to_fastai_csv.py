import csv
import shutil
from pathlib import Path

def main():
  # Settings
  out_dir = Path('fastai-scut-fbp5500-v2/')
  out_train_dir = out_dir / Path('train')
  out_test_dir = out_dir / Path('test')
  out_csv = Path('fastai-scut-fbp5500.csv')
  imgs_dir = Path('Images/')
  train_file = Path('train_test_files/split/train.txt')
  test_file = Path('train_test_files/split/test.txt')

  # Output Directory
  print(f"Creating output directory {str(out_dir)}")
  shutil.rmtree(out_dir, ignore_errors=True)
  out_dir.mkdir()
  out_train_dir.mkdir()
  out_test_dir.mkdir()

  with out_csv.open(mode='w') as out_csvfile:
    out_csv_writer = csv.writer(out_csvfile)

    # Train files
    print("Processing training files")
    with open(train_file) as f:
      for line in f:
        filename, score = line.split()
        filename = Path(filename)
        score = float(score)
        shutil.copyfile(imgs_dir / filename, out_train_dir / filename)
        out_csv_writer.writerow([str(out_train_dir / filename), score])

    # Test files
    print("Processing test files")
    with open(test_file) as f:
      for line in f:
        filename, score = line.split()
        filename = Path(filename)
        score = float(score)
        shutil.copyfile(imgs_dir / filename, out_test_dir / filename)
        out_csv_writer.writerow([str(out_test_dir / filename), score])

if __name__ == '__main__':
  main()
