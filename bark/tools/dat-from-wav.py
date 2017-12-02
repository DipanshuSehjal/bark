from scipy.io import wavfile as wavfile
import bark, os


def main(wav):
	if not isinstance(wav, str):
	    raise ValueError('A file path string is required')
	name, ext = os.path.splitext()   # get the original file name. e.g. ab from ab.wav
	rate, data = wavfile.read(wav)
	# make dat file with the same name as wav file
	datname = '{}.dat'.format(name)
	bark.write_sampled(datname, data, rate, original_file=wav)


def _run():
    ''' Function for getting commandline args.'''
    import argparse

    p = argparse.ArgumentParser(description='''
    converts wav file to bark format
    ''')
    p.add_argument('wav', help='path to wav file')
    args = p.parse_args()
    main(args.wav)


if __name__ == '__main__':
	_run()
