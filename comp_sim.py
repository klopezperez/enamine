from isim_comp import calculate_comp_sim, calculate_isim
import pickle 
import numpy as np
import bz2

# Load the fingerprints
file_path = 'enamine_HLL460_fp.pkl.bz2'
with bz2.BZ2File(file_path, 'rb') as f:
        uncompressed_data = f.read()
        data = pickle.loads(uncompressed_data)

data = np.array(data['ECFP4'])
data = np.stack(data)


# Calculate the complementarity similarity
comp_sim = calculate_comp_sim(data)
comp_sim = np.array(comp_sim)

# Save the complementarity similarity
output_file = 'enamine_HLL460_comp_sim_ECFP4.npy'
np.save(output_file, comp_sim)