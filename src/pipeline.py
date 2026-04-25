def process_packet(file):

    file_size_map = {
        "audit_logs.log": 550,
        "user_activity.csv": 1400,
        "payments.xlsx": 2100,
        "video_dump.mp4": 6000,
        "system_backup.zip": 9000
    }

    size = file_size_map.get(file, 500)

    # MUST BE 5 FEATURES (MATCH MODEL)
    return [
        size,
        1,
        0,
        1,
        0
    ]