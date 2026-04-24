from src.detect import detect
from src.camouflage import inject_noise, add_delay, fake_packets

def process_packet(features):

    if detect(features):

        print("🚨 ALERT: Suspicious activity detected!")

        # ACTIVE RESPONSE SYSTEM
        inject_noise()
        add_delay()
        fake_packets()

        print("🛡️ System is now in defensive camouflage mode")

    else:
        print("✅ Normal traffic flow")