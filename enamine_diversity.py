from isim_comp import *
from isim_div import *
import pickle
import bz2

# Load the fingerprints
file_path = 'enamine_HLL460_fp.pkl.bz2'
with bz2.BZ2File(file_path, 'rb') as f:
        uncompressed_data = f.read()
        data = pickle.loads(uncompressed_data)

fp = 'RDKit'

    
data = np.array(data[fp])
data = np.stack(data)

n = len(data)    
# Do diversity selection 
div =  diversity(data, percentage = 100000*100/n, start = 'medoid', n_ary="JT", method='isim')
        

# Save the diversity selection as pkl
output_file = 'HLL460_diversity_'+fp+'_isim.pkl'
with open(output_file, 'wb') as f:
    pickle.dump(div, f)
