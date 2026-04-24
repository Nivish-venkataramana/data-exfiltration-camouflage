from src.pipeline import process_packet
import numpy as np

# Simulated network packets
for i in range(5):

    # fake traffic data (5 features)
    packet = np.random.rand(5)

    process_packet(packet)