from isim_sampling import *
import pickle

fps = ['RDKit', 'MACCS', 'ECFP4']

for fp in fps:

    # Load the complementarity similarity
    comp_sim = np.load('enamine_HLL460_comp_sim_' + fp + '.npy')

    # Get the number of compounds
    n = len(comp_sim)

    s = {}

    for n_sample in [10000, 50000, 100000]:
        s[n_sample] = {}

        p = n_sample*100/n

        # Get the samples for the percentages
        batch_samp = batched_sampling(comp_sim = comp_sim, percentage = p)
        rep_samp = representative_sampling(comp_sim = comp_sim, percentage = p)

        sample = {'batch': batch_samp, 'rep': rep_samp}
        s[n_sample] = sample

    with open('HLL460_' + fp + '.pkl', 'wb') as f:
        pickle.dump(s, f)

