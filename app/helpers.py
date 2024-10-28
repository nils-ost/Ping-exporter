
def conv_int(value, default=0):
    try:
        return int(value)
    except Exception:
        return default


def conv_float(value, default=0.0):
    try:
        return float(value)
    except Exception:
        return default


def generate_output(ip, dns, p_send, p_recv, p_lost, rtt_min, rtt_max, rtt_avg, mdev, success):
    lines = list()
    lines.append('# HELP ping_packets_send count of packets send during ping')
    lines.append('# TYPE ping_packets_send gauge')
    lines.append(f'ping_packets_send{{dns="{dns}",ip="{ip}"}} {p_send}')

    lines.append('# HELP ping_packets_received count of packets received back during ping')
    lines.append('# TYPE ping_packets_received gauge')
    lines.append(f'ping_packets_received{{dns="{dns}",ip="{ip}"}} {p_recv}')

    lines.append('# HELP ping_packets_lost count of packets lost during ping')
    lines.append('# TYPE ping_packets_lost gauge')
    lines.append(f'ping_packets_lost{{dns="{dns}",ip="{ip}"}} {p_lost}')

    if rtt_min is not None and rtt_max is not None and rtt_avg is not None and mdev is not None:
        lines.append('# HELP ping_rtt_min minimum round trip time')
        lines.append('# TYPE ping_rtt_min gauge')
        lines.append(f'ping_rtt_min{{dns="{dns}",ip="{ip}"}} {rtt_min}')

        lines.append('# HELP ping_rtt_max maximum round trip time')
        lines.append('# TYPE ping_rtt_max gauge')
        lines.append(f'ping_rtt_max{{dns="{dns}",ip="{ip}"}} {rtt_max}')

        lines.append('# HELP ping_rtt_avg average round trip time')
        lines.append('# TYPE ping_rtt_avg gauge')
        lines.append(f'ping_rtt_avg{{dns="{dns}",ip="{ip}"}} {rtt_avg}')

        lines.append('# HELP ping_mdev maximum deviation of the round trip time')
        lines.append('# TYPE ping_mdev gauge')
        lines.append(f'ping_mdev{{dns="{dns}",ip="{ip}"}} {mdev}')

    lines.append('# HELP ping_success indicator if the ping was an overall success')
    lines.append('# TYPE ping_success gauge')
    lines.append(f'ping_success{{dns="{dns}",ip="{ip}"}} {success}')
    return '\n'.join(lines)
