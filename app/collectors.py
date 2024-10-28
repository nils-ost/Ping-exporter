import subprocess


def do_ping(host, count=3, timeout=0.5):
    ip, dns = (None, None)
    p_send, p_recv, p_lost = (None, None, None)
    rtt_min, rtt_max, rtt_avg, mdev = (None, None, None, None)
    success = 0
    try:
        r = subprocess.check_output(f'ping -c {count} -i 0.01 -q -W {timeout} {host}', shell=True).decode('utf-8')
    except Exception as e:
        r = e.stdout.decode('utf-8')
    for line in r.strip().split('\n'):
        line = line.strip()
        if line.startswith('PING'):
            try:
                splitted = line.split()
                dns = splitted[1]
                ip = splitted[2].replace('(', '').replace(')', '')
            except Exception:
                print(line)
            continue
        if 'transmitted' in line:
            try:
                splitted = line.split(', ')
                p_send = int(splitted[0].split()[0])
                p_recv = int(splitted[1].split()[0])
                p_lost = p_send - p_recv
                if p_recv > 0:
                    success = 1 if p_send / p_recv > 0.5 else 0
            except Exception:
                print(line)
            continue
        if line.startswith('rtt'):
            try:
                splitted = line.split()[3].split('/')
                rtt_min = float(splitted[0])
                rtt_avg = float(splitted[1])
                rtt_max = float(splitted[2])
                mdev = float(splitted[3])
            except Exception:
                print(line)
            continue
    return (ip, dns, p_send, p_recv, p_lost, rtt_min, rtt_max, rtt_avg, mdev, success)
