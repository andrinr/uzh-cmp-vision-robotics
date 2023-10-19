import numpy as np
from scipy.spatial.distance import cdist


def matchDescriptors(query_descriptors, database_descriptors, match_lambda):
    """
    Returns a 1xQ matrix where the i-th coefficient is the index of the database descriptor which matches to the
    i-th query descriptor. The descriptor vectors are MxQ and MxD where M is the descriptor dimension and Q and D the
    amount of query and database descriptors respectively. matches(i) will be -1 if there is no database descriptor
    with an SSD < lambda * min(SSD). No elements of matches will be equal except for the -1 elements.
    """
    distances = cdist(query_descriptors.T, database_descriptors.T, 'euclidean')

    min_distances = np.min(distances, axis=1)
    delta = match_lambda * min_distances

    matches = np.argmin(distances, axis=1)

    matches[min_distances > delta] = -1

    return matches
