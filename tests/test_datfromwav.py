import bark, pytest, numpy as np, os.path
from scipy.io import wavfile
from bark.io import datfromwav as dfw

def test_dat_from_wav_int(tmpdir):
	
#1.  Create wav file
	# dtype: int array

	fname_wav = os.path.join(tmpdir.strpath, 'test.wav')
	arr_int = np.random.randint(1000, size=(1,100))
	rate = 48000
	wavfile.write(fname_wav, rate, arr_int)
	assert os.path.exists(fname_wav), 'File Not Found: test.wav '


	
#2. Generate .dat and .dat.meta.yaml file
	#Give .dat file path
	fname_dat = os.path.join(tmpdir.strpath, 'test.dat')
	attrs = {"name": "hello bark", "project": "bark"}
	dat_file = dfw.dat_from_wav(fname_wav, fname_dat, **attrs)
	assert os.path.exists(fname_dat), 'File Not Found: test.dat'
	assert os.path.exists(os.path.join(tmpdir.strpath, 'test.dat.meta.yaml')), 'File Not Found: test.dat.meta.yaml'

#3. Compare data, rate in .dat file
	assert np.array_equal(arr_int, bark.read_sampled(fname_dat).data), 'Data in .wav and .dat files does not match' 
	assert rate == bark.read_sampled(fname_dat).sampling_rate, 'Sampling rates does not match'
	assert 'hello bark' == bark.read_sampled(fname_dat).attrs['name'], 'name attribute does not match'
	assert 'bark' == bark.read_sampled(fname_dat).attrs['project'], 'project attribute does not match'
	

	

def test_dat_from_wav_float(tmpdir):
#1.  Create wav file
	# dtype: float array

	fname_wav = os.path.join(tmpdir.strpath, 'test_float.wav')
	arr_float = np.random.uniform(low=0.0, high=1000, size=(1,100))
	rate = 48000
	wavfile.write(fname_wav, rate, arr_float)
	assert os.path.exists(fname_wav), 'File Not Found: test_float.wav '


	
#2. Generate .dat and .dat.meta.yaml file
	#Give .dat file path
	fname_dat = os.path.join(tmpdir.strpath, 'test_float.dat')
	attrs = {"name": "hello bark", "project": "bark"}
	dat_file = dfw.dat_from_wav(fname_wav, fname_dat, **attrs)
	assert os.path.exists(fname_dat), 'File Not Found: test_float.dat'
	assert os.path.exists(os.path.join(tmpdir.strpath, 'test_float.dat.meta.yaml')), 'File Not Found: test_float.dat.meta.yaml'

#3. Compare data, rate in .dat file
	assert np.array_equal(arr_float, bark.read_sampled(fname_dat).data), 'Data in .wav and .dat files does not match' 
	assert rate == bark.read_sampled(fname_dat).sampling_rate, 'Sampling rates does not match'
	assert 'hello bark' == bark.read_sampled(fname_dat).attrs['name'], 'name attribute does not match'
	assert 'bark' == bark.read_sampled(fname_dat).attrs['project'], 'project attribute does not match'
	

